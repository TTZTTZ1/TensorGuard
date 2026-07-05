export type Library = "torch" | "tf";
export type ResultCategory = "seed" | "valid" | "exception" | "crash" | "notarget" | "hangs" | "flaky";
export type ResultCounts = Record<ResultCategory, number>;

export interface OverviewResultSummary {
  path: string;
  exists: boolean;
  api_count: number;
  counts: ResultCounts;
  trace_path: string;
  trace_exists: boolean;
  trace_hits: number;
}

export interface OverviewSources {
  torch_api_list: string;
  tf_api_list: string;
  prompt_library: string;
  api_jobs: string;
  repro_jobs: string;
}

export interface OverviewPayload {
  api_total: number;
  api_by_lib: Record<Library, number>;
  prompt_ready_total: number;
  prompt_ready_by_lib: Record<Library, number>;
  results: Record<Library, OverviewResultSummary>;
  paper_bug_total: number;
  paper_bug_by_framework: Record<string, number>;
  latest_api_jobs: LatestApiJobSummary[];
  latest_repro_jobs: LatestReproJobSummary[];
  sources: OverviewSources;
}

export interface PlatformInfo {
  system: string;
  release: string;
  machine: string;
}

export interface PythonInfo {
  version: string;
  executable: string;
}

export type FrameworkPackageInfo =
  | { installed: true; version: string }
  | { installed: false; version: null }
  | { installed: null; version: null; error: string };

export interface FrameworkInfo {
  torch: FrameworkPackageInfo;
  tensorflow: FrameworkPackageInfo;
}

export interface CudaInfo {
  available: boolean;
  driver_version: string | null;
}

export interface GpuInfo {
  index: number;
  name: string;
  driver_version: string;
  memory_total_mib: number | null;
}

export interface EnvironmentPayload {
  collected_at: string;
  platform: PlatformInfo;
  python: PythonInfo;
  frameworks: FrameworkInfo;
  cuda: CudaInfo;
  gpus: GpuInfo[];
  warnings: string[];
}

interface PromptManifestEntryBase {
  api: string;
  library: Library;
  structured_info: string;
  structured_sha256: string;
  updated_at: string;
}

export type PromptManifestEntry = PromptManifestEntryBase &
  (
    | {
        has_greedy_prompt: true;
        greedy_prompt: string;
        greedy_sha256: string;
      }
    | {
        has_greedy_prompt: false;
        greedy_prompt: null;
        greedy_sha256: null;
      }
  );

export interface ApiListItem {
  api: string;
  lib: Library;
  has_prompt: boolean;
  prompt_path: string;
  result_counts: ResultCounts;
  has_results: boolean;
  manifest_entry: PromptManifestEntry;
}

export type ApiRunMode = "demo" | "normal";
export type ApiRunStatus = "pending" | "running" | "success" | "failed";
export type ApiPipelineStage = "prompt_check" | "qwen_seed" | "ev_generation" | "driver" | "summary";
export type ApiStage = "launch" | "init" | ApiPipelineStage | "done";
export type ApiStageStatus = "pending" | "running" | "success" | "failed" | "skipped";

export interface LatestApiJob {
  job_id: string;
  out: string;
  status: ApiRunStatus;
  stage: ApiStage;
  updated_at: string | null;
  summary_status: ApiRunStatus | null;
  mutation_model: string | null;
  error: string | null;
}

export interface ApiDetailPayload extends ApiListItem {
  api_list: string;
  prompt_exists: boolean;
  results_path: string;
  latest_job: LatestApiJob | null;
}

export interface ApiRunStartInput {
  lib: Library;
  api: string;
  mode: ApiRunMode;
}

export interface JobStartPayload {
  job_id: string;
  out: string;
}

export interface ApiJobParameters {
  qwen_n_samples: number;
  qwen_min_valid: number;
  qwen_max_rounds: number;
  qwen_per_api_budget: number;
  qwen_validate_timeout: number;
  ev_max_valid: number;
  ev_batch_size: number;
  ev_timeout: number;
  seed_pool_size: number;
  random_seed: number;
}

export interface CandidateCollectionSummary {
  job_id?: string;
  lib?: Library;
  api?: string;
  scanned?: number;
  registered?: number;
  deduplicated?: number;
  excluded_noise?: number;
  skipped_low_signal?: number;
  candidate_ids?: string[];
  path?: string;
  error?: string;
}

export interface ApiJobStatus {
  job_id: string;
  lib: Library;
  api: string;
  mode: ApiRunMode;
  qwen_model: string;
  mutation_model: string;
  cuda_device: string;
  status: ApiRunStatus;
  stage: ApiStage;
  stages: Record<ApiPipelineStage, ApiStageStatus>;
  error: string | null;
  updated_at: string;
  dry_run?: boolean;
  parameters?: ApiJobParameters;
  metrics_path?: string;
  environment_path?: string;
  started_at?: string;
  logs?: Record<string, string>;
  candidate_collection?: CandidateCollectionSummary;
}

export interface ApiJobSummary {
  job_id: string;
  lib: Library;
  api: string;
  mode: ApiRunMode;
  dry_run: boolean;
  prompt_library: string;
  qwen_model: string;
  mutation_model: string;
  status: ApiRunStatus;
  error: string | null;
  canonical_results_path: string;
  qwen_valid_seed_count: number;
  result_counts: ResultCounts;
  trace_path: string;
  trace_exists: boolean;
  catch_count: number;
  logs: Record<string, string>;
  updated_at: string;
}

export interface LatestApiJobSummary extends ApiJobSummary {
  _path: string;
}

export interface GpuMetricSample {
  collected_at: string;
  index: number;
  utilization_percent: number | null;
  memory_used_mib: number | null;
  memory_total_mib: number | null;
}

export type ApiJobMetric = ResultCounts & {
  timestamp: string;
  stage: ApiPipelineStage;
  elapsed_seconds: number;
  qwen_raw: number;
  qwen_valid: number;
  tested_cases?: number;
  total_files: number;
  trace_hits: number;
  gpu?: GpuMetricSample;
};

export interface ApiResultFile {
  name: string;
  path: string;
  size_bytes: number;
  source_excerpt: string;
  recommended: boolean;
}

export interface ApiJobPayload {
  job_id: string;
  out: string;
  status: ApiJobStatus;
  summary: Partial<ApiJobSummary>;
  metrics: ApiJobMetric[];
  environment: Partial<EnvironmentPayload>;
  result_files: Record<ResultCategory, ApiResultFile[]>;
  logs: Record<string, string>;
}

export type ApiJobLogName = "01_qwen_seed.log" | "02_ev_generation.log" | "03_driver.log";

export interface ApiJobLogChunkPayload {
  job_id: string;
  log_name: ApiJobLogName;
  text: string;
  offset: number;
  next_offset: number;
  size_bytes: number;
  has_more: boolean;
  reset: boolean;
}

export type CandidateCategory = ResultCategory;
export type CandidateStatus = "pending_review" | "reproduced" | "needs_review" | "rejected" | "promoted";
export type CandidateUpdateStatus = Exclude<CandidateStatus, "promoted">;

export interface CandidateRecord {
  id: string;
  job_id: string;
  lib: Library;
  api: string;
  category: CandidateCategory;
  source_path: string;
  source_sha256: string;
  status: CandidateStatus;
  recommended: boolean;
  error_summary: string;
  note: string;
  created_at: string;
  updated_at: string;
}

export interface CandidateDetail extends CandidateRecord {
  source_exists: boolean;
  source_code: string;
}

export type CandidateClusterStatus = "pending_review" | "reproduced" | "needs_review" | "needs_minimize" | "rejected" | "promoted";
export type CandidateClusterConfidence = "high" | "medium" | "low";

export interface CandidateClusterMember {
  candidate_id: string;
  source_path: string;
  source_name: string;
  error_summary: string;
  score: number;
  status: CandidateStatus;
}

export interface ExcludedCandidate {
  candidate_id: string;
  source_path: string;
  source_name: string;
  reason: string;
  error_summary: string;
}

export interface CandidateClusterSummary {
  cluster_id: string;
  lib: Library;
  api: string;
  job_id: string;
  category: CandidateCategory;
  bug_pattern: string;
  cluster_status: CandidateClusterStatus;
  confidence: CandidateClusterConfidence;
  member_count: number;
  excluded_count: number;
  representative: CandidateClusterMember;
  created_at: string;
  updated_at: string;
}

export interface CandidateClusterDetail extends CandidateClusterSummary {
  members: CandidateClusterMember[];
  excluded: ExcludedCandidate[];
  representative_source_code: string;
  minimization_draft: string;
  draft_saved: boolean;
  draft_modified: boolean;
  draft_sha256: string;
  latest_validation_job_id: string | null;
  latest_validation: CandidateValidationJobPayload | null;
  review_defaults: CandidateConfirmationInput;
}

export interface CandidateConfirmationInput {
  title: string;
  bug_type: string;
  review_note: string;
}

export type CandidateValidationMode = "cpu" | "gpu0";

export interface CandidateValidationExecution {
  status: ReproExecutionStatus;
  returncode: number | null;
  timed_out: boolean;
  log: string;
  started_at: string | null;
  finished_at: string | null;
  execution_profile?: ExecutionProfile;
  actual_device?: string;
  elapsed_seconds?: number;
  evidence?: ExecutionEvidence;
  error?: string;
}

export interface CandidateValidationJobPayload {
  run_id: string;
  cluster_id: string;
  status: "pending" | "running" | "finished" | "failed";
  source_sha256: string;
  timeout_seconds: number;
  started_at: string;
  updated_at: string;
  modes: Partial<Record<CandidateValidationMode, CandidateValidationExecution>>;
  logs: Partial<Record<CandidateValidationMode, string>>;
  error?: string;
}

export interface CandidateValidationStartPayload {
  run_id: string;
  cluster_id: string;
  source_sha256: string;
}

export interface CandidateCreateInput {
  job_id: string;
  lib: Library;
  api: string;
  category: CandidateCategory;
  source_path: string;
  note?: string;
}

export interface CandidateUpdateInput {
  status: CandidateUpdateStatus;
  note?: string;
}

export interface CandidateClusterUpdateInput {
  status: CandidateUpdateStatus;
  note?: string;
}

export type ConfirmedBugFramework = "PyTorch" | "TensorFlow";

export interface ConfirmedBugSource {
  document: string;
  section: string;
  paper_case?: string;
}

export interface ConfirmedBugFiles {
  repro: string;
  report: string;
}

export interface ConfirmedBugMeta {
  id: string;
  title: string;
  framework: ConfirmedBugFramework;
  api: string;
  related_apis: string[];
  bug_type: string;
  status: "confirmed";
  source: ConfirmedBugSource;
  trigger: string;
  expected: string;
  observed: string;
  reproducible: boolean;
  minimized: boolean;
  files: ConfirmedBugFiles;
  tags: string[];
  dynamic?: boolean;
  candidate_cluster_id?: string;
  validation_run_id?: string;
  review_note?: string;
}

export interface ConfirmedBugSummary extends ConfirmedBugMeta {
  path: string;
  meta_path: string;
  display_id: string;
  deletable?: boolean;
}

export interface DeleteRecordPayload {
  deleted: string;
}

export interface ConfirmedBugDetail {
  index: ConfirmedBugSummary;
  meta: ConfirmedBugMeta;
  display_id: string;
  bug_dir: string;
  repro_path: string;
  report_path: string;
  repro_code: string;
  report_markdown: string;
  latest_repro_job_id: string | null;
}

export type ExecutionMode = "cpu" | `gpu:${number}`;
export type ExecutionProfile = "cuda_hidden" | `visible_gpu_${number}`;
export type ExecutionVerdict = "reproduced" | "not_reproduced" | "timeout" | "needs_review";
export type ReproJobStatusValue = "pending" | "running" | "finished";
export type ReproExecutionStatus = "pending" | "running" | "finished" | "timeout" | "failed";

export interface ExecutionEvidence {
  verdict: ExecutionVerdict;
  outcome: string;
  reason: string;
  signal: string | null;
  signal_number: number | null;
}

export interface ReproExecution {
  status: ReproExecutionStatus;
  returncode: number | null;
  timed_out: boolean;
  log: string;
  started_at: string | null;
  finished_at: string | null;
  execution_profile: ExecutionProfile;
  actual_device: string;
  evidence: ExecutionEvidence | null;
  verdict?: ExecutionVerdict;
  elapsed_seconds?: number;
  error?: string;
}

export interface ReproJobMeta {
  title: string;
  framework: string;
  api: string;
  bug_type: string;
}

export interface ReproJobStatus {
  job_id: string;
  bug_id: string;
  status: ReproJobStatusValue;
  started_at: string;
  updated_at: string;
  out: string;
  timeout_seconds: number;
  modes: Partial<Record<ExecutionMode, ReproExecution>>;
  report: string;
  error: string | null;
  meta?: ReproJobMeta;
  environment?: string;
  report_id?: string;
}

export interface LatestReproJobSummary extends ReproJobStatus {
  _path: string;
}

export interface ReplayStartInput {
  modes: readonly ExecutionMode[];
  timeout?: number;
}

export interface ReproJobPayload {
  job_id: string;
  out: string;
  status: ReproJobStatus;
  logs: Record<string, string>;
  environment: Partial<EnvironmentPayload>;
  report_exists: boolean;
  report_path: string;
  report_markdown: string;
}

export interface ReproReportPayload {
  job_id: string;
  report_path: string;
  report_markdown: string;
  immutable: boolean;
}
