# tf.raw_ops.OutfeedDequeueV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OutfeedDequeueV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OutfeedDequeueV2)

---

Retrieves a single tensor from the computation outfeed.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.OutfeedDequeueV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OutfeedDequeueV2)

```
tf.raw_ops.OutfeedDequeueV2(
    device_ordinal, dtype, shape, name=None
)
```

Device ordinal is a
tensor allowing dynamic outfeed.

This operation will block indefinitely until data is available.

Args:
device\_ordinal: A `Tensor` of type `int32`.
An int scalar tensor, representing the TPU device to use. This should be -1 when
the Op is running on a TPU device, and >= 0 when the Op is running on the CPU
device.
dtype: A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). The type of elements in the tensor.
shape: A [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. The shape of the tensor.
name: A name for the operation (optional).

Returns:
A `Tensor` of type `dtype`.