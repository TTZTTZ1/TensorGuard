# PAPER-PT-003: `LSTMCell` Malformed Hidden State Segfault

## Summary

The appendix reports that `torch.nn.LSTMCell` can segfault when the hidden-state argument is a malformed tensor rather than the expected hidden/cell tuple.

## Expected Behavior

The malformed hidden state should be rejected by Python-level validation.

## Observed Behavior

```text
Segmentation fault
```

## Minimal Reproduction

```python
import torch

lstm_cell = torch.nn.LSTMCell(input_size=3, hidden_size=3)
lstm_cell(torch.randn(3), torch.zeros(2, 3, 3))
```

## Source

`基于大语言模型的深度学习库模糊测试.pdf`, appendix "缺陷触发代码示例".
