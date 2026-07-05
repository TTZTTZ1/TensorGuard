<script setup lang="ts">
import { computed } from "vue";

import type { ApiJobMetric, EnvironmentPayload } from "../../types/tensorguard";

const props = withDefaults(
  defineProps<{
    metrics: ApiJobMetric[];
    environment?: Partial<EnvironmentPayload>;
    title?: string;
  }>(),
  {
    environment: () => ({}),
    title: "GPU 监控",
  },
);

const latestSample = computed(() => {
  for (let index = props.metrics.length - 1; index >= 0; index -= 1) {
    const sample = props.metrics[index]?.gpu;
    if (sample) return sample;
  }
  return null;
});
const gpuInfo = computed(() => {
  const index = latestSample.value?.index ?? 0;
  return props.environment?.gpus?.find((item) => item.index === index) ?? props.environment?.gpus?.[0] ?? null;
});
const utilization = computed(() => latestSample.value?.utilization_percent ?? null);
const memoryUsed = computed(() => latestSample.value?.memory_used_mib ?? null);
const memoryTotal = computed(() => latestSample.value?.memory_total_mib ?? gpuInfo.value?.memory_total_mib ?? null);
const memoryPercent = computed(() => {
  if (memoryUsed.value === null || memoryTotal.value === null || memoryTotal.value <= 0) return null;
  return Math.round(Math.min(100, (memoryUsed.value / memoryTotal.value) * 100) * 10) / 10;
});
const utilizationText = computed(() => utilization.value === null ? "暂无采样" : `${Math.round(utilization.value)}%`);
const memoryText = computed(() => memoryUsed.value === null ? "暂无采样" : `${(memoryUsed.value / 1024).toFixed(1)} GB`);
const deviceText = computed(() => gpuInfo.value?.name ?? (latestSample.value ? `GPU ${latestSample.value.index}` : "等待 GPU 采样"));
</script>

<template>
  <section class="gpu-chart">
    <header class="gpu-chart__header">
      <h2>{{ title }}</h2>
      <span>{{ deviceText }}</span>
    </header>
    <div class="gpu-chart__body">
      <article>
        <span>GPU 利用率</span>
        <b>{{ utilizationText }}</b>
        <div class="gpu-chart__track"><i data-testid="gpu-utilization-bar" :style="{ width: `${utilization ?? 0}%` }" /></div>
      </article>
      <article>
        <span>显存占用</span>
        <b>{{ memoryText }}</b>
        <div class="gpu-chart__track"><i data-testid="gpu-memory-bar" :style="{ width: `${memoryPercent ?? 0}%` }" /></div>
      </article>
    </div>
  </section>
</template>

<style scoped>
.gpu-chart{height:100%;overflow:hidden;border:1px solid var(--tg-border);border-radius:var(--tg-radius);background:#fff;box-shadow:var(--tg-shadow)}
.gpu-chart__header{min-height:2.25rem;display:flex;align-items:center;justify-content:space-between;gap:1rem;padding:0 .85rem;border-bottom:1px solid #293750;background:var(--tg-navy);color:#fff}.gpu-chart__header h2{margin:0;font-size:.61rem}.gpu-chart__header span{max-width:13rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:#9cabca;font-size:.48rem}
.gpu-chart__body{height:8rem;display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--tg-border)}.gpu-chart__body article{display:grid;align-content:center;padding:1rem;background:#fff}.gpu-chart__body span{color:var(--tg-text-muted);font-size:.5rem}.gpu-chart__body b{margin-top:.38rem;color:var(--tg-text-strong);font-size:1.15rem;font-variant-numeric:tabular-nums}.gpu-chart__track{height:.42rem;margin-top:.65rem;overflow:hidden;border-radius:2px;background:#e9eef6}.gpu-chart__track i{display:block;height:100%;border-radius:inherit;background:var(--tg-action);transition:width .25s ease}.gpu-chart__body article:last-child .gpu-chart__track i{background:#168aa4}
</style>
