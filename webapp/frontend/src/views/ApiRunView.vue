<script setup lang="ts">
import { computed } from "vue";

import ApiSelector from "../components/api/ApiSelector.vue";
import GpuChart from "../components/api/GpuChart.vue";
import LiveLog from "../components/api/LiveLog.vue";
import ResultComposition from "../components/api/ResultComposition.vue";
import RunSnapshot from "../components/api/RunSnapshot.vue";
import RunTimeline from "../components/api/RunTimeline.vue";
import StageChart from "../components/api/StageChart.vue";
import { useApiRun } from "../composables/useApiRun";
import { candidateCollectionPresentation, timelineStages } from "../domain/apiRun";

const {
  selectedApi,
  selectedApiDetail,
  selectedJob,
  detailLoading,
  detailError,
  jobLoading,
  jobError,
  runLoading,
  runError,
  pollError,
  mode,
  canRun,
  liveStageKey,
  metricStageKey,
  stageStates,
  metrics,
  resultFiles,
  logs,
  summaryCounts,
  retryPollingNow,
  selectApi,
  clearSelection,
  retrySelection,
  setMode,
  selectMetricStage,
  startRun,
} = useApiRun();

const selectedApiLabel = computed(() => selectedApiDetail.value?.api ?? selectedApi.value?.api ?? "未选择 API");
const selectedJobStatus = computed(() => selectedJob.value?.status ?? null);
const latestMetric = computed(() => selectedJob.value?.metrics?.at(-1) ?? null);
const running = computed(() => selectedJob.value?.status.status === "running" || selectedJob.value?.status.status === "pending");
const selectedDeviceLabel = computed(() => `GPU ${selectedJobStatus.value?.cuda_device ?? "0"}`);
const candidateState = computed(() => candidateCollectionPresentation(
  selectedJobStatus.value?.candidate_collection,
  selectedJobStatus.value?.status,
));
const runButtonHint = computed(() => {
  if (running.value || runLoading.value) {
    return "后台任务执行中";
  }

  if (!canRun.value) {
    return selectedApi.value === null ? "先选择 API" : "等待就绪";
  }

  return mode.value === "demo" ? "启动演示链路" : "启动完整链路";
});
const activeStageIndex = computed(() => {
  const current = selectedJob.value?.status.stage;
  const index = timelineStages.findIndex((stage) => stage.key === current);
  return index >= 0 ? index + 1 : 0;
});
const activeStageLabel = computed(() => {
  if (selectedJob.value?.status.status === "success") {
    return "任务完成";
  }

  if (selectedJob.value?.status.status === "failed") {
    return "任务失败";
  }

  const current = selectedJob.value?.status.stage;
  return timelineStages.find((stage) => stage.key === current)?.label ?? (selectedApi.value ? "任务已就绪" : "等待选择 API");
});

function handleLibraryChange() {
  clearSelection();
}
</script>

<template>
  <section class="api-run-view" aria-labelledby="api-run-view-title">
    <header class="api-run-view__page-head">
      <div class="api-run-view__title-lockup">
        <span class="api-run-view__page-symbol" aria-hidden="true">API</span>
        <div class="api-run-view__title-copy">
          <p class="api-run-view__eyebrow">Orchestrated Fuzzing · Live Detection</p>
          <h1 id="api-run-view-title">单 API 安全检测</h1>
          <p>运行完整测试链路，并持续归集候选证据</p>
        </div>
      </div>
      <div class="api-run-view__status-stack">
        <small>ACTIVE STAGE {{ String(activeStageIndex || 0).padStart(2, "0") }} / 05</small>
        <span class="api-run-view__run-state" :class="{ 'api-run-view__run-state--active': running }">
          <i aria-hidden="true" />{{ activeStageLabel }}{{ running ? "进行中" : "" }}
        </span>
      </div>
    </header>

    <section class="api-run-view__panel api-run-view__orchestration" aria-label="API 选择与运行">
      <ApiSelector :selected="selectedApi" @select="selectApi" @library-change="handleLibraryChange" />

      <div class="api-run-view__run-controls" aria-label="运行控制">
        <div class="api-run-view__control api-run-view__control-card api-run-view__control-card--mode">
          <span class="api-run-view__control-label">运行模式</span>
          <span class="api-run-view__segmented" role="group" aria-label="运行模式">
            <button type="button" :aria-pressed="mode === 'demo'" @click="setMode('demo')">演示</button>
            <button type="button" :aria-pressed="mode === 'normal'" @click="setMode('normal')">完整</button>
          </span>
        </div>
        <div class="api-run-view__control api-run-view__control-card api-run-view__control-card--device">
          <span class="api-run-view__control-label">计算设备</span>
          <b>{{ selectedDeviceLabel }}</b>
        </div>
        <div class="api-run-view__control api-run-view__control-card api-run-view__control-card--candidate">
          <span class="api-run-view__control-label">候选状态</span>
          <b :class="`api-run-view__candidate-state api-run-view__candidate-state--${candidateState.tone}`">{{ candidateState.label }}</b>
        </div>
        <button type="button" class="api-run-view__control api-run-view__run" :disabled="!canRun" @click="startRun">
          <span>{{ running || runLoading ? "任务运行中" : "运行" }}</span>
          <small>{{ runButtonHint }}</small>
        </button>
      </div>
    </section>

    <RunTimeline
      :stages="stageStates"
      :metric-stage-key="metricStageKey"
      :live-stage-key="liveStageKey"
      @select-metric-stage="selectMetricStage"
    />

    <section class="api-run-view__dashboard" aria-label="阶段图表、实时摘要与日志">
      <div class="api-run-view__primary">
        <StageChart :metrics="metrics" :stage-key="metricStageKey" />
        <div class="api-run-view__telemetry-strip api-run-view__telemetry-strip--equal">
          <GpuChart :metrics="metrics" :environment="selectedJob?.environment" />
          <RunSnapshot
            :api-label="selectedApiLabel"
            :mode="mode"
            :live-stage-key="liveStageKey"
            :job-status="selectedJobStatus"
            :latest-metric="latestMetric"
          />
          <ResultComposition :counts="summaryCounts" />
        </div>
      </div>
      <aside class="api-run-view__log-column api-run-view__log-column--fixed api-run-view__log-column--row-aligned">
        <LiveLog
          :key="selectedJob?.job_id ?? `${selectedApi?.lib ?? 'none'}:${selectedApi?.api ?? 'none'}`"
          :stage-key="liveStageKey"
          :logs="logs"
        />
      </aside>
    </section>

    <div class="api-run-view__sync" aria-live="polite">
      <p v-if="selectedApi === null">请选择一个 API 后查看实时图表与日志。</p>
      <p v-else-if="detailLoading || jobLoading || runLoading">正在读取 API 详情。</p>
      <div v-else-if="detailError || jobError || runError" class="api-run-view__sync-row">
        <p class="api-run-view__sync-error">{{ detailError ?? jobError ?? runError }}</p>
        <button type="button" class="api-run-view__retry" @click="retrySelection">重试</button>
      </div>
      <div v-else-if="pollError" class="api-run-view__sync-row">
        <p>同步作业状态遇到暂时错误，自动重试中。</p>
        <button type="button" class="api-run-view__retry" @click="retryPollingNow">立即重试</button>
      </div>
    </div>
  </section>
</template>

<style scoped>
.api-run-view { display: grid; gap: 0.75rem; }
.api-run-view__page-head { display: flex; align-items: center; justify-content: space-between; gap: 1.1rem; margin-bottom: 0.1rem; }
.api-run-view__title-lockup { display: flex; align-items: center; gap: 0.8rem; }
.api-run-view__page-symbol { width: 2.75rem; height: 2.75rem; display: grid; place-items: center; flex: none; border: 1px solid #cfddf7; border-radius: 8px; background: var(--tg-action-soft); color: var(--tg-action-strong); font: 820 0.75rem/1 ui-monospace, monospace; box-shadow: inset 0 0 0 4px rgba(255,255,255,.7), 0 7px 16px rgba(37,99,235,.08); }
.api-run-view__title-copy { padding-left: 0.75rem; border-left: 2px solid var(--tg-action); }
.api-run-view__eyebrow { margin: 0 0 0.3rem; color: var(--tg-action); font: 760 0.5rem/1 ui-monospace, monospace; text-transform: uppercase; }
.api-run-view h1 { margin: 0; color: var(--tg-text-strong); font-size: 1.45rem; line-height: 1.15; font-weight: 790; }
.api-run-view__title-copy > p:last-child { margin: 0.3rem 0 0; color: var(--tg-text-muted); font-size: 0.63rem; }
.api-run-view__status-stack { display: grid; justify-items: end; gap: 0.3rem; }
.api-run-view__status-stack small { color: var(--tg-text-muted); font: 0.5rem/1 ui-monospace, monospace; }
.api-run-view__run-state { min-height: 2.2rem; display: flex; align-items: center; gap: 0.45rem; padding: 0 0.7rem; border-radius: 5px; background: var(--tg-surface-soft); color: var(--tg-text-muted); font-size: 0.62rem; font-weight: 740; }
.api-run-view__run-state i { width: 0.45rem; height: 0.45rem; border-radius: 50%; background: #9aa5b7; }
.api-run-view__run-state--active { background: var(--tg-amber-bg); color: var(--tg-amber-text); }
.api-run-view__run-state--active i { background: #d18b2b; box-shadow: 0 0 0 3px #f8dfb7; }
.api-run-view__panel { background: #fff; border: 1px solid var(--tg-border); border-radius: var(--tg-radius); box-shadow: var(--tg-shadow); }
.api-run-view__orchestration { display: grid; grid-template-columns: minmax(0, 1.45fr) minmax(27rem, 1fr); justify-content: space-between; align-items: end; gap: 0.75rem; padding: 0.85rem 1rem; }
.api-run-view__run-controls { display: grid; grid-template-columns: repeat(4,minmax(6.2rem,1fr)); align-items: stretch; gap: 0.5rem; }
.api-run-view__control { height: 3.45rem; min-width: 0; box-sizing: border-box; }
.api-run-view__control-card { display: grid; grid-template-rows:auto minmax(0,1fr); align-items:center; gap: 0.22rem; padding:0.42rem 0.52rem; border:1px solid #d6deeb; border-radius:6px; background:#fff; }
.api-run-view__control-label { color: var(--tg-text-muted); font-size: 0.5rem; font-weight: 720; }
.api-run-view__control-card--device { justify-content: stretch; }
.api-run-view__control-card--device b { color: var(--tg-text-strong); font: 780 0.62rem/1 ui-monospace, SFMono-Regular, Menlo, monospace; }
.api-run-view__control-card--candidate{justify-content:stretch}.api-run-view__candidate-state{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--tg-text-muted);font-size:.52rem}.api-run-view__candidate-state--running{color:var(--tg-action-strong)}.api-run-view__candidate-state--success{color:var(--tg-green-text)}.api-run-view__candidate-state--error{color:var(--tg-red-text)}
.api-run-view__segmented { height: 100%; display: flex; padding: 2px; border: 0; border-radius: 4px; background: #f5f7fb; }
.api-run-view__segmented button { min-width: 3.3rem; border: 0; border-radius: 3px; background: transparent; color: var(--tg-text-muted); font-size: 0.65rem; }
.api-run-view__segmented button[aria-pressed="true"] { background: #fff; color: var(--tg-action-strong); box-shadow: 0 2px 8px rgba(36,58,98,.08); }
.api-run-view__run { display: grid; align-content: center; gap: 0.12rem; border: 1px solid var(--tg-action); border-radius: 6px; background: var(--tg-action); color: #fff; padding: 0 0.75rem; text-align: left; box-shadow: 0 6px 14px rgba(37,99,235,.16); }
.api-run-view__run span { font-size: 0.64rem; font-weight: 760; }
.api-run-view__run small { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: rgba(255,255,255,.78); font-size: 0.46rem; }
.api-run-view__run:disabled { border-color: var(--tg-border); background: #eef1f6; color: #99a3b4; box-shadow: none; }
.api-run-view__run:disabled small { color: #a3adbd; }
.api-run-view__dashboard { display: grid; grid-template-columns: minmax(0, 1.05fr) minmax(22rem, 0.95fr); gap: 0.75rem; align-items: stretch; }
.api-run-view__primary { display: grid; grid-template-rows: auto minmax(9.5rem, auto); gap: 0.65rem; min-width: 0; }
.api-run-view__telemetry-strip { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.6rem; align-items: stretch; min-width: 0; }
.api-run-view__log-column { min-width: 0; }
.api-run-view__log-column--fixed { min-height: 0; }
.api-run-view__log-column--row-aligned { position: relative; }
.api-run-view__log-column--row-aligned :deep(.live-log) { position: absolute; inset: 0; width: 100%; height: 100%; }
.api-run-view__log-column :deep(.live-log__body), .api-run-view__log-column :deep(.live-log__empty) { min-height: 0; }
.api-run-view__telemetry-strip :deep(.gpu-chart__body) { height: calc(100% - 2.25rem); grid-template-columns: 1fr; }
.api-run-view__telemetry-strip :deep(.gpu-chart__body article) { padding: 0.7rem 0.75rem; }
.api-run-view__telemetry-strip :deep(.gpu-chart__body b) { margin-top: 0.25rem; font-size: 0.9rem; }
.api-run-view__telemetry-strip :deep(.gpu-chart__track) { margin-top: 0.42rem; }
.api-run-view__telemetry-strip :deep(.run-snapshot), .api-run-view__telemetry-strip :deep(.result-composition) { padding: 0.6rem; gap: 0.42rem; }
.api-run-view__telemetry-strip :deep(.run-snapshot__item) { padding: 0.38rem 0.42rem; }
.api-run-view__telemetry-strip :deep(.run-snapshot__models span) { padding: 0.3rem 0.4rem; grid-template-columns: 3.6rem minmax(0, 1fr); }
.api-run-view__telemetry-strip :deep(.result-composition__grid) { gap:0.24rem 0.52rem; }
.api-run-view__telemetry-strip :deep(.result-composition__bar) { height:0.55rem; }
.api-run-view__sync { min-height: 1.8rem; display: grid; align-items: center; color: var(--tg-text-muted); font-size: 0.62rem; }
.api-run-view__sync p { margin: 0; }
.api-run-view__sync-row { display: flex; align-items: center; justify-content: space-between; gap: 0.75rem; }
.api-run-view__sync-error { color: var(--tg-red-text); }
.api-run-view__retry { height: 1.8rem; border: 1px solid var(--tg-border); border-radius: 5px; background: #fff; color: var(--tg-action); padding: 0 0.65rem; font-size: 0.6rem; }
@media (max-width: 1100px) { .api-run-view__dashboard { grid-template-columns: 1fr; } .api-run-view__log-column--row-aligned { height: 18rem; min-height: 18rem; max-height: 18rem; } }
@media (max-width: 900px) { .api-run-view__orchestration { grid-template-columns: 1fr; } .api-run-view__run-controls { justify-self: end; width: min(24rem, 100%); } .api-run-view__telemetry-strip { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
@media (max-width: 720px) { .api-run-view__page-head { align-items: flex-start; } .api-run-view__status-stack { display: none; } .api-run-view__run-controls { grid-template-columns: 1fr; justify-self: stretch; width: 100%; } .api-run-view__telemetry-strip { grid-template-columns: 1fr; } }
</style>
