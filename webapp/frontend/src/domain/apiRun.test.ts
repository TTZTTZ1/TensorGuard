import { describe, expect, it } from "vitest";

import {
  candidateCollectionPresentation,
  jobElapsedSeconds,
  stageDefinitions,
  type ApiRunJobLike,
  resolveLiveStageKey,
} from "./apiRun";

describe("apiRun domain", () => {
  it("keeps the visible stage definitions in the expected order", () => {
    expect(stageDefinitions).toEqual([
      { key: "qwen_seed", label: "种子生成", metricKeys: [["生成候选", "qwen_raw", "#2563eb"], ["有效种子", "qwen_valid", "#178263"]] },
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
    ]);
  });

  it("tracks the running backend stage as the live visible stage before completion", () => {
    const job = {
      status: {
        stage: "ev_generation",
        stages: {
          prompt_check: "success",
          qwen_seed: "success",
          ev_generation: "running",
          driver: "pending",
          summary: "pending",
        },
      },
    } satisfies ApiRunJobLike;

    expect(resolveLiveStageKey(job)).toBe("ev_generation");
  });

  it("derives cumulative wall-clock runtime and freezes it at the terminal update", () => {
    const running = {
      status: "running",
      started_at: "2026-06-30T10:00:00+08:00",
      updated_at: "2026-06-30T10:00:10+08:00",
    } as const;
    const finished = {
      ...running,
      status: "success",
      updated_at: "2026-06-30T10:04:18+08:00",
    } as const;

    expect(jobElapsedSeconds(running, Date.parse("2026-06-30T10:01:05+08:00"))).toBe(65);
    expect(jobElapsedSeconds(finished, Date.parse("2026-06-30T11:00:00+08:00"))).toBe(258);
  });

  it("describes automatic candidate collection without treating every result as a candidate", () => {
    expect(candidateCollectionPresentation(null, "running")).toEqual({ tone: "running", label: "检测中" });
    expect(candidateCollectionPresentation({ candidate_ids: ["CAND-1", "CAND-2"] }, "success")).toEqual({
      tone: "success",
      label: "已进入候选 · 2 条",
    });
    expect(
      candidateCollectionPresentation({ candidate_ids: [], excluded_noise: 2, skipped_low_signal: 3 }, "success"),
    ).toEqual({ tone: "muted", label: "未进入候选 · 已过滤 5 条" });
    expect(candidateCollectionPresentation({ candidate_ids: [], error: "scan failed" }, "failed")).toEqual({
      tone: "error",
      label: "归集失败",
    });
  });
});
