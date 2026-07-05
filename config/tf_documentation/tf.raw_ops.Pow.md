# tf.raw_ops.Pow

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Pow](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Pow)

---

Computes the power of one value to another.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Pow`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Pow)

```
tf.raw_ops.Pow(
    x, y, name=None
)
```

Given a tensor `x` and a tensor `y`, this operation computes \(x^y\) for
corresponding elements in `x` and `y`. For example:

```
# tensor 'x' is [[2, 2]], [3, 3]]
# tensor 'y' is [[8, 16], [2, 3]]
tf.pow(x, y) ==> [[256, 65536], [9, 27]]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `float32`, `half`, `float64`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |