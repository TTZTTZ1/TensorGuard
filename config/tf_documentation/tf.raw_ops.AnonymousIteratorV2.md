# tf.raw_ops.AnonymousIteratorV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AnonymousIteratorV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AnonymousIteratorV2)

---

A container for an iterator resource.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.AnonymousIteratorV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AnonymousIteratorV2)

```
tf.raw_ops.AnonymousIteratorV2(
    output_types, output_shapes, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (handle, deleter). | |
| `handle` | A `Tensor` of type `resource`. |
| `deleter` | A `Tensor` of type `variant`. |