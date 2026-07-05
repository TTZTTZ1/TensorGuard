# tf.raw_ops.Copy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Copy](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Copy)

---

Copy a tensor from CPU-to-CPU or GPU-to-GPU.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Copy`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Copy)

```
tf.raw_ops.Copy(
    input, tensor_name='', debug_ops_spec=[], name=None
)
```

Performs CPU-to-CPU or GPU-to-GPU deep-copying of tensor, depending on the
device on which the tensor is allocated.
N.B.: If the all downstream attached debug ops are disabled given the current
gRPC gating status, the output will simply forward the input tensor without
deep-copying. See the documentation of Debug\* ops for more details.

Unlike the CopyHost Op, this op does not have HostMemory constraint on its
input or output.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Input tensor. |
| `tensor_name` | An optional `string`. Defaults to `""`. The name of the input tensor. |
| `debug_ops_spec` | An optional list of `strings`. Defaults to `[]`. A list of debug op spec (op, url, gated\_grpc) for attached debug ops. Each element of the list has the format ;;, wherein gated\_grpc is boolean represented as 0/1. E.g., "DebugIdentity;grpc://foo:3333;1", "DebugIdentity;file:///tmp/tfdbg\_1;0". |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |