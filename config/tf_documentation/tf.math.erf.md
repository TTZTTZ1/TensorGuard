# tf.math.erf

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/erf](https://tensorflow.google.cn/api_docs/python/tf/math/erf)

---

Computes the [Gauss error function](https://en.wikipedia.org/wiki/Error_function) of `x` element-wise. In statistics, for non-negative values of \(x\), the error function has the following interpretation: for a random variable \(Y\) that is normally distributed with mean 0 and variance \(1/\sqrt{2}\), \(erf(x)\) is the probability that \(Y\) falls in the range \([−x, x]\).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.erf`](https://tensorflow.google.cn/api_docs/python/tf/math/erf)

```
tf.math.erf(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

#### For example:

```
>>> tf.math.erf([[1.0, 2.0, 3.0], [0.0, -1.0, -2.0]])
<tf.Tensor: shape=(2, 3), dtype=float32, numpy=
array([[ 0.8427007,  0.9953223,  0.999978 ],
       [ 0.       , -0.8427007, -0.9953223]], dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.erf(x.values, ...), x.dense_shape)`