<script setup lang="ts">
import { LineChart } from "echarts/charts";
import { GridComponent, LegendComponent, TooltipComponent } from "echarts/components";
import { init, use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { computed, onBeforeUnmount, onMounted, ref, watch } from "vue";

import { stageDefinitions, type ApiRunStageKey } from "../../domain/apiRun";
import { stageSeries } from "../../domain/chartOptions";
import type { ApiJobMetric } from "../../types/tensorguard";

use([LineChart, GridComponent, LegendComponent, TooltipComponent, CanvasRenderer]);

const props = withDefaults(
  defineProps<{
    metrics: ApiJobMetric[];
    stageKey: ApiRunStageKey;
    title?: string;
  }>(),
  {
    title: "",
  },
);

type ChartInstance = {
  setOption: (option: Record<string, unknown>, notMerge?: boolean) => void;
  resize: () => void;
  dispose: () => void;
};

const chartEl = ref<HTMLDivElement | null>(null);
let chart: ChartInstance | null = null;

const stageLabelByKey = Object.fromEntries(stageDefinitions.map((definition) => [definition.key, definition.label]));
const selectedSeries = computed(() => stageSeries(props.metrics, props.stageKey));
const hasData = computed(() => selectedSeries.value.length > 0);
const headingId = `stage-chart-${Math.random().toString(36).slice(2, 10)}`;
const titleText = computed(() => props.title || stageLabelByKey[props.stageKey] || "阶段曲线");
const summaryText = computed(() => {
  if (!hasData.value) {
    return "暂无采样";
  }

  const pointCount = selectedSeries.value[0]?.data.length ?? 0;
  return `${pointCount} 个采样点`;
});
const latestSeriesValues = computed(() =>
  selectedSeries.value.map((series) => ({
    name: series.name,
    color: series.color,
    value: series.data.at(-1)?.[1] ?? 0,
  })),
);

function buildOption() {
  return {
    animation: false,
    color: selectedSeries.value.map((series) => series.color),
    grid: { left: 16, right: 18, top: 20, bottom: 20, containLabel: true },
    legend: { show: false },
    tooltip: {
      trigger: "axis",
      backgroundColor: "#15213b",
      borderWidth: 0,
      padding: [8, 10],
      textStyle: { color: "#fff", fontSize: 11 },
      axisPointer: { type: "line", lineStyle: { color: "#9fb2d0", type: "dashed" } },
      formatter: (params: Array<{ seriesName: string; value: [number, number | null]; color: string }>) => {
        const seconds = Math.round(params[0]?.value?.[0] ?? 0);
        const rows = params.map((item) => `${item.seriesName}：${item.value?.[1] ?? "-"}`).join("<br>");
        return `<b>第 ${seconds} 秒</b><br>${rows}`;
      },
    },
    xAxis: {
      type: "value",
      name: "阶段运行时间（秒）",
      nameLocation: "middle",
      nameGap: 24,
      nameTextStyle: { color: "#718096", fontSize: 10 },
      boundaryGap: false,
      axisLine: { lineStyle: { color: "#bcc8d8" } },
      axisTick: { show: false },
      axisLabel: { color: "#7d899d", fontSize: 10, margin: 9 },
      splitLine: { show: false },
      splitNumber: 4,
    },
    yAxis: {
      type: "value",
      name: "累计数量",
      nameLocation: "middle",
      nameGap: 38,
      nameRotate: 90,
      nameTextStyle: { color: "#718096", fontSize: 10 },
      min: 0,
      axisLine: { show: true, lineStyle: { color: "#bcc8d8" } },
      axisTick: { show: false },
      axisLabel: { color: "#7d899d", fontSize: 10, margin: 9 },
      splitLine: { lineStyle: { color: "#edf1f7" } },
      splitNumber: 4,
    },
    series: selectedSeries.value.map((series) => ({
      name: series.name,
      type: "line",
      data: series.data,
      showSymbol: false,
      smooth: 0.2,
      lineStyle: { width: 2.5, color: series.color },
      itemStyle: { color: series.color },
      areaStyle: { opacity: 0.08, color: series.color },
      emphasis: { focus: "series" },
    })),
  };
}

function syncChart() {
  if (!hasData.value) {
    chart?.dispose();
    chart = null;
    return;
  }

  if (chart === null) {
    if (chartEl.value === null) {
      return;
    }

    chart = init(chartEl.value) as unknown as ChartInstance;
  }

  chart.setOption(buildOption(), true);
  chart.resize();
}

function handleResize() {
  chart?.resize();
}

watch(selectedSeries, syncChart, { deep: true, flush: "post" });

onMounted(() => {
  syncChart();
  window.addEventListener("resize", handleResize);
});

onBeforeUnmount(() => {
  window.removeEventListener("resize", handleResize);
  chart?.dispose();
  chart = null;
});
</script>

<template>
  <section class="stage-chart" :aria-labelledby="headingId">
    <header class="stage-chart__header">
      <div class="stage-chart__heading">
        <p class="stage-chart__eyebrow">阶段曲线</p>
        <h2 :id="headingId" class="stage-chart__title">{{ titleText }}</h2>
      </div>
      <div class="stage-chart__stats">
        <div
          v-for="item in latestSeriesValues"
          :key="item.name"
          class="stage-chart__stat"
          :style="{ '--series-color': item.color }"
        >
          <i aria-hidden="true" /><span>{{ item.name }}</span><b>{{ item.value }}</b>
        </div>
        <p class="stage-chart__summary">{{ summaryText }}</p>
      </div>
    </header>

    <div v-if="hasData" ref="chartEl" class="stage-chart__canvas" :aria-label="`${titleText} 折线图`" role="img" />
    <div v-else class="stage-chart__empty" role="status">
      <span class="stage-chart__empty-rail" aria-hidden="true">
        <i class="stage-chart__empty-dot" />
        <i class="stage-chart__empty-dot" />
        <i class="stage-chart__empty-dot" />
      </span>
      <span class="stage-chart__empty-copy">
        <b>等待阶段采样</b>
        <small>运行后会实时绘制当前阶段的候选、有效种子或差异数量</small>
      </span>
    </div>
  </section>
</template>

<style scoped>
.stage-chart {
  display: grid;
  grid-template-rows: auto minmax(0, 1fr);
  gap: 0.85rem;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: linear-gradient(180deg, #ffffff 0%, #fbfdff 100%);
  padding: 0.85rem 1rem 0.75rem;
  box-shadow: var(--tg-shadow);
  min-width: 0;
  height: 100%;
}

.stage-chart__header {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 1rem;
}

.stage-chart__heading {
  display: grid;
  gap: 0.15rem;
}

.stage-chart__eyebrow {
  margin: 0;
  font-size: 0.5rem;
  color: var(--tg-text-soft);
}

.stage-chart__title {
  margin: 0;
  font-size: 0.74rem;
  color: var(--tg-text-strong);
}

.stage-chart__summary {
  margin: 0;
  color: var(--tg-text-muted);
  font-size: 0.52rem;
}

.stage-chart__stats {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  flex-wrap: wrap;
  gap: 0.45rem;
}

.stage-chart__stat {
  min-width: 4.35rem;
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 0.32rem;
  padding: 0.34rem 0.42rem;
  border: 1px solid #d9e2f0;
  border-radius: 5px;
  background: #f8faff;
}

.stage-chart__stat i {
  width: 0.82rem;
  height: 0.16rem;
  border-radius: 999px;
  background: var(--series-color);
}

.stage-chart__stat span {
  color: var(--tg-text-muted);
  font-size: 0.48rem;
}

.stage-chart__stat b {
  color: var(--tg-text-strong);
  font-size: 0.72rem;
  font-variant-numeric: tabular-nums;
}

.stage-chart__canvas {
  width: 100%;
  height: 11.5rem;
  min-height: 11.5rem;
  border: 1px solid #dce4f0;
  border-radius: 5px;
  background: #fbfdff;
}

.stage-chart__empty {
  margin: 0;
  border: 1px dashed #c8d8f2;
  border-radius: var(--tg-radius-sm);
  background:
    linear-gradient(135deg, rgba(37, 99, 235, 0.1), rgba(20, 127, 153, 0.08) 54%, rgba(255, 255, 255, 0.78)),
    #f7fbff;
  color: var(--tg-text-muted);
  min-height: 13rem;
  display: grid;
  place-items: center;
  gap: 0.75rem;
  padding: 1rem;
  text-align: center;
}

.stage-chart__empty-rail {
  position: relative;
  width: min(15rem, 72%);
  height: 2.2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.stage-chart__empty-rail::before {
  content: "";
  position: absolute;
  left: 0.4rem;
  right: 0.4rem;
  height: 2px;
  background: linear-gradient(90deg, #2563eb, #168263, #d29a43);
  opacity: 0.68;
}

.stage-chart__empty-dot {
  position: relative;
  z-index: 1;
  width: 0.8rem;
  height: 0.8rem;
  border: 3px solid #fff;
  border-radius: 50%;
  background: #2563eb;
  box-shadow: 0 6px 12px rgba(37, 99, 235, 0.2);
}

.stage-chart__empty-dot:nth-child(2) {
  background: #168263;
  box-shadow: 0 6px 12px rgba(22, 130, 99, 0.18);
}

.stage-chart__empty-dot:nth-child(3) {
  background: #d29a43;
  box-shadow: 0 6px 12px rgba(210, 154, 67, 0.18);
}

.stage-chart__empty-copy {
  display: grid;
  gap: 0.3rem;
  max-width: 24rem;
}

.stage-chart__empty-copy b {
  color: var(--tg-text-strong);
  font-size: 0.72rem;
}

.stage-chart__empty-copy small {
  color: var(--tg-text-muted);
  font-size: 0.58rem;
  line-height: 1.5;
}
</style>
