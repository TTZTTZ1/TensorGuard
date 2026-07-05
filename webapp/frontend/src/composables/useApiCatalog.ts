import { onBeforeUnmount, ref, watch } from "vue";

import { getApis } from "../services/tensorguard";
import type { ApiListItem, Library } from "../types/tensorguard";

const DEFAULT_LIMIT = 5000;
const DEBOUNCE_MS = 250;

export function useApiCatalog() {
  const library = ref<Library>("torch");
  const query = ref("");
  const items = ref<ApiListItem[]>([]);
  const loading = ref(false);
  const error = ref<string | null>(null);

  let timer: ReturnType<typeof setTimeout> | null = null;
  let requestToken = 0;

  function describeError(value: unknown): string {
    if (value instanceof Error) {
      return value.message;
    }

    return "API 列表加载失败";
  }

  async function loadCatalog() {
    const token = ++requestToken;
    loading.value = true;
    error.value = null;

    try {
      const nextItems = await getApis(library.value, query.value, DEFAULT_LIMIT);
      if (token === requestToken) {
        items.value = nextItems;
      }
    } catch (cause) {
      if (token === requestToken) {
        error.value = describeError(cause);
      }
    } finally {
      if (token === requestToken) {
        loading.value = false;
      }
    }
  }

  function scheduleLoad() {
    if (timer !== null) {
      clearTimeout(timer);
    }

    timer = setTimeout(() => {
      timer = null;
      void loadCatalog();
    }, DEBOUNCE_MS);
  }

  function invalidateAndScheduleLoad() {
    requestToken += 1;
    items.value = [];
    error.value = null;
    scheduleLoad();
  }

  function setLibrary(nextLibrary: Library) {
    library.value = nextLibrary;
  }

  function refresh() {
    if (timer !== null) {
      clearTimeout(timer);
      timer = null;
    }

    return loadCatalog();
  }

  watch([library, query], invalidateAndScheduleLoad, { immediate: true, flush: "sync" });

  onBeforeUnmount(() => {
    if (timer !== null) {
      clearTimeout(timer);
      timer = null;
    }

    requestToken += 1;
  });

  return {
    library,
    query,
    items,
    loading,
    error,
    setLibrary,
    refresh,
  };
}
