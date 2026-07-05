import { ref } from "vue";
import { flushPromises, mount } from "@vue/test-utils";
import { afterEach, describe, expect, it, vi } from "vitest";

import type { ApiDetailPayload, ApiJobPayload, ApiListItem } from "../types/tensorguard";

const selectedApi = ref<ApiListItem | null>(null);
const selectedApiDetail = ref<ApiDetailPayload | null>(null);
const selectedJob = ref<ApiJobPayload | null>(null);
const detailLoading = ref(false);
const detailError = ref<string | null>(null);
const jobLoading = ref(false);
const jobError = ref<string | null>(null);
const runLoading = ref(false);
const runError = ref<string | null>(null);
const pollError = ref<string | null>(null);
const mode = ref<"demo" | "normal">("demo");
const canRun = ref(false);
const liveStageKey = ref<"qwen_seed" | "ev_generation" | "driver">("qwen_seed");
const metricStageKey = ref<"qwen_seed" | "ev_generation" | "driver">("qwen_seed");
const stageStates = ref({
  prompt_check: "pending",
  qwen_seed: "pending",
  ev_generation: "pending",
  driver: "pending",
  summary: "pending",
});
const summaryCounts = ref<ApiDetailPayload["result_counts"] | null>(null);
const metrics = ref([]);
const resultFiles = ref({
  seed: [],
  valid: [],
  exception: [],
  crash: [],
  notarget: [],
  hangs: [],
  flaky: [],
});
const logs = ref<Record<string, string>>({});

const selectApi = vi.fn();
const clearSelection = vi.fn();
const retrySelection = vi.fn();
const retryPollingNow = vi.fn();
const setMode = vi.fn();
const selectMetricStage = vi.fn();
const startRun = vi.fn();

vi.mock("../composables/useApiRun", () => ({
  useApiRun: () => ({
    selectedApi,
    selectedApiDetail,
    selectedJob,
    detailLoading,
    detailError,
    jobLoading,
    jobError,
    runLoading,
    runError,
    pollError,
    mode,
    canRun,
    liveStageKey,
    metricStageKey,
    stageStates,
    metrics,
    resultFiles,
    logs,
    summaryCounts,
    retryPollingNow,
    selectApi,
    clearSelection,
    retrySelection,
    setMode,
    selectMetricStage,
    startRun,
  }),
}));

import ApiRunView from "./ApiRunView.vue";

const selectorStub = {
  props: ["selected"],
  emits: ["select", "library-change"],
  template: `
    <div data-testid="selector">
      <button type="button" data-testid="pick-api" @click="$emit('select', { api: 'torch.add', lib: 'torch' })">pick</button>
    </div>
  `,
};

const timelineStub = {
  props: ["stageStates", "metricStageKey", "liveStageKey"],
  template: `<div data-testid="timeline">{{ metricStageKey }}|{{ liveStageKey }}</div>`,
};

afterEach(() => {
  vi.clearAllMocks();
  selectedApi.value = null;
  selectedApiDetail.value = null;
  selectedJob.value = null;
  detailLoading.value = false;
  detailError.value = null;
  jobLoading.value = false;
  jobError.value = null;
  runLoading.value = false;
  runError.value = null;
  pollError.value = null;
  mode.value = "demo";
  canRun.value = false;
  liveStageKey.value = "qwen_seed";
  metricStageKey.value = "qwen_seed";
  stageStates.value = {
    prompt_check: "pending",
    qwen_seed: "pending",
    ev_generation: "pending",
    driver: "pending",
    summary: "pending",
  };
  summaryCounts.value = null;
  metrics.value = [];
  resultFiles.value = {
    seed: [],
    valid: [],
    exception: [],
    crash: [],
    notarget: [],
    hangs: [],
    flaky: [],
  };
  logs.value = {};
});

describe("ApiRunView", () => {
  it("uses the approved single-API workbench structure", () => {
    const wrapper = mount(ApiRunView, {
      global: {
        stubs: {
          ApiSelector: selectorStub,
          RunTimeline: timelineStub,
        },
      },
    });

    expect(wrapper.get(".api-run-view__page-symbol").text()).toBe("API");
    expect(wrapper.find(".api-run-view__orchestration").exists()).toBe(true);
    expect(wrapper.find(".api-run-view__control-card--device").exists()).toBe(true);
    expect(wrapper.findAll(".api-run-view__control")).toHaveLength(4);
    expect(wrapper.find(".api-run-view__dashboard").exists()).toBe(true);
    expect(wrapper.find(".api-run-view__primary").exists()).toBe(true);
    expect(wrapper.find(".api-run-view__telemetry-strip").exists()).toBe(true);
    expect(wrapper.get(".api-run-view__telemetry-strip").classes()).toContain("api-run-view__telemetry-strip--equal");
    expect(wrapper.find(".api-run-view__log-column").exists()).toBe(true);
    expect(wrapper.get(".api-run-view__log-column").classes()).toContain("api-run-view__log-column--fixed");
    expect(wrapper.get(".api-run-view__log-column").classes()).toContain("api-run-view__log-column--row-aligned");
    expect(wrapper.find(".api-run-view__primary > .stage-chart").exists()).toBe(true);
    expect(wrapper.find(".api-run-view__telemetry-strip > .gpu-chart").exists()).toBe(true);
    expect(wrapper.find(".api-run-view__log-column > .live-log").exists()).toBe(true);
  });

  it("renders the exact title, empty state, and a disabled run action before selection", () => {
    const wrapper = mount(ApiRunView, {
      global: {
        stubs: {
          ApiSelector: selectorStub,
          RunTimeline: timelineStub,
        },
      },
    });

    expect(wrapper.text()).toContain("单 API 安全检测");
    expect(wrapper.text()).toContain("请选择一个 API");
    expect(wrapper.get('button[type="button"][disabled]').text()).toContain("运行");
    expect(wrapper.text()).toContain("GPU 0");
  });

  it("shows loading and error states clearly", async () => {
    selectedApi.value = { api: "torch.add", lib: "torch" } as ApiListItem;
    detailLoading.value = true;

    const wrapper = mount(ApiRunView, {
      global: {
        stubs: {
          ApiSelector: selectorStub,
          RunTimeline: timelineStub,
        },
      },
    });

    expect(wrapper.text()).toContain("正在读取 API 详情");
    expect(wrapper.get('button[type="button"][disabled]').text()).toContain("运行");

    detailLoading.value = false;
    detailError.value = "API 详情加载失败";
    await flushPromises();

    expect(wrapper.text()).toContain("API 详情加载失败");
    await wrapper.get(".api-run-view__retry").trigger("click");
    expect(retrySelection).toHaveBeenCalledTimes(1);
  });

  it("shows a compact live-sync warning when polling is retrying after a transient error", async () => {
    selectedApi.value = { api: "torch.add", lib: "torch" } as ApiListItem;
    selectedApiDetail.value = {
      api: "torch.add",
      lib: "torch",
      has_prompt: true,
      prompt_path: "",
      result_counts: { seed: 0, valid: 9, exception: 1, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
      has_results: true,
      manifest_entry: {
        api: "torch.add",
        library: "torch",
        structured_info: "",
        structured_sha256: "a".repeat(64),
        has_greedy_prompt: false,
        greedy_prompt: null,
        greedy_sha256: null,
        updated_at: "2026-06-28T17:00:00",
      },
      api_list: "data/torch_apis.txt",
      prompt_exists: true,
      results_path: "Results/torch",
      latest_job: null,
    };
    pollError.value = "暂时无法同步作业状态";

    const wrapper = mount(ApiRunView, {
      global: {
        stubs: {
          ApiSelector: selectorStub,
          RunTimeline: timelineStub,
        },
      },
    });

    expect(wrapper.text()).toContain("同步作业状态");
    expect(wrapper.text()).toContain("自动重试中");
    expect(wrapper.text()).toContain("立即重试");
    await wrapper.get(".api-run-view__retry").trigger("click");
    expect(retryPollingNow).toHaveBeenCalledTimes(1);
  });

  it("shows the selected API summary and current counts once loaded", () => {
    selectedApi.value = { api: "torch.add", lib: "torch" } as ApiListItem;
    selectedApiDetail.value = {
      api: "torch.add",
      lib: "torch",
      has_prompt: true,
      prompt_path: "",
      result_counts: { seed: 0, valid: 9, exception: 1, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
      has_results: true,
      manifest_entry: {
        api: "torch.add",
        library: "torch",
        structured_info: "",
        structured_sha256: "a".repeat(64),
        has_greedy_prompt: false,
        greedy_prompt: null,
        greedy_sha256: null,
        updated_at: "2026-06-28T17:00:00",
      },
      api_list: "data/torch_apis.txt",
      prompt_exists: true,
      results_path: "Results/torch",
      latest_job: {
        job_id: "job-1",
        out: "demo_runs/job-1",
        status: "success",
        stage: "summary",
        updated_at: "2026-06-28T17:00:00",
        summary_status: "success",
        mutation_model: "facebook/incoder-1B",
        error: null,
      },
    };
    selectedJob.value = {
      job_id: "job-1",
      out: "demo_runs/job-1",
      status: {
        job_id: "job-1",
        lib: "torch",
        api: "torch.add",
        mode: "demo",
        qwen_model: "../Qwen2.5-Coder-7B-Instruct",
        mutation_model: "facebook/incoder-1B",
        cuda_device: "0",
        status: "success",
        stage: "summary",
        stages: {
          prompt_check: "success",
          qwen_seed: "success",
          ev_generation: "success",
          driver: "success",
          summary: "success",
        },
        error: null,
        updated_at: "2026-06-28T17:00:00",
        candidate_collection: {
          candidate_ids: ["CAND-0001"],
          registered: 1,
          excluded_noise: 2,
          skipped_low_signal: 3,
        },
      },
      summary: {},
      metrics: [],
      environment: {},
      result_files: {
        seed: [],
        valid: [],
        exception: [],
        crash: [],
        notarget: [],
        hangs: [],
        flaky: [],
      },
      logs: {},
    };
    summaryCounts.value = selectedApiDetail.value.result_counts;
    canRun.value = true;

    const wrapper = mount(ApiRunView, {
      global: {
        stubs: {
          ApiSelector: selectorStub,
          RunTimeline: timelineStub,
        },
      },
    });

    expect(wrapper.text()).toContain("torch.add");
    expect(wrapper.text()).toContain("9");
    expect(wrapper.text()).toContain("任务完成");
    expect(wrapper.text()).toContain("已进入候选 · 1 条");
    expect(wrapper.get(".api-run-view__run").text()).toContain("运行");
  });
});
