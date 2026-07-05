import { onBeforeUnmount, onMounted, ref } from "vue";

export type ViewKey = "overview" | "api-run" | "bug-replay";

const viewKeys: ReadonlyArray<ViewKey> = ["overview", "api-run", "bug-replay"];
const defaultViewKey: ViewKey = "overview";

function isViewKey(value: string): value is ViewKey {
  return (viewKeys as ReadonlyArray<string>).includes(value);
}

function parseHash(hash: string): ViewKey {
  const normalized = hash.replace(/^#/, "");
  return isViewKey(normalized) ? normalized : defaultViewKey;
}

export function useHashNavigation() {
  const activeKey = ref<ViewKey>(typeof window === "undefined" ? defaultViewKey : parseHash(window.location.hash));

  const syncFromHash = () => {
    if (typeof window === "undefined") {
      activeKey.value = defaultViewKey;
      return;
    }

    const nextKey = parseHash(window.location.hash);
    activeKey.value = nextKey;

    const normalizedHash = `#${nextKey}`;
    if (window.location.hash !== normalizedHash) {
      window.history.replaceState(null, "", normalizedHash);
    }
  };

  const selectKey = (key: ViewKey) => {
    activeKey.value = key;

    if (typeof window === "undefined") {
      return;
    }

    const nextHash = `#${key}`;
    if (window.location.hash !== nextHash) {
      window.location.hash = nextHash;
      return;
    }

    syncFromHash();
  };

  const handleHashChange = () => {
    syncFromHash();
  };

  onMounted(() => {
    syncFromHash();
    if (typeof window !== "undefined") {
      window.addEventListener("hashchange", handleHashChange);
    }
  });

  onBeforeUnmount(() => {
    if (typeof window !== "undefined") {
      window.removeEventListener("hashchange", handleHashChange);
    }
  });

  return {
    activeKey,
    selectKey,
  };
}
