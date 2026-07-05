<script setup lang="ts">
import { computed } from "vue";

import AsyncState from "../AsyncState.vue";
import type { OverviewPayload } from "../../types/tensorguard";

const props = withDefaults(
  defineProps<{
    overview: OverviewPayload | null;
    environmentSummary: string;
    loading?: boolean;
    error?: string | null;
  }>(),
  { loading: false, error: null },
);

defineEmits<{ retry: [] }>();

const apiTotal = computed(() => props.overview?.api_total ?? 0);
const torchTotal = computed(() => props.overview?.api_by_lib?.torch ?? 0);
const tfTotal = computed(() => props.overview?.api_by_lib?.tf ?? 0);
const promptReadyTotal = computed(() => props.overview?.prompt_ready_total ?? 0);
const confirmedTotal = computed(() => props.overview?.paper_bug_total ?? 0);
const frameworkCount = computed(() => Object.keys(props.overview?.api_by_lib ?? {}).length);

function formatCount(value: number): string {
  return value.toLocaleString("en-US");
}

function percent(count: number): number {
  return apiTotal.value > 0 ? (count / apiTotal.value) * 100 : 0;
}

function formatPercent(count: number): string {
  return `${percent(count).toFixed(apiTotal.value > 0 ? 1 : 0)}%`;
}
</script>

<template>
  <section class="coverage-baseline" aria-label="API 覆盖与系统状态">
    <div class="coverage-baseline__coverage-shell">
      <section class="coverage-baseline__panel coverage-baseline__coverage-main" aria-labelledby="coverage-baseline-title">
        <header class="coverage-baseline__panel-head">
          <div class="coverage-baseline__section-ident">
            <span class="coverage-baseline__section-icon" aria-hidden="true">API</span>
            <div>
              <h2 id="coverage-baseline-title" class="coverage-baseline__panel-title">API 覆盖基线</h2>
              <p class="coverage-baseline__panel-note">当前测试范围与框架分布</p>
            </div>
          </div>
          <span class="coverage-baseline__source-badge">{{ error ? "数据异常" : loading ? "读取中" : "数据源正常" }}</span>
        </header>

        <AsyncState :loading="loading" :error="error" :empty="!loading && !error && overview === null" @retry="$emit('retry')">
          <template #loading><p class="coverage-baseline__state-copy">正在读取总览数据</p></template>
          <template #error="{ error: errorText }"><p class="coverage-baseline__state-copy">{{ errorText }}</p></template>
          <template #empty><p class="coverage-baseline__state-copy">后端暂未返回总览数据</p></template>

          <div class="coverage-baseline__coverage-hero">
            <div>
              <p class="coverage-baseline__total-label">总覆盖 API</p>
              <p class="coverage-baseline__total-number">{{ formatCount(apiTotal) }}<small>APIs</small></p>
            </div>
            <div class="coverage-baseline__frameworks">
              <div class="coverage-baseline__framework">
                <span><i aria-hidden="true" />PyTorch</span>
                <b>{{ formatCount(torchTotal) }}<small>{{ formatPercent(torchTotal) }}</small></b>
              </div>
              <div class="coverage-baseline__framework coverage-baseline__framework--tf">
                <span><i aria-hidden="true" />TensorFlow</span>
                <b>{{ formatCount(tfTotal) }}<small>{{ formatPercent(tfTotal) }}</small></b>
              </div>
            </div>
          </div>
          <div class="coverage-baseline__track" aria-label="框架 API 占比">
            <i :style="{ width: `${percent(torchTotal)}%` }" />
            <i :style="{ width: `${percent(tfTotal)}%` }" />
          </div>
          <div class="coverage-baseline__track-meta">
            <span>{{ overview?.sources.torch_api_list || "data/torch_apis.txt" }}</span>
            <span>{{ overview?.sources.tf_api_list || "data/tf_apis.txt" }}</span>
          </div>
        </AsyncState>
      </section>

      <section class="coverage-baseline__panel coverage-baseline__evidence-card" aria-label="已确认问题">
        <div class="coverage-baseline__section-ident">
          <span class="coverage-baseline__section-icon coverage-baseline__section-icon--evidence" aria-hidden="true">✓</span>
          <div>
            <h2 class="coverage-baseline__panel-title">已确认问题</h2>
            <p class="coverage-baseline__panel-note">具备最小复现程序与运行证据</p>
          </div>
        </div>
        <p class="coverage-baseline__evidence-count">{{ formatCount(confirmedTotal) }}</p>
        <p class="coverage-baseline__evidence-caption">条可现场复现的框架缺陷证据</p>
        <a class="coverage-baseline__evidence-link" href="#bug-replay">进入证据库&nbsp;&nbsp;→</a>
      </section>
    </div>

    <section class="coverage-baseline__panel coverage-baseline__metrics" aria-label="系统状态">
      <div class="coverage-baseline__metric" data-metric="constraints">
        <span>约束库状态</span>
        <b class="coverage-baseline__metric-value"><em>{{ promptReadyTotal > 0 ? "已就绪" : "待补全" }}</em></b>
        <small>{{ formatCount(promptReadyTotal) }} 个 API 已具备约束</small>
      </div>
      <div class="coverage-baseline__metric" data-metric="frameworks">
        <span>测试框架</span>
        <b class="coverage-baseline__metric-value">{{ frameworkCount }}</b>
        <small>PyTorch · TensorFlow</small>
      </div>
      <div class="coverage-baseline__metric" data-metric="environment">
        <span>执行环境</span>
        <b class="coverage-baseline__metric-value coverage-baseline__metric-value--environment">{{ environmentSummary }}</b>
        <small>点击右上角查看实时环境</small>
      </div>
    </section>
  </section>
</template>

<style scoped>
.coverage-baseline { display: grid; gap: 0.875rem; }
.coverage-baseline__coverage-shell { display: grid; grid-template-columns: minmax(0, 1.75fr) minmax(18.75rem, 0.75fr); gap: 0.875rem; }
.coverage-baseline__panel { background: var(--tg-surface); border: 1px solid var(--tg-border); border-radius: var(--tg-radius); box-shadow: var(--tg-shadow); }
.coverage-baseline__coverage-main { padding: 1.25rem 1.45rem 1.1rem; }
.coverage-baseline__panel-head { display: flex; align-items: flex-start; justify-content: space-between; gap: 1rem; margin-bottom: 1rem; }
.coverage-baseline__section-ident { display: flex; align-items: center; gap: 0.65rem; }
.coverage-baseline__section-icon { width: 1.9rem; height: 1.9rem; display: grid; place-items: center; flex: none; border-radius: 6px; background: var(--tg-action-soft); color: var(--tg-action-strong); font: 800 0.5rem/1 ui-monospace, monospace; box-shadow: inset 0 0 0 1px #d6e4ff; }
.coverage-baseline__panel-title { margin: 0; color: var(--tg-text-strong); font-size: 0.875rem; font-weight: 760; }
.coverage-baseline__panel-note { margin: 0.28rem 0 0; color: var(--tg-text-muted); font-size: 0.625rem; }
.coverage-baseline__source-badge { padding: 0.3rem 0.5rem; border-radius: 4px; background: var(--tg-green-bg); color: var(--tg-green-text); font-size: 0.56rem; font-weight: 720; }
.coverage-baseline__state-copy { margin: 0; }
.coverage-baseline__coverage-hero { display: flex; align-items: flex-end; justify-content: space-between; gap: 1.4rem; }
.coverage-baseline__total-label { margin: 0; color: var(--tg-text-muted); font-size: 0.68rem; }
.coverage-baseline__total-number { margin: 0.4rem 0 0; color: var(--tg-text-strong); font-size: 2.9rem; line-height: 0.95; font-weight: 810; font-variant-numeric: tabular-nums; }
.coverage-baseline__total-number small { margin-left: 0.5rem; color: var(--tg-text-muted); font-size: 0.75rem; font-weight: 600; }
.coverage-baseline__frameworks { display: flex; gap: 2.4rem; padding-bottom: 0.2rem; }
.coverage-baseline__framework { min-width: 8rem; }
.coverage-baseline__framework span { display: flex; align-items: center; gap: 0.45rem; color: var(--tg-text-muted); font-size: 0.64rem; }
.coverage-baseline__framework i { width: 0.5rem; height: 0.5rem; border-radius: 2px; background: var(--tg-action); }
.coverage-baseline__framework--tf i { background: var(--tg-cyan); }
.coverage-baseline__framework b { display: block; margin-top: 0.5rem; color: var(--tg-text-strong); font-size: 1.55rem; }
.coverage-baseline__framework small { margin-left: 0.35rem; color: var(--tg-text-muted); font-size: 0.62rem; font-weight: 500; }
.coverage-baseline__track { display: flex; height: 0.68rem; margin-top: 1.3rem; overflow: hidden; border-radius: 3px; background: #edf1f7; }
.coverage-baseline__track i:first-child { background: var(--tg-action); }
.coverage-baseline__track i:last-child { background: var(--tg-cyan); }
.coverage-baseline__track-meta { display: flex; justify-content: space-between; gap: 1rem; margin-top: 0.55rem; color: var(--tg-text-muted); font-size: 0.56rem; }
.coverage-baseline__evidence-card { min-height: 13.6rem; padding: 1.25rem 1.4rem; display: flex; flex-direction: column; background: var(--tg-navy); color: #fff; border-color: var(--tg-navy); }
.coverage-baseline__evidence-card .coverage-baseline__panel-note { color: #aab7cf; }
.coverage-baseline__section-icon--evidence { background: #263858; color: #bcd0ff; box-shadow: inset 0 0 0 1px #40547a; font-size: 0.8rem; }
.coverage-baseline__evidence-count { margin: 1rem 0 0.35rem; font-size: 2.75rem; line-height: 1; font-weight: 800; }
.coverage-baseline__evidence-caption { margin: 0; color: #b9c4d7; font-size: 0.68rem; }
.coverage-baseline__evidence-link { margin-top: auto; padding-top: 1rem; border-top: 1px solid #33415d; color: #aac4ff; font-size: 0.68rem; font-weight: 700; }
.coverage-baseline__metrics { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); overflow: hidden; }
.coverage-baseline__metric { min-height: 4.9rem; padding: 0.92rem 1.25rem; border-right: 1px solid var(--tg-border); }
.coverage-baseline__metric:last-child { border-right: 0; }
.coverage-baseline__metric > span { color: var(--tg-text-muted); font-size: 0.62rem; }
.coverage-baseline__metric-value { display: block; margin: 0.35rem 0 0.2rem; color: var(--tg-text-strong); font-size: 1.2rem; }
.coverage-baseline__metric-value em { display: inline-flex; padding: 0.25rem 0.6rem; border-radius: 5px; background: var(--tg-green-bg); color: var(--tg-green-text); font-size: 0.86rem; font-style: normal; box-shadow: inset 0 0 0 1px #cde9df; }
.coverage-baseline__metric-value--environment { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; font-size: 0.92rem; }
.coverage-baseline__metric small { color: var(--tg-text-soft); font-size: 0.56rem; }
@media (max-width: 900px) { .coverage-baseline__coverage-shell { grid-template-columns: minmax(0, 1.55fr) minmax(13.75rem, 0.65fr); } .coverage-baseline__frameworks { gap: 1rem; } }
@media (max-width: 720px) { .coverage-baseline__coverage-shell, .coverage-baseline__metrics { grid-template-columns: 1fr; } .coverage-baseline__coverage-hero { align-items: flex-start; flex-direction: column; } .coverage-baseline__frameworks { width: 100%; justify-content: space-between; } .coverage-baseline__metric { border-right: 0; border-bottom: 1px solid var(--tg-border); } .coverage-baseline__metric:last-child { border-bottom: 0; } }
</style>
