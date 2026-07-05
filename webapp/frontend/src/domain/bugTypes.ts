export interface BugTypeOption {
  value: string;
  label: string;
}

export interface BugTypeGroup {
  label: string;
  options: BugTypeOption[];
}

export const bugTypeGroups: BugTypeGroup[] = [
  {
    label: "结果一致性",
    options: [
      { value: "CPU/GPU value mismatch", label: "CPU/GPU 数值不一致" },
      { value: "CPU/GPU exception mismatch", label: "CPU/GPU 异常行为不一致" },
      { value: "Output shape mismatch", label: "输出形状不一致" },
      { value: "Output dtype mismatch", label: "输出数据类型不一致" },
      { value: "Output device / layout mismatch", label: "输出设备或布局不一致" },
      { value: "Nondeterministic / flaky behavior", label: "非确定性或偶发行为" },
    ],
  },
  {
    label: "数值正确性",
    options: [
      { value: "Precision anomaly", label: "精度异常" },
      { value: "NaN / Inf propagation", label: "NaN / Inf 传播异常" },
      { value: "Overflow / underflow", label: "溢出或下溢" },
      { value: "Numerical stability defect", label: "数值稳定性缺陷" },
    ],
  },
  {
    label: "崩溃与可靠性",
    options: [
      { value: "Process crash / abnormal exit", label: "进程崩溃或异常退出" },
      { value: "Segmentation fault", label: "段错误" },
      { value: "Memory corruption / invalid free / out-of-bounds", label: "内存破坏、非法释放或越界" },
      { value: "Internal assertion failure", label: "框架内部断言失败" },
      { value: "Fatal check failure", label: "致命检查失败" },
      { value: "CUDA device-side assert", label: "CUDA 设备端断言" },
      { value: "CUDA kernel / backend failure", label: "CUDA 内核或后端失败" },
      { value: "Hang / timeout / deadlock", label: "卡死、超时或死锁" },
    ],
  },
  {
    label: "接口语义与状态",
    options: [
      { value: "Argument validation defect", label: "参数校验缺陷" },
      { value: "Invalid-input handling defect", label: "非法输入处理缺陷" },
      { value: "In-place / aliasing defect", label: "原地操作或别名缺陷" },
      { value: "State mutation defect", label: "状态修改缺陷" },
      { value: "Autograd / gradient defect", label: "自动求导或梯度缺陷" },
      { value: "Sparse / special layout defect", label: "稀疏张量或特殊布局缺陷" },
      { value: "Serialization / model-state defect", label: "序列化或模型状态缺陷" },
      { value: "Resource leak / unexpected OOM", label: "资源泄漏或异常 OOM" },
    ],
  },
];

export const bugTypeValues = bugTypeGroups.flatMap((group) => group.options.map((option) => option.value));
export const customBugTypeValue = "__custom__";
