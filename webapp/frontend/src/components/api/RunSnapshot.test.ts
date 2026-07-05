import { mount } from "@vue/test-utils";
import { afterEach, describe, expect, it, vi } from "vitest";

import type { ApiJobMetric, ApiJobStatus } from "../../types/tensorguard";

import RunSnapshot from "./RunSnapshot.vue";

describe("RunSnapshot", () => {
  afterEach(() => {
    vi.useRealTimers();
  });

  it("shows the live api, stage, status, stage sample, and returned model values", () => {
    const jobStatus: ApiJobStatus = {
      job_id: "job-1",
      lib: "torch",
      api: "torch.add",
      mode: "demo",
      qwen_model: "../Qwen2.5-Coder-7B-Instruct",
      mutation_model: "facebook/incoder-1B",
      cuda_device: "0",
      status: "running",
      stage: "ev_generation",
      stages: {
        prompt_check: "success",
        qwen_seed: "success",
        ev_generation: "running",
        driver: "pending",
        summary: "pending",
      },
      parameters: {
        qwen_n_samples: 5,
        qwen_min_valid: 2,
        qwen_max_rounds: 1,
        qwen_per_api_budget: 300,
        qwen_validate_timeout: 30,
        ev_max_valid: 40,
        ev_batch_size: 5,
        ev_timeout: 300,
        seed_pool_size: 10,
        random_seed: 420,
      },
      error: null,
      updated_at: "2026-06-28T17:00:00",
    };
    const latestMetric: ApiJobMetric = {
      timestamp: "2026-06-28T17:00:02",
      stage: "ev_generation",
      elapsed_seconds: 12,
      qwen_raw: 8,
      qwen_valid: 3,
      total_files: 9,
      trace_hits: 2,
      seed: 0,
      valid: 7,
      exception: 1,
      crash: 0,
      notarget: 0,
      hangs: 0,
      flaky: 0,
    };

    const wrapper = mount(RunSnapshot, {
      props: {
        apiLabel: "torch.add",
        mode: "demo",
        liveStageKey: "ev_generation",
        jobStatus,
        latestMetric,
      },
    });

    expect(wrapper.text()).toContain("torch.add");
    expect(wrapper.text()).toContain("生成候选9");
    expect(wrapper.text()).toContain("有效程序7");
    expect(wrapper.text()).toContain("当前批次2 / 8");
    expect(wrapper.text()).toContain("运行时间00:12");
    expect(wrapper.text()).toContain("../Qwen2.5-Coder-7B-Instruct");
    expect(wrapper.text()).toContain("facebook/incoder-1B");
  });

  it("ticks cumulative job runtime once per second and freezes after completion", async () => {
    vi.useFakeTimers();
    vi.setSystemTime(new Date("2026-06-30T10:01:05+08:00"));
    const status = {
      job_id: "job-1",
      lib: "torch",
      api: "torch.add",
      mode: "demo",
      qwen_model: "qwen",
      mutation_model: "incoder",
      cuda_device: "0",
      status: "running",
      stage: "ev_generation",
      stages: { prompt_check: "success", qwen_seed: "success", ev_generation: "running", driver: "pending", summary: "pending" },
      error: null,
      started_at: "2026-06-30T10:00:00+08:00",
      updated_at: "2026-06-30T10:01:00+08:00",
    } as ApiJobStatus;
    const wrapper = mount(RunSnapshot, {
      props: { apiLabel: "torch.add", mode: "demo", liveStageKey: "ev_generation", jobStatus: status, latestMetric: null },
    });

    expect(wrapper.text()).toContain("运行时间01:05");
    await vi.advanceTimersByTimeAsync(1000);
    expect(wrapper.text()).toContain("运行时间01:06");

    await wrapper.setProps({
      jobStatus: { ...status, status: "success", updated_at: "2026-06-30T10:04:18+08:00" },
    });
    await vi.advanceTimersByTimeAsync(5000);
    expect(wrapper.text()).toContain("运行时间04:18");
  });

  it("shows only live job data instead of stale latest-job details", () => {
    const wrapper = mount(RunSnapshot, {
      props: {
        apiLabel: "torch.add",
        mode: "demo",
        liveStageKey: "qwen_seed",
        jobStatus: null,
        latestMetric: null,
      },
    });

    expect(wrapper.text()).toContain("生成候选暂无");
    expect(wrapper.text()).toContain("有效程序暂无");
    expect(wrapper.text()).toContain("当前批次暂无");
    expect(wrapper.text()).toContain("运行时间暂无");
    expect(wrapper.text()).toContain("按后端配置");
    expect(wrapper.text()).not.toContain("Qwen 模型");
  });
});
