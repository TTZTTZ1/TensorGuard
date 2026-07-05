# tf.math.atan

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/atan](https://tensorflow.google.cn/api_docs/python/tf/math/atan)

---

Computes the trignometric inverse tangent of x element-wise.

#### View aliases

**Main aliases**

[`tf.atan`](https://tensorflow.google.cn/api_docs/python/tf/math/atan)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.atan`](https://tensorflow.google.cn/api_docs/python/tf/math/atan)

```
tf.math.atan(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

The [`tf.math.atan`](https://tensorflow.google.cn/api_docs/python/tf/math/atan) operation returns the inverse of [`tf.math.tan`](https://tensorflow.google.cn/api_docs/python/tf/math/tan), such that
if `y = tf.math.tan(x)` then, `x = tf.math.atan(y)`.

**Note:** The output of [`tf.math.atan`](https://tensorflow.google.cn/api_docs/python/tf/math/atan) will lie within the invertible range
of tan, i.e (-pi/2, pi/2).

#### For example:

```
# Note: [1.047, 0.785] ~= [(pi/3), (pi/4)]
x = tf.constant([1.047, 0.785])
y = tf.math.tan(x) # [1.731261, 0.99920404]

tf.math.atan(y) # [1.047, 0.785] = x
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |