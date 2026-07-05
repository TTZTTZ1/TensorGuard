# tf.math.asinh

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/asinh](https://tensorflow.google.cn/api_docs/python/tf/math/asinh)

---

Computes inverse hyperbolic sine of x element-wise.

#### View aliases

**Main aliases**

[`tf.asinh`](https://tensorflow.google.cn/api_docs/python/tf/math/asinh)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.asinh`](https://tensorflow.google.cn/api_docs/python/tf/math/asinh)

```
tf.math.asinh(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

Given an input tensor, this function computes inverse hyperbolic sine
for every element in the tensor. Both input and output has a range of
`[-inf, inf]`.

```
  x = tf.constant([-float("inf"), -2, -0.5, 1, 1.2, 200, 10000, float("inf")])
  tf.math.asinh(x) ==> [-inf -1.4436355 -0.4812118 0.8813736 1.0159732 5.991471 9.903487 inf]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |