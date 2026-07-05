import { computed, ref, watch } from "vue";

import { resolveLiveStageKey, stageDefinitions, timelineStages, type ApiRunJobLike, type ApiRunStageKey } from "../domain/apiRun";
import { getApiDetail, getApiJob, getApiJobLog, startApiRun } from "../services/tensorguard";
import type {
  ApiDetailPayload,
  ApiJobLogName,
  ApiJobPayload,
  ApiListItem,
  ApiRunMode,
  ApiStageStatus,
  Library,
} from "../types/tensorguard";
import { usePolling } from "./usePolling";

type TimelineStageKey = (typeof timelineStages)[number]["key"];

const activeRunStates = new Set(["pending", "running"] as const);
const apiJobLogNames: ApiJobLogName[] = ["01_qwen_seed.log", "02_ev_generation.log", "03_driver.log"];

function describeError(value: unknown, fallback: string): string {
  if (value instanceof Error) {
    return value.message;
  }

  return fallback;
}

function emptyResultFiles() {
  return {
    seed: [],
    valid: [],
    exception: [],
    crash: [],
    notarget: [],
    hangs: [],
    flaky: [],
  };
}

function isJobActive(status: ApiJobPayload["status"]["status"]): boolean {
  return activeRunStates.has(status as "pending" | "running");
}

function isStageSelectable(status: ApiStageStatus): boolean {
  return status === "success" || status === "failed";
}

function buildTimelineStages(job: ApiJobPayload | null): Record<TimelineStageKey, ApiStageStatus> {
  if (job === null) {
    return {
      prompt_check: "pending",
      qwen_seed: "pending",
      ev_generation: "pending",
      driver: "pending",
      summary: "pending",
    };
  }

  return { ...job.status.stages };
}

export function useApiRun() {
  const selectedApi = ref<ApiListItem | null>(null);
  const selectedApiDetail = ref<ApiDetailPayload | null>(null);
  const selectedJob = ref<ApiJobPayload | null>(null);
  const detailLoading = ref(false);
  const detailError = ref<string | null>(null);
  const jobLoading = ref(false);
  const jobError = ref<string | null>(null);
  const runLoading = ref(false);
  const runError = ref<string | null>(null);
  const mode = ref<ApiRunMode>("demo");
  const manualMetricStageKey = ref<ApiRunStageKey | null>(null);
  const selectedRevision = ref(0);
  const currentJobId = ref<string | null>(null);
  const completeLogs = ref<Record<string, string>>({});
  const logOffsets = new Map<ApiJobLogName, number>();
  let logJobId: string | null = null;
  let logRevision = 0;

  function resetLogState(jobId: string | null = null) {
    logRevision += 1;
    logJobId = jobId;
    completeLogs.value = {};
    logOffsets.clear();
  }

  async function drainJobLogs(jobId: string) {
    if (logJobId !== jobId) resetLogState(jobId);
    const revision = logRevision;
    await Promise.allSettled(apiJobLogNames.map(async (logName) => {
      let hasMore = true;
      while (hasMore && revision === logRevision && logJobId === jobId) {
        const requestedOffset = logOffsets.get(logName) ?? 0;
        const chunk = await getApiJobLog(jobId, logName, requestedOffset);
        if (revision !== logRevision || logJobId !== jobId) return;
        if (chunk.reset) {
          completeLogs.value = { ...completeLogs.value, [logName]: chunk.text };
        } else if (chunk.offset === requestedOffset && chunk.text) {
          completeLogs.value = {
            ...completeLogs.value,
            [logName]: `${completeLogs.value[logName] ?? ""}${chunk.text}`,
          };
        }
        logOffsets.set(logName, chunk.next_offset);
        hasMore = chunk.has_more && chunk.next_offset > requestedOffset;
      }
    }));
  }

  const polling = usePolling<ApiJobPayload>(async () => {
    if (currentJobId.value === null) {
      throw new Error("missing job id");
    }

    const payload = await getApiJob(currentJobId.value);
    if (payload.job_id === currentJobId.value) await drainJobLogs(payload.job_id);
    return {
      value: payload,
      continue: isJobActive(payload.status.status),
    };
  }, 2500);

  const liveStageKey = computed<ApiRunStageKey>(() => {
    if (selectedJob.value === null) {
      return "qwen_seed";
    }

    return resolveLiveStageKey(selectedJob.value as ApiRunJobLike);
  });

  const metricStageKey = computed<ApiRunStageKey>(() => manualMetricStageKey.value ?? liveStageKey.value);

  const stageStates = computed(() => buildTimelineStages(selectedJob.value));
  const metrics = computed(() => selectedJob.value?.metrics ?? []);
  const resultFiles = computed(() => selectedJob.value?.result_files ?? emptyResultFiles());
  const logs = computed(() => completeLogs.value);
  const summaryCounts = computed(
    () => selectedJob.value?.summary?.result_counts ?? selectedApiDetail.value?.result_counts ?? selectedApi.value?.result_counts ?? null,
  );

  watch(
    () => polling.latest.value,
    (payload) => {
      if (payload === null || payload.job_id !== currentJobId.value) {
        return;
      }

      applyJobPayload(payload, manualMetricStageKey.value);
    },
  );

  const canRun = computed(() => {
    if (selectedApi.value === null) {
      return false;
    }

    if (
      selectedApiDetail.value === null ||
      detailLoading.value ||
      detailError.value !== null ||
      jobError.value !== null ||
      runError.value !== null ||
      runLoading.value ||
      polling.running.value
    ) {
      return false;
    }

    const status = selectedJob.value?.status.status ?? selectedApiDetail.value?.latest_job?.status ?? null;
    return status === null || !activeRunStates.has(status as "pending" | "running");
  });

  function resetJobState() {
    selectedApiDetail.value = null;
    selectedJob.value = null;
    detailError.value = null;
    jobError.value = null;
    detailLoading.value = false;
    jobLoading.value = false;
    runError.value = null;
    runLoading.value = false;
    currentJobId.value = null;
    polling.stop();
    polling.error.value = null;
    manualMetricStageKey.value = null;
    resetLogState();
  }

  function applyJobPayload(payload: ApiJobPayload, preservedMetricStageKey: ApiRunStageKey | null = null) {
    if (logJobId !== payload.job_id) resetLogState(payload.job_id);
    selectedJob.value = payload;
    currentJobId.value = payload.job_id;
    jobError.value = null;
    if (preservedMetricStageKey !== null && isStageSelectable(payload.status.stages[preservedMetricStageKey])) {
      manualMetricStageKey.value = preservedMetricStageKey;
      return;
    }

    manualMetricStageKey.value = null;
  }

  async function hydrateJob(jobId: string, revision: number, preservedMetricStageKey: ApiRunStageKey | null = null) {
    jobLoading.value = true;
    jobError.value = null;

    try {
      const payload = await getApiJob(jobId);
      if (revision !== selectedRevision.value) {
        return;
      }

      applyJobPayload(payload, preservedMetricStageKey);
      await drainJobLogs(payload.job_id);
      if (isJobActive(payload.status.status)) {
        polling.start();
      } else {
        polling.stop();
      }
    } catch (cause) {
      if (revision === selectedRevision.value) {
        jobError.value = describeError(cause, "运行状态加载失败");
      }
    } finally {
      if (revision === selectedRevision.value) {
        jobLoading.value = false;
      }
    }
  }

  async function selectApi(item: ApiListItem) {
    selectedRevision.value += 1;
    const revision = selectedRevision.value;
    const previousSelection = selectedApi.value;
    const previousJobId = selectedJob.value?.job_id ?? selectedApiDetail.value?.latest_job?.job_id ?? null;
    const preservedMetricStageKey = manualMetricStageKey.value;

    selectedApi.value = item;
    detailLoading.value = true;
    detailError.value = null;
    resetJobState();
    selectedApi.value = item;
    detailLoading.value = true;

    try {
      const payload = await getApiDetail(item.lib, item.api);
      if (revision !== selectedRevision.value) {
        return;
      }

      selectedApiDetail.value = payload;
      detailError.value = null;

      const nextJobId = payload.latest_job?.job_id ?? null;
      const shouldPreserveMetricStage =
        previousSelection !== null &&
        previousSelection.api === item.api &&
        previousSelection.lib === item.lib &&
        previousJobId === nextJobId;
      const nextPreservedMetricStageKey = shouldPreserveMetricStage ? preservedMetricStageKey : null;

      if (payload.latest_job !== null) {
        await hydrateJob(payload.latest_job.job_id, revision, nextPreservedMetricStageKey);
      } else if (nextPreservedMetricStageKey !== null) {
        manualMetricStageKey.value = nextPreservedMetricStageKey;
      }
    } catch (cause) {
      if (revision === selectedRevision.value) {
        detailError.value = describeError(cause, "API 详情加载失败");
      }
    } finally {
      if (revision === selectedRevision.value) {
        detailLoading.value = false;
      }
    }
  }

  function clearSelection() {
    selectedRevision.value += 1;
    selectedApi.value = null;
    resetJobState();
  }

  async function startRun() {
    if (!canRun.value || selectedApi.value === null) {
      return;
    }

    selectedRevision.value += 1;
    const revision = selectedRevision.value;
    const current = selectedApi.value;
    runLoading.value = true;
    runError.value = null;
    polling.stop();
    polling.error.value = null;
    currentJobId.value = null;
    manualMetricStageKey.value = null;
    resetLogState();

    try {
      const started = await startApiRun({
        lib: current.lib as Library,
        api: current.api,
        mode: mode.value,
      });

      if (revision !== selectedRevision.value) {
        return;
      }

      await hydrateJob(started.job_id, revision);
    } catch (cause) {
      if (revision === selectedRevision.value) {
        runError.value = describeError(cause, "运行启动失败");
      }
    } finally {
      if (revision === selectedRevision.value) {
        runLoading.value = false;
      }
    }
  }

  function setMode(nextMode: ApiRunMode) {
    mode.value = nextMode;
  }

  function selectMetricStage(key: ApiRunStageKey | null) {
    manualMetricStageKey.value = key;
  }

  function retrySelection() {
    if (selectedApi.value !== null) {
      void selectApi(selectedApi.value);
    }
  }

  return {
    selectedApi,
    selectedApiDetail,
    selectedJob,
    detailLoading,
    detailError,
    jobLoading,
    jobError,
    runLoading,
    runError,
    mode,
    canRun,
    liveStageKey,
    metricStageKey,
    stageDefinitions,
    timelineStages,
    stageStates,
    metrics,
    resultFiles,
    logs,
    summaryCounts,
    pollError: polling.error,
    retryPollingNow: polling.retryNow,
    currentJobId,
    selectApi,
    clearSelection,
    retrySelection,
    setMode,
    selectMetricStage,
    startRun,
    polling,
  };
}
