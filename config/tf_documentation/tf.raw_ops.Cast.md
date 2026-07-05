# tf.raw_ops.Cast

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Cast](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Cast)

---

Cast x of type SrcT to y of DstT.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Cast`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Cast)

```
tf.raw_ops.Cast(
    x, DstT, Truncate=False, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. |
| `DstT` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `Truncate` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `DstT`. | |