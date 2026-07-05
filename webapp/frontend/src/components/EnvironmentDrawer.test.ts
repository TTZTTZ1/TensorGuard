import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";

import EnvironmentDrawer from "./EnvironmentDrawer.vue";

describe("EnvironmentDrawer", () => {
  it("keeps closed drawers out of the interactive tree", () => {
    const wrapper = mount(EnvironmentDrawer, {
      props: {
        open: false,
        loading: false,
        error: null,
        environment: null,
        environmentLabel: "Python 3.11 · 1 GPU",
      },
    });

    expect(wrapper.find("#environment-drawer").exists()).toBe(false);
    expect(wrapper.find("button").exists()).toBe(false);
  });
});
