# tf.math.negative

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/negative](https://tensorflow.google.cn/api_docs/python/tf/math/negative)

---

Computes numerical negative value element-wise.

#### View aliases

**Main aliases**

[`tf.negative`](https://tensorflow.google.cn/api_docs/python/tf/math/negative)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.negative`](https://tensorflow.google.cn/api_docs/python/tf/math/negative)

```
tf.math.negative(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

I.e., \(y = -x\).

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.negative(x.values, ...), x.dense_shape)`