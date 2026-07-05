import { defineComponent } from "vue";
import { mount } from "@vue/test-utils";
import { describe, expect, it, beforeEach, afterEach } from "vitest";

import { useHashNavigation } from "./useHashNavigation";

const Harness = defineComponent({
  template: `
    <div>
      <span data-testid="active">{{ activeKey }}</span>
      <button type="button" data-testid="bug" @click="selectKey('bug-replay')">Bug</button>
    </div>
  `,
  setup() {
    return useHashNavigation();
  },
});

describe("useHashNavigation", () => {
  beforeEach(() => {
    window.location.hash = "";
  });

  afterEach(() => {
    window.location.hash = "";
  });

  it("normalizes unknown hashes to overview and updates the hash on selection", async () => {
    window.location.hash = "#mystery";

    const wrapper = mount(Harness);

    expect(wrapper.get('[data-testid="active"]').text()).toBe("overview");
    expect(window.location.hash).toBe("#overview");

    await wrapper.get('[data-testid="bug"]').trigger("click");

    expect(wrapper.get('[data-testid="active"]').text()).toBe("bug-replay");
    expect(window.location.hash).toBe("#bug-replay");
  });
});
