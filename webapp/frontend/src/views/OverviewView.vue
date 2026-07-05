<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref } from "vue";

import { getConfirmedBugs, getOverview } from "../services/tensorguard";
import type { EnvironmentPayload, OverviewPayload } from "../types/tensorguard";
import CoverageBaseline from "../components/overview/CoverageBaseline.vue";
import ConfirmedEvidenceList from "../components/overview/ConfirmedEvidenceList.vue";
import DetectionPipeline from "../components/overview/DetectionPipeline.vue";

const props = withDefaults(
  defineProps<{
    environment?: EnvironmentPayload | null;
    environmentLoading?: boolean;
    environmentError?: string | null;
  }>(),
  {
    environment: null,
    environmentLoading: false,
    environmentError: null,
  },
);

const overview = ref<OverviewPayload | null>(null);
const overviewLoading = ref(true);
const overviewError = ref<string | null>(null);

const confirmedBugs = ref<Array<{ display_id: string; api: string; bug_type: string; status: "confirmed" }> | null>(null);
const confirmedBugsLoading = ref(true);
const confirmedBugsError = ref<string | null>(null);
let overviewRequestToken = 0;
let confirmedBugsRequestToken = 0;
let isMounted = false;

function describeError(value: unknown, fallback: string): string {
  if (value instanceof Error) {
    return value.message;
  }

  return fallback;
}

async function loadOverview() {
  const token = ++overviewRequestToken;
  overviewLoading.value = true;
  overviewError.value = null;

  try {
    const payload = await getOverview();
    if (isMounted && token === overviewRequestToken) {
      overview.value = payload;
    }
  } catch (error) {
    if (isMounted && token === overviewRequestToken) {
      overviewError.value = describeError(error, "总览数据加载失败");
    }
  } finally {
    if (isMounted && token === overviewRequestToken) {
      overviewLoading.value = false;
    }
  }
}

async function loadConfirmedBugs() {
  const token = ++confirmedBugsRequestToken;
  confirmedBugsLoading.value = true;
  confirmedBugsError.value = null;

  try {
    const payload = await getConfirmedBugs();
    if (isMounted && token === confirmedBugsRequestToken) {
      confirmedBugs.value = payload;
    }
  } catch (error) {
    if (isMounted && token === confirmedBugsRequestToken) {
      confirmedBugsError.value = describeError(error, "已确认证据加载失败");
    }
  } finally {
    if (isMounted && token === confirmedBugsRequestToken) {
      confirmedBugsLoading.value = false;
    }
  }
}

const environmentSummary = computed(() => {
  if (props.environment !== null) {
    const gpuSummary = props.environment.gpus.length === 0 ? "无 GPU" : `${props.environment.gpus.length} GPU`;
    const cudaSummary = props.environment.cuda.available ? "CUDA 可用" : "CUDA 不可用";
    return `Python ${props.environment.python.version} · ${cudaSummary} · ${gpuSummary}`;
  }

  if (props.environmentLoading) {
    return "环境信息加载中";
  }

  if (props.environmentError !== null && props.environmentError !== undefined) {
    return "环境信息异常";
  }

  return "环境信息暂不可用";
});

onMounted(() => {
  isMounted = true;
  void loadOverview();
  void loadConfirmedBugs();
});

onUnmounted(() => {
  isMounted = false;
  overviewRequestToken += 1;
  confirmedBugsRequestToken += 1;
});
</script>

<template>
  <section class="overview-view" aria-labelledby="overview-view-title">
    <header class="overview-view__head">
      <p class="overview-view__eyebrow">Coverage &amp; Evidence</p>
      <h1 id="overview-view-title">框架安全检测概览</h1>
      <p>基于实际 API 清单与已固化证据的当前快照</p>
    </header>

    <CoverageBaseline
      :overview="overview"
      :environment-summary="environmentSummary"
      :loading="overviewLoading"
      :error="overviewError"
      @retry="loadOverview"
    />

    <div class="overview-view__lower-grid">
      <DetectionPipeline
        :overview="overview"
        :loading="overviewLoading"
        :error="overviewError"
        @retry="loadOverview"
      />

      <ConfirmedEvidenceList
        :bugs="confirmedBugs"
        :loading="confirmedBugsLoading"
        :error="confirmedBugsError"
        @retry="loadConfirmedBugs"
      />
    </div>
  </section>
</template>

<style scoped>
.overview-view {
  display: grid;
  gap: 0.875rem;
}

.overview-view__head {
  margin-bottom: 0.25rem;
}

.overview-view__eyebrow {
  margin: 0 0 0.4rem;
  color: var(--tg-action);
  font: 760 0.58rem/1 ui-monospace, monospace;
  text-transform: uppercase;
}

.overview-view h1 {
  margin: 0;
  font-size: 1.65rem;
  line-height: 1.2;
  font-weight: 790;
  color: var(--tg-text-strong);
}

.overview-view__head > p:last-child {
  margin: 0.38rem 0 0;
  color: var(--tg-text-muted);
  font-size: 0.68rem;
}

.overview-view__lower-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.25fr) minmax(21.25rem, 0.75fr);
  gap: 0.875rem;
  align-items: stretch;
}

@media (max-width: 720px) { .overview-view__lower-grid { grid-template-columns: 1fr; } }
</style>
