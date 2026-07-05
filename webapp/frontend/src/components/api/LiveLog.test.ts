import { flushPromises, mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";

import LiveLog from "./LiveLog.vue";

describe("LiveLog", () => {
  it("switches among available stage logs and disables stages without output", async () => {
    const wrapper = mount(LiveLog, {
      attachTo: document.body,
      props: {
        stageKey: "qwen_seed",
        logs: {
          "01_qwen_seed.log": "seed <strong>safe</strong>",
          "02_ev_generation.log": "ev_generation log",
          extra: "hidden",
        },
      },
    });

    await flushPromises();

    expect(wrapper.text()).toContain("seed <strong>safe</strong>");
    expect(wrapper.text()).not.toContain("ev_generation log");
    expect(wrapper.text()).not.toContain("driver log");
    expect(wrapper.find("strong").exists()).toBe(false);
    expect(wrapper.find('[data-testid="auto-scroll-toggle"]').exists()).toBe(false);
    expect(wrapper.get(".live-log").classes()).toContain("live-log--fixed-viewport");

    const stageTabs = wrapper.findAll('[data-testid="log-stage-tab"]');
    expect(stageTabs).toHaveLength(3);
    expect(stageTabs.map((tab) => tab.text())).toEqual(["种子生成", "演化变异", "差异检测"]);
    expect(stageTabs[0].classes()).toContain("live-log__stage--active");
    expect(stageTabs[0].attributes("disabled")).toBeUndefined();
    expect(stageTabs[1].attributes("disabled")).toBeUndefined();
    expect(stageTabs[2].attributes("disabled")).toBe("");

    await stageTabs[1].trigger("click");
    await flushPromises();

    expect(wrapper.text()).toContain("ev_generation log");
    expect(wrapper.text()).not.toContain("seed <strong>safe</strong>");
    expect(stageTabs[1].classes()).toContain("live-log__stage--active");
  });

  it("keeps the reader position after manual scroll while new selected-stage output arrives", async () => {
    const wrapper = mount(LiveLog, {
      attachTo: document.body,
      props: {
        stageKey: "qwen_seed",
        logs: { "01_qwen_seed.log": "seed output" },
      },
    });

    await flushPromises();

    const body = wrapper.get("[data-testid='live-log-body']").element as HTMLElement;
    Object.defineProperty(body, "scrollHeight", { value: 500, configurable: true });
    Object.defineProperty(body, "clientHeight", { value: 200, configurable: true });
    Object.defineProperty(body, "scrollTop", { value: 250, writable: true, configurable: true });

    body.dispatchEvent(new Event("scroll"));
    await flushPromises();

    await wrapper.setProps({
      logs: {
        "01_qwen_seed.log": "seed output\nmore",
      },
    });
    await flushPromises();

    expect(body.scrollTop).toBe(250);
  });
});
