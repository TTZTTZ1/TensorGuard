import { defineComponent } from "vue";
import { flushPromises, mount } from "@vue/test-utils";
import { afterEach, describe, expect, it, vi } from "vitest";

import type { EnvironmentPayload } from "../types/tensorguard";

import { useEnvironment } from "./useEnvironment";

vi.mock("../services/tensorguard", () => ({
  getEnvironment: vi.fn(),
}));

import { getEnvironment } from "../services/tensorguard";

const mockedGetEnvironment = vi.mocked(getEnvironment);

const environmentFixture = {
  collected_at: "2026-06-28T17:00:00+08:00",
  platform: { system: "Linux", release: "6.8.0", machine: "x86_64" },
  python: { version: "3.11.9", executable: "/usr/bin/python3" },
  frameworks: {
    torch: { installed: true, version: "2.7.0" },
    tensorflow: { installed: false, version: null },
  },
  cuda: { available: true, driver_version: "550.54.15" },
  gpus: [{ index: 0, name: "GPU 0", driver_version: "550.54.15", memory_total_mib: 81920 }],
  warnings: [],
} satisfies EnvironmentPayload;

const Harness = defineComponent({
  template: `
    <div>
      <span data-testid="label">{{ environmentLabel }}</span>
      <span data-testid="loading">{{ loading }}</span>
      <span data-testid="error">{{ error ?? "" }}</span>
    </div>
  `,
  setup() {
    return useEnvironment();
  },
});

afterEach(() => {
  vi.clearAllMocks();
});

describe("useEnvironment", () => {
  it("loads once, caches the payload, and refreshes on demand", async () => {
    mockedGetEnvironment.mockResolvedValue(environmentFixture);

    const first = mount(Harness);
    await flushPromises();

    expect(mockedGetEnvironment).toHaveBeenCalledTimes(1);
    expect(first.get('[data-testid="label"]').text()).toBe("Python 3.11.9 · 1 GPU");
    expect(first.get('[data-testid="loading"]').text()).toBe("false");

    const second = mount(Harness);
    await flushPromises();

    expect(mockedGetEnvironment).toHaveBeenCalledTimes(1);
    expect(second.get('[data-testid="label"]').text()).toBe("Python 3.11.9 · 1 GPU");

    await first.vm.refresh();
    await flushPromises();

    expect(mockedGetEnvironment).toHaveBeenCalledTimes(2);
    expect(mockedGetEnvironment).toHaveBeenNthCalledWith(2, true);
  });
});
