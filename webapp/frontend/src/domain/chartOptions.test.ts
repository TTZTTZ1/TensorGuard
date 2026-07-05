import { describe, expect, it } from "vitest";

import type { ApiJobMetric } from "../types/tensorguard";

import { gpuSeries, resultCategoryOrder, stageSeries } from "./chartOptions";

describe("chartOptions", () => {
  it("keeps absent GPU samples as null gaps", () => {
    const metrics: ApiJobMetric[] = [
      {
        timestamp: "2026-06-28T17:00:00",
        stage: "qwen_seed",
        elapsed_seconds: 1,
        qwen_raw: 10,
        qwen_valid: 2,
        total_files: 0,
        trace_hits: 0,
        seed: 0,
        valid: 0,
        exception: 0,
        crash: 0,
        notarget: 0,
        hangs: 0,
        flaky: 0,
      },
      {
        timestamp: "2026-06-28T17:00:01",
        stage: "qwen_seed",
        elapsed_seconds: 2,
        qwen_raw: 11,
        qwen_valid: 3,
        total_files: 0,
        trace_hits: 0,
        seed: 0,
        valid: 0,
        exception: 0,
        crash: 0,
        notarget: 0,
        hangs: 0,
        flaky: 0,
        gpu: {
          collected_at: "2026-06-28T17:00:01",
          index: 0,
          utilization_percent: 50,
          memory_used_mib: 4096,
          memory_total_mib: 8192,
        },
      },
    ];

    const series = gpuSeries(metrics);

    expect(series[0].data).toEqual([
      [1, null],
      [2, 50],
    ]);
  });

  it("keeps only the selected stage and qwen_raw samples in stage series", () => {
    const metrics: ApiJobMetric[] = [
      {
        timestamp: "2026-06-28T17:00:00",
        stage: "qwen_seed",
        elapsed_seconds: 1,
        qwen_raw: 4,
        qwen_valid: 1,
        total_files: 0,
        trace_hits: 0,
        seed: 0,
        valid: 0,
        exception: 0,
        crash: 0,
        notarget: 0,
        hangs: 0,
        flaky: 0,
      },
      {
        timestamp: "2026-06-28T17:00:01",
        stage: "ev_generation",
        elapsed_seconds: 2,
        qwen_raw: 99,
        qwen_valid: 88,
        total_files: 0,
        trace_hits: 0,
        seed: 0,
        valid: 7,
        exception: 2,
        crash: 1,
        notarget: 0,
        hangs: 0,
        flaky: 0,
      },
      {
        timestamp: "2026-06-28T17:00:02",
        stage: "qwen_seed",
        elapsed_seconds: 3,
        qwen_raw: 8,
        qwen_valid: 3,
        total_files: 0,
        trace_hits: 0,
        seed: 0,
        valid: 0,
        exception: 0,
        crash: 0,
        notarget: 0,
        hangs: 0,
        flaky: 0,
      },
    ];

    const series = stageSeries(metrics, "qwen_seed");

    expect(series.map((item) => item.name)).toEqual(["生成候选", "有效种子"]);
    expect(series.map((item) => item.color)).toEqual(["#2563eb", "#178263"]);
    expect(series[0].data).toEqual([
      [1, 4],
      [3, 8],
    ]);
    expect(series[1].data).toEqual([
      [1, 1],
      [3, 3],
    ]);
  });

  it("keeps valid-program colors stable across generation stages", () => {
    const metrics: ApiJobMetric[] = [
      {
        timestamp: "2026-06-28T17:00:01",
        stage: "ev_generation",
        elapsed_seconds: 2,
        qwen_raw: 0,
        qwen_valid: 0,
        total_files: 10,
        trace_hits: 0,
        seed: 0,
        valid: 7,
        exception: 2,
        crash: 1,
        notarget: 0,
        hangs: 0,
        flaky: 0,
      },
    ];

    const series = stageSeries(metrics, "ev_generation");

    expect(series.map((item) => item.name)).toEqual(["有效程序", "异常", "崩溃", "超时"]);
    expect(series.map((item) => item.color)).toEqual(["#178263", "#d29a43", "#c65362", "#63738f"]);
  });

  it("uses incremental tested cases instead of the fixed generated-file total for driver progress", () => {
    const metrics: ApiJobMetric[] = [
      {
        timestamp: "2026-06-28T17:00:00",
        stage: "driver",
        elapsed_seconds: 1,
        qwen_raw: 0,
        qwen_valid: 0,
        tested_cases: 2,
        total_files: 20,
        trace_hits: 0,
        seed: 0,
        valid: 12,
        exception: 8,
        crash: 0,
        notarget: 0,
        hangs: 0,
        flaky: 0,
      },
      {
        timestamp: "2026-06-28T17:00:01",
        stage: "driver",
        elapsed_seconds: 2,
        qwen_raw: 0,
        qwen_valid: 0,
        tested_cases: 6,
        total_files: 20,
        trace_hits: 1,
        seed: 0,
        valid: 12,
        exception: 8,
        crash: 0,
        notarget: 0,
        hangs: 0,
        flaky: 0,
      },
    ];

    const series = stageSeries(metrics, "driver");

    expect(series.map((item) => item.name)).toEqual(["已检测程序", "差异 Catch"]);
    expect(series[0].data).toEqual([
      [1, 2],
      [2, 6],
    ]);
  });

  it("keeps the result categories in the required stable order", () => {
    expect(resultCategoryOrder).toEqual(["seed", "valid", "exception", "crash", "notarget", "hangs", "flaky"]);
  });
});
