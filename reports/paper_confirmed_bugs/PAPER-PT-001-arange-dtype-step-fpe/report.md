# PAPER-PT-001: `torch.arange` dtype/step Coupling Triggers SIGFPE

## Summary

`torch.arange(start=1, end=2, step=0.1, dtype=torch.int64)` triggers a process-level floating point exception according to the paper appendix.

## Expected Behavior

PyTorch should either construct a valid tensor or reject the incompatible `step` and integer `dtype` combination with a Python-level exception.

## Observed Behavior

```text
Floating point exception
```

## Minimal Reproduction

```python
import torch

input_data = torch.arange(start=1, end=2, step=0.1, dtype=torch.int64)
print(input_data)
```

## Source

`基于大语言模型的深度学习库模糊测试.pdf`, appendix "缺陷触发代码示例".
