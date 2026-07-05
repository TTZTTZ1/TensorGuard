<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from "vue";

import { jobElapsedSeconds, timelineStages, type ApiRunStageKey } from "../../domain/apiRun";
import type { ApiJobMetric, ApiJobStatus, ApiRunMode } from "../../types/tensorguard";

const props = withDefaults(
  defineProps<{
    apiLabel: string;
    mode: ApiRunMode;
    liveStageKey: ApiRunStageKey;
    jobStatus: ApiJobStatus | null;
    latestMetric: ApiJobMetric | null;
  }>(),
  {
    jobStatus: null,
    latestMetric: null,
  },
);

const headingId = `run-snapshot-${Math.random().toString(36).slice(2, 10)}`;
const currentTimeMilliseconds = ref(Date.now());
let clockTimer: ReturnType<typeof setInterval> | null = null;
const elapsedText = computed(() => {
  if (props.jobStatus?.started_at) {
    return formatDuration(jobElapsedSeconds(props.jobStatus, currentTimeMilliseconds.value));
  }
  if (props.latestMetric === null) {
    return "暂无";
  }

  return formatDuration(props.latestMetric.elapsed_seconds);
});
const qwenModel = computed(() => props.jobStatus?.qwen_model?.trim() || "");
const mutationModel = computed(() => props.jobStatus?.mutation_model?.trim() || "");
const generatedText = computed(() => {
  const metric = props.latestMetric;
  if (metric === null) {
    return "暂无";
  }

  if (metric.stage === "qwen_seed") {
    return String(metric.qwen_raw);
  }

  return String(metric.total_files);
});
const validText = computed(() => {
  const metric = props.latestMetric;
  if (metric === null) {
    return "暂无";
  }

  if (metric.stage === "qwen_seed") {
    return String(metric.qwen_valid);
  }

  return String(metric.valid);
});
const batchText = computed(() => {
  const metric = props.latestMetric;
  const params = props.jobStatus?.parameters;
  if (metric === null) {
    return "暂无";
  }

  if (metric.stage === "qwen_seed" && params !== undefined) {
    const perRound = Math.max(params.qwen_n_samples || 1, 1);
    const total = Math.max(params.qwen_max_rounds || 1, 1);
    const current = Math.min(total, Math.max(1, Math.ceil(Math.max(metric.qwen_raw, metric.qwen_valid) / perRound)));
    return `${current} / ${total}`;
  }

  if (metric.stage === "ev_generation" && params !== undefined) {
    const produced = Math.max(metric.total_files, metric.valid + metric.exception + metric.crash + metric.notarget + metric.hangs + metric.flaky);
    const batchSize = Math.max(params.ev_batch_size || 1, 1);
    const total = Math.max(1, Math.ceil(Math.max(params.ev_max_valid || produced, produced) / batchSize));
    const current = Math.min(total, Math.max(1, Math.ceil(produced / batchSize)));
    return `${current} / ${total}`;
  }

  const stageIndex = timelineStages.findIndex((stage) => stage.key === props.jobStatus?.stage);
  return stageIndex >= 0 ? `${stageIndex + 1} / ${timelineStages.length}` : "暂无";
});

const rows = computed(() => {
  return [
    ["生成候选", generatedText.value, "accent"],
    ["有效程序", validText.value, ""],
    ["当前批次", batchText.value, ""],
    ["运行时间", elapsedText.value, ""],
  ] as const;
});

function formatDuration(seconds: number): string {
  const safeSeconds = Math.max(0, Math.floor(seconds));
  const minutes = Math.floor(safeSeconds / 60);
  const rest = safeSeconds % 60;
  return `${String(minutes).padStart(2, "0")}:${String(rest).padStart(2, "0")}`;
}

onMounted(() => {
  clockTimer = setInterval(() => {
    currentTimeMilliseconds.value = Date.now();
  }, 1000);
});

onBeforeUnmount(() => {
  if (clockTimer !== null) clearInterval(clockTimer);
});
</script>

<template>
  <section class="run-snapshot" :aria-labelledby="headingId">
    <header class="run-snapshot__header">
      <span class="run-snapshot__icon">LIVE</span>
      <div class="run-snapshot__heading"><h2 :id="headingId" class="run-snapshot__title">实时摘要</h2><p>{{ apiLabel || "当前任务采样" }}</p></div>
    </header>

    <dl class="run-snapshot__grid">
      <div v-for="[label, value, tone] in rows" :key="label" class="run-snapshot__item">
        <dt class="run-snapshot__label">{{ label }}</dt>
        <dd class="run-snapshot__value" :class="{ 'run-snapshot__value--accent': tone === 'accent' }">{{ value }}</dd>
      </div>
    </dl>

    <div class="run-snapshot__models" aria-label="当前模型配置">
      <span><b>Qwen</b>{{ qwenModel || "按后端配置" }}</span>
      <span><b>变异模型</b>{{ mutationModel || "按后端配置" }}</span>
    </div>
  </section>
</template>

<style scoped>
.run-snapshot {
  display: grid;
  grid-template-rows: auto auto minmax(0, auto);
  gap: 0.7rem;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  padding: 0.85rem;
  box-shadow: var(--tg-shadow);
  min-width: 0;
  height: 100%;
}

.run-snapshot__header {
  display: flex;
  align-items: center;
  gap: 0.55rem;
}

.run-snapshot__heading {
  display: grid;
  gap: 0.12rem;
}

.run-snapshot__icon {
  width: 1.8rem;
  height: 1.8rem;
  display: grid;
  place-items: center;
  border-radius: 6px;
  background: var(--tg-action-soft);
  color: var(--tg-action-strong);
  box-shadow: inset 0 0 0 1px #d6e4ff;
  font: 800 0.43rem/1 ui-monospace, monospace;
}

.run-snapshot__title {
  margin: 0;
  font-size: 0.72rem;
  color: var(--tg-text-strong);
  word-break: break-word;
}

.run-snapshot__heading p { margin: 0; max-width: 12rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: var(--tg-text-muted); font-size: 0.48rem; }

.run-snapshot__grid {
  margin: 0;
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1px;
  border: 1px solid var(--tg-border);
  background: var(--tg-border);
}

.run-snapshot__item {
  margin: 0;
  background: #fff;
  padding: 0.6rem 0.62rem;
  min-width: 0;
}

.run-snapshot__label {
  margin: 0 0 0.2rem;
  font-size: 0.48rem;
  color: var(--tg-text-soft);
}

.run-snapshot__value {
  margin: 0;
  color: var(--tg-text-strong);
  word-break: break-word;
  font-size: 0.9rem;
  font-weight: 790;
  font-variant-numeric: tabular-nums;
}

.run-snapshot__value--accent {
  color: var(--tg-action);
}

.run-snapshot__models {
  display: grid;
  gap: 0.36rem;
}

.run-snapshot__models span {
  display: grid;
  grid-template-columns: 4.2rem minmax(0, 1fr);
  align-items: center;
  gap: 0.45rem;
  min-width: 0;
  border: 1px solid #d9e4f5;
  border-radius: 5px;
  background: linear-gradient(135deg, #f9fbff, #f1f6ff);
  padding: 0.4rem 0.48rem;
  color: var(--tg-text-muted);
  font: 0.52rem/1.25 ui-monospace, SFMono-Regular, Menlo, monospace;
}

.run-snapshot__models b {
  color: var(--tg-action-strong);
  font: 760 0.5rem/1 ui-sans-serif, system-ui, sans-serif;
}

@media (max-width: 720px) {
  .run-snapshot__grid {
    grid-template-columns: 1fr;
  }
}
</style>
