import { onBeforeUnmount, ref } from "vue";

export interface PollOutcome<T> {
  value: T;
  continue: boolean;
}

export function usePolling<T>(task: () => Promise<PollOutcome<T>>, intervalMs = 1000) {
  const latest = ref<T | null>(null);
  const running = ref(false);
  const loading = ref(false);
  const error = ref<string | null>(null);

  let timer: ReturnType<typeof setTimeout> | null = null;
  let generation = 0;
  let inFlightGeneration: number | null = null;

  function describeError(value: unknown): string {
    if (value instanceof Error) {
      return value.message;
    }

    return "轮询失败";
  }

  function clearTimer() {
    if (timer !== null) {
      clearTimeout(timer);
      timer = null;
    }
  }

  function stop() {
    running.value = false;
    loading.value = false;
    generation += 1;
    clearTimer();
  }

  function schedule(delay: number, nextGeneration: number) {
    clearTimer();
    timer = setTimeout(() => {
      timer = null;
      void tick(nextGeneration);
    }, delay);
  }

  function retryNow() {
    if (!running.value) {
      return;
    }

    clearTimer();
    error.value = null;
    schedule(0, generation);
  }

  async function tick(nextGeneration: number) {
    if (!running.value || nextGeneration !== generation) {
      return;
    }

    if (inFlightGeneration === nextGeneration) {
      return;
    }

    inFlightGeneration = nextGeneration;
    loading.value = true;

    try {
      const outcome = await task();
      if (nextGeneration !== generation || !running.value) {
        return;
      }

      latest.value = outcome.value;
      error.value = null;

      if (outcome.continue) {
        schedule(intervalMs, nextGeneration);
      } else {
        stop();
      }
    } catch (cause) {
      if (nextGeneration === generation && running.value) {
        error.value = describeError(cause);
        schedule(intervalMs, nextGeneration);
      }
    } finally {
      if (inFlightGeneration === nextGeneration) {
        inFlightGeneration = null;
        loading.value = false;
      }
    }
  }

  function start() {
    if (running.value) {
      return;
    }

    generation += 1;
    const nextGeneration = generation;
    running.value = true;
    error.value = null;
    schedule(0, nextGeneration);
  }

  onBeforeUnmount(() => {
    stop();
  });

  return {
    latest,
    running,
    loading,
    error,
    start,
    stop,
    retryNow,
  };
}
