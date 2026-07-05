# tf.raw_ops.Iterator

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Iterator](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Iterator)

---

A container for an iterator resource.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Iterator`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Iterator)

```
tf.raw_ops.Iterator(
    shared_name, container, output_types, output_shapes, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `shared_name` | A `string`. |
| `container` | A `string`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `resource`. | |