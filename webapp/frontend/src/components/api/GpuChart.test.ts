import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";

import type { ApiJobMetric, EnvironmentPayload } from "../../types/tensorguard";

import GpuChart from "./GpuChart.vue";

const environment = {
  gpus: [{ index: 0, name: "NVIDIA GeForce RTX 5090", driver_version: "590", memory_total_mib: 32640 }],
} as Partial<EnvironmentPayload>;

describe("GpuChart", () => {
  it("renders the latest utilization and memory gauges from live samples", () => {
    const metrics = [
      {
        timestamp: "2026-06-30T10:00:00",
        stage: "ev_generation",
        elapsed_seconds: 20,
        qwen_raw: 5,
        qwen_valid: 2,
        total_files: 8,
        trace_hits: 0,
        seed: 1,
        valid: 5,
        exception: 2,
        crash: 0,
        notarget: 0,
        hangs: 0,
        flaky: 0,
        gpu: {
          collected_at: "2026-06-30T10:00:00",
          index: 0,
          utilization_percent: 61,
          memory_used_mib: 13516,
          memory_total_mib: 32640,
        },
      },
    ] as ApiJobMetric[];
    const wrapper = mount(GpuChart, { props: { metrics, environment } });

    expect(wrapper.text()).toContain("NVIDIA GeForce RTX 5090");
    expect(wrapper.text()).toContain("61%");
    expect(wrapper.text()).toContain("13.2 GB");
    expect(wrapper.get("[data-testid='gpu-utilization-bar']").attributes("style")).toContain("61%");
    expect(wrapper.get("[data-testid='gpu-memory-bar']").attributes("style")).toContain("41.4%");
  });

  it("keeps the gauge layout visible before the first sample", () => {
    const wrapper = mount(GpuChart, { props: { metrics: [], environment } });
    expect(wrapper.text()).toContain("GPU 利用率");
    expect(wrapper.text()).toContain("显存占用");
    expect(wrapper.text()).toContain("暂无采样");
  });
});
