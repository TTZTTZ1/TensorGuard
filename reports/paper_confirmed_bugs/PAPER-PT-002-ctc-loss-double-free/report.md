# PAPER-PT-002: `ctc_loss` Backward Triggers Double Free

## Summary

The appendix reports that a `torch.nn.functional.ctc_loss` call followed by `backward()` aborts with allocator corruption.

## Expected Behavior

Invalid target values should be rejected with a normal Python-level exception.

## Observed Behavior

```text
double free or corruption (out)
Aborted
```

## Minimal Reproduction

```python
import torch

log_probs = torch.randn(5, 6, requires_grad=True)
targets = torch.tensor([[3, 5, 6, 7]])
input_lengths = torch.tensor([5])
target_lengths = torch.tensor([4])

loss = torch.nn.functional.ctc_loss(
    log_probs,
    targets,
    input_lengths,
    target_lengths=target_lengths,
)
loss.backward()
```

## Source

`基于大语言模型的深度学习库模糊测试.pdf`, appendix "缺陷触发代码示例".
