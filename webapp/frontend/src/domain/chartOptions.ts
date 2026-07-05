import { stageDefinitions, type ApiRunStageKey } from "./apiRun";
import type { ApiJobMetric, ResultCategory } from "../types/tensorguard";

export type ChartPoint = [number, number | null];

export interface ChartSeries {
  name: string;
  color: string;
  data: ChartPoint[];
}

export const resultCategoryOrder: ResultCategory[] = ["seed", "valid", "exception", "crash", "notarget", "hangs", "flaky"];

const stageDefinitionByKey = Object.fromEntries(stageDefinitions.map((definition) => [definition.key, definition]));

function metricValue(metric: ApiJobMetric, key: string): number | null {
  const value = metric[key as keyof ApiJobMetric];
  return typeof value === "number" ? value : null;
}

function hasVisibleData(series: ChartSeries[]): boolean {
  return series.some((item) => item.data.length > 0);
}

export function stageSeries(metrics: ApiJobMetric[], selectedStage: ApiRunStageKey): ChartSeries[] {
  const definition = stageDefinitionByKey[selectedStage];
  if (!definition) {
    return [];
  }

  const selectedMetrics = metrics.filter((metric) => metric.stage === selectedStage);
  if (selectedMetrics.length === 0) {
    return [];
  }

  const series = definition.metricKeys.map(([name, key, color]) => ({
    name,
    color,
    data: selectedMetrics.map((metric) => [metric.elapsed_seconds, metricValue(metric, key)] as ChartPoint),
  }));

  return hasVisibleData(series) ? series : [];
}

export function gpuSeries(metrics: ApiJobMetric[]): ChartSeries[] {
  const utilization: ChartSeries = {
    name: "GPU 利用率",
    color: "#2563eb",
    data: metrics.map((metric) => [metric.elapsed_seconds, metric.gpu?.utilization_percent ?? null]),
  };

  const memory: ChartSeries = {
    name: "GPU 显存",
    color: "#168aa4",
    data: metrics.map((metric) => [metric.elapsed_seconds, metric.gpu?.memory_used_mib ?? null]),
  };

  return hasVisibleData([utilization, memory]) ? [utilization, memory] : [];
}
