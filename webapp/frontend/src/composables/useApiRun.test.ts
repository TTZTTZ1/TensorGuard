import { defineComponent } from "vue";
import { flushPromises, mount } from "@vue/test-utils";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import type { ApiDetailPayload, ApiJobLogName, ApiJobPayload, ApiListItem } from "../types/tensorguard";

const { getApiDetail, getApiJob, getApiJobLog, startApiRun } = vi.hoisted(() => ({
  getApiDetail: vi.fn(),
  getApiJob: vi.fn(),
  getApiJobLog: vi.fn(),
  startApiRun: vi.fn(),
}));

vi.mock("../services/tensorguard", () => ({
  getApiDetail,
  getApiJob,
  getApiJobLog,
  startApiRun,
}));

import { useApiRun } from "./useApiRun";

function apiItem(api: string, lib: "torch" | "tf", valid = 0): ApiListItem {
  return {
    api,
    lib,
    has_prompt: true,
    prompt_path: `experiment/${lib}/${api}/prompts/structured_info.txt`,
    result_counts: { seed: 0, valid, exception: 0, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
    has_results: valid > 0,
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

function detailItem(api: string, lib: "torch" | "tf", jobId: string | null, valid = 0): ApiDetailPayload {
  return {
    ...apiItem(api, lib, valid),
    api_list: `data/${lib}_apis.txt`,
    prompt_exists: true,
    results_path: `Results/${lib}`,
    latest_job:
      jobId === null
        ? null
        : {
            job_id: jobId,
            out: `demo_runs/${jobId}`,
            status: "success",
            stage: "summary",
            updated_at: "2026-06-28T17:00:00",
            summary_status: "success",
            mutation_model: "facebook/incoder-1B",
            error: null,
          },
  };
}

function jobPayload(
  jobId: string,
  api: string,
  lib: "torch" | "tf",
  status: "success" | "running" | "pending" | "failed",
  summaryCounts: ApiJobPayload["summary"] = {},
): ApiJobPayload {
  return {
    job_id: jobId,
    out: `demo_runs/${jobId}`,
    status: {
      job_id: jobId,
      lib,
      api,
      mode: "demo",
      qwen_model: "../Qwen2.5-Coder-7B-Instruct",
      mutation_model: "facebook/incoder-1B",
      cuda_device: "0",
      status,
      stage: status === "success" ? "summary" : "qwen_seed",
      stages: {
        prompt_check: "success",
        qwen_seed: status === "pending" ? "running" : "success",
        ev_generation: status === "success" ? "success" : "pending",
        driver: status === "success" ? "success" : "pending",
        summary: status === "success" ? "success" : "pending",
      },
      error: null,
      updated_at: "2026-06-28T17:00:00",
    },
    summary: summaryCounts,
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
}

function deferred<T>() {
  let resolve!: (value: T) => void;
  let reject!: (reason?: unknown) => void;
  const promise = new Promise<T>((res, rej) => {
    resolve = res;
    reject = rej;
  });

  return { promise, resolve, reject };
}

const Harness = defineComponent({
  template: `
    <div>
      <span data-testid="selected">{{ selectedApi?.api ?? "" }}</span>
      <span data-testid="detail-valid">{{ selectedApiDetail?.result_counts.valid ?? "" }}</span>
      <span data-testid="summary-valid">{{ summaryCounts?.valid ?? "" }}</span>
      <span data-testid="metric-stage">{{ metricStageKey }}</span>
      <span data-testid="detail-loading">{{ detailLoading }}</span>
      <span data-testid="detail-error">{{ detailError ?? "" }}</span>
      <span data-testid="job-id">{{ selectedJob?.job_id ?? "" }}</span>
      <span data-testid="current-job-id">{{ currentJobId ?? "" }}</span>
      <span data-testid="job-status">{{ selectedJob?.status.status ?? "" }}</span>
      <span data-testid="prompt-stage">{{ stageStates.prompt_check }}</span>
      <span data-testid="summary-stage">{{ stageStates.summary }}</span>
      <span data-testid="mode">{{ mode }}</span>
      <span data-testid="can-run">{{ canRun }}</span>
      <span data-testid="qwen-log">{{ logs['01_qwen_seed.log'] ?? '' }}</span>
      <button type="button" data-testid="select-alpha" @click="selectApi(alpha)">alpha</button>
      <button type="button" data-testid="select-beta" @click="selectApi(beta)">beta</button>
      <button type="button" data-testid="pin-qwen" @click="selectMetricStage('qwen_seed')">pin</button>
      <button type="button" data-testid="mode-normal" @click="setMode('normal')">normal</button>
      <button type="button" data-testid="run" @click="startRun">run</button>
    </div>
  `,
  setup() {
    const run = useApiRun();
    const alpha = apiItem("torch.add", "torch", 1);
    const beta = apiItem("torch.matmul", "torch", 9);
    return { ...run, alpha, beta };
  },
});

afterEach(() => {
  vi.clearAllMocks();
  vi.useRealTimers();
});

beforeEach(() => {
  vi.useFakeTimers();
  getApiJobLog.mockImplementation((jobId: string, logName: ApiJobLogName, offset: number) =>
    Promise.resolve({
      job_id: jobId,
      log_name: logName,
      text: "",
      offset,
      next_offset: offset,
      size_bytes: offset,
      has_more: false,
      reset: false,
    }),
  );
});

describe("useApiRun", () => {
  it("drains and appends every available log chunk for the selected job", async () => {
    getApiDetail.mockResolvedValue(detailItem("torch.add", "torch", "job-logs", 1));
    getApiJob.mockResolvedValue(jobPayload("job-logs", "torch.add", "torch", "success"));
    getApiJobLog.mockImplementation((jobId: string, logName: ApiJobLogName, offset: number) => {
      if (logName !== "01_qwen_seed.log") {
        return Promise.resolve({ job_id: jobId, log_name: logName, text: "", offset, next_offset: offset, size_bytes: 0, has_more: false, reset: false });
      }
      if (offset === 0) {
        return Promise.resolve({ job_id: jobId, log_name: logName, text: "first\n", offset: 0, next_offset: 6, size_bytes: 13, has_more: true, reset: false });
      }
      return Promise.resolve({ job_id: jobId, log_name: logName, text: "second\n", offset: 6, next_offset: 13, size_bytes: 13, has_more: false, reset: false });
    });

    const wrapper = mount(Harness);
    await wrapper.get('[data-testid="select-alpha"]').trigger("click");
    await flushPromises();

    expect(wrapper.get('[data-testid="qwen-log"]').text()).toBe("first\nsecond");
    expect(getApiJobLog).toHaveBeenCalledWith("job-logs", "01_qwen_seed.log", 0);
    expect(getApiJobLog).toHaveBeenCalledWith("job-logs", "01_qwen_seed.log", 6);
  });

  it("keeps completed prompt checks successful while summary stays pending during Qwen", async () => {
    getApiDetail.mockResolvedValue({
      ...detailItem("torch.add", "torch", "job-running", 1),
      latest_job: {
        job_id: "job-running",
        out: "demo_runs/job-running",
        status: "running",
        stage: "qwen_seed",
        updated_at: "2026-06-28T17:00:00",
        summary_status: null,
        mutation_model: "facebook/incoder-1B",
        error: null,
      },
    });
    getApiJob.mockResolvedValue({
      ...jobPayload("job-running", "torch.add", "torch", "running"),
      status: {
        ...jobPayload("job-running", "torch.add", "torch", "running").status,
        stage: "qwen_seed",
        stages: {
          prompt_check: "success",
          qwen_seed: "running",
          ev_generation: "pending",
          driver: "pending",
          summary: "pending",
        },
      },
    });

    const wrapper = mount(Harness);
    await wrapper.get('[data-testid="select-alpha"]').trigger("click");
    await flushPromises();

    expect(wrapper.get('[data-testid="prompt-stage"]').text()).toBe("success");
    expect(wrapper.get('[data-testid="summary-stage"]').text()).toBe("pending");
  });

  it("ignores stale selection responses and hydrates the latest job after selection", async () => {
    const alpha = deferred<ApiDetailPayload>();
    const beta = deferred<ApiDetailPayload>();

    getApiDetail.mockImplementationOnce(() => alpha.promise);
    getApiDetail.mockImplementationOnce(() => beta.promise);
    getApiJob.mockResolvedValue(jobPayload("job-beta", "torch.matmul", "torch", "success"));

    const wrapper = mount(Harness);

    await wrapper.get('[data-testid="select-alpha"]').trigger("click");
    await wrapper.get('[data-testid="select-beta"]').trigger("click");

    alpha.resolve(detailItem("torch.add", "torch", "job-alpha", 1));
    await flushPromises();

    expect(wrapper.get('[data-testid="selected"]').text()).toBe("torch.matmul");
    expect(wrapper.get('[data-testid="detail-loading"]').text()).toBe("true");

    beta.resolve(detailItem("torch.matmul", "torch", "job-beta", 9));
    await flushPromises();

    expect(getApiJob).toHaveBeenCalledWith("job-beta");
    expect(wrapper.get('[data-testid="selected"]').text()).toBe("torch.matmul");
    expect(wrapper.get('[data-testid="detail-valid"]').text()).toBe("9");
    expect(wrapper.get('[data-testid="job-id"]').text()).toBe("job-beta");
    expect(wrapper.get('[data-testid="job-status"]').text()).toBe("success");
    expect(wrapper.get('[data-testid="detail-loading"]').text()).toBe("false");
  });

  it("starts a run with the exact backend payload and updates the selected job", async () => {
    getApiDetail.mockResolvedValue(detailItem("torch.add", "torch", null, 2));
    getApiJob.mockResolvedValue(jobPayload("job-run", "torch.add", "torch", "success"));
    startApiRun.mockResolvedValue({ job_id: "job-run", out: "demo_runs/job-run" });

    const wrapper = mount(Harness);
    await wrapper.get('[data-testid="select-alpha"]').trigger("click");
    await flushPromises();

    await wrapper.get('[data-testid="mode-normal"]').trigger("click");
    await wrapper.get('[data-testid="run"]').trigger("click");
    await flushPromises();

    expect(startApiRun).toHaveBeenCalledWith({ lib: "torch", api: "torch.add", mode: "normal" });
    expect(getApiJob).toHaveBeenCalledWith("job-run");
    expect(wrapper.get('[data-testid="job-id"]').text()).toBe("job-run");
    expect(wrapper.get('[data-testid="job-status"]').text()).toBe("success");
    expect(wrapper.get('[data-testid="can-run"]').text()).toBe("true");
  });

  it("allows launching a new run after the latest job has completed", async () => {
    getApiDetail.mockResolvedValue(detailItem("torch.add", "torch", "job-old", 2));
    getApiJob
      .mockResolvedValueOnce(
        jobPayload("job-old", "torch.add", "torch", "success", {
          result_counts: { seed: 0, valid: 3, exception: 0, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
        }),
      )
      .mockResolvedValueOnce(jobPayload("job-new", "torch.add", "torch", "success"));
    startApiRun.mockResolvedValue({ job_id: "job-new", out: "demo_runs/job-new" });

    const wrapper = mount(Harness);
    await wrapper.get('[data-testid="select-alpha"]').trigger("click");
    await flushPromises();

    expect(wrapper.get('[data-testid="can-run"]').text()).toBe("true");

    await wrapper.get('[data-testid="run"]').trigger("click");
    await flushPromises();

    expect(startApiRun).toHaveBeenCalledWith({ lib: "torch", api: "torch.add", mode: "demo" });
    expect(getApiJob).toHaveBeenCalledWith("job-new");
    expect(wrapper.get('[data-testid="job-id"]').text()).toBe("job-new");
    expect(wrapper.get('[data-testid="job-status"]').text()).toBe("success");
  });

  it("prefers the selected job summary counts and refreshes them on hydration", async () => {
    getApiDetail
      .mockResolvedValueOnce(detailItem("torch.add", "torch", "job-1", 1))
      .mockResolvedValueOnce(detailItem("torch.add", "torch", "job-1", 1));
    getApiJob
      .mockResolvedValueOnce(
        jobPayload("job-1", "torch.add", "torch", "success", {
          result_counts: { seed: 0, valid: 7, exception: 2, crash: 1, notarget: 0, hangs: 0, flaky: 0 },
        }),
      )
      .mockResolvedValueOnce(
        jobPayload("job-1", "torch.add", "torch", "success", {
          result_counts: { seed: 0, valid: 12, exception: 1, crash: 0, notarget: 0, hangs: 0, flaky: 0 },
        }),
      );

    const wrapper = mount(Harness);
    await wrapper.get('[data-testid="select-alpha"]').trigger("click");
    await flushPromises();

    expect(wrapper.get('[data-testid="detail-valid"]').text()).toBe("1");
    expect(wrapper.get('[data-testid="summary-valid"]').text()).toBe("7");

    await wrapper.get('[data-testid="select-alpha"]').trigger("click");
    await flushPromises();

    expect(wrapper.get('[data-testid="summary-valid"]').text()).toBe("12");
  });

  it("keeps a stale selection response from rewriting the current job id", async () => {
    const alphaJob = deferred<ApiJobPayload>();

    getApiDetail
      .mockResolvedValueOnce({
        ...detailItem("torch.add", "torch", "job-a", 1),
        latest_job: {
          job_id: "job-a",
          out: "demo_runs/job-a",
          status: "running",
          stage: "ev_generation",
          updated_at: "2026-06-28T17:00:00",
          summary_status: null,
          mutation_model: "facebook/incoder-1B",
          error: null,
        },
      })
      .mockResolvedValueOnce({
        ...detailItem("torch.matmul", "torch", "job-b", 9),
        latest_job: {
          job_id: "job-b",
          out: "demo_runs/job-b",
          status: "success",
          stage: "summary",
          updated_at: "2026-06-28T17:00:00",
          summary_status: "success",
          mutation_model: "facebook/incoder-1B",
          error: null,
        },
      });

    getApiJob
      .mockImplementationOnce(() => alphaJob.promise)
      .mockResolvedValueOnce(jobPayload("job-b", "torch.matmul", "torch", "success"));

    const wrapper = mount(Harness);

    await wrapper.get('[data-testid="select-alpha"]').trigger("click");
    await flushPromises();

    expect(wrapper.get('[data-testid="current-job-id"]').text()).toBe("");

    await wrapper.get('[data-testid="select-beta"]').trigger("click");
    await flushPromises();

    expect(wrapper.get('[data-testid="current-job-id"]').text()).toBe("job-b");
    expect(wrapper.get('[data-testid="job-id"]').text()).toBe("job-b");

    alphaJob.resolve(jobPayload("job-a", "torch.add", "torch", "running"));
    await flushPromises();

    expect(wrapper.get('[data-testid="current-job-id"]').text()).toBe("job-b");
    expect(wrapper.get('[data-testid="job-id"]').text()).toBe("job-b");
    expect(wrapper.get('[data-testid="job-status"]').text()).toBe("success");
  });

  it("keeps a manually selected metric stage pinned when the same API refreshes with the same job", async () => {
    const runningJob = {
      ...jobPayload("job-1", "torch.add", "torch", "running"),
      status: {
        ...jobPayload("job-1", "torch.add", "torch", "running").status,
        stage: "ev_generation",
        stages: {
          prompt_check: "success",
          qwen_seed: "success",
          ev_generation: "running",
          driver: "pending",
          summary: "pending",
        },
      },
    };

    getApiDetail
      .mockResolvedValueOnce({
        ...detailItem("torch.add", "torch", "job-1", 1),
        latest_job: {
          job_id: "job-1",
          out: "demo_runs/job-1",
          status: "running",
          stage: "ev_generation",
          updated_at: "2026-06-28T17:00:00",
          summary_status: null,
          mutation_model: "facebook/incoder-1B",
          error: null,
        },
      })
      .mockResolvedValueOnce({
        ...detailItem("torch.add", "torch", "job-1", 1),
        latest_job: {
          job_id: "job-1",
          out: "demo_runs/job-1",
          status: "running",
          stage: "ev_generation",
          updated_at: "2026-06-28T17:00:00",
          summary_status: null,
          mutation_model: "facebook/incoder-1B",
          error: null,
        },
      });

    getApiJob.mockResolvedValue(runningJob);

    const wrapper = mount(Harness);
    await wrapper.get('[data-testid="select-alpha"]').trigger("click");
    await flushPromises();

    expect(wrapper.get('[data-testid="selected"]').text()).toBe("torch.add");

    await wrapper.get('[data-testid="pin-qwen"]').trigger("click");
    expect(wrapper.get('[data-testid="metric-stage"]').text()).toBe("qwen_seed");

    await wrapper.get('[data-testid="select-alpha"]').trigger("click");
    await flushPromises();

    expect(wrapper.get('[data-testid="job-id"]').text()).toBe("job-1");
    expect(wrapper.get('[data-testid="metric-stage"]').text()).toBe("qwen_seed");
  });

  it("ignores a stale poll result after switching to a new API and hydrating the new job", async () => {
    const stalePoll = deferred<ApiJobPayload>();

    getApiDetail
      .mockResolvedValueOnce({
        ...detailItem("torch.add", "torch", "job-a", 1),
        latest_job: {
          job_id: "job-a",
          out: "demo_runs/job-a",
          status: "running",
          stage: "ev_generation",
          updated_at: "2026-06-28T17:00:00",
          summary_status: null,
          mutation_model: "facebook/incoder-1B",
          error: null,
        },
      })
      .mockResolvedValueOnce({
        ...detailItem("torch.matmul", "torch", "job-b", 9),
        latest_job: {
          job_id: "job-b",
          out: "demo_runs/job-b",
          status: "success",
          stage: "summary",
          updated_at: "2026-06-28T17:00:00",
          summary_status: "success",
          mutation_model: "facebook/incoder-1B",
          error: null,
        },
      });

    getApiJob
      .mockResolvedValueOnce(jobPayload("job-a", "torch.add", "torch", "running"))
      .mockImplementationOnce(() => stalePoll.promise)
      .mockResolvedValueOnce(jobPayload("job-b", "torch.matmul", "torch", "success"));

    const wrapper = mount(Harness);

    await wrapper.get('[data-testid="select-alpha"]').trigger("click");
    await flushPromises();
    await vi.runOnlyPendingTimersAsync();
    await flushPromises();

    expect(wrapper.get('[data-testid="selected"]').text()).toBe("torch.add");
    expect(wrapper.get('[data-testid="job-id"]').text()).toBe("job-a");
    expect(wrapper.get('[data-testid="metric-stage"]').text()).toBe("qwen_seed");

    await wrapper.get('[data-testid="select-beta"]').trigger("click");
    await flushPromises();

    expect(wrapper.get('[data-testid="selected"]').text()).toBe("torch.matmul");
    expect(wrapper.get('[data-testid="job-id"]').text()).toBe("job-b");
    expect(wrapper.get('[data-testid="detail-valid"]').text()).toBe("9");
    expect(wrapper.get('[data-testid="metric-stage"]').text()).toBe("driver");

    stalePoll.resolve(jobPayload("job-a", "torch.add", "torch", "running"));
    await flushPromises();

    expect(wrapper.get('[data-testid="selected"]').text()).toBe("torch.matmul");
    expect(wrapper.get('[data-testid="job-id"]').text()).toBe("job-b");
    expect(wrapper.get('[data-testid="detail-valid"]').text()).toBe("9");
    expect(wrapper.get('[data-testid="metric-stage"]').text()).toBe("driver");
  });
});
