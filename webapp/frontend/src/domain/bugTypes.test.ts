import { describe, expect, it } from "vitest";

import { bugTypeGroups, bugTypeValues } from "./bugTypes";

describe("bug type taxonomy", () => {
  it("covers consistency, numerical, reliability, and semantic framework defects without duplicates", () => {
    expect(bugTypeGroups.map((group) => group.label)).toEqual([
      "结果一致性",
      "数值正确性",
      "崩溃与可靠性",
      "接口语义与状态",
    ]);
    expect(bugTypeValues).toContain("CPU/GPU value mismatch");
    expect(bugTypeValues).toContain("CUDA device-side assert");
    expect(bugTypeValues).toContain("Autograd / gradient defect");
    expect(new Set(bugTypeValues).size).toBe(bugTypeValues.length);
  });
});
