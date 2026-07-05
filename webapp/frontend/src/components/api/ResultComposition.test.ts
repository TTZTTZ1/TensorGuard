import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";

import type { ResultCounts } from "../../types/tensorguard";

import { resultCategoryOrder } from "../../domain/chartOptions";
import ResultComposition from "./ResultComposition.vue";

describe("ResultComposition", () => {
  it("renders the seven categories in the required stable order", () => {
    const counts: ResultCounts = {
      seed: 2,
      valid: 7,
      exception: 1,
      crash: 0,
      notarget: 3,
      hangs: 0,
      flaky: 4,
    };

    const wrapper = mount(ResultComposition, {
      props: { counts },
    });

    const labels = wrapper.findAll("[data-testid='result-category']").map((entry) => entry.text());
    expect(labels).toEqual(resultCategoryOrder);
    expect(wrapper.findAll("[data-testid='result-swatch']")).toHaveLength(7);
    expect(wrapper.get("[data-testid='result-total']").text()).toContain("17");
    expect(wrapper.text()).toContain("2");
    expect(wrapper.text()).toContain("7");
    expect(wrapper.text()).toContain("4");
  });
});
