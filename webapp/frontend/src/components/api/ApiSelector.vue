<script setup lang="ts">
import { computed, ref, watch } from "vue";

import type { ApiListItem, Library } from "../../types/tensorguard";
import { useApiCatalog } from "../../composables/useApiCatalog";

const props = withDefaults(
  defineProps<{
    selected?: ApiListItem | null;
  }>(),
  {
    selected: null,
  },
);

const emit = defineEmits<{
  select: [ApiListItem];
  libraryChange: [Library];
}>();

const { library, query, items, loading, error, setLibrary, refresh } = useApiCatalog();
const isOpen = ref(false);
const activeIndex = ref(-1);
const listboxId = "api-selector-listbox";

function isSelected(item: ApiListItem): boolean {
  return props.selected !== null && props.selected.api === item.api && props.selected.lib === item.lib;
}

const activeDescendantId = computed(() =>
  isOpen.value && activeIndex.value >= 0 && activeIndex.value < items.value.length
    ? `api-selector-option-${activeIndex.value}`
    : undefined,
);

function handleInput(event: Event) {
  query.value = (event.target as HTMLInputElement).value;
  isOpen.value = true;
  activeIndex.value = -1;
}

function handleLibraryChange(nextLibrary: Library) {
  setLibrary(nextLibrary);
  emit("libraryChange", nextLibrary);
  isOpen.value = true;
  activeIndex.value = -1;
}

function setActiveIndex(nextIndex: number) {
  activeIndex.value = nextIndex;
}

function selectItem(item: ApiListItem, index: number) {
  setActiveIndex(index);
  query.value = item.api;
  emit("select", item);
  isOpen.value = false;
}

function getNextEnabledIndex(step: 1 | -1) {
  if (items.value.length === 0) {
    return -1;
  }

  if (activeIndex.value < 0) {
    return step > 0 ? 0 : items.value.length - 1;
  }

  return (activeIndex.value + step + items.value.length) % items.value.length;
}

function moveActive(step: 1 | -1) {
  const nextIndex = getNextEnabledIndex(step);
  if (nextIndex < 0) {
    return;
  }

  isOpen.value = true;
  setActiveIndex(nextIndex);
}

function handleKeydown(event: KeyboardEvent) {
  if (event.key === "ArrowDown") {
    event.preventDefault();
    moveActive(1);
    return;
  }

  if (event.key === "ArrowUp") {
    event.preventDefault();
    moveActive(-1);
    return;
  }

  if (event.key === "Home") {
    if (items.value.length === 0) {
      return;
    }

    event.preventDefault();
    isOpen.value = true;
    setActiveIndex(0);
    return;
  }

  if (event.key === "End") {
    if (items.value.length === 0) {
      return;
    }

    event.preventDefault();
    isOpen.value = true;
    setActiveIndex(items.value.length - 1);
    return;
  }

  if (event.key === "Enter") {
    if (activeIndex.value < 0 || activeIndex.value >= items.value.length) {
      return;
    }

    event.preventDefault();
    selectItem(items.value[activeIndex.value], activeIndex.value);
    return;
  }

  if (event.key === "Escape") {
    if (!isOpen.value) {
      return;
    }

    event.preventDefault();
    isOpen.value = false;
  }
}

watch(
  items,
  (nextItems) => {
    if (nextItems.length === 0) {
      activeIndex.value = -1;
      return;
    }

    if (activeIndex.value >= nextItems.length) {
      activeIndex.value = -1;
    }
  },
  { immediate: true },
);
</script>

<template>
  <section class="api-selector" aria-label="API 搜索">
    <div class="api-selector__toolbar" aria-label="API 库">
      <div class="api-selector__field">
        <span class="api-selector__field-label">框架</span>
        <div class="api-selector__libraries" role="group" aria-label="选择框架">
          <button
            type="button"
            class="api-selector__library"
            :class="{ 'api-selector__library--active': library === 'torch' }"
            :aria-pressed="library === 'torch'"
            @click="handleLibraryChange('torch')"
          >
            PyTorch
          </button>
          <button
            type="button"
            class="api-selector__library"
            :class="{ 'api-selector__library--active': library === 'tf' }"
            :aria-pressed="library === 'tf'"
            @click="handleLibraryChange('tf')"
          >
            TensorFlow
          </button>
        </div>
      </div>

      <div class="api-selector__field api-selector__field--search">
        <label class="api-selector__field-label" for="api-selector-search">当前 API</label>
        <div class="api-selector__search-control">
          <span aria-hidden="true">⌕</span>
          <input
            id="api-selector-search"
            class="api-selector__search-input"
            type="search"
            role="combobox"
            aria-autocomplete="list"
            :aria-expanded="isOpen"
            :aria-controls="listboxId"
            :aria-activedescendant="activeDescendantId"
            :placeholder="selected?.api ?? '输入关键字或展开选择'"
            :value="query"
            @input="handleInput"
            @keydown="handleKeydown"
            @focus="isOpen = true"
          />
          <span class="api-selector__chevron" aria-hidden="true">⌄</span>
        </div>
      </div>
    </div>

    <div v-if="loading" class="api-selector__state" role="status" aria-live="polite">正在加载 API 列表</div>

    <div v-else-if="error" class="api-selector__state api-selector__state--error" role="alert">
      <p class="api-selector__state-copy">{{ error }}</p>
      <button type="button" class="api-selector__retry" @click="refresh">重试</button>
    </div>

    <ul v-else-if="isOpen" :id="listboxId" class="api-selector__list" role="listbox" aria-label="API 结果">
      <li v-for="(item, index) in items" :key="`${item.lib}:${item.api}`" class="api-selector__item">
        <button
          :id="`api-selector-option-${index}`"
          type="button"
          role="option"
          class="api-selector__option"
          :class="{
            'api-selector__option--selected': isSelected(item),
            'api-selector__option--active': activeIndex === index,
          }"
          :aria-selected="isSelected(item)"
          tabindex="-1"
          @click="selectItem(item, index)"
        >
          <span class="api-selector__option-api">{{ item.api }}</span>
          <span class="api-selector__option-lib">{{ item.lib }}</span>
        </button>
      </li>
    </ul>

    <div v-if="!loading && !error && isOpen && items.length === 0" class="api-selector__state">未找到 API</div>
  </section>
</template>

<style scoped>
.api-selector {
  position: relative;
  min-width: 0;
}

.api-selector__toolbar {
  display: grid;
  grid-template-columns: minmax(11rem, 0.82fr) minmax(16rem, 1.18fr);
  gap: 0.65rem;
  align-items: end;
}

.api-selector__field {
  display: grid;
  gap: 0.3rem;
  min-width: 0;
}

.api-selector__field-label {
  color: var(--tg-text-muted);
  font-size: 0.56rem;
  font-weight: 720;
}

.api-selector__libraries {
  height: 2.2rem;
  display: flex;
  padding: 3px;
  border: 1px solid #d6deeb;
  border-radius: 5px;
  background: #f5f7fb;
}

.api-selector__library {
  flex: 1;
  border: 0;
  border-radius: 3px;
  background: transparent;
  color: var(--tg-text-muted);
  padding: 0 0.55rem;
  font-size: 0.62rem;
}

.api-selector__library--active {
  color: var(--tg-action-strong);
  background: #fff;
  box-shadow: 0 2px 8px rgba(36, 58, 98, 0.08);
}

.api-selector__search-control {
  height: 2.2rem;
  display: grid;
  grid-template-columns: auto minmax(0, 1fr) auto;
  align-items: center;
  gap: 0.45rem;
  border: 1px solid #d6deeb;
  border-radius: 5px;
  background: #f8fbff;
  padding: 0 0.65rem;
  color: #7890b6;
}

.api-selector__search-input {
  width: 100%;
  min-width: 0;
  border: 0;
  outline: 0;
  background: transparent;
  padding: 0;
  color: #1a3f8b;
  font: 0.66rem/1 ui-monospace, SFMono-Regular, Menlo, monospace;
}

.api-selector__search-input::placeholder {
  color: #7890b6;
  opacity: 1;
}

.api-selector__chevron {
  color: var(--tg-text-muted);
}

.api-selector__list {
  position: absolute;
  z-index: 20;
  top: calc(100% + 0.35rem);
  right: 0;
  width: min(32rem, 100%);
  max-height: 17rem;
  overflow: auto;
  list-style: none;
  margin: 0;
  padding: 0.35rem;
  display: grid;
  gap: 0.2rem;
  border: 1px solid var(--tg-border);
  border-radius: 7px;
  background: #fff;
  box-shadow: 0 16px 34px rgba(31, 48, 87, 0.15);
}

.api-selector__option {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  border: 0;
  border-radius: 5px;
  background: #fff;
  padding: 0.58rem 0.68rem;
  color: var(--tg-text);
  text-align: left;
  font-size: 0.65rem;
}

.api-selector__option--selected {
  background: var(--tg-action-soft);
  color: var(--tg-action-strong);
  font-weight: 720;
}

.api-selector__option--active {
  background: #f3f7fe;
}

.api-selector__option-api {
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.api-selector__option-lib {
  flex: none;
  color: var(--tg-text-soft);
  font-size: 0.82rem;
  text-transform: uppercase;
}

.api-selector__state {
  position: absolute;
  z-index: 20;
  top: calc(100% + 0.35rem);
  right: 0;
  width: min(32rem, 100%);
  border: 1px solid var(--tg-border);
  border-radius: 7px;
  background: #fff;
  color: var(--tg-text-muted);
  padding: 0.7rem;
  font-size: 0.65rem;
  box-shadow: 0 16px 34px rgba(31, 48, 87, 0.12);
}

.api-selector__state--error {
  position: static;
  width: 100%;
  margin-top: 0.35rem;
  background: var(--tg-red-bg);
  border-color: var(--tg-red-border);
  color: var(--tg-red-text);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.65rem;
}

.api-selector__state-copy {
  margin: 0;
}

.api-selector__retry {
  justify-self: start;
  border: 1px solid currentColor;
  border-radius: 999px;
  background: #ffffff;
  color: inherit;
  padding: 0.45rem 0.85rem;
}

@media (max-width: 720px) {
  .api-selector__toolbar {
    grid-template-columns: 1fr;
  }

  .api-selector__list,
  .api-selector__state {
    width: 100%;
  }
}
</style>
