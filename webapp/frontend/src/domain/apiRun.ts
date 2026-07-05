import type {
  ApiJobPayload,
  ApiJobStatus,
  ApiPipelineStage,
  ApiRunStatus,
  ApiStage,
  ApiStageStatus,
  CandidateCollectionSummary,
} from "../types/tensorguard";

export const stageDefinitions = [
  {
    key: "qwen_seed",
    label: "种子生成",
    metricKeys: [
      ["生成候选", "qwen_raw", "#2563eb"],
      ["有效种子", "qwen_valid", "#178263"],
    ],
  },
  {
    key: "ev_generation",
    label: "演化变异",
    metricKeys: [
      ["有效程序", "valid", "#178263"],
      ["异常", "exception", "#d29a43"],
      ["崩溃", "crash", "#c65362"],
      ["超时", "hangs", "#63738f"],
    ],
  },
  {
    key: "driver",
    label: "差异检测",
    metricKeys: [
      ["已检测程序", "tested_cases", "#2563eb"],
      ["差异 Catch", "trace_hits", "#c65362"],
    ],
  },
] as const;

export type ApiRunStageKey = (typeof stageDefinitions)[number]["key"];

export const timelineStages = [
  { key: "prompt_check", label: "约束检查" },
  { key: "qwen_seed", label: "Qwen" },
  { key: "ev_generation", label: "InCoder" },
  { key: "driver", label: "CPU/GPU difference" },
  { key: "summary", label: "summary" },
] as const;

export type ApiTimelineStageKey = (typeof timelineStages)[number]["key"];

type StageMap = Record<ApiPipelineStage, ApiStageStatus>;

export interface ApiRunJobLike {
  status: Pick<ApiJobStatus, "stage" | "stages"> &
    Partial<Pick<ApiJobStatus, "status">> & {
    stage: ApiStage;
    stages: StageMap;
  };
  metrics?: ApiJobPayload["metrics"];
  result_files?: ApiJobPayload["result_files"];
  logs?: ApiJobPayload["logs"];
}

const liveStageOrder: ApiRunStageKey[] = ["qwen_seed", "ev_generation", "driver"];

function isVisibleStageKey(value: ApiStage): value is ApiRunStageKey {
  return liveStageOrder.includes(value as ApiRunStageKey);
}

function isActiveStage(status: ApiStageStatus): boolean {
  return status === "running" || status === "success" || status === "failed";
}

export function resolveLiveStageKey(job: ApiRunJobLike): ApiRunStageKey {
  const stage = job.status.stage;
  if (isVisibleStageKey(stage)) {
    return stage;
  }

  for (let index = liveStageOrder.length - 1; index >= 0; index -= 1) {
    const key = liveStageOrder[index];
    if (isActiveStage(job.status.stages[key])) {
      return key;
    }
  }

  return "qwen_seed";
}

export function jobElapsedSeconds(
  status: Pick<ApiJobStatus, "status" | "started_at" | "updated_at">,
  nowMilliseconds = Date.now(),
): number {
  const started = Date.parse(status.started_at ?? "");
  if (!Number.isFinite(started)) {
    return 0;
  }
  const active = status.status === "pending" || status.status === "running";
  const terminal = Date.parse(status.updated_at);
  const ended = active || !Number.isFinite(terminal) ? nowMilliseconds : terminal;
  return Math.max(0, Math.floor((ended - started) / 1000));
}

export type CandidateCollectionTone = "pending" | "running" | "success" | "muted" | "error";

export function candidateCollectionPresentation(
  collection: CandidateCollectionSummary | null | undefined,
  status: ApiRunStatus | null | undefined,
): { tone: CandidateCollectionTone; label: string } {
  if (collection?.error) {
    return { tone: "error", label: "归集失败" };
  }
  if (status === "pending" || status === "running") {
    return { tone: "running", label: "检测中" };
  }
  if (collection === null || collection === undefined) {
    return { tone: "pending", label: "待归集" };
  }
  const candidateCount = collection.candidate_ids?.length ?? 0;
  if (candidateCount > 0) {
    return { tone: "success", label: `已进入候选 · ${candidateCount} 条` };
  }
  const filtered = (collection.excluded_noise ?? 0) + (collection.skipped_low_signal ?? 0);
  if (filtered > 0) {
    return { tone: "muted", label: `未进入候选 · 已过滤 ${filtered} 条` };
  }
  return { tone: "muted", label: "未进入候选 · 无高信号异常" };
}
