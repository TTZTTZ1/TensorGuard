# tf.raw_ops.IteratorFromStringHandleV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IteratorFromStringHandleV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IteratorFromStringHandleV2)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.IteratorFromStringHandleV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IteratorFromStringHandleV2)

```
tf.raw_ops.IteratorFromStringHandleV2(
    string_handle, output_types=[], output_shapes=[], name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `string_handle` | A `Tensor` of type `string`. |
| `output_types` | An optional list of `tf.DTypes`. Defaults to `[]`. |
| `output_shapes` | An optional list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`). Defaults to `[]`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `resource`. | |