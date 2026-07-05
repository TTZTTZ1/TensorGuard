# tf.math.tan

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/tan](https://tensorflow.google.cn/api_docs/python/tf/math/tan)

---

Computes tan of x element-wise.

#### View aliases

**Main aliases**

[`tf.tan`](https://tensorflow.google.cn/api_docs/python/tf/math/tan)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.tan`](https://tensorflow.google.cn/api_docs/python/tf/math/tan)

```
tf.math.tan(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

Given an input tensor, this function computes tangent of every
element in the tensor. Input range is `(-inf, inf)` and
output range is `(-inf, inf)`. If input lies outside the boundary, `nan`
is returned.

```
  x = tf.constant([-float("inf"), -9, -0.5, 1, 1.2, 200, 10000, float("inf")])
  tf.math.tan(x) ==> [nan 0.45231566 -0.5463025 1.5574077 2.572152 -1.7925274 0.32097113 nan]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |