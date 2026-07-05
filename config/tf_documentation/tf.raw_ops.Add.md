# tf.raw_ops.Add

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Add](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Add)

---

Returns x + y element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Add`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Add)

```
tf.raw_ops.Add(
    x, y, name=None
)
```

**Note:** `Add` supports broadcasting. `AddN` does not. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

Given two input tensors, the [`tf.add`](https://tensorflow.google.cn/api_docs/python/tf/math/add) operation computes the sum for every element in the tensor.

Both input and output have a range `(-inf, inf)`.

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`, `string`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |