<script setup lang="ts">
defineProps<{
  loading?: boolean;
  error?: string | null;
  empty?: boolean;
  retryLabel?: string;
}>();

defineEmits<{
  retry: [];
}>();
</script>

<template>
  <div v-if="loading" class="async-state async-state--loading" role="status" aria-live="polite">
    <slot name="loading">
      <p class="async-state__copy">正在加载</p>
    </slot>
  </div>
  <div v-else-if="error" class="async-state async-state--error" role="alert">
    <div class="async-state__content">
      <slot name="error" :error="error">
        <p class="async-state__copy">{{ error }}</p>
      </slot>
    </div>
    <button type="button" class="async-state__retry" @click="$emit('retry')">
      {{ retryLabel ?? "重试" }}
    </button>
  </div>
  <div v-else-if="empty" class="async-state async-state--empty">
    <slot name="empty">
      <p class="async-state__copy">暂无内容</p>
    </slot>
  </div>
  <slot v-else />
</template>

<style scoped>
.async-state {
  border: 1px solid var(--tg-border);
  border-radius: var(--tg-radius);
  background: var(--tg-surface-muted);
  padding: 1rem;
  color: var(--tg-text-muted);
}

.async-state--error {
  background: var(--tg-red-bg);
  border-color: var(--tg-red-border);
  color: var(--tg-red-text);
}

.async-state--empty {
  background: var(--tg-surface-muted);
}

.async-state__content {
  margin-bottom: 0.75rem;
}

.async-state__copy {
  margin: 0;
}

.async-state__retry {
  border: 1px solid currentColor;
  border-radius: 999px;
  background: #ffffff;
  color: inherit;
  padding: 0.45rem 0.85rem;
}
</style>
