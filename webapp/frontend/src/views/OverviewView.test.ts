import { flushPromises, mount } from "@vue/test-utils";
import { afterEach, describe, expect, it, vi } from "vitest";

import CoverageBaseline from "../components/overview/CoverageBaseline.vue";
import ConfirmedEvidenceList from "../components/overview/ConfirmedEvidenceList.vue";
import type { Library, OverviewPayload, OverviewResultSummary, OverviewSources } from "../types/tensorguard";

const { getOverview, getConfirmedBugs } = vi.hoisted(() => ({
  getOverview: vi.fn(),
  getConfirmedBugs: vi.fn(),
}));

vi.mock("../services/tensorguard", () => ({
  getOverview,
  getConfirmedBugs,
}));

import OverviewView from "./OverviewView.vue";

const overviewPayload = {
  api_total: 4608,
  api_by_lib: { torch: 1568, tf: 3040 },
  prompt_ready_total: 0,
  prompt_ready_by_lib: { torch: 0, tf: 0 },
  paper_bug_total: 14,
  paper_bug_by_framework: { PyTorch: 5, TensorFlow: 9 },
  results: {
    torch: {
      path: "",
      exists: false,
      api_count: 0,
      counts: { seed: 0, valid: 0, exception: 0, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
      trace_path: "",
      trace_exists: false,
      trace_hits: 0,
    },
    tf: {
      path: "",
      exists: false,
      api_count: 0,
      counts: { seed: 0, valid: 0, exception: 0, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
      trace_path: "",
      trace_exists: false,
      trace_hits: 0,
    },
  } satisfies Record<Library, OverviewResultSummary>,
  latest_api_jobs: [],
  latest_repro_jobs: [],
  sources: {
    torch_api_list: "",
    tf_api_list: "",
    prompt_library: "",
    api_jobs: "",
    repro_jobs: "",
  } satisfies OverviewSources,
} satisfies OverviewPayload;

afterEach(() => {
  getOverview.mockReset();
  getConfirmedBugs.mockReset();
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

describe("OverviewView", () => {
  it("renders live overview payload and confirmed bugs", async () => {
    getOverview.mockResolvedValueOnce(overviewPayload);
    getConfirmedBugs.mockResolvedValueOnce([
      {
        id: "PAPER-PT-004",
        display_id: "PT-004",
        api: "torch.sparse.mm",
        bug_type: "Crash / allocator corruption",
        status: "confirmed",
      },
    ]);

    const wrapper = mount(OverviewView);
    await flushPromises();

    expect(wrapper.text()).toContain("框架安全检测概览");
    expect(wrapper.text()).toContain("4,608");
    expect(wrapper.text()).toContain("1,568");
    expect(wrapper.text()).toContain("3,040");
    expect(wrapper.text()).toContain("PT-004");
    expect(wrapper.text()).not.toContain("PAPER-PT-004");
  });

  it("matches the approved overview information architecture", async () => {
    getOverview.mockResolvedValueOnce(overviewPayload);
    getConfirmedBugs.mockResolvedValueOnce([
      {
        id: "PAPER-PT-004",
        display_id: "PT-004",
        api: "torch.sparse.mm",
        bug_type: "Crash / allocator corruption",
        status: "confirmed",
      },
    ]);

    const wrapper = mount(OverviewView);
    await flushPromises();

    expect(wrapper.get(".overview-view__eyebrow").text()).toBe("Coverage & Evidence");
    expect(wrapper.find(".coverage-baseline__coverage-shell").exists()).toBe(true);
    expect(wrapper.find(".coverage-baseline__evidence-card").exists()).toBe(true);
    expect(wrapper.findAll(".coverage-baseline__metric")).toHaveLength(3);
    expect(wrapper.findAll(".detection-pipeline__flow-step")).toHaveLength(5);
    expect(wrapper.findAll(".confirmed-evidence-list__row")).toHaveLength(1);
  });

  it("renders the overview root as a labeled section instead of a main landmark", async () => {
    getOverview.mockResolvedValueOnce(overviewPayload);
    getConfirmedBugs.mockResolvedValueOnce([]);

    const wrapper = mount(OverviewView);
    await flushPromises();

    expect(wrapper.find("main").exists()).toBe(false);
    expect(wrapper.find("section[aria-labelledby='overview-view-title']").exists()).toBe(true);
  });

  it("keeps the newest overview response when overlapping loads resolve out of order", async () => {
    const first = deferred<OverviewPayload>();
    const second = deferred<OverviewPayload>();

    getOverview.mockImplementationOnce(() => first.promise);
    getOverview.mockImplementationOnce(() => second.promise);
    getConfirmedBugs.mockResolvedValueOnce([]);

    const wrapper = mount(OverviewView);
    wrapper.findComponent(CoverageBaseline).vm.$emit("retry");

    await flushPromises();

    first.resolve(overviewPayload);
    await flushPromises();

    expect(wrapper.text()).toContain("正在读取总览数据");

    second.resolve({
      ...overviewPayload,
      api_total: 9999,
      api_by_lib: { torch: 1111, tf: 8888 },
    });
    await flushPromises();

    expect(wrapper.text()).toContain("9,999");
    expect(wrapper.text()).toContain("1,111");
    expect(wrapper.text()).toContain("8,888");
    expect(wrapper.text()).not.toContain("4,608");
  });

  it("keeps the newest confirmed bug response when overlapping loads resolve out of order", async () => {
    const first = deferred<Array<{ display_id: string; api: string; bug_type: string; status: "confirmed" }>>();
    const second = deferred<Array<{ display_id: string; api: string; bug_type: string; status: "confirmed" }>>();

    getOverview.mockResolvedValueOnce(overviewPayload);
    getConfirmedBugs.mockImplementationOnce(() => first.promise);
    getConfirmedBugs.mockImplementationOnce(() => second.promise);

    const wrapper = mount(OverviewView);
    wrapper.findComponent(ConfirmedEvidenceList).vm.$emit("retry");

    await flushPromises();

    first.resolve([
      {
        display_id: "PT-001",
        api: "torch.mul",
        bug_type: "Hang / timeout",
        status: "confirmed",
      },
    ]);
    await flushPromises();

    expect(wrapper.text()).toContain("正在读取已确认证据");

    second.resolve([
      {
        display_id: "PT-999",
        api: "torch.add",
        bug_type: "Crash / allocator corruption",
        status: "confirmed",
      },
    ]);
    await flushPromises();

    expect(wrapper.text()).toContain("PT-999");
    expect(wrapper.text()).not.toContain("PT-001");
  });

  it("renders zero-total coverage as 0% without infinities", () => {
    const wrapper = mount(CoverageBaseline, {
      props: {
        overview: {
          api_total: 0,
          api_by_lib: { torch: 0, tf: 0 },
          prompt_ready_total: 0,
          prompt_ready_by_lib: { torch: 0, tf: 0 },
          paper_bug_total: 0,
          paper_bug_by_framework: {},
          results: {
            torch: {
              path: "",
              exists: false,
              api_count: 0,
              counts: { seed: 0, valid: 0, exception: 0, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
              trace_path: "",
              trace_exists: false,
              trace_hits: 0,
            },
            tf: {
              path: "",
              exists: false,
              api_count: 0,
              counts: { seed: 0, valid: 0, exception: 0, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
              trace_path: "",
              trace_exists: false,
              trace_hits: 0,
            },
          } satisfies Record<Library, OverviewResultSummary>,
          latest_api_jobs: [],
          latest_repro_jobs: [],
          sources: {
            torch_api_list: "",
            tf_api_list: "",
            prompt_library: "",
            api_jobs: "",
            repro_jobs: "",
          } satisfies OverviewSources,
        } satisfies OverviewPayload,
        environmentSummary: "环境信息暂不可用",
      },
    });

    expect(wrapper.text()).toContain("0%");
    expect(wrapper.text()).not.toContain("NaN");
    expect(wrapper.text()).not.toContain("Infinity");
  });

  it("derives framework count from supported API libraries, not bug distribution", () => {
    const wrapper = mount(CoverageBaseline, {
      props: {
        overview: {
          api_total: 4608,
          api_by_lib: { torch: 1568, tf: 3040 },
          prompt_ready_total: 0,
          prompt_ready_by_lib: { torch: 0, tf: 0 },
          paper_bug_total: 1,
          paper_bug_by_framework: { TensorFlow: 1 },
          results: {
            torch: {
              path: "",
              exists: false,
              api_count: 0,
              counts: { seed: 0, valid: 0, exception: 0, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
              trace_path: "",
              trace_exists: false,
              trace_hits: 0,
            },
            tf: {
              path: "",
              exists: false,
              api_count: 0,
              counts: { seed: 0, valid: 0, exception: 0, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
              trace_path: "",
              trace_exists: false,
              trace_hits: 0,
            },
          } satisfies Record<Library, OverviewResultSummary>,
          latest_api_jobs: [],
          latest_repro_jobs: [],
          sources: {
            torch_api_list: "",
            tf_api_list: "",
            prompt_library: "",
            api_jobs: "",
            repro_jobs: "",
          } satisfies OverviewSources,
        } satisfies OverviewPayload,
        environmentSummary: "环境信息暂不可用",
      },
    });

    expect(wrapper.get('[data-metric="frameworks"] .coverage-baseline__metric-value').text()).toBe("2");
  });

  it("suppresses raw PAPER ids and fake severity labels in confirmed evidence rows", () => {
    const wrapper = mount(ConfirmedEvidenceList, {
      props: {
        bugs: [
          {
            display_id: "PT-004",
            api: "torch.sparse.mm",
            bug_type: "Crash / allocator corruption",
            status: "confirmed",
          },
        ],
      },
    });

    const text = wrapper.text();

    expect(text).toContain("PT-004");
    expect(text).toContain("torch.sparse.mm");
    expect(text).toContain("Crash / allocator corruption");
    expect(text).not.toContain("PAPER-PT-004");
    expect(text).not.toMatch(/\bpaper\b/i);
    expect(text).not.toContain("论文");
    expect(text).not.toMatch(/\b(High|Medium|Low)\b/);
  });

  it("renders every confirmed evidence row inside the scrollable evidence list", () => {
    const wrapper = mount(ConfirmedEvidenceList, {
      props: {
        bugs: [
          { display_id: "PT-001", api: "torch.arange", bug_type: "dtype mismatch", status: "confirmed" },
          { display_id: "PT-002", api: "torch.is_nonzero", bug_type: "internal assert", status: "confirmed" },
          { display_id: "TF-001", api: "tf.raw_ops.Abs", bug_type: "backend mismatch", status: "confirmed" },
          { display_id: "TF-002", api: "tf.image.resize", bug_type: "numeric mismatch", status: "confirmed" },
        ],
      },
    });

    expect(wrapper.find(".confirmed-evidence-list__rows").attributes("tabindex")).toBe("0");
    expect(wrapper.findAll(".confirmed-evidence-list__row")).toHaveLength(4);
    expect(wrapper.text()).toContain("TF-002");
  });
});
