# tf.raw_ops.BatchSvd

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BatchSvd](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BatchSvd)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.BatchSvd`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BatchSvd)

```
tf.raw_ops.BatchSvd(
    input, compute_uv=True, full_matrices=False, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `float64`, `float32`, `complex64`, `complex128`. |
| `compute_uv` | An optional `bool`. Defaults to `True`. |
| `full_matrices` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (s, u, v). | |
| `s` | A `Tensor`. Has the same type as `input`. |
| `u` | A `Tensor`. Has the same type as `input`. |
| `v` | A `Tensor`. Has the same type as `input`. |