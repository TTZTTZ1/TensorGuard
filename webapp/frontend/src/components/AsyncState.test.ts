import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";

import AsyncState from "./AsyncState.vue";

describe("AsyncState", () => {
  it("renders the loading slot, the empty slot, and a retryable error state", async () => {
    const loading = mount(AsyncState, {
      props: { loading: true },
      slots: { loading: "<p data-testid=\"loading\">加载中</p>" },
    });

    expect(loading.get('[data-testid="loading"]').text()).toBe("加载中");

    const empty = mount(AsyncState, {
      props: { empty: true },
      slots: { empty: "<p data-testid=\"empty\">暂无数据</p>" },
    });

    expect(empty.get('[data-testid="empty"]').text()).toBe("暂无数据");

    const error = mount(AsyncState, {
      props: { error: "请求失败" },
      slots: { error: "<p data-testid=\"error\">请求失败</p>" },
    });

    expect(error.get('[data-testid="error"]').text()).toBe("请求失败");
    await error.get("button").trigger("click");
    expect(error.emitted("retry")).toHaveLength(1);
  });
});
