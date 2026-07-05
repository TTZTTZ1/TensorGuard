import vue from "@vitejs/plugin-vue";
import { defineConfig } from "vitest/config";

export default defineConfig(({ command }) => ({
  plugins: [vue()],
  base: command === "build" ? "/static/" : "/",
  build: {
    outDir: "../static",
    emptyOutDir: true,
  },
  server: {
    proxy: {
      "/api": "http://127.0.0.1:8008",
    },
  },
  test: {
    environment: "jsdom",
    globals: true,
  },
}));
