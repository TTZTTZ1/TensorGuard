<script setup lang="ts">
import { computed } from "vue";

import { resultCategoryOrder } from "../../domain/chartOptions";
import type { ResultCounts } from "../../types/tensorguard";

const props = withDefaults(
  defineProps<{
    counts: ResultCounts | null;
  }>(),
  {
    counts: null,
  },
);

const headingId = `result-composition-${Math.random().toString(36).slice(2, 10)}`;
const rows = computed(() => {
  if (props.counts === null) {
    return [];
  }

  return resultCategoryOrder.map((category) => ({
    category,
    value: props.counts?.[category] ?? 0,
  }));
});
const total = computed(() => rows.value.reduce((sum, row) => sum + row.value, 0));
function widthFor(value: number) { return total.value > 0 ? `${(value / total.value) * 100}%` : "0%"; }
</script>

<template>
  <section class="result-composition" :aria-labelledby="headingId">
    <header class="result-composition__header">
      <span class="result-composition__icon">R</span>
      <div class="result-composition__heading"><h2 :id="headingId" class="result-composition__title">Results 构成</h2><p>已归类程序</p></div>
      <span v-if="rows.length" class="result-composition__total" data-testid="result-total">总计 {{ total }}</span>
    </header>

    <template v-if="rows.length > 0">
      <div class="result-composition__bar" aria-hidden="true"><i v-for="row in rows" :key="row.category" :class="`result-composition__bar--${row.category}`" :style="{ width: widthFor(row.value) }" /></div>
      <div class="result-composition__grid">
      <div v-for="row in rows" :key="row.category" class="result-composition__item">
        <span class="result-composition__category" data-testid="result-category"><i data-testid="result-swatch" :class="`result-composition__swatch--${row.category}`" />{{ row.category }}</span>
        <span class="result-composition__count">{{ row.value }}</span>
      </div>
      </div>
    </template>
    <p v-else class="result-composition__empty">暂无结果统计</p>
  </section>
</template>

<style scoped>
.result-composition {
  display: grid;
  grid-template-rows: auto auto minmax(0, 1fr);
  gap: 0.65rem;
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface);
  padding: 0.85rem;
  box-shadow: var(--tg-shadow);
  min-width: 0;
  height: 100%;
}

.result-composition__header { display: flex; align-items: center; gap: 0.55rem; }
.result-composition__total { margin-left: auto; padding: 0.25rem 0.4rem; border-radius: 4px; background: var(--tg-surface-soft); color: var(--tg-text-muted); font-size: 0.48rem; font-weight: 720; }
.result-composition__heading {
  display: grid;
  gap: 0.15rem;
}

.result-composition__title {
  margin: 0;
  font-size: 0.72rem;
  color: var(--tg-text-strong);
}
.result-composition__heading p { margin: 0; color: var(--tg-text-muted); font-size: 0.48rem; }
.result-composition__icon { width: 1.8rem; height: 1.8rem; display: grid; place-items: center; border-radius: 6px; background: var(--tg-action-soft); color: var(--tg-action-strong); box-shadow: inset 0 0 0 1px #d6e4ff; font: 800 0.5rem/1 ui-monospace, monospace; }
.result-composition__bar { display: flex; height: 0.7rem; overflow: hidden; border-radius: 3px; background: #edf1f6; }
.result-composition__bar i { min-width: 0; background: #8d9ab0; }
.result-composition__bar--seed,.result-composition__swatch--seed { background: #2563eb !important; }.result-composition__bar--valid,.result-composition__swatch--valid { background: #178263 !important; }.result-composition__bar--exception,.result-composition__swatch--exception { background: #d29a43 !important; }.result-composition__bar--crash,.result-composition__swatch--crash { background: #c65362 !important; }.result-composition__bar--notarget,.result-composition__swatch--notarget { background: #8b70c9 !important; }.result-composition__bar--hangs,.result-composition__swatch--hangs { background: #63738f !important; }.result-composition__bar--flaky,.result-composition__swatch--flaky { background: #168aa4 !important; }

.result-composition__grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.32rem 0.7rem;
}

.result-composition__item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  padding: 0;
  min-width: 0;
}

.result-composition__category {
  display: inline-flex;
  align-items: center;
  gap: 0.38rem;
  color: var(--tg-text-muted);
  font-size: 0.56rem;
  word-break: break-word;
}
.result-composition__category i { width: 0.48rem; height: 0.48rem; flex: none; border-radius: 2px; }

.result-composition__count {
  font-weight: 700;
  color: var(--tg-text-strong);
  font-size: 0.68rem;
}

.result-composition__empty {
  margin: 0;
  border: 1px dashed var(--tg-border);
  border-radius: var(--tg-radius-sm);
  background: linear-gradient(135deg, #f8fbff, #eef6ff);
  color: var(--tg-text-muted);
  padding: 1rem;
  min-height: 4.8rem;
  display: grid;
  align-items: center;
}

@media (max-width: 720px) {
  .result-composition__grid {
    grid-template-columns: 1fr;
  }
}
</style>
