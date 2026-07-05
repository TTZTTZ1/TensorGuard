<script setup lang="ts">
import AsyncState from "../AsyncState.vue";

type Evidence = { display_id: string; api: string; bug_type: string; status: "confirmed" };

withDefaults(defineProps<{ bugs: Evidence[] | null; loading?: boolean; error?: string | null }>(), {
  loading: false,
  error: null,
});

defineEmits<{ retry: [] }>();

function framework(api: string): "PT" | "TF" {
  return api.startsWith("tf.") ? "TF" : "PT";
}
</script>

<template>
  <section class="confirmed-evidence-list" aria-labelledby="confirmed-evidence-title">
    <header class="confirmed-evidence-list__head">
      <div class="confirmed-evidence-list__ident">
        <span class="confirmed-evidence-list__icon" aria-hidden="true">✓</span>
        <div>
          <h2 id="confirmed-evidence-title">已确认证据</h2>
          <p>可直接进入复现工作台</p>
        </div>
      </div>
      <a class="confirmed-evidence-list__all" href="#bug-replay">查看全部</a>
    </header>

    <AsyncState :loading="loading" :error="error" :empty="!loading && !error && (bugs?.length ?? 0) === 0" @retry="$emit('retry')">
      <template #loading><p class="confirmed-evidence-list__state">正在读取已确认证据</p></template>
      <template #error="{ error: text }"><p class="confirmed-evidence-list__state">{{ text }}</p></template>
      <template #empty><p class="confirmed-evidence-list__state">后端暂未返回已确认证据</p></template>

      <div class="confirmed-evidence-list__rows" role="list" tabindex="0" aria-label="已确认证据列表，可滚动查看更多">
        <a v-for="bug in (bugs ?? [])" :key="bug.display_id" class="confirmed-evidence-list__row" href="#bug-replay" role="listitem">
          <span class="confirmed-evidence-list__framework" :class="{ 'confirmed-evidence-list__framework--tf': framework(bug.api) === 'TF' }">{{ framework(bug.api) }}</span>
          <span class="confirmed-evidence-list__copy">
            <b>{{ bug.display_id }} · {{ bug.api }}</b>
            <small>{{ bug.bug_type }}</small>
          </span>
          <span class="confirmed-evidence-list__status">已确认</span>
        </a>
      </div>
    </AsyncState>
  </section>
</template>

<style scoped>
.confirmed-evidence-list { display: grid; grid-template-rows: auto minmax(0, 1fr); height: 100%; min-height: 12.25rem; padding: 1.1rem 1.25rem; background: #fff; border: 1px solid var(--tg-border); border-radius: var(--tg-radius); box-shadow: var(--tg-shadow); }
.confirmed-evidence-list__head { display: flex; align-items: flex-start; justify-content: space-between; gap: 1rem; margin-bottom: 0.7rem; }
.confirmed-evidence-list__ident { display: flex; align-items: center; gap: 0.65rem; }
.confirmed-evidence-list__icon { width: 1.9rem; height: 1.9rem; display: grid; place-items: center; border-radius: 6px; background: #e9f7f2; color: #126c52; box-shadow: inset 0 0 0 1px #cce9de; font-weight: 800; }
.confirmed-evidence-list h2 { margin: 0; color: var(--tg-text-strong); font-size: 0.875rem; }
.confirmed-evidence-list__ident p { margin: 0.28rem 0 0; color: var(--tg-text-muted); font-size: 0.625rem; }
.confirmed-evidence-list__all { height: 2rem; display: inline-flex; align-items: center; padding: 0 0.7rem; border: 1px solid var(--tg-border); border-radius: 6px; background: #fff; color: var(--tg-text-strong); font-size: 0.62rem; font-weight: 720; }
.confirmed-evidence-list__state { margin: 0; }
.confirmed-evidence-list__rows { display: grid; align-content: start; max-height: 10.8rem; min-height: 0; overflow-y: auto; padding-right: 0.25rem; margin-right: -0.25rem; scrollbar-gutter: stable; }
.confirmed-evidence-list__rows:focus-visible { outline: 2px solid var(--tg-action); outline-offset: 3px; border-radius: 6px; }
.confirmed-evidence-list__rows::-webkit-scrollbar { width: 0.44rem; }
.confirmed-evidence-list__rows::-webkit-scrollbar-track { background: #f0f4fb; border-radius: 999px; }
.confirmed-evidence-list__rows::-webkit-scrollbar-thumb { background: #b7c7df; border-radius: 999px; }
.confirmed-evidence-list__row { display: grid; grid-template-columns: 2rem minmax(0, 1fr) auto; align-items: center; gap: 0.7rem; padding: 0.6rem 0; border-bottom: 1px solid var(--tg-border); }
.confirmed-evidence-list__row:last-child { border-bottom: 0; }
.confirmed-evidence-list__framework { width: 2rem; height: 1.55rem; display: grid; place-items: center; border-radius: 4px; background: #245dcc; color: #fff; box-shadow: 0 4px 9px rgba(36,93,204,.18); font: 790 0.5rem/1 ui-monospace, monospace; }
.confirmed-evidence-list__framework--tf { background: #147f99; }
.confirmed-evidence-list__copy { min-width: 0; display: grid; gap: 0.2rem; }
.confirmed-evidence-list__copy b { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: var(--tg-text-strong); font: 600 0.62rem/1.2 ui-monospace, monospace; }
.confirmed-evidence-list__copy small { color: var(--tg-text-muted); font-size: 0.55rem; }
.confirmed-evidence-list__status { padding: 0.25rem 0.45rem; border-radius: 4px; background: var(--tg-green-bg); color: var(--tg-green-text); font-size: 0.5rem; font-weight: 750; }
</style>
