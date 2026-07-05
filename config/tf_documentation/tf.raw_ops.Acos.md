# tf.raw_ops.Acos

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Acos](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Acos)

---

Computes acos of x element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Acos`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Acos)

```
tf.raw_ops.Acos(
    x, name=None
)
```

Provided an input tensor, the [`tf.math.acos`](https://tensorflow.google.cn/api_docs/python/tf/math/acos) operation returns the inverse cosine of each element of the tensor. If `y = tf.math.cos(x)` then, `x = tf.math.acos(y)`.

Input range is `[-1, 1]` and the output has a range of `[0, pi]`.

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |