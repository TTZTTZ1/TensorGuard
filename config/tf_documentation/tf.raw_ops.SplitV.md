# tf.raw_ops.SplitV

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SplitV](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SplitV)

---

Splits a tensor into `num_split` tensors along one dimension.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SplitV`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SplitV)

```
tf.raw_ops.SplitV(
    value, size_splits, axis, num_split, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `value` | A `Tensor`. The tensor to split. |
| `size_splits` | A `Tensor`. Must be one of the following types: `int8`, `int32`, `int64`. list containing the sizes of each output tensor along the split dimension. Must sum to the dimension of value along split\_dim. Can contain one -1 indicating that dimension is to be inferred. |
| `axis` | A `Tensor` of type `int32`. 0-D. The dimension along which to split. Must be in the range `[-rank(value), rank(value))`. |
| `num_split` | An `int` that is `>= 1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `num_split` `Tensor` objects with the same type as `value`. | |