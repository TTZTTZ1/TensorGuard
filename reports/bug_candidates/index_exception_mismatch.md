# PT-N1-003: Invalid Index Handling Mismatch in `gather` / `take`

## Summary

For invalid indices, CPU reports a normal Python-level exception while CUDA triggers a device-side assert. This is not a normal-input wrong-result bug; it is a backend exception-handling and robustness discrepancy.

## Environment

```text
PyTorch: 2.11.0+cu130
CUDA: 13.0
```

## Minimal Reproduction: `torch.Tensor.gather`

```python
import sys
import torch

device = sys.argv[1]

x = torch.randn(4, 3, device=device)
index = torch.tensor(
    [[0, 1, 3], [0, 1, 2], [0, 1, 2], [0, 1, 2]],
    device=device,
)
y = torch.Tensor.gather(x, 1, index)

if device.startswith("cuda"):
    torch.cuda.synchronize()
```

CPU:

```text
RuntimeError: index 3 is out of bounds for dimension 1 with size 3
```

CUDA:

```text
ScatterGatherKernel.cu: Assertion `idx_dim >= 0 && idx_dim < index_size ...` failed.
torch.AcceleratorError: CUDA error: device-side assert triggered
```

## Minimal Reproduction: `torch.Tensor.take`

```python
import sys
import torch

device = sys.argv[1]

x = torch.tensor([1, 2], dtype=torch.int32, device=device)
indices = torch.arange(3, device=device)
y = torch.Tensor.take(x, indices)

if device.startswith("cuda"):
    torch.cuda.synchronize()
```

CPU:

```text
IndexError: out of range: tried to access index 2 on a tensor of 2 elements
```

CUDA:

```text
IndexKernel.cu: Assertion failed.
torch.AcceleratorError: CUDA error: device-side assert triggered
```

## Triage Notes

- The input index is invalid, so this should not be presented as a normal-input numerical bug.
- The issue is that CUDA surfaces a lower-level device-side assert, which can poison the CUDA context and make later operations fail in the same process.
- This is weaker than `fractional_max_pool3d`, but it is still useful evidence for CUDA backend exception-handling inconsistency.

## Current Status

Candidate. Count as one exception-handling family, not as many independent bugs.
