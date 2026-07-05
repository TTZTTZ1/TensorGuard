# tf.raw_ops.WindowOp

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/WindowOp](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/WindowOp)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.WindowOp`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/WindowOp)

```
tf.raw_ops.WindowOp(
    inputs, output_types, output_shapes, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `inputs` | A list of `Tensor` objects. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |