# tf.math.expm1

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/expm1](https://tensorflow.google.cn/api_docs/python/tf/math/expm1)

---

Computes `exp(x) - 1` element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.expm1`](https://tensorflow.google.cn/api_docs/python/tf/math/expm1)

```
tf.math.expm1(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

i.e. `exp(x) - 1` or `e^(x) - 1`, where `x` is the input tensor.
`e` denotes Euler's number and is approximately equal to 2.718281.

```
  x = tf.constant(2.0)
  tf.math.expm1(x) ==> 6.389056

  x = tf.constant([2.0, 8.0])
  tf.math.expm1(x) ==> array([6.389056, 2979.958], dtype=float32)

  x = tf.constant(1 + 1j)
  tf.math.expm1(x) ==> (0.46869393991588515+2.2873552871788423j)
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |