import { defineComponent, ref } from "vue";
import { flushPromises, mount } from "@vue/test-utils";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import type { ApiStageStatus } from "../../types/tensorguard";

import RunTimeline from "./RunTimeline.vue";

afterEach(() => {
  document.body.innerHTML = "";
  vi.clearAllMocks();
  vi.useRealTimers();
});

beforeEach(() => {
  vi.useFakeTimers();
});

function stageState(
  qwenSeed: ApiStageStatus,
  evGeneration: ApiStageStatus,
  driver: ApiStageStatus,
): Record<"prompt_check" | "qwen_seed" | "ev_generation" | "driver" | "summary", ApiStageStatus> {
  return {
    prompt_check: "success",
    qwen_seed: qwenSeed,
    ev_generation: evGeneration,
    driver,
    summary: "pending",
  };
}

const Harness = defineComponent({
  components: { RunTimeline },
  setup() {
    const metricStageKey = ref<"qwen_seed" | "ev_generation" | "driver">("qwen_seed");
    const liveStageKey = ref<"qwen_seed" | "ev_generation" | "driver">("qwen_seed");
    const stages = ref(stageState("success", "pending", "success"));
    const selected = ref<"qwen_seed" | "ev_generation" | "driver">("qwen_seed");

    function selectMetricStage(next: "qwen_seed" | "ev_generation" | "driver") {
      selected.value = next;
      metricStageKey.value = next;
    }

    return { metricStageKey, liveStageKey, stages, selected, selectMetricStage };
  },
  template: `
    <RunTimeline
      :stages="stages"
      :metric-stage-key="metricStageKey"
      :live-stage-key="liveStageKey"
      @select-metric-stage="selectMetricStage"
    />
  `,
});

describe("RunTimeline", () => {
  it("keeps completed stages marked as successful after the pipeline advances", () => {
    const wrapper = mount(RunTimeline, {
      props: {
        stages: stageState("success", "running", "pending"),
        metricStageKey: "qwen_seed",
        liveStageKey: "ev_generation",
      },
    });

    const railItems = wrapper.findAll(".run-timeline__rail-item");
    expect(railItems[0].classes()).toContain("run-timeline__rail-item--success");
    expect(railItems[0].get(".run-timeline__rail-index").text()).toBe("✓");
    expect(railItems[0].get(".run-timeline__rail-status").text()).toBe("已完成");
    expect(railItems[1].classes()).toContain("run-timeline__rail-item--success");
    expect(railItems[2].classes()).toContain("run-timeline__rail-item--running");
  });

  it("navigates enabled metric tabs with keyboard shortcuts and skips disabled stages", async () => {
    const wrapper = mount(Harness, { attachTo: document.body });

    await flushPromises();

    const tabs = wrapper.findAll('[role="tab"]');
    expect(tabs[0].attributes("disabled")).toBeUndefined();
    expect(tabs[1].attributes("disabled")).toBe("");
    expect(tabs[2].attributes("disabled")).toBeUndefined();

    const activeTab = () => wrapper.get('[role="tab"][aria-selected="true"]');

    await activeTab().trigger("keydown", { key: "ArrowRight" });
    await flushPromises();

    expect(wrapper.get('[role="tab"][aria-selected="true"]').text()).toContain("差异检测");
    expect(document.activeElement?.textContent).toContain("差异检测");

    await wrapper.get('[role="tab"][aria-selected="true"]').trigger("keydown", { key: "ArrowLeft" });
    await flushPromises();

    expect(wrapper.get('[role="tab"][aria-selected="true"]').text()).toContain("种子生成");

    await activeTab().trigger("keydown", { key: "End" });
    await flushPromises();

    expect(wrapper.get('[role="tab"][aria-selected="true"]').text()).toContain("差异检测");

    await wrapper.get('[role="tab"][aria-selected="true"]').trigger("keydown", { key: "Home" });
    await flushPromises();

    expect(wrapper.get('[role="tab"][aria-selected="true"]').text()).toContain("种子生成");
  });

  it("allows switching back to the currently running stage", async () => {
    const wrapper = mount(RunTimeline, {
      attachTo: document.body,
      props: {
        stages: stageState("success", "running", "pending"),
        metricStageKey: "qwen_seed",
        liveStageKey: "ev_generation",
      },
    });

    const tabs = wrapper.findAll('[role="tab"]');
    expect(tabs[1].attributes("disabled")).toBeUndefined();
    await tabs[1].trigger("click");
    expect(wrapper.emitted("selectMetricStage")?.[0]).toEqual(["ev_generation"]);
  });
});
