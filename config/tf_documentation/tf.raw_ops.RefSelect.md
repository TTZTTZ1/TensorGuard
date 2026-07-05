# tf.raw_ops.RefSelect

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RefSelect](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RefSelect)

---

Forwards the `index`th element of `inputs` to `output`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.RefSelect`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RefSelect)

```
tf.raw_ops.RefSelect(
    index, inputs, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `index` | A `Tensor` of type `int32`. A scalar that determines the input that gets selected. |
| `inputs` | A list of at least 1 mutable `Tensor` objects with the same type. A list of ref tensors, one of which will be forwarded to `output`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A mutable `Tensor`. Has the same type as `inputs`. | |