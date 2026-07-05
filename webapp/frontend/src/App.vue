<script setup lang="ts">
import { ref } from "vue";

import AppHeader from "./components/AppHeader.vue";
import EnvironmentDrawer from "./components/EnvironmentDrawer.vue";
import { useEnvironment } from "./composables/useEnvironment";
import { useHashNavigation } from "./composables/useHashNavigation";
import OverviewView from "./views/OverviewView.vue";
import ApiRunView from "./views/ApiRunView.vue";
import BugReplayView from "./views/BugReplayView.vue";

const { activeKey, selectKey } = useHashNavigation();
const { environment, loading, error, environmentLabel, refresh } = useEnvironment();
const environmentOpen = ref(false);

function toggleEnvironment() {
  environmentOpen.value = !environmentOpen.value;
}

function closeEnvironment() {
  environmentOpen.value = false;
}

function handleRefresh() {
  void refresh().catch(() => undefined);
}
</script>

<template>
  <div class="app-shell">
    <AppHeader
      :active-key="activeKey"
      :environment-label="environmentLabel"
      :environment-open="environmentOpen"
      @select="selectKey"
      @toggle-environment="toggleEnvironment"
    />

    <div class="app-shell__frame">
      <main class="app-shell__main" :class="{ 'app-shell__main--drawer-open': environmentOpen }">
        <OverviewView
          v-if="activeKey === 'overview'"
          :environment="environment"
          :environment-loading="loading"
          :environment-error="error"
        />

        <ApiRunView v-else-if="activeKey === 'api-run'" />

        <BugReplayView v-else />
      </main>

      <EnvironmentDrawer
        :open="environmentOpen"
        :environment="environment"
        :loading="loading"
        :error="error"
        :environment-label="environmentLabel"
        @close="closeEnvironment"
        @refresh="handleRefresh"
      />
    </div>
  </div>
</template>

<style scoped>
.app-shell {
  min-height: 100vh;
  background: var(--tg-bg);
}

.app-shell__frame {
  position: relative;
  min-height: calc(100vh - var(--tg-header-height));
  padding: 1.25rem 1.5rem 2.25rem;
}

.app-shell__main {
  width: 100%;
  max-width: var(--tg-content-width);
  margin: 0 auto;
  transition: padding-right 0.18s ease;
}

.app-shell__main--drawer-open {
  padding-right: min(28rem, 42vw);
}

@media (max-width: 720px) {
  .app-shell__frame {
    padding: 0.75rem;
  }

  .app-shell__main,
  .app-shell__main--drawer-open {
    padding-right: 0;
  }

}
</style>
