# tf.raw_ops.ShapeN

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShapeN](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShapeN)

---

Returns shape of tensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ShapeN`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShapeN)

```
tf.raw_ops.ShapeN(
    input,
    out_type=tf.dtypes.int32,
    name=None
)

tf.dtypes.int32
```

This operation returns N 1-D integer tensors representing shape of `input[i]s`.

| Args | |

|  |  |
| --- | --- |
| `input` | A list of at least 1 `Tensor` objects with the same type. |
| `out_type` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.int32, tf.int64`. Defaults to [`tf.int32`](https://tensorflow.google.cn/api_docs/python/tf#int32). |
| `name` | A name for the operation (optional). |

| Returns | |
| A list with the same length as `input` of `Tensor` objects with type `out_type`. | |