# tf.raw_ops.OutfeedDequeueTupleV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OutfeedDequeueTupleV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OutfeedDequeueTupleV2)

---

Retrieve multiple values from the computation outfeed.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.OutfeedDequeueTupleV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OutfeedDequeueTupleV2)

```
tf.raw_ops.OutfeedDequeueTupleV2(
    device_ordinal, dtypes, shapes, name=None
)
```

Device ordinal is a
tensor allowing dynamic outfeed.

This operation will block indefinitely until data is available. Output `i`
corresponds to XLA tuple element `i`.

Args:
device\_ordinal: A `Tensor` of type `int32`.
An int scalar tensor, representing the TPU device to use. This should be -1 when
the Op is running on a TPU device, and >= 0 when the Op is running on the CPU
device.
dtypes: A list of `tf.DTypes` that has length `>= 1`.
The element types of each element in `outputs`.
shapes: A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`).
The shapes of each tensor in `outputs`.
name: A name for the operation (optional).

Returns:
A list of `Tensor` objects of type `dtypes`.