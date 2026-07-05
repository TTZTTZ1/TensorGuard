# tf.raw_ops.IteratorGetNext

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IteratorGetNext](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IteratorGetNext)

---

Gets the next output from the given iterator .

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.IteratorGetNext`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IteratorGetNext)

```
tf.raw_ops.IteratorGetNext(
    iterator, output_types, output_shapes, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `iterator` | A `Tensor` of type `resource`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `Tensor` objects of type `output_types`. | |