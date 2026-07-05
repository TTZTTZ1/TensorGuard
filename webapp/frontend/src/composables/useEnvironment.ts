import { computed, onMounted, ref } from "vue";

import { getEnvironment } from "../services/tensorguard";
import type { EnvironmentPayload } from "../types/tensorguard";

const environment = ref<EnvironmentPayload | null>(null);
const loading = ref(false);
const error = ref<string | null>(null);
let inFlight: Promise<EnvironmentPayload> | null = null;
let requestToken = 0;

function describeError(value: unknown): string {
  if (value instanceof Error) {
    return value.message;
  }

  return "环境信息加载失败";
}

function buildEnvironmentLabel(payload: EnvironmentPayload | null, loadingState: boolean, errorState: string | null): string {
  if (payload !== null) {
    const gpuLabel = payload.gpus.length === 0 ? "无 GPU" : `${payload.gpus.length} GPU`;
    return `Python ${payload.python.version} · ${gpuLabel}`;
  }

  if (loadingState) {
    return "正在加载环境";
  }

  if (errorState !== null) {
    return "环境信息异常";
  }

  return "环境信息";
}

async function loadEnvironment(refresh = false) {
  if (!refresh) {
    if (environment.value !== null) {
      return environment.value;
    }

    if (inFlight !== null) {
      return inFlight;
    }
  }

  const token = ++requestToken;
  loading.value = true;
  error.value = null;

  const request = getEnvironment(refresh);
  inFlight = request;

  try {
    const payload = await request;
    if (token === requestToken) {
      environment.value = payload;
      error.value = null;
    }

    return payload;
  } catch (cause) {
    if (token === requestToken) {
      error.value = describeError(cause);
    }

    throw cause;
  } finally {
    if (token === requestToken) {
      loading.value = false;
      if (inFlight === request) {
        inFlight = null;
      }
    }
  }
}

export function useEnvironment() {
  onMounted(() => {
    void loadEnvironment().catch(() => undefined);
  });

  const environmentLabel = computed(() => buildEnvironmentLabel(environment.value, loading.value, error.value));

  return {
    environment,
    loading,
    error,
    environmentLabel,
    refresh: () => loadEnvironment(true),
  };
}
