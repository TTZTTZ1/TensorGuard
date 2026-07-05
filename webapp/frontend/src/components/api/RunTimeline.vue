<script setup lang="ts">
import { ref, type ComponentPublicInstance } from "vue";

import {
  stageDefinitions,
  timelineStages,
  type ApiRunStageKey,
  type ApiTimelineStageKey,
} from "../../domain/apiRun";
import type { ApiStageStatus } from "../../types/tensorguard";

const props = defineProps<{
  stages: Record<ApiTimelineStageKey, ApiStageStatus>;
  metricStageKey: ApiRunStageKey;
  liveStageKey: ApiRunStageKey;
}>();

const emit = defineEmits<{
  selectMetricStage: [ApiRunStageKey];
}>();

const tabRefs = ref<Array<HTMLButtonElement | null>>([]);

function isSelectable(key: ApiRunStageKey): boolean {
  const state = props.stages[key];
  return state === "running" || state === "success" || state === "failed";
}

function firstSelectableIndex(): number {
  return stageDefinitions.findIndex((definition) => isSelectable(definition.key));
}

function lastSelectableIndex(): number {
  for (let index = stageDefinitions.length - 1; index >= 0; index -= 1) {
    if (isSelectable(stageDefinitions[index].key)) {
      return index;
    }
  }

  return -1;
}

function nextSelectableIndex(fromIndex: number, direction: 1 | -1): number {
  for (let offset = 1; offset <= stageDefinitions.length; offset += 1) {
    const index = (fromIndex + direction * offset + stageDefinitions.length) % stageDefinitions.length;
    if (isSelectable(stageDefinitions[index].key)) {
      return index;
    }
  }

  return -1;
}

function focusTab(index: number) {
  tabRefs.value[index]?.focus();
}

function setTabRef(index: number, element: Element | ComponentPublicInstance | null) {
  tabRefs.value[index] = element instanceof HTMLButtonElement ? element : null;
}

function selectStage(index: number) {
  const definition = stageDefinitions[index];
  if (!definition || !isSelectable(definition.key)) {
    return;
  }

  emit("selectMetricStage", definition.key);
  focusTab(index);
}

function handleTabKeydown(event: KeyboardEvent, index: number) {
  if (event.key === "ArrowRight" || event.key === "ArrowDown") {
    event.preventDefault();
    const nextIndex = nextSelectableIndex(index, 1);
    if (nextIndex >= 0) {
      selectStage(nextIndex);
    }
    return;
  }

  if (event.key === "ArrowLeft" || event.key === "ArrowUp") {
    event.preventDefault();
    const nextIndex = nextSelectableIndex(index, -1);
    if (nextIndex >= 0) {
      selectStage(nextIndex);
    }
    return;
  }

  if (event.key === "Home") {
    event.preventDefault();
    const nextIndex = firstSelectableIndex();
    if (nextIndex >= 0) {
      selectStage(nextIndex);
    }
    return;
  }

  if (event.key === "End") {
    event.preventDefault();
    const nextIndex = lastSelectableIndex();
    if (nextIndex >= 0) {
      selectStage(nextIndex);
    }
  }
}
</script>

<template>
  <section class="run-timeline" aria-labelledby="run-timeline-title">
    <ol class="run-timeline__rail" aria-label="五阶段流水线">
      <li
        v-for="(stage, index) in timelineStages"
        :key="stage.key"
        class="run-timeline__rail-item"
        :class="[`run-timeline__rail-item--${stages[stage.key]}`]"
      >
        <span class="run-timeline__rail-index">
          <span v-if="stages[stage.key] === 'success'">✓</span>
          <span v-else>{{ String(index + 1).padStart(2, "0") }}</span>
        </span>
        <span class="run-timeline__rail-label">{{ stage.label }}</span>
        <span class="run-timeline__rail-status">
          {{ stages[stage.key] === "success" ? "已完成" : stages[stage.key] === "running" ? "正在执行" : stages[stage.key] === "failed" ? "执行失败" : "等待执行" }}
        </span>
      </li>
    </ol>

    <div class="run-timeline__tabs" role="tablist" aria-label="指标阶段">
      <button
        v-for="(definition, index) in stageDefinitions"
        :key="definition.key"
        :ref="(el) => setTabRef(index, el)"
        type="button"
        role="tab"
        class="run-timeline__tab"
        :class="{
          'run-timeline__tab--active': metricStageKey === definition.key,
          'run-timeline__tab--live': liveStageKey === definition.key,
          'run-timeline__tab--done': stages[definition.key] === 'success',
          'run-timeline__tab--failed': stages[definition.key] === 'failed',
        }"
        :aria-selected="metricStageKey === definition.key"
        :tabindex="isSelectable(definition.key) && metricStageKey === definition.key ? 0 : -1"
        :disabled="!isSelectable(definition.key)"
        @click="selectStage(index)"
        @keydown="handleTabKeydown($event, index)"
      >
        <span>{{ definition.label }}<b v-if="stages[definition.key] === 'success'"> ✓</b></span>
      </button>
    </div>

  </section>
</template>

<style scoped>
.run-timeline {
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  box-shadow: var(--tg-shadow);
  overflow: hidden;
}

.run-timeline__rail {
  position: relative;
  list-style: none;
  margin: 0;
  padding: 0.85rem 1rem 0.7rem;
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
}

.run-timeline__rail::before {
  content: "";
  position: absolute;
  top: 1.78rem;
  left: 10%;
  right: 10%;
  height: 2px;
  background: #d4ddec;
}

.run-timeline__rail-item {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.2rem;
  text-align: center;
}

.run-timeline__rail-index {
  width: 1.95rem;
  height: 1.95rem;
  display: grid;
  place-items: center;
  margin-bottom: 0.25rem;
  border: 4px solid #fff;
  border-radius: 50%;
  background: #dbe2ec;
  color: #7b8799;
  box-shadow: 0 0 0 1px #cbd5e5;
  font: 780 0.5rem/1 ui-monospace, SFMono-Regular, Menlo, monospace;
}

.run-timeline__rail-item--success .run-timeline__rail-index {
  background: var(--tg-green);
  color: #fff;
  box-shadow: 0 0 0 1px #b8ddcf;
}

.run-timeline__rail-item--running .run-timeline__rail-index {
  background: var(--tg-action);
  color: #fff;
  box-shadow: 0 0 0 1px #bdd0f4, 0 4px 11px rgba(37, 99, 235, 0.2);
}

.run-timeline__rail-item--failed .run-timeline__rail-index {
  background: var(--tg-red-text);
  color: #fff;
}

.run-timeline__rail-label {
  display: block;
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  color: var(--tg-text-strong);
  font-size: 0.61rem;
  font-weight: 740;
}

.run-timeline__rail-item--running .run-timeline__rail-label {
  color: var(--tg-action-strong);
}

.run-timeline__rail-item--success .run-timeline__rail-label,
.run-timeline__rail-item--success .run-timeline__rail-status {
  color: var(--tg-green-text);
}

.run-timeline__rail-status {
  color: var(--tg-text-soft);
  font-size: 0.49rem;
}

.run-timeline__tabs {
  display: flex;
  border-top: 1px solid var(--tg-border);
  background: #fbfcff;
}

.run-timeline__tab {
  position: relative;
  min-width: 8.2rem;
  height: 2.3rem;
  border: 0;
  border-right: 1px solid var(--tg-border);
  border-radius: 0;
  background: transparent;
  color: var(--tg-text-muted);
  padding: 0 0.8rem;
  font-size: 0.59rem;
  font-weight: 740;
}

.run-timeline__tab--active {
  color: var(--tg-action-strong);
  background: #fff;
}

.run-timeline__tab--active::after {
  content: "";
  position: absolute;
  left: 1rem;
  right: 1rem;
  bottom: -1px;
  height: 3px;
  background: var(--tg-action);
}

.run-timeline__tab--live {
  color: var(--tg-action-strong);
}

.run-timeline__tab--done {
  color: var(--tg-green-text);
}

.run-timeline__tab--done b {
  color: var(--tg-green);
}

.run-timeline__tab--failed {
  color: var(--tg-red-text);
}

.run-timeline__tab:disabled {
  color: #adb5c3;
}

@media (max-width: 720px) {
  .run-timeline__rail-status {
    display: none;
  }

  .run-timeline__rail-label {
    max-width: 4.2rem;
    white-space: normal;
  }

  .run-timeline__tab {
    min-width: 0;
    flex: 1;
  }
}
</style>
