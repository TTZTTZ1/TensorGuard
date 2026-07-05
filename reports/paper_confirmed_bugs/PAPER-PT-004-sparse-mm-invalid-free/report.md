# PAPER-PT-004: `torch.sparse.mm` Invalid Free

## Summary

The appendix reports that sparse matrix multiplication on malformed sparse tensors can abort with allocator corruption. The appendix notes that a related trigger also appears through `torch.sparse_csr_tensor`.

## Expected Behavior

Invalid sparse tensor invariants should be detected and reported as a normal framework exception.

## Observed Behavior

```text
free(): invalid next size (fast)
Aborted
```

## Minimal Reproduction

```python
import torch

mat1 = torch.sparse_coo_tensor(
    indices=torch.tensor([[0, 1], [1, 2]]),
    values=torch.tensor([1.0, 2.0]),
    size=(2, 3),
)
mat2 = torch.sparse_coo_tensor(
    indices=torch.tensor([[0, 2], [0, 3]]),
    values=torch.tensor([3.0, 1.0]),
    size=(3, 2),
)

torch.sparse.mm(mat1, mat2)
```

## Source

`基于大语言模型的深度学习库模糊测试.pdf`, appendix "缺陷触发代码示例".
