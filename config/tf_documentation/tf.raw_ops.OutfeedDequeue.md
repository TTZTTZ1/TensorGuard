# tf.raw_ops.OutfeedDequeue

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OutfeedDequeue](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OutfeedDequeue)

---

Retrieves a single tensor from the computation outfeed.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.OutfeedDequeue`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OutfeedDequeue)

```
tf.raw_ops.OutfeedDequeue(
    dtype, shape, device_ordinal=-1, name=None
)
```

This operation will block indefinitely until data is available.

| Args | |

|  |  |
| --- | --- |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). The type of elements in the tensor. |
| `shape` | A [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. The shape of the tensor. |
| `device_ordinal` | An optional `int`. Defaults to `-1`. The TPU device to use. This should be -1 when the Op is running on a TPU device, and >= 0 when the Op is running on the CPU device. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |