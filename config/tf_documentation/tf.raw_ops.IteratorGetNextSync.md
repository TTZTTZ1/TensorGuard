# tf.raw_ops.IteratorGetNextSync

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IteratorGetNextSync](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IteratorGetNextSync)

---

Gets the next output from the given iterator.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.IteratorGetNextSync`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IteratorGetNextSync)

```
tf.raw_ops.IteratorGetNextSync(
    iterator, output_types, output_shapes, name=None
)
```

This operation is a synchronous version IteratorGetNext. It should only be used
in situations where the iterator does not block the calling thread, or where
the calling thread is not a member of the thread pool used to execute parallel
operations (e.g. in eager mode).

| Args | |

|  |  |
| --- | --- |
| `iterator` | A `Tensor` of type `resource`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `Tensor` objects of type `output_types`. | |