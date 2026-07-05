# PAPER-PT-005: Complex32 Normalization Internal Assert

## Summary

The appendix reports that `torch.nn.BatchNorm1d` with a `complex32` zero-width tensor reaches an internal assert in `AccumulateType.cpp`.

## Expected Behavior

Unsupported dtype/input combinations should be rejected with a normal user-facing exception.

## Observed Behavior

```text
false INTERNAL ASSERT FAILED at "/pytorch/aten/src/ATen/AccumulateType.cpp":23, please report a bug to PyTorch.
Unrecognized ScalarType: ComplexHalf
```

## Minimal Reproduction

```python
import torch

torch.nn.BatchNorm1d(1)(torch.zeros(2, 0, dtype=torch.complex32))
```

## Related APIs Mentioned In Appendix

`torch.nn.BatchNorm2d`, `torch.nn.BatchNorm3d`, `torch.nn.InstanceNorm1d`, `torch.nn.InstanceNorm2d`, `torch.nn.InstanceNorm3d`, `torch.renorm`, `torch.Tensor.renorm`, `torch.Tensor.renorm_`.

## Source

`基于大语言模型的深度学习库模糊测试.pdf`, appendix "缺陷触发代码示例".
