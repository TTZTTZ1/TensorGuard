import type {
  ApiDetailPayload,
  ApiJobLogChunkPayload,
  ApiJobLogName,
  ApiJobPayload,
  ApiListItem,
  ApiRunStartInput,
  CandidateClusterDetail,
  CandidateConfirmationInput,
  CandidateClusterSummary,
  CandidateClusterUpdateInput,
  CandidateValidationJobPayload,
  CandidateValidationStartPayload,
  CandidateCreateInput,
  CandidateDetail,
  CandidateRecord,
  CandidateUpdateInput,
  ConfirmedBugDetail,
  ConfirmedBugSummary,
  DeleteRecordPayload,
  EnvironmentPayload,
  JobStartPayload,
  Library,
  OverviewPayload,
  ReplayStartInput,
  ReproJobPayload,
  ReproReportPayload,
} from "../types/tensorguard";
import { request } from "./http";

export const endpoints = {
  overview: "/api/overview",
  environment: "/api/environment",
  apis: "/api/apis",
  apiDetail: "/api/api-detail",
  runApi: "/api/run-api",
  apiJob: (id: string) => `/api/api-jobs/${encodeURIComponent(id)}`,
  apiJobLog: (id: string, name: ApiJobLogName) => `/api/api-jobs/${encodeURIComponent(id)}/logs/${encodeURIComponent(name)}`,
  candidateClusters: "/api/candidate-clusters",
  candidateCluster: (id: string) => `/api/candidate-clusters/${encodeURIComponent(id)}`,
  candidateClusterStatus: (id: string) => `/api/candidate-clusters/${encodeURIComponent(id)}/status`,
  candidateClusterDraft: (id: string) => `/api/candidate-clusters/${encodeURIComponent(id)}/draft`,
  candidateClusterDraftReset: (id: string) => `/api/candidate-clusters/${encodeURIComponent(id)}/draft/reset`,
  candidateClusterValidate: (id: string) => `/api/candidate-clusters/${encodeURIComponent(id)}/validate`,
  candidateClusterConfirm: (id: string) => `/api/candidate-clusters/${encodeURIComponent(id)}/confirm`,
  candidateClusterDelete: (id: string) => `/api/candidate-clusters/${encodeURIComponent(id)}/delete`,
  candidateValidationJob: (id: string) => `/api/candidate-validation-jobs/${encodeURIComponent(id)}`,
  candidates: "/api/candidates",
  candidate: (id: string) => `/api/candidates/${encodeURIComponent(id)}`,
  candidateStatus: (id: string) => `/api/candidates/${encodeURIComponent(id)}/status`,
  confirmedBugs: "/api/confirmed-bugs",
  confirmedBug: (id: string) => `/api/confirmed-bugs/${encodeURIComponent(id)}`,
  confirmedBugDelete: (id: string) => `/api/confirmed-bugs/${encodeURIComponent(id)}/delete`,
  reproduce: (id: string) => `/api/confirmed-bugs/${encodeURIComponent(id)}/reproduce`,
  reproJob: (id: string) => `/api/repro-jobs/${encodeURIComponent(id)}`,
  reproReport: (id: string) => `/api/repro-jobs/${encodeURIComponent(id)}/report`,
} as const;

function withQuery(path: string, values: Record<string, string | number>): string {
  const query = new URLSearchParams();
  for (const [key, value] of Object.entries(values)) {
    query.set(key, String(value));
  }
  return `${path}?${query.toString()}`;
}

function get<T>(path: string): Promise<T> {
  return request<T>(path, { method: "GET" });
}

function post<T>(path: string, body?: unknown): Promise<T> {
  return request<T>(path, {
    method: "POST",
    ...(body === undefined ? {} : { body: JSON.stringify(body) }),
  });
}

export function getOverview(): Promise<OverviewPayload> {
  return get(endpoints.overview);
}

export function getEnvironment(refresh = false): Promise<EnvironmentPayload> {
  const path = refresh ? withQuery(endpoints.environment, { refresh: 1 }) : endpoints.environment;
  return get(path);
}

export function getApis(lib: Library, query = "", limit = 200): Promise<ApiListItem[]> {
  return get(withQuery(endpoints.apis, { lib, q: query, limit }));
}

export function getApiDetail(lib: Library, api: string): Promise<ApiDetailPayload> {
  return get(withQuery(endpoints.apiDetail, { lib, api }));
}

export function startApiRun(input: ApiRunStartInput): Promise<JobStartPayload> {
  return post(endpoints.runApi, { lib: input.lib, api: input.api, mode: input.mode });
}

export function getApiJob(id: string): Promise<ApiJobPayload> {
  return get(endpoints.apiJob(id));
}

export function getApiJobLog(id: string, name: ApiJobLogName, offset = 0): Promise<ApiJobLogChunkPayload> {
  return get(withQuery(endpoints.apiJobLog(id, name), { offset }));
}

export function getCandidates(): Promise<CandidateRecord[]> {
  return get(endpoints.candidates);
}

export function getCandidateClusters(): Promise<CandidateClusterSummary[]> {
  return get(endpoints.candidateClusters);
}

export function getCandidateCluster(id: string): Promise<CandidateClusterDetail> {
  return get(endpoints.candidateCluster(id));
}

export function updateCandidateClusterStatus(id: string, input: CandidateClusterUpdateInput): Promise<CandidateClusterDetail> {
  return post(endpoints.candidateClusterStatus(id), input);
}

export function saveCandidateClusterDraft(id: string, source: string): Promise<CandidateClusterDetail> {
  return post(endpoints.candidateClusterDraft(id), { source });
}

export function resetCandidateClusterDraft(id: string): Promise<CandidateClusterDetail> {
  return post(endpoints.candidateClusterDraftReset(id));
}

export function startCandidateValidation(id: string, source: string, timeout = 60): Promise<CandidateValidationStartPayload> {
  return post(endpoints.candidateClusterValidate(id), { source, timeout });
}

export function getCandidateValidationJob(id: string): Promise<CandidateValidationJobPayload> {
  return get(endpoints.candidateValidationJob(id));
}

export function confirmCandidateCluster(id: string, input: CandidateConfirmationInput): Promise<ConfirmedBugDetail> {
  return post(endpoints.candidateClusterConfirm(id), input);
}

export function deleteCandidateCluster(id: string, confirmationId: string): Promise<DeleteRecordPayload> {
  return post(endpoints.candidateClusterDelete(id), { confirmation_id: confirmationId });
}

export function deleteConfirmedBug(id: string, confirmationId: string): Promise<DeleteRecordPayload> {
  return post(endpoints.confirmedBugDelete(id), { confirmation_id: confirmationId });
}

export function createCandidate(input: CandidateCreateInput): Promise<CandidateRecord> {
  return post(endpoints.candidates, input);
}

export function getCandidate(id: string): Promise<CandidateDetail> {
  return get(endpoints.candidate(id));
}

export function updateCandidateStatus(id: string, input: CandidateUpdateInput): Promise<CandidateRecord> {
  return post(endpoints.candidateStatus(id), input);
}

export function getConfirmedBugs(): Promise<ConfirmedBugSummary[]> {
  return get(endpoints.confirmedBugs);
}

export function getConfirmedBug(id: string): Promise<ConfirmedBugDetail> {
  return get(endpoints.confirmedBug(id));
}

export function reproduceConfirmedBug(id: string, input: ReplayStartInput): Promise<JobStartPayload> {
  return post(endpoints.reproduce(id), input);
}

export function getReproJob(id: string): Promise<ReproJobPayload> {
  return get(endpoints.reproJob(id));
}

export function getReproReport(id: string): Promise<ReproReportPayload> {
  return get(endpoints.reproReport(id));
}

export function generateReproReport(id: string): Promise<ReproReportPayload> {
  return post(endpoints.reproReport(id));
}
