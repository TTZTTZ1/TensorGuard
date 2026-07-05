import { defineComponent } from "vue";
import { flushPromises, mount } from "@vue/test-utils";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import type { ApiListItem } from "../types/tensorguard";

import { useApiCatalog } from "./useApiCatalog";

const { getApis } = vi.hoisted(() => ({
  getApis: vi.fn(),
}));

vi.mock("../services/tensorguard", () => ({
  getApis,
}));

function catalogItem(api: string, lib: "torch" | "tf"): ApiListItem {
  return {
    api,
    lib,
    has_prompt: true,
    prompt_path: `experiment/${lib}/${api}/prompts/structured_info.txt`,
    result_counts: { seed: 0, valid: 0, exception: 0, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
    has_results: false,
    manifest_entry: {
      api,
      library: lib,
      structured_info: `experiment/${lib}/${api}/prompts/structured_info.txt`,
      structured_sha256: "a".repeat(64),
      has_greedy_prompt: false,
      greedy_prompt: null,
      greedy_sha256: null,
      updated_at: "2026-06-28T17:00:00",
    },
  };
}

const items: ApiListItem[] = [
  catalogItem("torch.add", "torch"),
  catalogItem("torch.matmul", "torch"),
  catalogItem("torch.special.Add", "torch"),
];

const tfItems: ApiListItem[] = [catalogItem("tf.add", "tf")];

const Harness = defineComponent({
  template: `
    <div>
      <span data-testid="library">{{ library }}</span>
      <input data-testid="query" v-model="query" />
      <button type="button" data-testid="torch" @click="setLibrary('torch')">torch</button>
      <button type="button" data-testid="tf" @click="setLibrary('tf')">tf</button>
      <span data-testid="loading">{{ loading }}</span>
      <span data-testid="error">{{ error ?? "" }}</span>
      <span data-testid="items">{{ items.map((item) => item.api).join(",") }}</span>
    </div>
  `,
  setup() {
    return useApiCatalog();
  },
});

function deferred<T>() {
  let resolve!: (value: T) => void;
  let reject!: (reason?: unknown) => void;
  const promise = new Promise<T>((res, rej) => {
    resolve = res;
    reject = rej;
  });

  return { promise, resolve, reject };
}

afterEach(() => {
  vi.clearAllMocks();
  vi.useRealTimers();
});

beforeEach(() => {
  vi.useFakeTimers();
});

describe("useApiCatalog", () => {
  it("debounces catalog fetches, preserves empty-query results, and matches partial queries case-insensitively", async () => {
    getApis.mockImplementation(async (_lib: string, query: string) => {
      if (query.toLowerCase().includes("add")) {
        return items.filter((item) => item.api.toLowerCase().includes("add"));
      }

      return items;
    });

    const wrapper = mount(Harness);
    await vi.runAllTimersAsync();
    await flushPromises();

    expect(getApis).toHaveBeenCalledWith("torch", "", 5000);
    expect(wrapper.get('[data-testid="items"]').text()).toBe("torch.add,torch.matmul,torch.special.Add");

    await wrapper.get('[data-testid="query"]').setValue("ADD");
    await vi.advanceTimersByTimeAsync(250);
    await flushPromises();

    expect(getApis).toHaveBeenLastCalledWith("torch", "ADD", 5000);
    expect(wrapper.get('[data-testid="items"]').text()).toBe("torch.add,torch.special.Add");
  });

  it("ignores stale responses when the library changes and stops updating after unmount", async () => {
    const first = deferred<ApiListItem[]>();
    const second = deferred<ApiListItem[]>();

    getApis.mockImplementationOnce(() => first.promise);
    getApis.mockImplementationOnce(() => second.promise);

    const wrapper = mount(Harness);
    await vi.runAllTimersAsync();
    await flushPromises();

    await wrapper.get('[data-testid="tf"]').trigger("click");
    await vi.runAllTimersAsync();
    await flushPromises();

    first.resolve(items);
    await flushPromises();

    expect(wrapper.get('[data-testid="items"]').text()).not.toContain("torch.add");

    second.resolve(tfItems);
    await flushPromises();

    expect(wrapper.get('[data-testid="items"]').text()).toBe("tf.add");

    wrapper.unmount();
    await flushPromises();
  });

  it("invalidates an in-flight response immediately when the query or library changes during debounce", async () => {
    const first = deferred<ApiListItem[]>();
    const second = deferred<ApiListItem[]>();

    getApis
      .mockImplementationOnce(() => first.promise)
      .mockImplementationOnce(() => second.promise);

    const wrapper = mount(Harness);
    await vi.runAllTimersAsync();
    await flushPromises();

    await wrapper.get('[data-testid="query"]').setValue("mat");
    await wrapper.get('[data-testid="tf"]').trigger("click");

    first.resolve(items);
    await flushPromises();

    expect(wrapper.get('[data-testid="items"]').text()).toBe("");

    await vi.advanceTimersByTimeAsync(250);
    await flushPromises();

    second.resolve(tfItems);
    await flushPromises();

    expect(wrapper.get('[data-testid="items"]').text()).toBe("tf.add");
  });
});
