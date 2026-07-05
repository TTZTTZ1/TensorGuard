import { flushPromises, mount } from "@vue/test-utils";
import { afterEach, describe, expect, it, vi } from "vitest";

import type { ApiJobMetric } from "../../types/tensorguard";

const { setOption, resize, dispose, echartsInit } = vi.hoisted(() => {
  const setOption = vi.fn();
  const resize = vi.fn();
  const dispose = vi.fn();
  const echartsInit = vi.fn(() => ({ setOption, resize, dispose }));
  return { setOption, resize, dispose, echartsInit };
});

vi.mock("echarts/core", () => ({
  init: echartsInit,
  use: vi.fn(),
}));

import StageChart from "./StageChart.vue";

afterEach(() => {
  vi.clearAllMocks();
  document.body.innerHTML = "";
});

function sampleMetrics(): ApiJobMetric[] {
  return [
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
    {
      timestamp: "2026-06-28T17:00:02",
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
  ];
}

describe("StageChart", () => {
  it("reuses one chart instance and updates the selected stage series", async () => {
    const wrapper = mount(StageChart, {
      props: {
        metrics: sampleMetrics(),
        stageKey: "qwen_seed",
      },
    });

    await flushPromises();

    expect(echartsInit).toHaveBeenCalledTimes(1);
    expect(setOption).toHaveBeenCalledTimes(1);
    expect(setOption.mock.calls[0][0].series[0].data).toEqual([
      [1, 4],
      [3, 8],
    ]);
    expect(setOption.mock.calls[0][0].xAxis.name).toBe("阶段运行时间（秒）");
    expect(setOption.mock.calls[0][0].yAxis.name).toBe("累计数量");
    expect(setOption.mock.calls[0][0].xAxis.axisTick.show).toBe(false);
    expect(setOption.mock.calls[0][0].yAxis.axisTick.show).toBe(false);

    await wrapper.setProps({ stageKey: "ev_generation" });
    await flushPromises();

    expect(echartsInit).toHaveBeenCalledTimes(1);
    expect(setOption).toHaveBeenCalledTimes(2);
    expect(setOption.mock.calls[1][0].series.map((series: { name: string }) => series.name)).toEqual([
      "有效程序",
      "异常",
      "崩溃",
      "超时",
    ]);
    expect(setOption.mock.calls[1][0].series.map((series: { lineStyle: { color: string } }) => series.lineStyle.color)).toEqual([
      "#178263",
      "#d29a43",
      "#c65362",
      "#63738f",
    ]);

    const stats = wrapper.findAll(".stage-chart__stat");
    expect(stats).toHaveLength(4);
    expect(stats.map((stat) => stat.text())).toEqual(["有效程序7", "异常2", "崩溃1", "超时0"]);
    expect(stats.map((stat) => stat.attributes("style"))).toEqual([
      "--series-color: #178263;",
      "--series-color: #d29a43;",
      "--series-color: #c65362;",
      "--series-color: #63738f;",
    ]);

    wrapper.unmount();

    expect(dispose).toHaveBeenCalledTimes(1);
  });

  it("shows an empty state instead of a blank chart when no samples match", async () => {
    const wrapper = mount(StageChart, {
      props: {
        metrics: [
          {
            timestamp: "2026-06-28T17:00:00",
            stage: "driver",
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
        ],
        stageKey: "qwen_seed",
      },
    });

    await flushPromises();

    expect(wrapper.text()).toContain("暂无");
    expect(wrapper.find(".stage-chart__empty-rail").exists()).toBe(true);
    expect(wrapper.findAll(".stage-chart__empty-dot")).toHaveLength(3);
    expect(echartsInit).not.toHaveBeenCalled();
  });
});
