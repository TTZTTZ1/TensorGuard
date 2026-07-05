# PT-N1-002: `fractional_max_pool3d` CPU/CUDA Boundary Discrepancy

## Summary

`torch.nn.functional.fractional_max_pool3d` shows a backend discrepancy at a channel boundary. With `C=65535`, both CPU and CUDA succeed. With `C=65536`, CPU succeeds while CUDA fails with `CUDA error: invalid argument`.

This is currently the strongest PyTorch candidate because it is independent of the testing instrumentation and has a clear boundary condition.

## Environment

```text
PyTorch: 2.11.0+cu130
CUDA: 13.0
```

## Minimal Reproduction

```python
import sys
import torch
import torch.nn.functional as F

device = sys.argv[1] if len(sys.argv) > 1 else "cpu"

torch.manual_seed(420)
x = torch.randn(1, 65536, 4, 4, 4, device=device)

y = F.fractional_max_pool3d(
    x,
    kernel_size=(2, 2, 2),
    output_size=(1, 1, 1),
)

if device.startswith("cuda"):
    torch.cuda.synchronize()

print("ok")
print("y.shape:", tuple(y.shape))
```

## Expected Behavior

CPU and CUDA should either both accept the input or both reject it with a clear framework-level error.

## Observed Behavior

```text
C=65535 CPU:  success
C=65535 CUDA: success
C=65536 CPU:  success
C=65536 CUDA: CUDA error: invalid argument
```

## Triage Notes

- Not a Python syntax error.
- Not a generated-code `NameError`.
- Not an `out=` alias issue.
- Not a TF32 numeric tolerance issue.
- The boundary at `65536` suggests a CUDA backend launch/indexing limit or missing CUDA-side validation.

## Current Status

Strong candidate. Needs upstream maintainer confirmation before calling it a confirmed PyTorch bug.
