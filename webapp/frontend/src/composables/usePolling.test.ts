import { defineComponent, ref } from "vue";
import { flushPromises, mount } from "@vue/test-utils";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import { usePolling } from "./usePolling";

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
  vi.useRealTimers();
  vi.restoreAllMocks();
});

beforeEach(() => {
  vi.useFakeTimers();
});

describe("usePolling", () => {
  it("stops after a terminal poll result and keeps the last value", async () => {
    const calls: string[] = [];
    const task = vi.fn(async () => {
      const next = calls.length === 0 ? "running" : "done";
      calls.push(next);
      return {
        value: next,
        continue: next === "running",
      };
    });

    const Harness = defineComponent({
      template: `
        <div>
          <span data-testid="latest">{{ latest ?? "" }}</span>
          <span data-testid="running">{{ running }}</span>
          <span data-testid="loading">{{ loading }}</span>
          <button type="button" data-testid="start" @click="start">start</button>
          <button type="button" data-testid="stop" @click="stop">stop</button>
        </div>
      `,
      setup() {
        return usePolling(task, 20);
      },
    });

    const wrapper = mount(Harness);
    await wrapper.get('[data-testid="start"]').trigger("click");
    await vi.runAllTimersAsync();
    await flushPromises();

    expect(task).toHaveBeenCalledTimes(2);
    expect(wrapper.get('[data-testid="latest"]').text()).toBe("done");
    expect(wrapper.get('[data-testid="running"]').text()).toBe("false");
    expect(wrapper.get('[data-testid="loading"]').text()).toBe("false");
  });

  it("cancels late updates after unmount", async () => {
    const first = deferred<{ value: string; continue: boolean }>();
    const task = vi.fn(() => first.promise);

    const latest = ref("");
    const Harness = defineComponent({
      template: `<span data-testid="latest">{{ latest }}</span>`,
      setup() {
        const polling = usePolling(task, 20);
        latest.value = "";
        return polling;
      },
    });

    const wrapper = mount(Harness);
    await wrapper.vm.start();
    await vi.runOnlyPendingTimersAsync();

    wrapper.unmount();
    first.resolve({ value: "late", continue: false });
    await flushPromises();

    expect(task).toHaveBeenCalledTimes(1);
  });

  it("retries after a transient rejection and clears the error on the next success", async () => {
    const task = vi
      .fn()
      .mockRejectedValueOnce(new Error("temporary network"))
      .mockResolvedValueOnce({ value: "recovered", continue: false });

    const Harness = defineComponent({
      template: `
        <div>
          <span data-testid="latest">{{ latest ?? "" }}</span>
          <span data-testid="running">{{ running }}</span>
          <span data-testid="loading">{{ loading }}</span>
          <span data-testid="error">{{ error ?? "" }}</span>
          <button type="button" data-testid="start" @click="start">start</button>
        </div>
      `,
      setup() {
        return usePolling(task, 20);
      },
    });

    const wrapper = mount(Harness);
    await wrapper.get('[data-testid="start"]').trigger("click");
    await vi.runOnlyPendingTimersAsync();
    await flushPromises();

    expect(task).toHaveBeenCalledTimes(1);
    expect(wrapper.get('[data-testid="error"]').text()).toBe("temporary network");
    expect(wrapper.get('[data-testid="running"]').text()).toBe("true");

    await vi.advanceTimersByTimeAsync(20);
    await flushPromises();

    expect(task).toHaveBeenCalledTimes(2);
    expect(wrapper.get('[data-testid="latest"]').text()).toBe("recovered");
    expect(wrapper.get('[data-testid="error"]').text()).toBe("");
    expect(wrapper.get('[data-testid="running"]').text()).toBe("false");
  });

  it("restarts immediately after stop even if the prior request is still unresolved", async () => {
    const first = deferred<{ value: string; continue: boolean }>();
    const task = vi
      .fn()
      .mockImplementationOnce(() => first.promise)
      .mockResolvedValueOnce({ value: "fresh", continue: false });

    const Harness = defineComponent({
      template: `
        <div>
          <span data-testid="latest">{{ latest ?? "" }}</span>
          <span data-testid="running">{{ running }}</span>
          <button type="button" data-testid="start" @click="start">start</button>
          <button type="button" data-testid="stop" @click="stop">stop</button>
        </div>
      `,
      setup() {
        return usePolling(task, 20);
      },
    });

    const wrapper = mount(Harness);
    await wrapper.get('[data-testid="start"]').trigger("click");
    await vi.runOnlyPendingTimersAsync();
    await flushPromises();

    expect(task).toHaveBeenCalledTimes(1);

    await wrapper.get('[data-testid="stop"]').trigger("click");
    await wrapper.get('[data-testid="start"]').trigger("click");
    await vi.runOnlyPendingTimersAsync();
    await flushPromises();

    expect(task).toHaveBeenCalledTimes(2);
    expect(wrapper.get('[data-testid="latest"]').text()).toBe("fresh");

    first.resolve({ value: "stale", continue: false });
    await flushPromises();

    expect(wrapper.get('[data-testid="latest"]').text()).toBe("fresh");
    expect(wrapper.get('[data-testid="running"]').text()).toBe("false");
  });
});
