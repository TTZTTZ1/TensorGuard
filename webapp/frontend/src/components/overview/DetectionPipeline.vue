<script setup lang="ts">
import AsyncState from "../AsyncState.vue";
import type { OverviewPayload } from "../../types/tensorguard";

withDefaults(defineProps<{ overview: OverviewPayload | null; loading?: boolean; error?: string | null }>(), {
  loading: false,
  error: null,
});

defineEmits<{ retry: [] }>();

const steps = [
  { label: "约束加载", detail: "API 结构信息" },
  { label: "种子生成", detail: "Qwen 生成测试" },
  { label: "变异测试", detail: "InCoder 扩展输入" },
  { label: "差异检测", detail: "CPU / GPU Oracle" },
  { label: "证据归档", detail: "代码、日志、报告" },
] as const;
</script>

<template>
  <section class="detection-pipeline" aria-labelledby="detection-pipeline-title">
    <header class="detection-pipeline__head">
      <div class="detection-pipeline__ident">
        <span class="detection-pipeline__icon" aria-hidden="true">→</span>
        <div>
          <h2 id="detection-pipeline-title">自动化检测链路</h2>
          <p>从 API 约束到可归档证据</p>
        </div>
      </div>
      <span class="detection-pipeline__badge">完整流程</span>
    </header>

    <AsyncState :loading="loading" :error="error" :empty="!loading && !error && overview === null" @retry="$emit('retry')">
      <template #loading><p class="detection-pipeline__state">正在读取检测链路</p></template>
      <template #error="{ error: text }"><p class="detection-pipeline__state">{{ text }}</p></template>
      <template #empty><p class="detection-pipeline__state">后端暂未返回检测数据</p></template>

      <ol class="detection-pipeline__flow" aria-label="TensorGuard 自动化检测链路">
        <li v-for="(step, index) in steps" :key="step.label" class="detection-pipeline__flow-step">
          <span class="detection-pipeline__index">{{ String(index + 1).padStart(2, "0") }}</span>
          <b>{{ step.label }}</b>
          <small>{{ step.detail }}</small>
        </li>
      </ol>
    </AsyncState>
  </section>
</template>

<style scoped>
.detection-pipeline { display: grid; grid-template-rows: auto minmax(0, 1fr); height: 100%; min-height: 12.25rem; padding: 1.1rem 1.25rem; background: #fff; border: 1px solid var(--tg-border); border-radius: var(--tg-radius); box-shadow: var(--tg-shadow); }
.detection-pipeline__head { display: flex; align-items: flex-start; justify-content: space-between; gap: 1rem; margin-bottom: 0.75rem; }
.detection-pipeline__ident { display: flex; align-items: center; gap: 0.65rem; }
.detection-pipeline__icon { width: 1.9rem; height: 1.9rem; display: grid; place-items: center; border-radius: 6px; background: #fff3df; color: #9a5c0c; box-shadow: inset 0 0 0 1px #f2dfbc; font-weight: 800; }
.detection-pipeline h2 { margin: 0; color: var(--tg-text-strong); font-size: 0.875rem; }
.detection-pipeline__ident p { margin: 0.28rem 0 0; color: var(--tg-text-muted); font-size: 0.625rem; }
.detection-pipeline__badge { padding: 0.3rem 0.5rem; border-radius: 4px; background: var(--tg-green-bg); color: var(--tg-green-text); font-size: 0.56rem; font-weight: 720; }
.detection-pipeline__state { margin: 0; }
.detection-pipeline__flow { position: relative; display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 0; align-items: center; margin: 0; padding: 0.5rem 0.25rem 0.2rem; list-style: none; }
.detection-pipeline__flow::before { content: ""; position: absolute; z-index: 0; top: 1.55rem; left: 10%; right: 10%; height: 2px; background: #cbd7eb; }
.detection-pipeline__flow-step { position: relative; z-index: 1; padding: 0 0.5rem; text-align: center; }
.detection-pipeline__flow-step:not(:last-child)::after { content: ""; position: absolute; top: 0.82rem; right: -0.1rem; width: 0.4rem; height: 0.4rem; border-top: 2px solid #8fa5c9; border-right: 2px solid #8fa5c9; transform: rotate(45deg); }
.detection-pipeline__index { width: 2.15rem; height: 2.15rem; display: grid; place-items: center; margin: 0 auto; border: 4px solid #fff; border-radius: 50%; background: var(--tg-action); color: #fff; box-shadow: 0 0 0 1px #bfd0ee, 0 5px 12px rgba(37,99,235,.15); font: 760 0.56rem/1 ui-monospace, monospace; }
.detection-pipeline__flow-step:nth-child(2) .detection-pipeline__index { background: #3d6fc2; }
.detection-pipeline__flow-step:nth-child(3) .detection-pipeline__index { background: #7557a8; }
.detection-pipeline__flow-step:nth-child(4) .detection-pipeline__index { background: #c27623; }
.detection-pipeline__flow-step:nth-child(5) .detection-pipeline__index { background: #168263; }
.detection-pipeline__flow-step b { display: block; margin: 0.6rem 0 0.25rem; color: var(--tg-text-strong); font-size: 0.68rem; }
.detection-pipeline__flow-step small { color: var(--tg-text-muted); font-size: 0.55rem; }
@media (max-width: 720px) { .detection-pipeline__flow { grid-template-columns: 1fr; gap: 0.6rem; } .detection-pipeline__flow::before, .detection-pipeline__flow-step::after { display: none; } .detection-pipeline__flow-step { display: grid; grid-template-columns: 2.5rem 1fr; text-align: left; align-items: center; padding: 0.5rem; border: 1px solid var(--tg-border); border-radius: 5px; } .detection-pipeline__index { grid-row: 1 / 3; margin: 0; } .detection-pipeline__flow-step b { margin: 0; } }
</style>
