# tf.raw_ops.MultiDeviceIteratorFromStringHandle

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MultiDeviceIteratorFromStringHandle](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MultiDeviceIteratorFromStringHandle)

---

Generates a MultiDeviceIterator resource from its provided string handle.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.MultiDeviceIteratorFromStringHandle`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MultiDeviceIteratorFromStringHandle)

```
tf.raw_ops.MultiDeviceIteratorFromStringHandle(
    string_handle, output_types=[], output_shapes=[], name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `string_handle` | A `Tensor` of type `string`. String representing the resource. |
| `output_types` | An optional list of `tf.DTypes`. Defaults to `[]`. The type list for the return values. |
| `output_shapes` | An optional list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`). Defaults to `[]`. The list of shapes being produced. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `resource`. | |