import { flushPromises, mount } from "@vue/test-utils";
import { beforeEach, describe, expect, it, vi } from "vitest";

const services = vi.hoisted(() => ({
  getConfirmedBugs: vi.fn(),
  getConfirmedBug: vi.fn(),
  getCandidates: vi.fn(),
  getCandidateClusters: vi.fn(),
  getOverview: vi.fn(),
  getEnvironment: vi.fn(),
  getCandidate: vi.fn(),
  getCandidateCluster: vi.fn(),
  getCandidateValidationJob: vi.fn(),
  saveCandidateClusterDraft: vi.fn(),
  resetCandidateClusterDraft: vi.fn(),
  startCandidateValidation: vi.fn(),
  confirmCandidateCluster: vi.fn(),
  deleteCandidateCluster: vi.fn(),
  deleteConfirmedBug: vi.fn(),
  updateCandidateClusterStatus: vi.fn(),
  reproduceConfirmedBug: vi.fn(),
  getReproJob: vi.fn(),
  getReproReport: vi.fn(),
  generateReproReport: vi.fn(),
}));

vi.mock("../services/tensorguard", () => services);

import BugReplayView from "./BugReplayView.vue";

const summary = {
  id: "PAPER-PT-004",
  display_id: "PT-004",
  title: "Malformed sparse tensor triggers invalid free",
  framework: "PyTorch",
  api: "torch.sparse.mm",
  related_apis: [],
  bug_type: "allocator corruption",
  status: "confirmed",
  source: { document: "internal", section: "appendix" },
  trigger: "malformed sparse structure",
  expected: "Reject invalid sparse indices with a Python exception.",
  observed: "The child process aborts with SIGABRT.",
  reproducible: true,
  minimized: true,
  files: { repro: "repro.py", report: "report.md" },
  tags: ["sparse"],
  path: "reports/confirmed/PT-004",
  meta_path: "reports/confirmed/PT-004/meta.json",
};

const dynamicSummary = {
  ...summary,
  id: "BUG-0001",
  display_id: "BUG-0001",
  title: "torch.quantile confirmed candidate",
  api: "torch.quantile",
  dynamic: true,
  deletable: true,
};

const dynamicDetail = {
  index: dynamicSummary,
  meta: dynamicSummary,
  display_id: "BUG-0001",
  bug_dir: "demo_runs/confirmed_bugs/BUG-0001",
  repro_path: "demo_runs/confirmed_bugs/BUG-0001/repro.py",
  report_path: "demo_runs/confirmed_bugs/BUG-0001/report.md",
  repro_code: "print('confirmed')\n",
  report_markdown: "",
  latest_repro_job_id: null,
};

const candidateCluster = {
  cluster_id: "torch_quantile_exception_mismatch_001",
  lib: "torch",
  api: "torch.quantile",
  job_id: "api_torch_quantile_1",
  category: "exception",
  bug_pattern: "CPU/GPU exception mismatch / CUDA device-side assert",
  cluster_status: "needs_minimize",
  confidence: "high",
  member_count: 37,
  excluded_count: 5,
  representative: {
    candidate_id: "CAND-0001",
    source_path: "demo_runs/api_jobs/api_torch_quantile_1/Results/torch/exception/torch.quantile_1.py",
    source_name: "torch.quantile_1.py",
    error_summary: "CPU RuntimeError GPU CUDA device-side assert triggered",
    score: 0.95,
  },
  created_at: "2026-06-30T10:00:00+08:00",
  updated_at: "2026-06-30T10:00:00+08:00",
};

const candidateClusterDetail = {
  ...candidateCluster,
  members: [
    {
      candidate_id: "CAND-0001",
      source_path: "demo_runs/api_jobs/api_torch_quantile_1/Results/torch/exception/torch.quantile_1.py",
      source_name: "torch.quantile_1.py",
      error_summary: "CPU RuntimeError GPU CUDA device-side assert triggered",
      score: 0.95,
      status: "pending_review",
    },
  ],
  excluded: [
    {
      candidate_id: "CAND-0002",
      source_path: "demo_runs/api_jobs/api_torch_quantile_1/Results/torch/exception/torch.quantile_2.py",
      source_name: "torch.quantile_2.py",
      reason: "generated_code_error",
      error_summary: "SyntaxError: unterminated triple-quoted string literal",
    },
  ],
  representative_source_code: "import torch\nq = torch.tensor([1.0, 2.5])\ntorch.quantile(torch.ones(4), q)",
  minimization_draft: "import torch\n# TODO: minimize candidate\n",
  draft_saved: false,
  draft_modified: true,
  draft_sha256: "a".repeat(64),
  latest_validation_job_id: null,
  latest_validation: null,
  review_defaults: {
    title: "torch.quantile · CPU/GPU exception mismatch",
    bug_type: "CPU/GPU exception mismatch",
    review_note: "已完成独立进程复现，等待人工确认。",
  },
};

describe("BugReplayView", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    services.getConfirmedBugs.mockResolvedValue([summary]);
    services.getCandidates.mockResolvedValue([]);
    services.getCandidateClusters.mockResolvedValue([candidateCluster]);
    services.getOverview.mockResolvedValue({ latest_repro_jobs: [] });
    services.getEnvironment.mockResolvedValue({
      collected_at: "2026-06-30T10:00:00+08:00",
      platform: { system: "Linux", release: "6.8", machine: "x86_64" },
      python: { version: "3.10.20", executable: "/env/bin/python" },
      frameworks: {
        torch: { installed: true, version: "2.11.0+cu130" },
        tensorflow: { installed: true, version: "2.21.0" },
      },
      cuda: { available: true, driver_version: "590.00" },
      gpus: [{ index: 0, name: "NVIDIA GeForce RTX 5090", driver_version: "590.00", memory_total_mib: 32640 }],
      warnings: [],
    });
    services.getConfirmedBug.mockResolvedValue({
      index: summary,
      meta: summary,
      display_id: "PT-004",
      bug_dir: "reports/confirmed/PT-004",
      repro_path: "reports/confirmed/PT-004/repro.py",
      report_path: "reports/confirmed/PT-004/report.md",
      repro_code: "import torch\ntorch.sparse.mm(a, b)",
      report_markdown: "",
      latest_repro_job_id: null,
    });
    services.getCandidateCluster.mockResolvedValue(candidateClusterDetail);
    services.saveCandidateClusterDraft.mockResolvedValue({
      ...candidateClusterDetail,
      minimization_draft: "print('saved draft')\n",
      draft_saved: true,
    });
    services.resetCandidateClusterDraft.mockResolvedValue({
      ...candidateClusterDetail,
      minimization_draft: candidateClusterDetail.representative_source_code,
      draft_saved: true,
      draft_modified: false,
    });
    services.startCandidateValidation.mockResolvedValue({
      run_id: "candidate-run-1",
      cluster_id: candidateCluster.cluster_id,
      source_sha256: "validated-hash",
    });
    services.getCandidateValidationJob.mockResolvedValue({
      run_id: "candidate-run-1",
      cluster_id: candidateCluster.cluster_id,
      status: "finished",
      source_sha256: "validated-hash",
      timeout_seconds: 60,
      started_at: "2026-07-01T18:00:00+08:00",
      updated_at: "2026-07-01T18:00:01+08:00",
      modes: {
        cpu: { status: "finished", returncode: 0, timed_out: false, log: "cpu.log", started_at: null, finished_at: null },
        gpu0: { status: "finished", returncode: 1, timed_out: false, log: "gpu0.log", started_at: null, finished_at: null },
      },
      logs: { cpu: "CPU output", gpu0: "GPU output" },
    });
    services.confirmCandidateCluster.mockResolvedValue(dynamicDetail);
    services.deleteCandidateCluster.mockResolvedValue({ deleted: candidateCluster.cluster_id });
    services.deleteConfirmedBug.mockResolvedValue({ deleted: "BUG-0001" });
    services.updateCandidateClusterStatus.mockResolvedValue({ ...candidateCluster, cluster_status: "needs_minimize" });
  });

  it("shows current environment before any reproduction has run", async () => {
    const wrapper = mount(BugReplayView);
    await flushPromises();

    expect(services.getEnvironment).toHaveBeenCalledTimes(1);
    expect(wrapper.text()).toContain("当前环境");
    expect(wrapper.text()).toContain("NVIDIA GeForce RTX 5090");
    expect(wrapper.text()).toContain("3.10.20");
    expect(wrapper.text()).toContain("等待当前环境复现");
  });

  it("renders the approved evidence workbench from live confirmed-bug data", async () => {
    const wrapper = mount(BugReplayView);
    await flushPromises();

    const counters = wrapper.findAll(".bug-replay-view__count-item");
    expect(counters).toHaveLength(3);
    expect(counters.map((item) => item.classes())).toEqual([
      expect.arrayContaining(["bug-replay-view__count-item--confirmed"]),
      expect.arrayContaining(["bug-replay-view__count-item--candidate"]),
      expect.arrayContaining(["bug-replay-view__count-item--minimize"]),
    ]);
    expect(counters.map((item) => item.get("b").text())).toEqual(["1", "1", "1"]);

    expect(wrapper.get(".bug-replay-view__page-symbol").text()).toBe("!");
    expect(wrapper.findAll(".bug-replay-view__layout")).toHaveLength(1);
    expect(wrapper.get(".bug-replay-view__master").classes()).toContain("bug-replay-view__master--page-flow");
    expect(wrapper.findAll(".bug-replay-view__master-frame")).toHaveLength(1);
    expect(wrapper.get(".bug-replay-view__list").classes()).toContain("bug-replay-view__list--contained");
    expect(wrapper.text()).toContain("PT-004");
    expect(wrapper.text()).toContain("torch.sparse.mm");
    expect(wrapper.text()).toContain("Reject invalid sparse indices");
    expect(wrapper.text()).toContain("SIGABRT");
    expect(wrapper.text()).not.toContain("PAPER");
    expect(wrapper.text()).not.toContain("严重性");
  });

  it("separates reproduction evidence and orders the compact confirmed tools", async () => {
    const wrapper = mount(BugReplayView);
    await flushPromises();

    const evidencePanes = wrapper.findAll(".bug-replay-view__evidence-pane");
    expect(evidencePanes).toHaveLength(2);
    expect(evidencePanes.map((pane) => pane.get("small").text())).toEqual(["repro.py", "CURRENT RUN OUTPUT"]);

    const toolPanels = wrapper.findAll(".bug-replay-view__confirmed-tool");
    expect(toolPanels.map((panel) => panel.attributes("data-tool"))).toEqual(["environment", "execution", "report"]);

    expect(wrapper.find(".bug-replay-view__tag--confirmed").exists()).toBe(true);
    expect(wrapper.find(".bug-replay-view__tag--minimized").exists()).toBe(true);
  });

  it("filters the evidence list without discarding the selected detail", async () => {
    const wrapper = mount(BugReplayView);
    await flushPromises();

    await wrapper.get('input[type="search"]').setValue("not-found");
    expect(wrapper.text()).toContain("未找到匹配证据");
    expect(wrapper.text()).toContain("torch.sparse.mm");
  });

  it("reuses an existing current-environment report instead of generating over it", async () => {
    services.getConfirmedBug.mockResolvedValueOnce({
      index: summary,
      meta: summary,
      display_id: "PT-004",
      bug_dir: "reports/confirmed/PT-004",
      repro_path: "reports/confirmed/PT-004/repro.py",
      report_path: "reports/confirmed/PT-004/report.md",
      repro_code: "import torch\ntorch.sparse.mm(a, b)",
      report_markdown: "",
      latest_repro_job_id: "repro-1",
    });
    services.getReproJob.mockResolvedValueOnce({
      job_id: "repro-1",
      out: "demo_runs/repro-1",
      status: {
        job_id: "repro-1",
        bug_id: summary.id,
        status: "finished",
        started_at: "2026-06-29T08:00:00",
        updated_at: "2026-06-29T08:00:02",
        out: "demo_runs/repro-1",
        timeout_seconds: 60,
        modes: {
          "gpu:0": {
            status: "finished",
            returncode: -6,
            timed_out: false,
            log: "gpu:0.log",
            started_at: "2026-06-29T08:00:00",
            finished_at: "2026-06-29T08:00:02",
            execution_profile: "visible_gpu_0",
            actual_device: "cuda:0",
            evidence: {
              verdict: "reproduced",
              outcome: "signal",
              reason: "SIGABRT reproduced",
              signal: "SIGABRT",
              signal_number: 6,
            },
          },
        },
        report: "report.md",
        error: null,
      },
      logs: {},
      environment: {},
      report_exists: true,
      report_path: "demo_runs/repro-1/report.md",
      report_markdown: "# current environment evidence",
    });
    services.getReproReport.mockResolvedValueOnce({
      job_id: "repro-1",
      report_path: "demo_runs/repro-1/report.md",
      report_markdown: "# current environment evidence",
      immutable: true,
    });

    const wrapper = mount(BugReplayView);
    await flushPromises();

    expect(wrapper.text()).toContain("报告已归档");
    expect(wrapper.text()).toContain("当前环境复现成功");
    expect(services.getReproJob).toHaveBeenCalledWith("repro-1");
    const reportButton = wrapper.findAll("button").find((button) => button.text() === "查看报告");
    expect(reportButton).toBeDefined();
    await reportButton?.trigger("click");
    await flushPromises();

    expect(services.getReproReport).toHaveBeenCalledWith("repro-1");
    expect(services.generateReproReport).not.toHaveBeenCalled();
  });

  it("keeps candidate review visible when no candidate clusters exist", async () => {
    services.getCandidateClusters.mockResolvedValueOnce([]);
    const wrapper = mount(BugReplayView);
    await flushPromises();

    const candidateTab = wrapper.findAll(".bug-replay-view__source-tabs button").find((button) => button.text() === "候选审核");
    await candidateTab?.trigger("click");
    await flushPromises();

    expect(wrapper.find(".bug-replay-view__master-frame").exists()).toBe(true);
    expect(wrapper.text()).toContain("暂无候选簇");
    expect(wrapper.get(".bug-replay-view__candidate-empty").text()).toContain("暂无可审核的候选簇");
  });

  it("renders searchable candidate clusters instead of raw candidate files", async () => {
    const wrapper = mount(BugReplayView);
    await flushPromises();

    const candidateTab = wrapper.findAll(".bug-replay-view__source-tabs button").find((button) => button.text() === "候选审核");
    expect(candidateTab).toBeDefined();
    await candidateTab?.trigger("click");
    await flushPromises();

    expect(services.getCandidateClusters).toHaveBeenCalledTimes(1);
    expect(services.getCandidateCluster).toHaveBeenCalledWith(candidateCluster.cluster_id);
    expect(wrapper.text()).toContain("CPU/GPU exception mismatch");
    expect(wrapper.text()).toContain("同类程序 37");
    expect(wrapper.text()).toContain("已过滤 5");
    expect(wrapper.text()).toContain("聚类依据");
    expect(wrapper.text()).toContain("人工整理 repro.py");
    expect(wrapper.findAll(".bug-replay-view__file-head")).toHaveLength(2);
    expect(wrapper.findAll(".bug-replay-view__file-head .bug-replay-view__file-icon").map((item) => item.text())).toEqual(["SRC", "PY"]);
    expect(wrapper.get('[data-testid="candidate-source-path"]').text()).toBe(candidateCluster.representative.source_path);
    expect(wrapper.find(".bug-replay-view__review-footer").exists()).toBe(true);
    expect(wrapper.findAll(".bug-replay-view__candidate-reason > article")).toHaveLength(3);
    expect(wrapper.findAll(".bug-replay-view__candidate-workbench > section")).toHaveLength(4);
    expect(wrapper.findAll(".bug-replay-view__candidate-file--wide")).toHaveLength(2);
    expect(wrapper.find(".bug-replay-view__review-card--full").exists()).toBe(true);

    await wrapper.get('input[type="search"]').setValue("device assert");
    expect(wrapper.text()).toContain("torch.quantile");
    await wrapper.get('input[type="search"]').setValue("sparse");
    expect(wrapper.text()).toContain("暂无候选簇");
  });

  it("removes ambiguous review actions and requires the cluster ID to delete", async () => {
    const wrapper = mount(BugReplayView);
    await flushPromises();

    const candidateTab = wrapper.findAll(".bug-replay-view__source-tabs button").find((button) => button.text() === "候选审核");
    await candidateTab?.trigger("click");
    await flushPromises();

    expect(wrapper.text()).not.toContain("标记待分析");
    expect(wrapper.text()).not.toContain("标记可复现");
    await wrapper.get('[data-testid="delete-candidate"]').trigger("click");
    const input = wrapper.get('[data-testid="delete-id-input"]');
    await input.setValue(candidateCluster.cluster_id);
    await wrapper.get('[data-testid="confirm-delete"]').trigger("click");
    await flushPromises();

    expect(services.deleteCandidateCluster).toHaveBeenCalledWith(candidateCluster.cluster_id, candidateCluster.cluster_id);
  });

  it("edits, saves, resets, and validates a minimized candidate draft", async () => {
    const wrapper = mount(BugReplayView);
    await flushPromises();

    const candidateTab = wrapper.findAll(".bug-replay-view__source-tabs button").find((button) => button.text() === "候选审核");
    await candidateTab?.trigger("click");
    await flushPromises();

    const editor = wrapper.get('[data-testid="candidate-draft-editor"]');
    expect((editor.element as HTMLTextAreaElement).value).toContain("TODO: minimize candidate");
    await editor.setValue("print('saved draft')\n");
    await wrapper.get('[data-testid="save-candidate-draft"]').trigger("click");
    await flushPromises();
    expect(services.saveCandidateClusterDraft).toHaveBeenCalledWith(candidateCluster.cluster_id, "print('saved draft')\n");

    await wrapper.get('[data-testid="reset-candidate-draft"]').trigger("click");
    await flushPromises();
    expect(services.resetCandidateClusterDraft).toHaveBeenCalledWith(candidateCluster.cluster_id);

    await editor.setValue("print('validate')\n");
    await wrapper.get('[data-testid="validate-candidate-draft"]').trigger("click");
    await flushPromises();
    expect(services.startCandidateValidation).toHaveBeenCalledWith(candidateCluster.cluster_id, "print('validate')\n", 60);
    expect(services.getCandidateValidationJob).toHaveBeenCalledWith("candidate-run-1");
    expect(wrapper.get('[data-testid="candidate-cpu-output"]').text()).toContain("CPU output");
    expect(wrapper.get('[data-testid="candidate-gpu-output"]').text()).toContain("GPU output");
    expect((wrapper.get('[data-testid="candidate-review-title"]').element as HTMLInputElement).value).toBe(
      "torch.quantile · CPU/GPU exception mismatch",
    );
    await wrapper.get('[data-testid="candidate-review-note"]').setValue("CPU 与 GPU 异常路径稳定不一致。");
    await wrapper.get('[data-testid="confirm-candidate-bug"]').trigger("click");
    await flushPromises();
    expect(services.confirmCandidateCluster).toHaveBeenCalledWith(candidateCluster.cluster_id, {
      title: "torch.quantile · CPU/GPU exception mismatch",
      bug_type: "CPU/GPU exception mismatch",
      review_note: "CPU 与 GPU 异常路径稳定不一致。",
    });
    expect(wrapper.text()).toContain("BUG-0001");
  });

  it("allows ID-protected deletion only for dynamic confirmed Bugs", async () => {
    services.getConfirmedBugs.mockResolvedValue([dynamicSummary]);
    services.getConfirmedBug.mockResolvedValue(dynamicDetail);
    const wrapper = mount(BugReplayView);
    await flushPromises();

    await wrapper.get('[data-testid="delete-confirmed-bug"]').trigger("click");
    await wrapper.get('[data-testid="delete-id-input"]').setValue("BUG-0001");
    await wrapper.get('[data-testid="confirm-delete"]').trigger("click");
    await flushPromises();

    expect(services.deleteConfirmedBug).toHaveBeenCalledWith("BUG-0001", "BUG-0001");
  });

  it("requires another validation after the saved repro changes", async () => {
    const wrapper = mount(BugReplayView);
    await flushPromises();

    const candidateTab = wrapper.findAll(".bug-replay-view__source-tabs button").find((button) => button.text() === "候选审核");
    await candidateTab?.trigger("click");
    await flushPromises();

    const editor = wrapper.get('[data-testid="candidate-draft-editor"]');
    await editor.setValue("print('validated')\n");
    await wrapper.get('[data-testid="validate-candidate-draft"]').trigger("click");
    await flushPromises();
    expect(wrapper.get('[data-testid="confirm-candidate-bug"]').attributes("disabled")).toBeUndefined();

    services.saveCandidateClusterDraft.mockResolvedValueOnce({
      ...candidateClusterDetail,
      minimization_draft: "print('changed after validation')\n",
      draft_saved: true,
      draft_sha256: "changed-hash",
      latest_validation_job_id: "candidate-run-1",
      latest_validation: {
        run_id: "candidate-run-1",
        cluster_id: candidateCluster.cluster_id,
        status: "finished",
        source_sha256: "validated-hash",
        timeout_seconds: 60,
        started_at: "2026-07-01T18:00:00+08:00",
        updated_at: "2026-07-01T18:00:01+08:00",
        modes: {},
        logs: {},
      },
    });
    await editor.setValue("print('changed after validation')\n");
    await wrapper.get('[data-testid="save-candidate-draft"]').trigger("click");
    await flushPromises();

    expect(wrapper.get('[data-testid="confirm-candidate-bug"]').attributes("disabled")).toBeDefined();
  });
});
