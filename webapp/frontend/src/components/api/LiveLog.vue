<script setup lang="ts">
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from "vue";

import { stageDefinitions, type ApiRunStageKey } from "../../domain/apiRun";

const props = withDefaults(
  defineProps<{
    stageKey: ApiRunStageKey;
    logs: Record<string, string>;
  }>(),
  {
    logs: () => ({}),
  },
);

const headingId = `live-log-${Math.random().toString(36).slice(2, 10)}`;
const bodyRef = ref<HTMLDivElement | null>(null);
const followTail = ref(true);
const manualStageSelection = ref(false);
const selectedStageKey = ref<ApiRunStageKey>(props.stageKey);
const stageLabelByKey = Object.fromEntries(stageDefinitions.map((definition) => [definition.key, definition.label]));
const stageLogFileByKey: Record<ApiRunStageKey, string> = {
  qwen_seed: "01_qwen_seed.log",
  ev_generation: "02_ev_generation.log",
  driver: "03_driver.log",
};

function logForStage(key: ApiRunStageKey): string {
  return props.logs[stageLogFileByKey[key]] ?? props.logs[key] ?? "";
}

const logStages = stageDefinitions.map((definition) => ({ key: definition.key, label: definition.label }));
const stageLabel = computed(() => stageLabelByKey[selectedStageKey.value] || selectedStageKey.value);
const currentLog = computed(() => logForStage(selectedStageKey.value));
const hasLog = computed(() => currentLog.value.trim().length > 0);

function hasStageLog(key: ApiRunStageKey): boolean {
  return logForStage(key).trim().length > 0;
}

function isAtBottom() {
  const body = bodyRef.value;
  if (body === null) {
    return true;
  }

  return body.scrollHeight - body.scrollTop - body.clientHeight <= 12;
}

function scrollToBottom() {
  const body = bodyRef.value;
  if (body === null) {
    return;
  }

  body.scrollTop = body.scrollHeight;
}

function handleScroll() {
  followTail.value = isAtBottom();
}

async function selectStage(key: ApiRunStageKey) {
  if (!hasStageLog(key)) return;
  selectedStageKey.value = key;
  manualStageSelection.value = true;
  followTail.value = true;
  await nextTick();
  scrollToBottom();
}

watch(
  currentLog,
  async () => {
    if (!followTail.value) return;

    await nextTick();
    scrollToBottom();
  },
  { flush: "post" },
);

watch(
  () => props.stageKey,
  (nextStage) => {
    if (!manualStageSelection.value || !hasStageLog(selectedStageKey.value)) {
      selectedStageKey.value = nextStage;
      manualStageSelection.value = false;
      followTail.value = true;
    }
  },
);

watch(
  () => props.logs,
  () => {
    if (!hasStageLog(selectedStageKey.value) && hasStageLog(props.stageKey)) {
      selectedStageKey.value = props.stageKey;
      manualStageSelection.value = false;
      followTail.value = true;
    }
  },
  { deep: true },
);

onMounted(() => {
  scrollToBottom();
});

onBeforeUnmount(() => {
  followTail.value = false;
});
</script>

<template>
  <section class="live-log live-log--fixed-viewport" :aria-labelledby="headingId">
    <header class="live-log__header">
      <div class="live-log__heading">
        <h2 :id="headingId" class="live-log__title">实时日志</h2>
        <small>{{ stageLabel }}</small>
      </div>
      <div class="live-log__stages" role="tablist" aria-label="选择日志阶段">
        <button
          v-for="stage in logStages"
          :key="stage.key"
          type="button"
          role="tab"
          data-testid="log-stage-tab"
          class="live-log__stage"
          :class="{
            'live-log__stage--active': selectedStageKey === stage.key,
            'live-log__stage--complete': hasStageLog(stage.key) && stageKey !== stage.key,
            'live-log__stage--live': stageKey === stage.key,
          }"
          :aria-selected="selectedStageKey === stage.key"
          :disabled="!hasStageLog(stage.key)"
          @click="selectStage(stage.key)"
        >{{ stage.label }}</button>
      </div>
    </header>

    <div
      v-if="hasLog"
      ref="bodyRef"
      class="live-log__body"
      data-testid="live-log-body"
      @scroll="handleScroll"
    >
      <pre class="live-log__text">{{ currentLog }}</pre>
    </div>
    <p v-else class="live-log__empty">暂无当前阶段日志</p>
  </section>
</template>

<style scoped>
.live-log {
  display: grid;
  grid-template-rows: auto minmax(0, 1fr);
  width: 100%;
  max-width: 100%;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: #111a2d;
  min-width: 0;
  overflow: hidden;
  box-shadow: var(--tg-shadow);
  height: 100%;
  contain: inline-size;
}

.live-log--fixed-viewport { height: 100%; min-height: 0; }

.live-log__header {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  min-height: 3rem;
  padding: 0.4rem 0.7rem;
  border-bottom: 1px solid #293750;
  background: var(--tg-navy);
}

.live-log__heading { display: grid; gap: 0.12rem; }
.live-log__heading small { color: #8fa0bd; font-size: 0.44rem; }

.live-log__title {
  margin: 0;
  font-size: 0.61rem;
  color: #fff;
}

.live-log__stages { min-width: 0; display: flex; justify-content: flex-end; gap: 0.25rem; }
.live-log__stage { height: 1.75rem; border: 1px solid #34435e; border-radius: 5px; background: #1d2a43; color: #9cabc4; padding: 0 0.55rem; font-size: 0.47rem; white-space: nowrap; }
.live-log__stage--active { border-color: #739cea; background: #274678; color: #fff; }
.live-log__stage--complete::before { content: ""; display: inline-block; width: 0.3rem; height: 0.3rem; margin-right: 0.3rem; border-radius: 50%; background: #54c59a; }
.live-log__stage--live:not(.live-log__stage--active) { color: #c9d8f2; }
.live-log__stage:disabled { opacity: 0.38; cursor: not-allowed; }

.live-log__body {
  width: 100%;
  min-width: 0;
  min-height: 0;
  overflow-x: hidden;
  overflow-y: auto;
  scrollbar-gutter: stable;
  background: #111a2d;
  color: #eef4ff;
  padding: 0.65rem 0.85rem;
}

.live-log__text {
  width: 100%;
  min-width: 0;
  max-width: 100%;
  margin: 0;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  word-break: break-word;
  font-family:
    SFMono-Regular,
    ui-monospace,
    "SF Mono",
    Menlo,
    Consolas,
    monospace;
  font-size: 0.54rem;
  line-height: 1.65;
}

.live-log__empty {
  margin: 0;
  min-height: 8rem;
  display: grid;
  place-items: center;
  background: #111a2d;
  color: #7888a4;
  padding: 1rem;
  font-size: 0.58rem;
}
</style>
