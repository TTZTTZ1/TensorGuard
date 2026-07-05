# tf.raw_ops.Empty

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Empty](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Empty)

---

Creates a tensor with the given shape.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Empty`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Empty)

```
tf.raw_ops.Empty(
    shape, dtype, init=False, name=None
)
```

This operation creates a tensor of `shape` and `dtype`.

Args:
shape: A `Tensor` of type `int32`.
1-D. Represents the shape of the output tensor.
dtype: A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType).
init: An optional `bool`. Defaults to `False`.
If True, initialize the returned tensor with the default value of dtype. Otherwise, the implementation is free not to initializethe tensor's content.
name: A name for the operation (optional).

Returns:
A `Tensor` of type `dtype`.