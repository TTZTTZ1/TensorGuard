import { afterEach, describe, expect, it, vi } from "vitest";

import type {
  ApiJobMetric,
  ApiJobParameters,
  ApiListItem,
  ApiRunStartInput,
  CandidateClusterDetail,
  CandidateClusterSummary,
  EnvironmentPayload,
  PromptManifestEntry,
} from "../types/tensorguard";

import { ApiError, request } from "./http";
import {
  createCandidate,
  confirmCandidateCluster,
  deleteCandidateCluster,
  deleteConfirmedBug,
  generateReproReport,
  getApiDetail,
  getApiJob,
  getApiJobLog,
  getApis,
  getCandidate,
  getCandidateCluster,
  getCandidateClusters,
  getCandidateValidationJob,
  getCandidates,
  getConfirmedBug,
  getConfirmedBugs,
  getEnvironment,
  getOverview,
  getReproJob,
  getReproReport,
  reproduceConfirmedBug,
  resetCandidateClusterDraft,
  saveCandidateClusterDraft,
  startApiRun,
  startCandidateValidation,
  updateCandidateClusterStatus,
  updateCandidateStatus,
} from "./tensorguard";

afterEach(() => {
  vi.unstubAllGlobals();
});

type Equal<Left, Right> =
  (<Value>() => Value extends Left ? 1 : 2) extends (<Value>() => Value extends Right ? 1 : 2) ? true : false;
type Assert<Condition extends true> = Condition;
type ManifestEntryContract = Assert<Equal<ApiListItem["manifest_entry"], PromptManifestEntry>>;
type ApiRunInputKeys = Assert<Equal<keyof ApiRunStartInput, "lib" | "api" | "mode">>;
type CandidateClusterRepresentativeContract = Assert<
  Equal<CandidateClusterSummary["representative"], CandidateClusterDetail["representative"]>
>;

const backendEnvironmentFixture = {
  collected_at: "2026-06-28T17:00:00+08:00",
  platform: { system: "Linux", release: "6.8.0", machine: "x86_64" },
  python: { version: "3.11.9", executable: "/usr/bin/python3" },
  frameworks: {
    torch: { installed: true, version: "2.7.0" },
    tensorflow: { installed: false, version: null },
  },
  cuda: { available: true, driver_version: "550.54.15" },
  gpus: [{ index: 0, name: "NVIDIA A800", driver_version: "550.54.15", memory_total_mib: 81920 }],
  warnings: [],
} satisfies EnvironmentPayload;

const backendJobParametersFixture = {
  qwen_n_samples: 5,
  qwen_min_valid: 2,
  qwen_max_rounds: 1,
  qwen_per_api_budget: 300,
  qwen_validate_timeout: 30,
  ev_max_valid: 5,
  ev_batch_size: 1,
  ev_timeout: 300,
  seed_pool_size: 10,
  random_seed: 420,
} satisfies ApiJobParameters;

const backendMetricFixture = {
  timestamp: "2026-06-28T17:00:01+08:00",
  stage: "ev_generation",
  elapsed_seconds: 1.25,
  qwen_raw: 5,
  qwen_valid: 2,
  seed: 2,
  valid: 1,
  exception: 0,
  crash: 0,
  notarget: 0,
  hangs: 0,
  flaky: 0,
  total_files: 3,
  trace_hits: 0,
  gpu: {
    collected_at: "2026-06-28T17:00:01+08:00",
    index: 0,
    utilization_percent: 37,
    memory_used_mib: 20480,
    memory_total_mib: 81920,
  },
} satisfies ApiJobMetric;

const backendManifestEntryFixture = {
  api: "torch.add",
  library: "torch",
  structured_info: "experiment/torch/torch.add/prompts/structured_info.txt",
  greedy_prompt: "experiment/torch/torch.add/prompts/greedy_prompt.txt",
  has_greedy_prompt: true,
  structured_sha256: "a".repeat(64),
  greedy_sha256: "b".repeat(64),
  updated_at: "2026-04-11T04:28:00",
} satisfies PromptManifestEntry;

function jsonResponse(body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}

describe("TensorGuard API service", () => {
  it("encodes API search parameters", async () => {
    const fetchMock = vi.fn().mockResolvedValue(jsonResponse([]));
    vi.stubGlobal("fetch", fetchMock);

    await getApis("torch", "Tensor add&slice/[0]", 5000);

    expect(fetchMock).toHaveBeenCalledWith(
      "/api/apis?lib=torch&q=Tensor+add%26slice%2F%5B0%5D&limit=5000",
      expect.objectContaining({ method: "GET" }),
    );
  });

  it("sends only the supported run-api fields", async () => {
    const fetchMock = vi.fn().mockResolvedValue(jsonResponse({ job_id: "job-1", out: "demo_runs/job-1" }, 202));
    vi.stubGlobal("fetch", fetchMock);
    const input = {
      lib: "torch",
      api: "torch.add",
      mode: "demo",
      cuda_device: "0",
      qwen_model: "qwen-model",
      mut_model: "mutation-model",
    } as const;

    await startApiRun(input);

    const [path, init] = fetchMock.mock.calls[0] as [string, RequestInit];
    expect(path).toBe("/api/run-api");
    expect(init.method).toBe("POST");
    expect(JSON.parse(String(init.body))).toEqual({ lib: "torch", api: "torch.add", mode: "demo" });
  });

  it("throws ApiError with status and backend error message", async () => {
    const payload = { error: "api not found" };
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(jsonResponse(payload, 404)));

    const error = await getApiDetail("torch", "missing.api").catch((reason: unknown) => reason);

    expect(error).toBeInstanceOf(ApiError);
    expect(error).toMatchObject({ status: 404, message: "api not found", payload });
  });

  it("uses the report endpoint for existing retrieval and generation", async () => {
    const fetchMock = vi.fn().mockImplementation(() =>
      Promise.resolve(
        jsonResponse({ job_id: "job/one", report_path: "report.md", report_markdown: "# Report", immutable: true }),
      ),
    );
    vi.stubGlobal("fetch", fetchMock);

    await getReproReport("job/one");
    await generateReproReport("job/one");

    expect(fetchMock).toHaveBeenNthCalledWith(
      1,
      "/api/repro-jobs/job%2Fone/report",
      expect.objectContaining({ method: "GET" }),
    );
    expect(fetchMock).toHaveBeenNthCalledWith(
      2,
      "/api/repro-jobs/job%2Fone/report",
      expect.objectContaining({ method: "POST" }),
    );
  });

  it("wraps overview, environment, and encoded job routes", async () => {
    const fetchMock = vi.fn().mockImplementation(() => Promise.resolve(jsonResponse({})));
    vi.stubGlobal("fetch", fetchMock);

    await getOverview();
    await getEnvironment();
    await getEnvironment(true);
    await getApiJob("api/job 1");
    await getReproJob("repro/job 1");

    expect(fetchMock.mock.calls.map(([path]) => path)).toEqual([
      "/api/overview",
      "/api/environment",
      "/api/environment?refresh=1",
      "/api/api-jobs/api%2Fjob%201",
      "/api/repro-jobs/repro%2Fjob%201",
    ]);
  });

  it("reads API job logs from an encoded byte offset", async () => {
    const fetchMock = vi.fn().mockImplementation(() => Promise.resolve(jsonResponse({})));
    vi.stubGlobal("fetch", fetchMock);

    await getApiJobLog("api/job 1", "01_qwen_seed.log", 128);

    expect(fetchMock).toHaveBeenCalledWith(
      "/api/api-jobs/api%2Fjob%201/logs/01_qwen_seed.log?offset=128",
      expect.objectContaining({ method: "GET" }),
    );
  });

  it("wraps candidate collection, detail, creation, and status routes", async () => {
    const fetchMock = vi.fn().mockImplementation(() => Promise.resolve(jsonResponse({})));
    vi.stubGlobal("fetch", fetchMock);
    const createInput = {
      job_id: "job-1",
      lib: "tf",
      api: "tf.add",
      category: "crash",
      source_path: "demo_runs/api_jobs/job-1/Results/tf/crash/tf.add_1.py",
      note: "review",
    } as const;
    const updateInput = { status: "needs_review", note: "inspect log" } as const;

    await getCandidates();
    await createCandidate(createInput);
    await getCandidate("CAND/1");
    await updateCandidateStatus("CAND/1", updateInput);

    expect(fetchMock.mock.calls.map(([path, init]) => [path, (init as RequestInit).method])).toEqual([
      ["/api/candidates", "GET"],
      ["/api/candidates", "POST"],
      ["/api/candidates/CAND%2F1", "GET"],
      ["/api/candidates/CAND%2F1/status", "POST"],
    ]);
    expect(JSON.parse(String((fetchMock.mock.calls[1][1] as RequestInit).body))).toEqual(createInput);
    expect(JSON.parse(String((fetchMock.mock.calls[3][1] as RequestInit).body))).toEqual(updateInput);
  });

  it("wraps candidate cluster collection and detail routes", async () => {
    const fetchMock = vi.fn().mockImplementation(() => Promise.resolve(jsonResponse({})));
    vi.stubGlobal("fetch", fetchMock);

    await getCandidateClusters();
    await getCandidateCluster("torch.add/device assert");

    expect(fetchMock.mock.calls.map(([path, init]) => [path, (init as RequestInit).method])).toEqual([
      ["/api/candidate-clusters", "GET"],
      ["/api/candidate-clusters/torch.add%2Fdevice%20assert", "GET"],
    ]);
  });

  it("wraps candidate cluster status updates", async () => {
    const fetchMock = vi.fn().mockImplementation(() => Promise.resolve(jsonResponse({})));
    vi.stubGlobal("fetch", fetchMock);

    await updateCandidateClusterStatus("cluster/one", { status: "reproduced", note: "stable" });

    expect(fetchMock).toHaveBeenCalledWith(
      "/api/candidate-clusters/cluster%2Fone/status",
      expect.objectContaining({
        method: "POST",
        body: JSON.stringify({ status: "reproduced", note: "stable" }),
      }),
    );
  });

  it("wraps candidate draft and CPU/GPU validation routes", async () => {
    const fetchMock = vi.fn().mockImplementation(() => Promise.resolve(jsonResponse({})));
    vi.stubGlobal("fetch", fetchMock);

    await saveCandidateClusterDraft("cluster/one", "print('draft')\n");
    await resetCandidateClusterDraft("cluster/one");
    await startCandidateValidation("cluster/one", "print('run')\n", 45);
    await getCandidateValidationJob("run/one");

    expect(fetchMock.mock.calls.map(([path, init]) => [path, (init as RequestInit).method])).toEqual([
      ["/api/candidate-clusters/cluster%2Fone/draft", "POST"],
      ["/api/candidate-clusters/cluster%2Fone/draft/reset", "POST"],
      ["/api/candidate-clusters/cluster%2Fone/validate", "POST"],
      ["/api/candidate-validation-jobs/run%2Fone", "GET"],
    ]);
    expect(JSON.parse(String((fetchMock.mock.calls[0][1] as RequestInit).body))).toEqual({ source: "print('draft')\n" });
    expect(JSON.parse(String((fetchMock.mock.calls[2][1] as RequestInit).body))).toEqual({ source: "print('run')\n", timeout: 45 });
  });

  it("wraps candidate confirmation and ID-protected deletion routes", async () => {
    const fetchMock = vi.fn().mockImplementation(() => Promise.resolve(jsonResponse({})));
    vi.stubGlobal("fetch", fetchMock);

    await confirmCandidateCluster("cluster/one", {
      title: "torch.add 内部断言失败",
      bug_type: "Internal assertion failure",
      review_note: "独立复现后确认。",
    });
    await deleteCandidateCluster("cluster/one", "cluster/one");
    await deleteConfirmedBug("BUG-0001", "BUG-0001");

    expect(fetchMock.mock.calls.map(([path, init]) => [path, (init as RequestInit).method])).toEqual([
      ["/api/candidate-clusters/cluster%2Fone/confirm", "POST"],
      ["/api/candidate-clusters/cluster%2Fone/delete", "POST"],
      ["/api/confirmed-bugs/BUG-0001/delete", "POST"],
    ]);
    expect(JSON.parse(String((fetchMock.mock.calls[0][1] as RequestInit).body))).toEqual({
      title: "torch.add 内部断言失败",
      bug_type: "Internal assertion failure",
      review_note: "独立复现后确认。",
    });
    expect(JSON.parse(String((fetchMock.mock.calls[1][1] as RequestInit).body))).toEqual({ confirmation_id: "cluster/one" });
    expect(JSON.parse(String((fetchMock.mock.calls[2][1] as RequestInit).body))).toEqual({ confirmation_id: "BUG-0001" });
  });

  it("wraps confirmed bug list, detail, and reproduce routes", async () => {
    const fetchMock = vi.fn().mockImplementation(() => Promise.resolve(jsonResponse({})));
    vi.stubGlobal("fetch", fetchMock);
    const replayInput = { modes: ["cpu", "gpu:0"], timeout: 45 } as const;

    await getConfirmedBugs();
    await getConfirmedBug("PAPER/1");
    await reproduceConfirmedBug("PAPER/1", replayInput);

    expect(fetchMock.mock.calls.map(([path, init]) => [path, (init as RequestInit).method])).toEqual([
      ["/api/confirmed-bugs", "GET"],
      ["/api/confirmed-bugs/PAPER%2F1", "GET"],
      ["/api/confirmed-bugs/PAPER%2F1/reproduce", "POST"],
    ]);
    expect(JSON.parse(String((fetchMock.mock.calls[2][1] as RequestInit).body))).toEqual(replayInput);
  });
});

describe("request", () => {
  it("defaults JSON content type while preserving supplied headers", async () => {
    const fetchMock = vi.fn().mockResolvedValue(jsonResponse({ ok: true }));
    vi.stubGlobal("fetch", fetchMock);

    await request("/api/test", {
      headers: { "Content-Type": "application/problem+json", "X-Trace-Id": "trace-1" },
    });

    const headers = new Headers((fetchMock.mock.calls[0][1] as RequestInit).headers);
    expect(headers.get("Content-Type")).toBe("application/problem+json");
    expect(headers.get("X-Trace-Id")).toBe("trace-1");
  });

  it("uses a useful HTTP message for non-JSON errors", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue(new Response("service unavailable", { status: 503, statusText: "Service Unavailable" })),
    );

    const error = await request("/api/test").catch((reason: unknown) => reason);

    expect(error).toBeInstanceOf(ApiError);
    expect(error).toMatchObject({ status: 503, message: "HTTP 503 Service Unavailable", payload: "service unavailable" });
  });
});
