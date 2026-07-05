# tf.raw_ops.MultiDeviceIterator

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MultiDeviceIterator](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MultiDeviceIterator)

---

Creates a MultiDeviceIterator resource.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.MultiDeviceIterator`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MultiDeviceIterator)

```
tf.raw_ops.MultiDeviceIterator(
    devices, shared_name, container, output_types, output_shapes, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `devices` | A list of `strings` that has length `>= 1`. A list of devices the iterator works across. |
| `shared_name` | A `string`. If non-empty, this resource will be shared under the given name across multiple sessions. |
| `container` | A `string`. If non-empty, this resource is placed in the given container. Otherwise, a default container is used. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. The type list for the return values. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. The list of shapes being produced. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `resource`. | |