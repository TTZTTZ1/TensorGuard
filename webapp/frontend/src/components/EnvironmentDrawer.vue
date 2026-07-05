<script setup lang="ts">
import { RefreshCw, X } from "@lucide/vue";

import AsyncState from "./AsyncState.vue";
import type { EnvironmentPayload, FrameworkPackageInfo } from "../types/tensorguard";

defineProps<{
  open: boolean;
  loading: boolean;
  error: string | null;
  environment: EnvironmentPayload | null;
  environmentLabel: string;
}>();

const emit = defineEmits<{
  close: [];
  refresh: [];
}>();

function formatPackageState(value: FrameworkPackageInfo | undefined): string {
  if (value === undefined) {
    return "未返回版本";
  }

  if (value.installed === true) {
    return value.version;
  }

  if (value.installed === false) {
    return "未安装";
  }

  return value.error;
}

function formatMemory(memoryTotalMiB: number | null | undefined): string {
  if (memoryTotalMiB === null || memoryTotalMiB === undefined) {
    return "未返回显存";
  }

  return `${memoryTotalMiB.toLocaleString("en-US")} MiB`;
}
</script>

<template>
  <aside
    v-if="open"
    id="environment-drawer"
    class="environment-drawer"
  >
    <div class="environment-drawer__panel">
      <header class="environment-drawer__header">
        <div class="environment-drawer__title-block">
          <p class="environment-drawer__eyebrow">运行环境</p>
          <h2 class="environment-drawer__title">环境信息</h2>
          <p class="environment-drawer__subtitle">{{ environmentLabel }}</p>
        </div>

        <div class="environment-drawer__actions">
          <button
            type="button"
            class="environment-drawer__action"
            :disabled="loading"
            @click="$emit('refresh')"
          >
            <RefreshCw class="environment-drawer__action-icon" aria-hidden="true" />
            <span>刷新</span>
          </button>
          <button type="button" class="environment-drawer__close" aria-label="关闭环境面板" @click="$emit('close')">
            <X aria-hidden="true" />
          </button>
        </div>
      </header>

      <div class="environment-drawer__body">
        <AsyncState :loading="loading && environment === null" :error="environment === null ? error : null" @retry="$emit('refresh')">
          <template #loading>
            <p class="environment-drawer__state-copy">正在读取后端环境信息。</p>
          </template>

          <template #error="{ error: errorText }">
            <p class="environment-drawer__state-copy">{{ errorText }}</p>
          </template>

          <template #default>
            <div v-if="environment !== null && error !== null" class="environment-drawer__notice">
              <AsyncState :error="error" @retry="$emit('refresh')" />
            </div>

            <section class="environment-drawer__section">
              <h3 class="environment-drawer__section-title">平台</h3>
              <dl class="environment-drawer__grid">
                <div class="environment-drawer__row">
                  <dt>采集时间</dt>
                  <dd>{{ environment?.collected_at }}</dd>
                </div>
                <div class="environment-drawer__row">
                  <dt>系统</dt>
                  <dd>{{ environment?.platform.system }}</dd>
                </div>
                <div class="environment-drawer__row">
                  <dt>版本</dt>
                  <dd>{{ environment?.platform.release }}</dd>
                </div>
                <div class="environment-drawer__row">
                  <dt>架构</dt>
                  <dd>{{ environment?.platform.machine }}</dd>
                </div>
                <div class="environment-drawer__row">
                  <dt>Python</dt>
                  <dd>{{ environment?.python.version }}</dd>
                </div>
                <div class="environment-drawer__row">
                  <dt>解释器</dt>
                  <dd>{{ environment?.python.executable }}</dd>
                </div>
              </dl>
            </section>

            <section class="environment-drawer__section">
              <h3 class="environment-drawer__section-title">框架</h3>
              <dl class="environment-drawer__grid">
                <div class="environment-drawer__row">
                  <dt>Torch</dt>
                  <dd>{{ formatPackageState(environment?.frameworks.torch) }}</dd>
                </div>
                <div class="environment-drawer__row">
                  <dt>TensorFlow</dt>
                  <dd>{{ formatPackageState(environment?.frameworks.tensorflow) }}</dd>
                </div>
              </dl>
            </section>

            <section class="environment-drawer__section">
              <h3 class="environment-drawer__section-title">CUDA</h3>
              <dl class="environment-drawer__grid">
                <div class="environment-drawer__row">
                  <dt>可用性</dt>
                  <dd>{{ environment?.cuda.available ? "可用" : "不可用" }}</dd>
                </div>
                <div class="environment-drawer__row">
                  <dt>驱动版本</dt>
                  <dd>{{ environment?.cuda.driver_version ?? "未返回驱动版本" }}</dd>
                </div>
              </dl>
            </section>

            <section class="environment-drawer__section">
              <h3 class="environment-drawer__section-title">GPU</h3>
              <AsyncState :empty="(environment?.gpus.length ?? 0) === 0">
                <template #empty>
                  <p class="environment-drawer__state-copy">后端未返回 GPU 条目。</p>
                </template>

                <ul class="environment-drawer__gpu-list">
                  <li v-for="gpu in environment?.gpus ?? []" :key="`${gpu.index}-${gpu.name}`" class="environment-drawer__gpu">
                    <div class="environment-drawer__gpu-head">
                      <span class="environment-drawer__gpu-name">GPU {{ gpu.index }}</span>
                      <span class="environment-drawer__gpu-chip">{{ gpu.driver_version }}</span>
                    </div>
                    <p class="environment-drawer__gpu-model">{{ gpu.name }}</p>
                    <p class="environment-drawer__gpu-memory">{{ formatMemory(gpu.memory_total_mib) }}</p>
                  </li>
                </ul>
              </AsyncState>
            </section>

            <section v-if="(environment?.warnings.length ?? 0) > 0" class="environment-drawer__section">
              <h3 class="environment-drawer__section-title">提示</h3>
              <ul class="environment-drawer__warnings">
                <li v-for="warning in environment?.warnings ?? []" :key="warning" class="environment-drawer__warning">
                  {{ warning }}
                </li>
              </ul>
            </section>
          </template>
        </AsyncState>
      </div>
    </div>
  </aside>
</template>

<style scoped>
.environment-drawer {
  position: fixed;
  inset: 0 0 0 auto;
  width: min(100vw, 27rem);
}

.environment-drawer__panel {
  position: absolute;
  inset: 0;
  display: grid;
  grid-template-rows: auto minmax(0, 1fr);
  background: var(--tg-surface);
  border-left: 1px solid var(--tg-border);
  box-shadow: var(--tg-shadow-raised);
}

.environment-drawer__header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
  padding: 1rem 1rem 0.9rem;
  border-bottom: 1px solid var(--tg-border);
}

.environment-drawer__eyebrow {
  margin: 0;
  font-size: 0.74rem;
  color: var(--tg-text-soft);
}

.environment-drawer__title {
  margin: 0.15rem 0 0;
  font-size: 1.08rem;
  color: var(--tg-text-strong);
}

.environment-drawer__subtitle {
  margin: 0.25rem 0 0;
  color: var(--tg-text-muted);
}

.environment-drawer__actions {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.environment-drawer__action,
.environment-drawer__close {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  border-radius: 999px;
  border: 1px solid var(--tg-border);
  background: #ffffff;
  color: var(--tg-text-muted);
  padding: 0.55rem 0.75rem;
}

.environment-drawer__action:hover,
.environment-drawer__close:hover {
  border-color: rgba(25, 86, 209, 0.28);
  color: var(--tg-action);
}

.environment-drawer__action:disabled {
  opacity: 0.6;
  cursor: wait;
}

.environment-drawer__action-icon {
  width: 1rem;
  height: 1rem;
}

.environment-drawer__body {
  overflow: auto;
  padding: 1rem;
}

.environment-drawer__state-copy {
  margin: 0;
}

.environment-drawer__notice {
  margin-bottom: 0.9rem;
}

.environment-drawer__section {
  display: grid;
  gap: 0.75rem;
  padding: 0.9rem 0;
  border-bottom: 1px solid var(--tg-border);
}

.environment-drawer__section:first-child {
  padding-top: 0;
}

.environment-drawer__section:last-child {
  border-bottom: 0;
}

.environment-drawer__section-title {
  margin: 0;
  font-size: 0.84rem;
  color: var(--tg-text-soft);
  text-transform: uppercase;
  letter-spacing: 0;
}

.environment-drawer__grid {
  display: grid;
  gap: 0.6rem;
  margin: 0;
}

.environment-drawer__row {
  display: grid;
  grid-template-columns: minmax(5rem, 7rem) minmax(0, 1fr);
  gap: 0.75rem;
  align-items: baseline;
}

.environment-drawer__row dt,
.environment-drawer__row dd {
  margin: 0;
}

.environment-drawer__row dt {
  color: var(--tg-text-soft);
}

.environment-drawer__row dd {
  color: var(--tg-text-strong);
  text-align: right;
  word-break: break-word;
}

.environment-drawer__gpu-list,
.environment-drawer__warnings {
  display: grid;
  gap: 0.75rem;
  margin: 0;
  padding: 0;
  list-style: none;
}

.environment-drawer__gpu,
.environment-drawer__warning {
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface-muted);
  padding: 0.85rem;
}

.environment-drawer__gpu-head {
  display: flex;
  justify-content: space-between;
  gap: 0.75rem;
  margin-bottom: 0.45rem;
}

.environment-drawer__gpu-name {
  font-weight: 600;
  color: var(--tg-text-strong);
}

.environment-drawer__gpu-chip {
  color: var(--tg-action);
}

.environment-drawer__gpu-model,
.environment-drawer__gpu-memory {
  margin: 0;
  color: var(--tg-text-muted);
}

@media (max-width: 720px) {
  .environment-drawer {
    width: 100vw;
  }

  .environment-drawer__row {
    grid-template-columns: 1fr;
    gap: 0.2rem;
  }

  .environment-drawer__row dd {
    text-align: left;
  }
}
</style>
