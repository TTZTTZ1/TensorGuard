<script setup lang="ts">
import type { ViewKey } from "../composables/useHashNavigation";

withDefaults(
  defineProps<{
    activeKey: ViewKey;
    environmentLabel: string;
    environmentOpen?: boolean;
  }>(),
  { environmentOpen: false },
);

const emit = defineEmits<{
  select: [ViewKey];
  toggleEnvironment: [];
}>();

const navItems: Array<{ key: ViewKey; label: string; hash: string }> = [
  { key: "overview", label: "系统总览", hash: "#overview" },
  { key: "api-run", label: "单 API 运行", hash: "#api-run" },
  { key: "bug-replay", label: "Bug 复现", hash: "#bug-replay" },
];
</script>

<template>
  <header class="app-header">
    <div class="app-header__brand">
      <span class="app-header__mark" aria-hidden="true">TG</span>
      <span class="app-header__brand-copy">
        <strong class="app-header__name">TensorGuard</strong>
        <small class="app-header__subtitle">深度学习框架缺陷检测平台</small>
      </span>
    </div>

    <nav class="app-header__nav" aria-label="TensorGuard 主要视图">
      <a
        v-for="item in navItems"
        :key="item.key"
        class="app-header__nav-item"
        :class="{ 'app-header__nav-item--active': activeKey === item.key }"
        :href="item.hash"
        :aria-current="activeKey === item.key ? 'page' : undefined"
        @click.prevent="emit('select', item.key)"
      >
        {{ item.label }}
      </a>
    </nav>

    <div class="app-header__actions shell-chrome">
      <button
        type="button"
        class="app-header__environment"
        :aria-label="`环境信息：${environmentLabel}`"
        :aria-expanded="environmentOpen"
        aria-controls="environment-drawer"
        @click="emit('toggleEnvironment')"
      >
        <span class="app-header__environment-dot" aria-hidden="true" />
        <span class="app-header__environment-label">{{ environmentLabel }}</span>
        <span class="app-header__avatar" aria-hidden="true">0</span>
      </button>
    </div>
  </header>
</template>

<style scoped>
.app-header {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.25rem;
  height: var(--tg-header-height);
  padding: 0 2rem;
  background: #ffffff;
  border-bottom: 1px solid var(--tg-border);
}

.app-header__brand {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  min-width: 13rem;
}

.app-header__mark {
  width: 2.125rem;
  height: 2.125rem;
  display: grid;
  place-items: center;
  flex: none;
  border-radius: 7px;
  background: var(--tg-action);
  color: #ffffff;
  font-size: 0.7rem;
  font-weight: 850;
  box-shadow: 0 7px 16px rgba(37, 99, 235, 0.2);
}

.app-header__brand-copy {
  display: grid;
  gap: 0.05rem;
}

.app-header__name {
  color: var(--tg-text-strong);
  font-size: 0.94rem;
  font-weight: 780;
}

.app-header__subtitle {
  color: var(--tg-text-muted);
  font-size: 0.58rem;
}

.app-header__nav {
  align-self: stretch;
  display: flex;
  align-items: stretch;
  justify-content: center;
  flex: 1;
  gap: 1.75rem;
}

.app-header__nav-item {
  position: relative;
  display: inline-flex;
  align-items: center;
  padding: 0 0.25rem;
  color: var(--tg-text-muted);
  font-size: 0.75rem;
  font-weight: 680;
  white-space: nowrap;
  transition: color 0.15s ease;
}

.app-header__nav-item:hover {
  color: var(--tg-action);
}

.app-header__nav-item--active {
  color: var(--tg-text-strong);
}

.app-header__nav-item--active::after {
  content: "";
  position: absolute;
  left: 0.25rem;
  right: 0.25rem;
  bottom: 0;
  height: 3px;
  border-radius: 3px 3px 0 0;
  background: var(--tg-action);
}

.app-header__actions {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  min-width: 13rem;
}

.app-header__environment {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  border: 0;
  background: transparent;
  color: var(--tg-text-muted);
  padding: 0.35rem 0;
  font-size: 0.65rem;
}

.app-header__environment:hover {
  color: var(--tg-action);
}

.app-header__environment-dot {
  width: 0.5rem;
  height: 0.5rem;
  border-radius: 50%;
  background: #22a878;
  box-shadow: 0 0 0 4px #e8f7f1;
}

.app-header__avatar {
  width: 1.8rem;
  height: 1.8rem;
  display: grid;
  place-items: center;
  margin-left: 0.35rem;
  border: 1px solid var(--tg-border);
  border-radius: 50%;
  background: #f4f7fc;
  color: #4f5d75;
  font-weight: 760;
}

@media (max-width: 900px) {
  .app-header { padding: 0 0.875rem; gap: 0.75rem; }
  .app-header__brand { min-width: auto; }
  .app-header__subtitle { display: none; }
  .app-header__nav { gap: clamp(0.5rem, 3vw, 1.4rem); }
  .app-header__actions { min-width: auto; }
  .app-header__environment-label,
  .app-header__avatar { display: none; }
}

@media (max-width: 560px) {
  .app-header__name { display: none; }
  .app-header__nav { gap: 0.5rem; }
  .app-header__nav-item { font-size: 0.64rem; }
  .app-header__actions { display: none; }
}
</style>
