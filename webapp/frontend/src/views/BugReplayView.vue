<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from "vue";

import {
  confirmCandidateCluster,
  deleteCandidateCluster,
  deleteConfirmedBug,
  generateReproReport,
  getCandidateCluster,
  getCandidateClusters,
  getCandidateValidationJob,
  getConfirmedBug,
  getConfirmedBugs,
  getEnvironment,
  getReproJob,
  getReproReport,
  reproduceConfirmedBug,
  resetCandidateClusterDraft,
  saveCandidateClusterDraft,
  startCandidateValidation,
} from "../services/tensorguard";
import { bugTypeGroups, bugTypeValues, customBugTypeValue } from "../domain/bugTypes";
import type {
  CandidateClusterDetail,
  CandidateClusterSummary,
  CandidateValidationJobPayload,
  ConfirmedBugDetail,
  ConfirmedBugSummary,
  ExecutionMode,
  ReproExecution,
  ReproJobPayload,
  EnvironmentPayload,
} from "../types/tensorguard";

type SourceKind = "confirmed" | "candidate";
type DeleteTarget = { kind: "candidate" | "confirmed"; id: string; label: string };

const sourceKind = ref<SourceKind>("confirmed");
const query = ref("");
const confirmed = ref<ConfirmedBugSummary[]>([]);
const candidateClusters = ref<CandidateClusterSummary[]>([]);
const selectedConfirmedId = ref<string | null>(null);
const selectedCandidateClusterId = ref<string | null>(null);
const detail = ref<ConfirmedBugDetail | null>(null);
const candidateClusterDetail = ref<CandidateClusterDetail | null>(null);
const candidateDraft = ref("");
const candidateValidation = ref<CandidateValidationJobPayload | null>(null);
const candidateDraftSaving = ref(false);
const candidateValidationRunning = ref(false);
const candidateActionLoading = ref(false);
const candidateReviewTitle = ref("");
const candidateReviewType = ref("");
const candidateReviewCustomType = ref("");
const candidateReviewNote = ref("");
const deleteTarget = ref<DeleteTarget | null>(null);
const deleteConfirmation = ref("");
const loading = ref(true);
const detailLoading = ref(false);
const error = ref<string | null>(null);
const actionError = ref<string | null>(null);
const selectedModes = ref<ExecutionMode[]>(["cpu", "gpu:0"]);
const job = ref<ReproJobPayload | null>(null);
const jobRunning = ref(false);
const reportMarkdown = ref("");
const reportOpen = ref(false);
const reportLoading = ref(false);
const runtimeEnvironment = ref<Partial<EnvironmentPayload> | null>(null);
let pollTimer: ReturnType<typeof setTimeout> | null = null;
let candidatePollTimer: ReturnType<typeof setTimeout> | null = null;
let selectionRevision = 0;

function describeError(value: unknown, fallback: string) {
  return value instanceof Error ? value.message : fallback;
}

function clusterStatusLabel(status: string) {
  const labels: Record<string, string> = {
    pending_review: "待审核",
    needs_review: "待审核",
    reproduced: "待审核",
    needs_minimize: "待审核",
    rejected: "已忽略",
    promoted: "已收录",
  };
  return labels[status] ?? status;
}

const filteredConfirmed = computed(() => {
  const needle = query.value.trim().toLowerCase();
  if (!needle) return confirmed.value;
  return confirmed.value.filter((item) =>
    [item.display_id, item.title, item.api, item.bug_type, item.framework].some((value) => value.toLowerCase().includes(needle)),
  );
});

const filteredCandidateClusters = computed(() => {
  const needle = query.value.trim().toLowerCase();
  if (!needle) return candidateClusters.value;
  return candidateClusters.value.filter((item) =>
    [
      item.cluster_id,
      item.api,
      item.lib,
      item.category,
      item.bug_pattern,
      item.cluster_status,
      item.confidence,
      item.representative.source_name,
      item.representative.error_summary,
    ].some((value) => value.toLowerCase().includes(needle)),
  );
});

const candidateClusterStats = computed(() => {
  const total = candidateClusters.value.length;
  const needsMinimize = candidateClusters.value.filter((item) => item.cluster_status === "needs_minimize").length;
  return { total, needsMinimize };
});

const candidateDraftDirty = computed(() => candidateDraft.value !== (candidateClusterDetail.value?.minimization_draft ?? ""));
const candidateValidationFinished = computed(() => candidateValidation.value?.status === "finished");
const candidateReviewFinalType = computed(() =>
  candidateReviewType.value === customBugTypeValue ? candidateReviewCustomType.value.trim() : candidateReviewType.value.trim(),
);
const candidateReviewValid = computed(() => Boolean(
  candidateReviewTitle.value.trim()
  && candidateReviewFinalType.value
  && candidateReviewNote.value.trim()
));
const candidateCanConfirm = computed(() => Boolean(
  candidateValidationFinished.value
  && candidateClusterDetail.value?.draft_saved
  && candidateValidation.value?.source_sha256 === candidateClusterDetail.value?.draft_sha256
  && !candidateDraftDirty.value
  && candidateReviewValid.value
));
const candidateCpuOutput = computed(() => candidateValidation.value?.logs?.cpu || "尚未运行 CPU 验证。");
const candidateGpuOutput = computed(() => candidateValidation.value?.logs?.gpu0 || "尚未运行 GPU 0 验证。");

const activeExecution = computed<ReproExecution | null>(() => {
  const modes = job.value?.status.modes;
  return modes?.["gpu:0"] ?? modes?.cpu ?? null;
});
const currentOutput = computed(() => {
  if (job.value === null) return "尚未在当前环境执行复现。";
  const chunks = Object.entries(job.value.logs).map(([name, value]) => `===== ${name} =====\n${value}`);
  return chunks.length ? chunks.join("\n\n") : "复现进程已启动，等待输出。";
});
const verdict = computed(() => {
  const executions = Object.values(job.value?.status.modes ?? {}).filter(Boolean) as ReproExecution[];
  if (executions.some((item) => item.evidence?.verdict === "reproduced")) {
    return { state: "reproduced", title: "当前环境复现成功", code: "REPRODUCED", detail: executions.find((item) => item.evidence?.verdict === "reproduced")?.evidence?.reason ?? "执行证据与归档缺陷特征一致。" };
  }
  if (jobRunning.value || job.value?.status.status === "running" || job.value?.status.status === "pending") {
    return { state: "running", title: "正在执行独立进程", code: "RUNNING", detail: "CPU 与 GPU 配置按所选模式依次运行。" };
  }
  if (job.value?.status.status === "finished") {
    return { state: "review", title: "复现结果需要复核", code: "NEEDS REVIEW", detail: activeExecution.value?.evidence?.reason ?? "本次运行未匹配确定性复现规则。" };
  }
  return { state: "idle", title: "等待当前环境复现", code: "NOT RUN", detail: "运行最小程序后，系统将依据返回码、进程信号与输出特征给出证据判定。" };
});
const reportHref = computed(() => `data:text/markdown;charset=utf-8,${encodeURIComponent(reportMarkdown.value)}`);
const environmentRows = computed(() => {
  const env = runtimeEnvironment.value ?? job.value?.environment;
  if (!env) return [];
  const framework = detail.value?.meta.framework === "TensorFlow" ? env.frameworks?.tensorflow : env.frameworks?.torch;
  return [
    ["Framework", framework?.installed ? framework.version : "unavailable"],
    ["CUDA", env.cuda?.driver_version ?? (env.cuda?.available ? "available" : "unavailable")],
    ["Device", env.gpus?.[0]?.name ?? "CPU only"],
    ["Python", env.python?.version ?? "unknown"],
  ];
});

function clearPoll() {
  if (pollTimer !== null) clearTimeout(pollTimer);
  pollTimer = null;
}

function clearCandidatePoll() {
  if (candidatePollTimer !== null) clearTimeout(candidatePollTimer);
  candidatePollTimer = null;
}

function applyCandidateCluster(payload: CandidateClusterDetail) {
  const changedCluster = candidateClusterDetail.value?.cluster_id !== payload.cluster_id;
  candidateClusterDetail.value = payload;
  candidateDraft.value = payload.minimization_draft;
  candidateValidation.value = payload.latest_validation ?? null;
  candidateValidationRunning.value = ["pending", "running"].includes(candidateValidation.value?.status ?? "");
  if (changedCluster) {
    const defaults = payload.review_defaults;
    candidateReviewTitle.value = defaults.title;
    candidateReviewNote.value = defaults.review_note;
    if (bugTypeValues.includes(defaults.bug_type)) {
      candidateReviewType.value = defaults.bug_type;
      candidateReviewCustomType.value = "";
    } else {
      candidateReviewType.value = customBugTypeValue;
      candidateReviewCustomType.value = defaults.bug_type;
    }
  }
}

async function pollCandidateValidation(runId: string) {
  clearCandidatePoll();
  try {
    const payload = await getCandidateValidationJob(runId);
    candidateValidation.value = payload;
    candidateValidationRunning.value = ["pending", "running"].includes(payload.status);
    if (candidateValidationRunning.value) {
      candidatePollTimer = setTimeout(() => void pollCandidateValidation(runId), 1000);
    }
  } catch (cause) {
    actionError.value = describeError(cause, "候选验证状态读取失败");
    candidateValidationRunning.value = false;
  }
}

async function pollJob(jobId: string) {
  clearPoll();
  try {
    const payload = await getReproJob(jobId);
    job.value = payload;
    reportMarkdown.value = payload.report_markdown || reportMarkdown.value;
    jobRunning.value = payload.status.status !== "finished";
    if (jobRunning.value) pollTimer = setTimeout(() => void pollJob(jobId), 1500);
  } catch (cause) {
    actionError.value = describeError(cause, "复现状态读取失败");
    jobRunning.value = false;
  }
}

async function selectConfirmed(item: ConfirmedBugSummary) {
  selectionRevision += 1;
  const revision = selectionRevision;
  selectedConfirmedId.value = item.id;
  detailLoading.value = true;
  actionError.value = null;
  job.value = null;
  jobRunning.value = false;
  reportMarkdown.value = "";
  reportOpen.value = false;
  clearPoll();
  try {
    const payload = await getConfirmedBug(item.id);
    if (revision !== selectionRevision) return;
    detail.value = payload;
    reportMarkdown.value = "";
    if (payload.latest_repro_job_id) {
      const previousPayload = await getReproJob(payload.latest_repro_job_id);
      if (revision !== selectionRevision) return;
      job.value = previousPayload;
      reportMarkdown.value = previousPayload.report_markdown;
      jobRunning.value = previousPayload.status.status !== "finished";
      if (jobRunning.value) pollTimer = setTimeout(() => void pollJob(previousPayload.job_id), 1500);
    }
  } catch (cause) {
    if (revision === selectionRevision) actionError.value = describeError(cause, "证据详情加载失败");
  } finally {
    if (revision === selectionRevision) detailLoading.value = false;
  }
}

async function selectCandidateCluster(item: CandidateClusterSummary) {
  selectionRevision += 1;
  const revision = selectionRevision;
  selectedCandidateClusterId.value = item.cluster_id;
  detailLoading.value = true;
  actionError.value = null;
  clearCandidatePoll();
  try {
    const payload = await getCandidateCluster(item.cluster_id);
    if (revision !== selectionRevision) return;
    applyCandidateCluster(payload);
    if (payload.latest_validation_job_id && ["pending", "running"].includes(payload.latest_validation?.status ?? "")) {
      candidatePollTimer = setTimeout(() => void pollCandidateValidation(payload.latest_validation_job_id as string), 1000);
    }
  } catch (cause) {
    if (revision === selectionRevision) actionError.value = describeError(cause, "候选簇详情加载失败");
  } finally {
    if (revision === selectionRevision) detailLoading.value = false;
  }
}

async function refreshCandidateCluster(clusterId: string) {
  const [clusterList, payload] = await Promise.all([getCandidateClusters(), getCandidateCluster(clusterId)]);
  candidateClusters.value = clusterList;
  applyCandidateCluster(payload);
}

async function saveCandidateDraft() {
  if (!candidateClusterDetail.value || !candidateDraft.value.trim()) return;
  candidateDraftSaving.value = true;
  actionError.value = null;
  try {
    const payload = await saveCandidateClusterDraft(candidateClusterDetail.value.cluster_id, candidateDraft.value);
    applyCandidateCluster(payload);
  } catch (cause) {
    actionError.value = describeError(cause, "最小复现草稿保存失败");
  } finally {
    candidateDraftSaving.value = false;
  }
}

async function resetCandidateDraft() {
  if (!candidateClusterDetail.value) return;
  candidateDraftSaving.value = true;
  actionError.value = null;
  try {
    const payload = await resetCandidateClusterDraft(candidateClusterDetail.value.cluster_id);
    applyCandidateCluster(payload);
  } catch (cause) {
    actionError.value = describeError(cause, "恢复候选源码失败");
  } finally {
    candidateDraftSaving.value = false;
  }
}

async function validateCandidateDraft() {
  if (!candidateClusterDetail.value || !candidateDraft.value.trim()) return;
  actionError.value = null;
  candidateValidationRunning.value = true;
  try {
    const started = await startCandidateValidation(candidateClusterDetail.value.cluster_id, candidateDraft.value, 60);
    candidateClusterDetail.value = {
      ...candidateClusterDetail.value,
      minimization_draft: candidateDraft.value,
      draft_saved: true,
      draft_modified: candidateDraft.value !== candidateClusterDetail.value.representative_source_code,
      draft_sha256: started.source_sha256,
    };
    await pollCandidateValidation(started.run_id);
  } catch (cause) {
    actionError.value = describeError(cause, "CPU/GPU 候选验证启动失败");
    candidateValidationRunning.value = false;
  }
}

async function confirmCurrentCandidate() {
  if (!candidateClusterDetail.value || !candidateCanConfirm.value) return;
  candidateActionLoading.value = true;
  actionError.value = null;
  try {
    const clusterId = candidateClusterDetail.value.cluster_id;
    const confirmedDetail = await confirmCandidateCluster(clusterId, {
      title: candidateReviewTitle.value.trim(),
      bug_type: candidateReviewFinalType.value,
      review_note: candidateReviewNote.value.trim(),
    });
    confirmed.value = [confirmedDetail.index, ...confirmed.value.filter((item) => item.id !== confirmedDetail.index.id)];
    candidateClusters.value = candidateClusters.value.filter((item) => item.cluster_id !== clusterId);
    candidateClusterDetail.value = null;
    selectedCandidateClusterId.value = null;
    sourceKind.value = "confirmed";
    selectedConfirmedId.value = confirmedDetail.meta.id;
    detail.value = confirmedDetail;
    job.value = null;
    reportMarkdown.value = confirmedDetail.report_markdown;
  } catch (cause) {
    actionError.value = describeError(cause, "候选确认为 Bug 失败");
  } finally {
    candidateActionLoading.value = false;
  }
}

function requestDelete(target: DeleteTarget) {
  deleteTarget.value = target;
  deleteConfirmation.value = "";
}

function closeDeleteDialog() {
  deleteTarget.value = null;
  deleteConfirmation.value = "";
}

async function confirmDeleteRecord() {
  const target = deleteTarget.value;
  if (!target || deleteConfirmation.value !== target.id) return;
  candidateActionLoading.value = true;
  actionError.value = null;
  try {
    if (target.kind === "candidate") {
      await deleteCandidateCluster(target.id, deleteConfirmation.value);
      candidateClusters.value = candidateClusters.value.filter((item) => item.cluster_id !== target.id);
      candidateClusterDetail.value = null;
      selectedCandidateClusterId.value = null;
      if (candidateClusters.value[0]) await selectCandidateCluster(candidateClusters.value[0]);
    } else {
      await deleteConfirmedBug(target.id, deleteConfirmation.value);
      confirmed.value = confirmed.value.filter((item) => item.id !== target.id);
      detail.value = null;
      selectedConfirmedId.value = null;
      if (confirmed.value[0]) await selectConfirmed(confirmed.value[0]);
    }
    closeDeleteDialog();
  } catch (cause) {
    actionError.value = describeError(cause, "删除记录失败");
  } finally {
    candidateActionLoading.value = false;
  }
}

function switchSource(next: SourceKind) {
  sourceKind.value = next;
  query.value = "";
  if (next === "candidate" && selectedCandidateClusterId.value === null && candidateClusters.value[0]) void selectCandidateCluster(candidateClusters.value[0]);
}

function toggleMode(mode: ExecutionMode) {
  selectedModes.value = selectedModes.value.includes(mode)
    ? selectedModes.value.filter((item) => item !== mode)
    : [...selectedModes.value, mode];
}

async function startRepro() {
  if (!detail.value || selectedModes.value.length === 0) return;
  actionError.value = null;
  jobRunning.value = true;
  try {
    const started = await reproduceConfirmedBug(detail.value.meta.id, { modes: selectedModes.value, timeout: 60 });
    await pollJob(started.job_id);
  } catch (cause) {
    actionError.value = describeError(cause, "复现任务启动失败");
    jobRunning.value = false;
  }
}

async function openOrGenerateReport() {
  if (!job.value || job.value.status.status !== "finished") return;
  reportLoading.value = true;
  actionError.value = null;
  try {
    const payload = job.value.report_exists
      ? await getReproReport(job.value.job_id)
      : await generateReproReport(job.value.job_id);
    reportMarkdown.value = payload.report_markdown;
    reportOpen.value = true;
    job.value = { ...job.value, report_exists: true, report_markdown: payload.report_markdown, report_path: payload.report_path };
  } catch (cause) {
    actionError.value = describeError(cause, "证据报告读取失败");
  } finally {
    reportLoading.value = false;
  }
}

async function load() {
  loading.value = true;
  error.value = null;
  try {
    const [bugList, clusterList, environment] = await Promise.all([getConfirmedBugs(), getCandidateClusters(), getEnvironment()]);
    confirmed.value = bugList;
    candidateClusters.value = clusterList;
    runtimeEnvironment.value = environment;
    if (bugList[0]) await selectConfirmed(bugList[0]);
  } catch (cause) {
    error.value = describeError(cause, "证据库加载失败");
  } finally {
    loading.value = false;
  }
}

onMounted(() => void load());
onBeforeUnmount(() => {
  clearPoll();
  clearCandidatePoll();
});
</script>

<template>
  <section class="bug-replay-view" aria-labelledby="bug-replay-title">
    <header class="bug-replay-view__page-head">
      <div class="bug-replay-view__title-lockup">
        <span class="bug-replay-view__page-symbol" aria-hidden="true">!</span>
        <div class="bug-replay-view__title-copy">
          <p class="bug-replay-view__eyebrow">Evidence Validation · Deterministic Replay</p>
          <h1 id="bug-replay-title">缺陷复现与证据验证</h1>
          <p>在当前环境执行最小程序，核对框架行为并固化运行证据</p>
        </div>
      </div>
      <div class="bug-replay-view__count">
        <span class="bug-replay-view__count-item bug-replay-view__count-item--confirmed">已确认 <b>{{ confirmed.length }}</b></span>
        <span class="bug-replay-view__count-item bug-replay-view__count-item--candidate">候选簇 <b>{{ candidateClusterStats.total }}</b></span>
        <span class="bug-replay-view__count-item bug-replay-view__count-item--minimize">待审核 <b>{{ candidateClusterStats.total }}</b></span>
      </div>
    </header>

    <div v-if="loading" class="bug-replay-view__message">正在读取证据库</div>
    <div v-else-if="error" class="bug-replay-view__message bug-replay-view__message--error">{{ error }} <button type="button" @click="load">重试</button></div>

    <div v-else class="bug-replay-view__layout">
      <aside class="bug-replay-view__master bug-replay-view__master--page-flow">
        <div class="bug-replay-view__master-frame">
          <div class="bug-replay-view__source-tabs" role="tablist" aria-label="证据来源">
            <button type="button" :class="{ active: sourceKind === 'confirmed' }" @click="switchSource('confirmed')">已确认</button>
            <button type="button" :class="{ active: sourceKind === 'candidate' }" @click="switchSource('candidate')">候选审核</button>
          </div>
          <input v-model="query" type="search" placeholder="搜索 API / 错误类型 / 状态" aria-label="搜索证据" />

          <div v-if="sourceKind === 'confirmed'" class="bug-replay-view__list bug-replay-view__list--contained">
            <button v-for="item in filteredConfirmed" :key="item.id" type="button" :class="{ active: selectedConfirmedId === item.id }" @click="selectConfirmed(item)">
              <span><small>{{ item.display_id }}</small><em>{{ item.framework }}</em></span>
              <b>{{ item.api }}</b><i>{{ item.bug_type }}</i>
            </button>
            <p v-if="filteredConfirmed.length === 0">未找到匹配证据</p>
          </div>
          <div v-else class="bug-replay-view__list bug-replay-view__list--contained">
            <button v-for="item in filteredCandidateClusters" :key="item.cluster_id" type="button" :class="{ active: selectedCandidateClusterId === item.cluster_id }" @click="selectCandidateCluster(item)">
              <span><small>{{ item.api }}</small><em>{{ item.member_count }} files</em></span>
              <b>{{ item.bug_pattern }}</b><i>代表程序 {{ item.representative.source_name }}</i>
              <strong :class="`bug-replay-view__cluster-badge bug-replay-view__cluster-badge--${item.cluster_status}`">{{ clusterStatusLabel(item.cluster_status) }}</strong>
            </button>
            <p v-if="filteredCandidateClusters.length === 0">暂无候选簇</p>
          </div>
        </div>
      </aside>

      <main class="bug-replay-view__detail">
        <p v-if="detailLoading" class="bug-replay-view__message">正在读取详情</p>

        <template v-else-if="sourceKind === 'confirmed' && detail">
          <section class="bug-replay-view__panel bug-replay-view__case-head">
            <div class="bug-replay-view__case-title">
              <div><small>{{ detail.display_id }} · {{ detail.meta.framework }}</small><h2>{{ detail.meta.title }}</h2><code>{{ detail.meta.api }}</code></div>
              <div class="bug-replay-view__tags">
                <span class="bug-replay-view__tag bug-replay-view__tag--confirmed">已确认</span>
                <span v-if="detail.meta.minimized" class="bug-replay-view__tag bug-replay-view__tag--minimized">已最小化</span>
                <button
                  v-if="detail.index.deletable"
                  data-testid="delete-confirmed-bug"
                  type="button"
                  class="bug-replay-view__delete-trigger"
                  @click="requestDelete({ kind: 'confirmed', id: detail.meta.id, label: detail.meta.title })"
                >删除</button>
                <span v-else class="bug-replay-view__tag bug-replay-view__tag--review">基线只读</span>
              </div>
            </div>
            <div class="bug-replay-view__verdict" :class="`bug-replay-view__verdict--${verdict.state}`">
              <strong>{{ verdict.state === "reproduced" ? "✓" : verdict.state === "running" ? "…" : "i" }}</strong>
              <div><b>{{ verdict.title }}</b><p>{{ verdict.detail }}</p></div><code>{{ verdict.code }}</code>
            </div>
          </section>

          <section class="bug-replay-view__panel bug-replay-view__reason">
            <header><span>WHY</span><div><b>问题依据</b><small>预期行为与实际行为对照</small></div><em>{{ detail.meta.bug_type }}</em></header>
            <div class="bug-replay-view__behavior">
              <article><small>Expected · 预期行为</small><b>框架应当给出可处理结果</b><p>{{ detail.meta.expected }}</p></article>
              <article class="observed"><small>Observed · 实际行为</small><b>当前归档异常行为</b><p>{{ detail.meta.observed }}</p></article>
            </div>
          </section>

          <section class="bug-replay-view__evidence-workbench" aria-label="最小复现程序与实际输出">
            <section class="bug-replay-view__panel bug-replay-view__code-panel bug-replay-view__evidence-pane">
              <header><div><b>最小复现程序</b><small>repro.py</small></div><span>PY</span></header>
              <div class="bug-replay-view__evidence-scroll"><pre>{{ detail.repro_code }}</pre></div>
            </section>
            <section class="bug-replay-view__panel bug-replay-view__code-panel bug-replay-view__evidence-pane">
              <header><div><b>当前环境实际输出</b><small>CURRENT RUN OUTPUT</small></div><span>LOG</span></header>
              <div class="bug-replay-view__evidence-scroll"><pre>{{ currentOutput }}</pre></div>
            </section>
          </section>

          <section class="bug-replay-view__confirmed-tools">
            <section class="bug-replay-view__panel bug-replay-view__confirmed-tool bug-replay-view__confirmed-tool--environment" data-tool="environment">
              <header class="bug-replay-view__tool-head"><span>ENV</span><div><b>当前环境</b><small>页面加载时实时采集</small></div><em>{{ environmentRows.length ? "已连接" : "不可用" }}</em></header>
              <dl v-if="environmentRows.length"><div v-for="[label, value] in environmentRows" :key="label"><dt>{{ label }}</dt><dd :title="value">{{ value }}</dd></div></dl>
              <p v-else class="bug-replay-view__tool-empty">暂未采集到当前运行环境。</p>
            </section>

            <section class="bug-replay-view__panel bug-replay-view__confirmed-tool bug-replay-view__confirmed-tool--execution" data-tool="execution">
              <header class="bug-replay-view__tool-head"><span>RUN</span><div><b>执行配置</b><small>选择独立复现进程</small></div></header>
              <div class="bug-replay-view__profiles">
                <button type="button" :class="{ active: selectedModes.includes('cpu') }" @click="toggleMode('cpu')"><b>CPU 独立进程</b><small>CUDA_VISIBLE_DEVICES=""</small></button>
                <button type="button" :class="{ active: selectedModes.includes('gpu:0') }" @click="toggleMode('gpu:0')"><b>GPU 0 独立进程</b><small>CUDA_VISIBLE_DEVICES="0"</small></button>
              </div>
              <button type="button" class="bug-replay-view__primary" :disabled="jobRunning || selectedModes.length === 0" @click="startRepro">{{ jobRunning ? "复现运行中" : "运行当前复现" }}</button>
            </section>

            <section class="bug-replay-view__panel bug-replay-view__confirmed-tool bug-replay-view__confirmed-tool--report" data-tool="report">
              <header class="bug-replay-view__tool-head"><span>RPT</span><div><b>证据报告</b><small>当前环境运行证据</small></div></header>
              <p class="bug-replay-view__report-state" :class="{ 'bug-replay-view__report-state--ready': Boolean(reportMarkdown) }">{{ reportMarkdown ? "报告已归档，后续读取不会覆盖" : "完成一次当前环境复现后生成报告" }}</p>
              <div class="bug-replay-view__report-actions">
                <button type="button" :disabled="!job || job.status.status !== 'finished' || reportLoading" @click="openOrGenerateReport">{{ reportMarkdown ? "查看报告" : "生成报告" }}</button>
                <a v-if="reportMarkdown" :href="reportHref" :download="`${detail.display_id}-report.md`">下载 Markdown</a>
              </div>
            </section>
          </section>

          <section v-if="reportOpen" class="bug-replay-view__panel bug-replay-view__report"><header><b>当前环境证据报告</b><button type="button" @click="reportOpen = false">收起</button></header><pre>{{ reportMarkdown }}</pre></section>
          <p v-if="actionError" class="bug-replay-view__action-error">{{ actionError }}</p>
        </template>

        <template v-else-if="sourceKind === 'candidate' && candidateClusterDetail">
          <section class="bug-replay-view__panel bug-replay-view__case-head bug-replay-view__cluster-head">
            <div class="bug-replay-view__case-title">
              <div>
                <small>{{ candidateClusterDetail.cluster_id }} · {{ candidateClusterDetail.lib }}</small>
                <h2>{{ candidateClusterDetail.api }} 候选问题簇</h2>
                <code>{{ candidateClusterDetail.bug_pattern }}</code>
              </div>
              <div class="bug-replay-view__tags">
                <span>同类程序 {{ candidateClusterDetail.member_count }}</span>
                <span>已过滤 {{ candidateClusterDetail.excluded_count }}</span>
              </div>
            </div>
            <div class="bug-replay-view__cluster-pipeline">
              <article class="done"><small>01 候选</small><b>已归集</b></article>
              <article class="done"><small>02 分析</small><b>人工审核</b></article>
              <article :class="{ done: candidateValidationFinished, current: !candidateValidationFinished }"><small>03 复现</small><b>{{ candidateValidationFinished ? "已完成" : "待运行" }}</b></article>
              <article :class="{ current: candidateValidationFinished }"><small>04 确认</small><b>{{ candidateValidationFinished ? "等待判断" : "未就绪" }}</b></article>
            </div>
          </section>

          <section class="bug-replay-view__panel bug-replay-view__candidate-reason">
            <article><small>聚类依据</small><b>同一 API + 同一异常模式</b><p>{{ candidateClusterDetail.bug_pattern }}</p></article>
            <article><small>代表选择</small><b>优先推荐、代码短、日志清晰</b><p>当前代表程序 {{ candidateClusterDetail.representative.source_name }}，评分 {{ candidateClusterDetail.representative.score }}。</p></article>
            <article><small>确认条件</small><b>repro.py 独立验证通过</b><p>候选不会自动升级为已确认 Bug，需要人工裁剪最小复现并重新运行。</p></article>
          </section>

          <section class="bug-replay-view__candidate-workbench">
            <section class="bug-replay-view__panel bug-replay-view__code-panel bug-replay-view__candidate-file bug-replay-view__candidate-file--wide">
              <header class="bug-replay-view__file-head">
                <span class="bug-replay-view__file-icon">SRC</span>
                <div><b>候选代表源码</b><span data-testid="candidate-source-path">{{ candidateClusterDetail.representative.source_path }}</span></div>
              </header>
              <div class="bug-replay-view__candidate-code"><pre>{{ candidateClusterDetail.representative_source_code || "源文件当前不可用" }}</pre></div>
            </section>

            <section class="bug-replay-view__panel bug-replay-view__code-panel bug-replay-view__candidate-file bug-replay-view__candidate-file--wide">
              <header class="bug-replay-view__file-head">
                <span class="bug-replay-view__file-icon">PY</span>
                <div>
                  <b>人工整理 repro.py</b>
                  <span>{{ candidateDraftDirty ? "存在未保存修改" : candidateClusterDetail.draft_saved ? "草稿已持久化" : "由候选源码初始化" }}</span>
                </div>
              </header>
              <textarea
                v-model="candidateDraft"
                data-testid="candidate-draft-editor"
                class="bug-replay-view__candidate-editor"
                aria-label="人工最小复现代码"
                spellcheck="false"
              />
              <footer class="bug-replay-view__draft-actions">
                <span>每次删除一处无关语句，再运行 CPU + GPU 验证；不能复现就撤销本次删除。</span>
                <div>
                  <button data-testid="reset-candidate-draft" type="button" :disabled="candidateDraftSaving || candidateValidationRunning" @click="resetCandidateDraft">恢复原始代码</button>
                  <button data-testid="save-candidate-draft" type="button" :disabled="candidateDraftSaving || !candidateDraftDirty" @click="saveCandidateDraft">{{ candidateDraftSaving ? "保存中" : "保存草稿" }}</button>
                  <button data-testid="validate-candidate-draft" type="button" class="bug-replay-view__primary" :disabled="candidateValidationRunning || !candidateDraft.trim()" @click="validateCandidateDraft">{{ candidateValidationRunning ? "验证运行中" : "CPU + GPU 验证" }}</button>
                </div>
              </footer>
            </section>

            <section class="bug-replay-view__panel bug-replay-view__candidate-validation">
              <header>
                <div><b>当前草稿验证结果</b><span>CPU 与 GPU 0 使用两个独立子进程</span></div>
                <strong :class="{ done: candidateValidationFinished }">{{ candidateValidationRunning ? "运行中" : candidateValidationFinished ? "验证完成" : "尚未验证" }}</strong>
              </header>
              <div class="bug-replay-view__validation-grid">
                <article>
                  <div><b>CPU</b><span>CUDA_VISIBLE_DEVICES=""</span></div>
                  <pre data-testid="candidate-cpu-output">{{ candidateCpuOutput }}</pre>
                </article>
                <article>
                  <div><b>GPU 0</b><span>CUDA_VISIBLE_DEVICES="0"</span></div>
                  <pre data-testid="candidate-gpu-output">{{ candidateGpuOutput }}</pre>
                </article>
              </div>
            </section>

            <section class="bug-replay-view__panel bug-replay-view__review-card bug-replay-view__review-card--full">
              <header class="bug-replay-view__review-head">
                <span class="bug-replay-view__file-icon">REV</span>
                <div><b>人工判断</b><span>完成复现后确认是 Bug，或输入 ID 删除候选</span></div>
              </header>
              <div class="bug-replay-view__review-body">
                <article class="bug-replay-view__candidate-note">
                  <b>{{ candidateValidationFinished ? "复现已完成，等待人工判断" : "请先运行 CPU + GPU 复现" }}</b>
                  <p>系统不会根据返回码自动确认框架 Bug，最终结论由审核者根据源码和两端输出作出。</p>
                </article>
                <div class="bug-replay-view__review-field bug-replay-view__review-field--title">
                  <label for="candidate-review-title">Bug 标题</label>
                  <input id="candidate-review-title" v-model="candidateReviewTitle" data-testid="candidate-review-title" type="text" maxlength="200" />
                </div>
                <div class="bug-replay-view__review-field bug-replay-view__review-field--type">
                  <label for="candidate-review-type">问题类型</label>
                  <select id="candidate-review-type" v-model="candidateReviewType" data-testid="candidate-review-type">
                    <optgroup v-for="group in bugTypeGroups" :key="group.label" :label="group.label">
                      <option v-for="option in group.options" :key="option.value" :value="option.value">{{ option.label }}</option>
                    </optgroup>
                    <option :value="customBugTypeValue">其他 / 自定义</option>
                  </select>
                  <input v-if="candidateReviewType === customBugTypeValue" v-model="candidateReviewCustomType" data-testid="candidate-review-custom-type" type="text" maxlength="160" placeholder="输入自定义问题类型" />
                </div>
                <div class="bug-replay-view__review-field bug-replay-view__review-field--note">
                  <label for="candidate-review-note">人工判断说明</label>
                  <textarea id="candidate-review-note" v-model="candidateReviewNote" data-testid="candidate-review-note" maxlength="4000" />
                </div>
              </div>
              <footer class="bug-replay-view__review-footer">
                <div class="bug-replay-view__review-actions bug-replay-view__review-actions--decision">
                  <button data-testid="delete-candidate" type="button" class="bug-replay-view__danger" :disabled="candidateActionLoading" @click="requestDelete({ kind: 'candidate', id: candidateClusterDetail.cluster_id, label: `${candidateClusterDetail.api} 候选` })">删除候选</button>
                  <button data-testid="confirm-candidate-bug" type="button" class="bug-replay-view__primary" :disabled="!candidateCanConfirm || candidateActionLoading" :title="candidateCanConfirm ? '人工确认后写入已确认 Bug 库' : '需要保存代码并完成 CPU + GPU 复现'" @click="confirmCurrentCandidate">确认为 Bug</button>
                </div>
              </footer>
            </section>
          </section>
          <p v-if="actionError" class="bug-replay-view__action-error">{{ actionError }}</p>
        </template>

        <section v-else-if="sourceKind === 'candidate'" class="bug-replay-view__panel bug-replay-view__candidate-empty">
          <span aria-hidden="true">Ø</span>
          <div><h2>暂无可审核的候选簇</h2><p>当前环境中尚未归集到候选问题。</p></div>
        </section>
      </main>
    </div>

    <div v-if="deleteTarget" class="bug-replay-view__dialog-backdrop" role="presentation">
      <section class="bug-replay-view__delete-dialog" role="dialog" aria-modal="true" aria-labelledby="delete-dialog-title">
        <header><span>DEL</span><div><b id="delete-dialog-title">确认删除</b><small>{{ deleteTarget.label }}</small></div></header>
        <p>删除后将从当前列表移除。请输入下面的完整 ID 继续：</p>
        <code>{{ deleteTarget.id }}</code>
        <input v-model="deleteConfirmation" data-testid="delete-id-input" type="text" autocomplete="off" :placeholder="deleteTarget.id" aria-label="输入待删除记录 ID" />
        <footer>
          <button type="button" @click="closeDeleteDialog">取消</button>
          <button data-testid="confirm-delete" type="button" class="bug-replay-view__danger" :disabled="deleteConfirmation !== deleteTarget.id || candidateActionLoading" @click="confirmDeleteRecord">确认删除</button>
        </footer>
      </section>
    </div>
  </section>
</template>

<style scoped>
.bug-replay-view { --candidate-columns:minmax(0,1.1fr) minmax(0,1fr) minmax(17rem,1fr); display:grid;gap:.75rem; }
.bug-replay-view__page-head { display:flex;align-items:center;justify-content:space-between;gap:1.1rem;margin-bottom:.1rem }.bug-replay-view__title-lockup{display:flex;align-items:center;gap:.8rem}.bug-replay-view__page-symbol{width:2.75rem;height:2.75rem;display:grid;place-items:center;flex:none;border:1px solid #f2d0d6;border-radius:8px;background:var(--tg-red-bg);color:var(--tg-red-text);font:820 .82rem/1 ui-monospace,monospace;box-shadow:inset 0 0 0 4px rgba(255,255,255,.66),0 7px 16px rgba(189,63,82,.07)}.bug-replay-view__title-copy{padding-left:.75rem;border-left:2px solid var(--tg-red-text)}.bug-replay-view__eyebrow{margin:0 0 .3rem;color:var(--tg-red-text);font:760 .5rem/1 ui-monospace,monospace;text-transform:uppercase}.bug-replay-view h1{margin:0;font-size:1.45rem;line-height:1.15;font-weight:790}.bug-replay-view__title-copy>p:last-child{margin:.3rem 0 0;color:var(--tg-text-muted);font-size:.63rem}.bug-replay-view__count{display:flex;align-items:stretch;gap:.38rem;padding:.3rem;border:1px solid #dce5f1;border-radius:8px;background:rgba(255,255,255,.88);box-shadow:0 6px 18px rgba(41,63,101,.05)}.bug-replay-view__count-item{min-width:4.5rem;display:flex;align-items:center;justify-content:center;gap:.28rem;padding:.42rem .52rem;border:1px solid transparent;border-radius:6px;font-size:.48rem;font-weight:690;white-space:nowrap}.bug-replay-view__count-item::before{width:.38rem;height:.38rem;content:"";flex:none;border-radius:50%;background:currentColor;box-shadow:0 0 0 3px rgba(255,255,255,.65)}.bug-replay-view__count-item b{margin-left:.08rem;font-size:.9rem;line-height:1;font-weight:820}.bug-replay-view__count-item--confirmed{border-color:#b9e0ce;background:var(--tg-green-bg);color:var(--tg-green-text)}.bug-replay-view__count-item--candidate{border-color:#efd59f;background:var(--tg-amber-bg);color:var(--tg-amber-text)}.bug-replay-view__count-item--minimize{border-color:#c9dcff;background:var(--tg-action-soft);color:var(--tg-action-strong)}
.bug-replay-view__layout{display:grid;grid-template-columns:15.6rem minmax(0,1fr);gap:.75rem;align-items:stretch;min-height:clamp(24rem,calc(100vh - var(--tg-header-height) - 8rem),46rem)}.bug-replay-view__master,.bug-replay-view__panel{border:1px solid var(--tg-border);border-radius:var(--tg-radius);background:#fff;box-shadow:var(--tg-shadow)}.bug-replay-view__master{min-height:0;overflow:hidden}.bug-replay-view__master--page-flow{position:relative}.bug-replay-view__master-frame{position:absolute;inset:0;display:grid;grid-template-rows:auto auto minmax(0,1fr);min-height:0;padding:.75rem;overflow:hidden}.bug-replay-view__source-tabs{display:grid;grid-template-columns:1fr 1fr;gap:3px;padding:3px;border:1px solid var(--tg-border);border-radius:6px;background:#f5f7fb}.bug-replay-view__source-tabs button{height:1.95rem;border:0;border-radius:4px;background:transparent;color:var(--tg-text-muted);font-size:.56rem;font-weight:740}.bug-replay-view__source-tabs button.active{background:#fff;color:var(--tg-action-strong);box-shadow:0 2px 8px rgba(36,58,98,.08)}.bug-replay-view__master-frame>input{width:100%;height:2.1rem;margin:.55rem 0;border:1px solid #d6deeb;border-radius:5px;padding:0 .65rem;outline:none;font-size:.61rem}.bug-replay-view__master-frame>input:focus{border-color:var(--tg-action);box-shadow:0 0 0 3px rgba(37,99,235,.1)}.bug-replay-view__list{display:grid;gap:.2rem;max-height:none}.bug-replay-view__list--contained{min-height:0;overflow:auto;overscroll-behavior:contain;scrollbar-gutter:stable;align-content:start}.bug-replay-view__list>button{width:100%;display:grid;gap:.3rem;padding:.62rem;border:0;border-left:3px solid transparent;border-radius:4px;background:transparent;text-align:left}.bug-replay-view__list>button:hover{background:#f7f9fd}.bug-replay-view__list>button.active{border-left-color:var(--tg-action);background:var(--tg-action-soft)}.bug-replay-view__list span{display:flex;justify-content:space-between;gap:.4rem;color:var(--tg-text-muted);font:.45rem/1 ui-monospace,monospace}.bug-replay-view__list em{font-style:normal}.bug-replay-view__list b{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font:.66rem/1.3 ui-monospace,monospace}.bug-replay-view__list i{color:var(--tg-text-muted);font-size:.5rem;font-style:normal}.bug-replay-view__list>p{margin:.8rem;text-align:center;color:var(--tg-text-muted);font-size:.58rem}.bug-replay-view__detail{display:grid;gap:.75rem;min-width:0}.bug-replay-view__candidate-empty{min-height:100%;display:flex;align-items:center;justify-content:center;gap:.75rem;padding:1.2rem;text-align:left}.bug-replay-view__candidate-empty>span{width:2.2rem;height:2.2rem;display:grid;place-items:center;flex:none;border:1px solid #d8e2f1;border-radius:7px;background:#f4f7fb;color:#7b8aa3;font:800 .72rem/1 ui-monospace,monospace}.bug-replay-view__candidate-empty h2{margin:0;font-size:.76rem}.bug-replay-view__candidate-empty p{margin:.25rem 0 0;color:var(--tg-text-muted);font-size:.55rem}.bug-replay-view__message{padding:1rem;border:1px solid var(--tg-border);border-radius:8px;background:#fff;color:var(--tg-text-muted);font-size:.65rem}.bug-replay-view__message--error,.bug-replay-view__action-error{color:var(--tg-red-text)}
.bug-replay-view__case-head,.bug-replay-view__reason{padding:1rem 1.1rem}.bug-replay-view__case-title{display:flex;align-items:flex-start;justify-content:space-between;gap:.9rem}.bug-replay-view__case-title small{color:var(--tg-action);font:.5rem/1 ui-monospace,monospace}.bug-replay-view__case-title h2{margin:.38rem 0 .32rem;font-size:1.05rem}.bug-replay-view__case-title code{color:var(--tg-text-muted);font:.62rem/1.3 ui-monospace,monospace}.bug-replay-view__tags{display:flex;flex-wrap:wrap;justify-content:flex-end;gap:.35rem}.bug-replay-view__tag{padding:.3rem .48rem;border:1px solid transparent;border-radius:4px;font-size:.5rem;font-weight:760;box-shadow:inset 0 1px 0 rgba(255,255,255,.65)}.bug-replay-view__tag--confirmed{border-color:#b8dfce;background:var(--tg-green-bg);color:var(--tg-green-text)}.bug-replay-view__tag--minimized{border-color:#c8d9fb;background:var(--tg-action-soft);color:var(--tg-action-strong)}.bug-replay-view__tag--review{border-color:#efd39c;background:var(--tg-amber-bg);color:var(--tg-amber-text)}.bug-replay-view__verdict{display:grid;grid-template-columns:auto minmax(0,1fr) auto;align-items:center;gap:.75rem;margin-top:.85rem;padding:.72rem .82rem;border:1px solid #e8d2ab;border-left:4px solid #c98624;border-radius:5px;background:#fff8eb}.bug-replay-view__verdict>strong{width:2rem;height:2rem;display:grid;place-items:center;border-radius:50%;background:#c98624;color:#fff}.bug-replay-view__verdict b{font-size:.68rem}.bug-replay-view__verdict p{margin:.22rem 0 0;color:#6f6250;font-size:.55rem}.bug-replay-view__verdict>code{padding:.3rem .42rem;border-radius:4px;background:#fff;color:#9a671d;font:.5rem/1 ui-monospace,monospace}.bug-replay-view__verdict--reproduced{border-color:#99d4bd;border-left-color:#117a58;background:#e8f7f0;box-shadow:inset 0 0 0 1px rgba(17,122,88,.03)}.bug-replay-view__verdict--reproduced>strong{background:#117a58}.bug-replay-view__verdict--reproduced b,.bug-replay-view__verdict--reproduced>code{color:#0d684b}.bug-replay-view__verdict--reproduced p{color:#426c5d}.bug-replay-view__verdict--running{border-color:#b9cff6;border-left-color:var(--tg-action);background:#edf4ff}.bug-replay-view__verdict--running>strong{background:var(--tg-action)}.bug-replay-view__verdict--review{border-color:#dccaa8;border-left-color:#a76b16;background:#fff8eb}.bug-replay-view__verdict--review>strong{background:#a76b16}
.bug-replay-view__reason{border-left:3px solid #d5deec}.bug-replay-view__reason>header{display:flex;align-items:center;gap:.55rem;margin-bottom:.72rem}.bug-replay-view__reason>header>span{width:1.8rem;height:1.8rem;display:grid;place-items:center;border-radius:6px;background:#f8e8eb;color:#b23d50;font:800 .45rem/1 ui-monospace,monospace}.bug-replay-view__reason header b{font-size:.76rem}.bug-replay-view__reason header small{display:block;margin-top:.15rem;color:var(--tg-text-muted);font-size:.48rem}.bug-replay-view__reason header em{margin-left:auto;padding:.3rem .42rem;border-radius:4px;background:var(--tg-amber-bg);color:var(--tg-amber-text);font-size:.5rem;font-style:normal;font-weight:730}.bug-replay-view__behavior{display:grid;grid-template-columns:1fr 1fr;gap:.6rem}.bug-replay-view__behavior article{min-height:6rem;padding:.78rem .82rem;border:1px solid #d9e3f0;border-top:3px solid var(--tg-action);border-radius:6px;background:#f7faff}.bug-replay-view__behavior article.observed{border-color:#ecd5da;border-top-color:#b83e52;background:#fff8f9}.bug-replay-view__behavior small{display:block;margin-bottom:.38rem;color:var(--tg-text-muted);font-size:.48rem;font-weight:760;text-transform:uppercase}.bug-replay-view__behavior b{display:block;margin-bottom:.32rem;font-size:.66rem}.bug-replay-view__behavior p{margin:0;color:#4f5d72;font-size:.55rem;line-height:1.55}
.bug-replay-view__code-panel{overflow:hidden}.bug-replay-view__code-panel>header{display:flex;align-items:center;justify-content:space-between;padding:.65rem .85rem;border-bottom:1px solid #293750;background:var(--tg-navy);color:#fff}.bug-replay-view__code-panel>header b{font-size:.61rem}.bug-replay-view__code-panel>header span{color:#a9b6d0;font-size:.48rem}.bug-replay-view__code-panel>header small{display:block;margin-top:.18rem;color:#8fa0bd;font:.43rem/1 ui-monospace,monospace}.bug-replay-view__evidence-workbench{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:.75rem;min-width:0}.bug-replay-view__evidence-pane{height:15rem;display:grid;grid-template-rows:auto minmax(0,1fr);min-width:0}.bug-replay-view__evidence-scroll{min-width:0;min-height:0;overflow:auto;scrollbar-gutter:stable;background:#111a2d}.bug-replay-view__evidence-scroll pre{width:max-content;min-width:100%;min-height:100%;margin:0;padding:.72rem .82rem;color:#dce6f7;font:.53rem/1.52 ui-monospace,monospace;white-space:pre;word-break:normal}.bug-replay-view__candidate-code pre{height:13.6rem;margin:0;padding:.68rem .8rem;overflow:auto;color:#dce6f7;font:.53rem/1.52 ui-monospace,monospace;white-space:pre-wrap;word-break:break-word}.bug-replay-view__candidate-code{background:#111a2d}
.bug-replay-view__confirmed-tools{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr) minmax(0,.9fr);gap:.75rem;align-items:stretch}.bug-replay-view__confirmed-tool{min-width:0;min-height:10.6rem;padding:.78rem;display:grid;grid-template-rows:auto minmax(0,1fr) auto;align-content:start}.bug-replay-view__tool-head{display:flex;align-items:center;gap:.52rem;min-width:0}.bug-replay-view__tool-head>span{width:1.8rem;height:1.8rem;display:grid;place-items:center;flex:none;border:1px solid #c9dcff;border-radius:6px;background:var(--tg-action-soft);color:var(--tg-action-strong);font:800 .4rem/1 ui-monospace,monospace}.bug-replay-view__tool-head>div{min-width:0}.bug-replay-view__tool-head b{display:block;font-size:.63rem}.bug-replay-view__tool-head small{display:block;margin-top:.14rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--tg-text-muted);font-size:.44rem}.bug-replay-view__tool-head em{margin-left:auto;padding:.24rem .38rem;border-radius:4px;background:var(--tg-green-bg);color:var(--tg-green-text);font-size:.45rem;font-style:normal;font-weight:760}.bug-replay-view__confirmed-tool--environment dl{display:grid;grid-template-columns:1fr 1fr;gap:.38rem;margin:.58rem 0 0}.bug-replay-view__confirmed-tool--environment dl>div{min-width:0;padding:.43rem .48rem;border:1px solid #dce5f1;border-left:3px solid #8fb0eb;border-radius:5px;background:#f8faff}.bug-replay-view__confirmed-tool--environment dt{color:var(--tg-text-muted);font-size:.42rem}.bug-replay-view__confirmed-tool--environment dd{margin:.16rem 0 0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:#23314b;font-size:.5rem;font-weight:750}.bug-replay-view__tool-empty{margin:.6rem 0 0;color:var(--tg-text-muted);font-size:.5rem}.bug-replay-view__profiles{display:grid;grid-template-columns:1fr 1fr;gap:.4rem;margin:.58rem 0}.bug-replay-view__profiles button{min-width:0;padding:.48rem .5rem;border:1px solid var(--tg-border);border-radius:5px;background:#fff;text-align:left}.bug-replay-view__profiles button.active{border-color:var(--tg-action);background:var(--tg-action-soft);box-shadow:inset 0 0 0 1px rgba(37,99,235,.08)}.bug-replay-view__profiles b{display:block;font-size:.52rem}.bug-replay-view__profiles small{display:block;margin-top:.18rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--tg-text-muted);font-size:.4rem}.bug-replay-view__primary,.bug-replay-view__report-actions button,.bug-replay-view__report-actions a{height:2.05rem;display:inline-flex;align-items:center;justify-content:center;border:1px solid var(--tg-border);border-radius:5px;background:#fff;color:var(--tg-text-strong);padding:0 .6rem;font-size:.52rem;font-weight:720;text-decoration:none}.bug-replay-view__confirmed-tool .bug-replay-view__primary{width:100%;border-color:var(--tg-action);background:var(--tg-action);color:#fff}.bug-replay-view__report-state{margin:.58rem 0;padding:.52rem;border:1px solid #ead7b7;border-radius:5px;background:#fff8eb;color:#87601f;font-size:.48rem;line-height:1.45}.bug-replay-view__report-state--ready{border-color:#b6dece;background:#edf8f3;color:#326c58}.bug-replay-view__report-actions{display:grid;grid-template-columns:1fr;gap:.38rem}.bug-replay-view__report-actions button,.bug-replay-view__report-actions a{width:100%}.bug-replay-view__report{overflow:hidden}.bug-replay-view__report header{display:flex;justify-content:space-between;padding:.7rem .8rem;border-bottom:1px solid var(--tg-border)}.bug-replay-view__report pre{max-height:22rem;margin:0;padding:1rem;overflow:auto;white-space:pre-wrap;font:.6rem/1.6 ui-monospace,monospace}.bug-replay-view__candidate-note{margin-top:.8rem;padding:.7rem;border:1px solid var(--tg-border);border-left:4px solid var(--tg-amber-text);border-radius:5px;background:var(--tg-amber-bg)}.bug-replay-view__candidate-note b{font-size:.65rem}.bug-replay-view__candidate-note p{margin:.25rem 0 0;color:var(--tg-text-muted);font-size:.55rem}
.bug-replay-view__cluster-badge{width:max-content;padding:.24rem .36rem;border-radius:4px;background:var(--tg-amber-bg);color:var(--tg-amber-text);font-size:.46rem;font-style:normal;font-weight:780}.bug-replay-view__cluster-badge--promoted,.bug-replay-view__cluster-badge--reproduced{background:var(--tg-green-bg);color:var(--tg-green-text)}.bug-replay-view__cluster-badge--rejected{background:var(--tg-red-bg);color:var(--tg-red-text)}
.bug-replay-view__cluster-head{display:grid;grid-template-columns:minmax(0,1fr) minmax(18rem,.58fr);gap:.9rem;align-items:start}.bug-replay-view__cluster-pipeline{display:grid;grid-template-columns:repeat(4,1fr);gap:.35rem}.bug-replay-view__cluster-pipeline article{min-height:3.6rem;padding:.55rem;border:1px solid var(--tg-border);border-radius:6px;background:var(--tg-surface-soft)}.bug-replay-view__cluster-pipeline article.done{border-color:#c9e8d9;background:var(--tg-green-bg)}.bug-replay-view__cluster-pipeline article.current{border-color:#f1d49e;background:var(--tg-amber-bg)}.bug-replay-view__cluster-pipeline small{display:block;color:var(--tg-text-muted);font:.45rem/1 ui-monospace,monospace}.bug-replay-view__cluster-pipeline b{display:block;margin-top:.38rem;font-size:.58rem}
.bug-replay-view__candidate-reason{padding:.85rem 1rem;display:grid;grid-template-columns:var(--candidate-columns);gap:.75rem}.bug-replay-view__candidate-reason article{min-width:0;min-height:5.2rem;padding:.68rem .72rem;border:1px solid var(--tg-border);border-top:3px solid var(--tg-action);border-radius:6px;background:var(--tg-surface-soft)}.bug-replay-view__candidate-reason article:nth-child(2){border-top-color:var(--tg-amber-text)}.bug-replay-view__candidate-reason article:nth-child(3){border-top-color:var(--tg-green)}.bug-replay-view__candidate-reason small{display:block;margin-bottom:.34rem;color:var(--tg-text-muted);font:.46rem/1 ui-monospace,monospace;text-transform:uppercase}.bug-replay-view__candidate-reason b{display:block;margin-bottom:.26rem;font-size:.64rem}.bug-replay-view__candidate-reason p{margin:0;overflow-wrap:anywhere;color:#5e687a;font-size:.53rem;line-height:1.5}
.bug-replay-view__candidate-workbench{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.75rem;align-items:stretch}.bug-replay-view__candidate-workbench>.bug-replay-view__panel{min-width:0}.bug-replay-view__candidate-file{height:20rem;display:grid;grid-template-rows:auto minmax(0,1fr)}.bug-replay-view__candidate-file:has(.bug-replay-view__candidate-editor){grid-template-rows:auto minmax(0,1fr) auto}.bug-replay-view__review-card--full{grid-column:1/-1;height:auto}
.bug-replay-view__code-panel>.bug-replay-view__file-head,.bug-replay-view__review-head{display:grid;grid-template-columns:1.9rem minmax(0,1fr);align-items:start;justify-content:initial;gap:.55rem;padding:.7rem .75rem;border-bottom:1px solid var(--tg-border);background:#fff;color:var(--tg-text-strong)}.bug-replay-view__file-head>div,.bug-replay-view__review-head>div{min-width:0}.bug-replay-view__file-head b,.bug-replay-view__review-head b{display:block;color:var(--tg-text-strong);font-size:.61rem}.bug-replay-view__file-head div>span,.bug-replay-view__review-head div>span{display:block;max-width:none;margin-top:.22rem;overflow-wrap:anywhere;word-break:break-word;white-space:normal;color:var(--tg-text-muted);font:.43rem/1.45 ui-monospace,monospace;text-align:left}.bug-replay-view__file-head>.bug-replay-view__file-icon,.bug-replay-view__review-head>.bug-replay-view__file-icon{width:1.8rem;height:1.8rem;display:grid;place-items:center;border:1px solid #c9dcff;border-radius:6px;background:var(--tg-action-soft);color:var(--tg-action-strong);font:800 .42rem/1 ui-monospace,monospace}
.bug-replay-view__candidate-code{min-width:0;min-height:0;overflow:auto;scrollbar-gutter:stable;background:#111a2d}.bug-replay-view__candidate-file .bug-replay-view__candidate-code pre{width:max-content;min-width:100%;height:auto;min-height:100%;overflow:visible;white-space:pre;word-break:normal}
.bug-replay-view__candidate-editor{width:100%;min-width:0;min-height:0;resize:none;border:0;outline:0;padding:.72rem .8rem;overflow:auto;scrollbar-gutter:stable;background:#111a2d;color:#eef4ff;font:500 .52rem/1.65 SFMono-Regular,ui-monospace,Menlo,Consolas,monospace;tab-size:4;white-space:pre}.bug-replay-view__candidate-editor:focus{box-shadow:inset 0 0 0 2px #4f7fe8}.bug-replay-view__draft-actions{display:grid;gap:.48rem;padding:.55rem .65rem;border-top:1px solid #293750;background:#17223a}.bug-replay-view__draft-actions>span{color:#aab8cf;font-size:.45rem;line-height:1.45}.bug-replay-view__draft-actions>div{display:flex;justify-content:flex-end;gap:.36rem;flex-wrap:wrap}.bug-replay-view__draft-actions button{height:1.8rem;padding:0 .58rem;border:1px solid #44536c;border-radius:5px;background:#22304a;color:#dbe5f5;font-size:.48rem;font-weight:730}.bug-replay-view__draft-actions .bug-replay-view__primary{border-color:var(--tg-action);background:var(--tg-action);color:#fff}.bug-replay-view__draft-actions button:disabled{opacity:.48;cursor:not-allowed}
.bug-replay-view__candidate-validation{grid-column:1/-1;overflow:hidden}.bug-replay-view__candidate-validation>header{display:flex;align-items:center;justify-content:space-between;gap:.75rem;padding:.65rem .75rem;border-bottom:1px solid var(--tg-border);background:#fff}.bug-replay-view__candidate-validation>header div{display:grid;gap:.15rem}.bug-replay-view__candidate-validation>header b{font-size:.62rem}.bug-replay-view__candidate-validation>header span{color:var(--tg-text-muted);font-size:.46rem}.bug-replay-view__candidate-validation>header strong{padding:.25rem .42rem;border-radius:4px;background:var(--tg-surface-soft);color:var(--tg-text-muted);font-size:.48rem}.bug-replay-view__candidate-validation>header strong.done{background:var(--tg-green-bg);color:var(--tg-green-text)}.bug-replay-view__validation-grid{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--tg-border)}.bug-replay-view__validation-grid article{min-width:0;background:#111a2d}.bug-replay-view__validation-grid article>div{display:flex;align-items:center;justify-content:space-between;gap:.5rem;padding:.48rem .65rem;border-bottom:1px solid #293750;color:#fff}.bug-replay-view__validation-grid article>div b{font-size:.54rem}.bug-replay-view__validation-grid article>div span{color:#8fa0bd;font:.43rem/1 ui-monospace,monospace}.bug-replay-view__validation-grid pre{height:9rem;margin:0;padding:.65rem .72rem;overflow:auto;white-space:pre;scrollbar-gutter:stable;color:#dfe8f8;font:500 .48rem/1.55 SFMono-Regular,ui-monospace,Menlo,Consolas,monospace}
.bug-replay-view__review-card{overflow:hidden;display:grid;grid-template-rows:auto minmax(0,1fr) auto;background:linear-gradient(180deg,#fff 0,#fbfcff 100%)}
.bug-replay-view__review-head{border-top:3px solid var(--tg-action)}
.bug-replay-view__review-body{min-height:0;display:grid;grid-template-columns:minmax(12rem,.9fr) minmax(12rem,1fr) minmax(14rem,1.15fr);gap:.65rem;align-content:start;padding:.8rem;overflow:auto;scrollbar-gutter:stable}
.bug-replay-view__review-card .bug-replay-view__candidate-note{grid-column:1/-1;margin:0;padding:.62rem .72rem;background:linear-gradient(90deg,var(--tg-amber-bg),#fffaf0)}
.bug-replay-view__review-field{min-width:0;display:grid;align-content:start;gap:.32rem;padding:.62rem;border:1px solid #dde6f3;border-radius:7px;background:#fff;box-shadow:0 4px 12px rgba(31,48,87,.035)}
.bug-replay-view__review-card label{color:#52617a;font-size:.5rem;font-weight:790}
.bug-replay-view__review-field input,.bug-replay-view__review-field select,.bug-replay-view__review-field textarea{width:100%;min-width:0;border:1px solid #ced9e9;border-radius:5px;background:#f9fbff;color:var(--tg-text-strong);outline:0;font-size:.54rem;line-height:1.45;transition:border-color .15s,box-shadow .15s,background .15s}
.bug-replay-view__review-field input,.bug-replay-view__review-field select{height:2.25rem;padding:0 .58rem}
.bug-replay-view__review-field textarea{height:4.85rem;resize:vertical;padding:.55rem .58rem}
.bug-replay-view__review-field input:focus,.bug-replay-view__review-field select:focus,.bug-replay-view__review-field textarea:focus{border-color:var(--tg-action);background:#fff;box-shadow:0 0 0 3px rgba(37,99,235,.1)}
.bug-replay-view__review-field--type{gap:.38rem}
.bug-replay-view__review-footer{padding:.65rem .75rem;border-top:1px solid var(--tg-border);background:#f8faff}.bug-replay-view__review-actions{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:.4rem}.bug-replay-view__review-actions button{height:2rem;border:1px solid var(--tg-border);border-radius:5px;background:#fff;color:var(--tg-text-strong);font-size:.52rem;font-weight:730}.bug-replay-view__review-actions button:first-child{border-color:#ebc6cd;color:var(--tg-red-text)}.bug-replay-view__review-actions .bug-replay-view__primary{border-color:var(--tg-action);background:var(--tg-action);color:#fff}.bug-replay-view__review-actions button:disabled{cursor:not-allowed;opacity:.56}
.bug-replay-view__review-actions--decision{grid-template-columns:minmax(0,.7fr) minmax(0,1.3fr);max-width:30rem;margin-left:auto}.bug-replay-view__danger,.bug-replay-view__delete-trigger{border-color:#e4aeb8!important;background:#fff4f6!important;color:var(--tg-red-text)!important}.bug-replay-view__delete-trigger{height:1.75rem;padding:0 .55rem;border:1px solid;border-radius:5px;font-size:.5rem;font-weight:760}.bug-replay-view__dialog-backdrop{position:fixed;inset:0;z-index:80;display:grid;place-items:center;padding:1rem;background:rgba(15,24,43,.48);backdrop-filter:blur(2px)}.bug-replay-view__delete-dialog{width:min(26rem,100%);padding:.9rem;border:1px solid #e4c1c8;border-radius:8px;background:#fff;box-shadow:0 24px 60px rgba(18,29,49,.25)}.bug-replay-view__delete-dialog>header{display:flex;align-items:center;gap:.55rem}.bug-replay-view__delete-dialog>header>span{width:2rem;height:2rem;display:grid;place-items:center;border-radius:6px;background:var(--tg-red-bg);color:var(--tg-red-text);font:800 .48rem/1 ui-monospace,monospace}.bug-replay-view__delete-dialog header b{display:block;font-size:.72rem}.bug-replay-view__delete-dialog header small{display:block;margin-top:.16rem;color:var(--tg-text-muted);font-size:.48rem}.bug-replay-view__delete-dialog>p{margin:.8rem 0 .42rem;color:#59667a;font-size:.56rem;line-height:1.5}.bug-replay-view__delete-dialog>code{display:block;padding:.5rem .58rem;border:1px solid #edd3d8;border-radius:5px;background:#fff7f8;color:#9f3144;font:.5rem/1.4 ui-monospace,monospace;overflow-wrap:anywhere}.bug-replay-view__delete-dialog>input{width:100%;height:2.2rem;margin-top:.55rem;border:1px solid #d7dfeb;border-radius:5px;padding:0 .6rem;outline:0;font:500 .54rem/1 ui-monospace,monospace}.bug-replay-view__delete-dialog>input:focus{border-color:#c55367;box-shadow:0 0 0 3px rgba(197,83,103,.1)}.bug-replay-view__delete-dialog>footer{display:flex;justify-content:flex-end;gap:.4rem;margin-top:.75rem}.bug-replay-view__delete-dialog>footer button{height:2rem;padding:0 .7rem;border:1px solid var(--tg-border);border-radius:5px;background:#fff;font-size:.52rem;font-weight:740}.bug-replay-view__delete-dialog>footer button:disabled{opacity:.48;cursor:not-allowed}
@media(max-width:900px){.bug-replay-view__layout{grid-template-columns:13.5rem minmax(0,1fr)}.bug-replay-view__cluster-head,.bug-replay-view__candidate-workbench{grid-template-columns:1fr}.bug-replay-view__candidate-reason{grid-template-columns:1fr}.bug-replay-view__candidate-file{height:20rem}.bug-replay-view__review-card--full,.bug-replay-view__candidate-validation{grid-column:auto}.bug-replay-view__validation-grid{grid-template-columns:1fr}.bug-replay-view__review-body{grid-template-columns:1fr 1fr}.bug-replay-view__review-actions{grid-template-columns:1fr 1fr}.bug-replay-view__confirmed-tool{padding:.65rem}.bug-replay-view__confirmed-tool--environment dl{grid-template-columns:1fr}.bug-replay-view__profiles{grid-template-columns:1fr}.bug-replay-view__tool-head small{display:none}}
@media(max-width:720px){.bug-replay-view__count{display:none}.bug-replay-view__layout{grid-template-columns:1fr}.bug-replay-view__master{overflow:visible}.bug-replay-view__master--page-flow{position:static}.bug-replay-view__master-frame{position:static}.bug-replay-view__list--contained{max-height:14rem}.bug-replay-view__behavior,.bug-replay-view__evidence-workbench,.bug-replay-view__confirmed-tools,.bug-replay-view__cluster-pipeline{grid-template-columns:1fr}.bug-replay-view__confirmed-tool--environment{grid-column:auto}.bug-replay-view__evidence-pane{height:13rem}.bug-replay-view__environment dl{grid-template-columns:1fr 1fr}}
</style>
