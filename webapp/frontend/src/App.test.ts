import { flushPromises, mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";

import App from "./App.vue";

describe("App", () => {
  it("renders the product name and primary view labels", async () => {
    const wrapper = mount(App);

    await flushPromises();

    const text = wrapper.text();

    expect(text).toContain("TensorGuard");
    expect(text).toContain("框架安全检测概览");
    expect(text).toContain("单 API 运行");
    expect(text).toContain("Bug 复现");
  });

  it("keeps a single main landmark in the shell", async () => {
    const wrapper = mount(App);
    await flushPromises();

    expect(wrapper.findAll("main")).toHaveLength(1);
  });

  it("uses the approved compact TensorGuard product header", async () => {
    const wrapper = mount(App);
    await flushPromises();

    expect(wrapper.get(".app-header__mark").text()).toBe("TG");
    expect(wrapper.get(".app-header__subtitle").text()).toBe("深度学习框架缺陷检测平台");
    expect(wrapper.findAll(".app-header__nav-item")).toHaveLength(3);
    expect(wrapper.get(".app-shell__main").classes()).not.toContain("app-shell__main--drawer-open");
  });
});
