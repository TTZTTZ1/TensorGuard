function backendErrorMessage(payload: unknown): string | undefined {
  if (typeof payload !== "object" || payload === null || !("error" in payload)) {
    return undefined;
  }
  return typeof payload.error === "string" && payload.error ? payload.error : undefined;
}

export class ApiError extends Error {
  readonly name = "ApiError";

  constructor(
    public readonly status: number,
    public readonly payload: unknown,
    statusText = "",
  ) {
    super(backendErrorMessage(payload) ?? `HTTP ${status}${statusText ? ` ${statusText}` : ""}`);
  }
}

export async function request<T>(path: string, init: RequestInit = {}): Promise<T> {
  const headers = new Headers(init.headers);
  if (!headers.has("Content-Type")) {
    headers.set("Content-Type", "application/json");
  }

  const response = await fetch(path, { ...init, headers });
  const text = await response.text();
  let payload: unknown;

  if (text) {
    try {
      payload = JSON.parse(text) as unknown;
    } catch {
      payload = text;
      if (response.ok) {
        throw new Error(`Invalid JSON response from ${path}`);
      }
    }
  }

  if (!response.ok) {
    throw new ApiError(response.status, payload, response.statusText);
  }

  return payload as T;
}
