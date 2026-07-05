# tf.raw_ops.AnonymousMultiDeviceIterator

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AnonymousMultiDeviceIterator](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AnonymousMultiDeviceIterator)

---

A container for a multi device iterator resource.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.AnonymousMultiDeviceIterator`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AnonymousMultiDeviceIterator)

```
tf.raw_ops.AnonymousMultiDeviceIterator(
    devices, output_types, output_shapes, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `devices` | A list of `strings` that has length `>= 1`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (handle, deleter). | |
| `handle` | A `Tensor` of type `resource`. |
| `deleter` | A `Tensor` of type `variant`. |