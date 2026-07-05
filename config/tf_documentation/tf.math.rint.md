# tf.math.rint

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/rint](https://tensorflow.google.cn/api_docs/python/tf/math/rint)

---

Returns element-wise integer closest to x.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.rint`](https://tensorflow.google.cn/api_docs/python/tf/math/rint)

```
tf.math.rint(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

If the result is midway between two representable values,
the even representable is chosen.

#### Example:

```
rint(-1.5) ==> -2.0
rint(0.5000001) ==> 1.0
rint([4.5, 0.5]) ==> [4., 0.]
rint([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0]) ==> [-2., -2., -0., 0., 2., 2., 2.]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |