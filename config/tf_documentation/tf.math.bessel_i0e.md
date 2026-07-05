# tf.math.bessel_i0e

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/bessel_i0e](https://tensorflow.google.cn/api_docs/python/tf/math/bessel_i0e)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/special_math_ops.py#L282-L306) |

Computes the Bessel i0e function of `x` element-wise.

#### View aliases

**Main aliases**

[`tf.math.special.bessel_i0e`](https://tensorflow.google.cn/api_docs/python/tf/math/bessel_i0e)

```
tf.math.bessel_i0e(
    x, name=None
)
```

Modified Bessel function of order 0.

```
>>> tf.math.special.bessel_i0e([-1., -0.5, 0.5, 1.]).numpy()
array([0.46575961, 0.64503527, 0.64503527, 0.46575961], dtype=float32)
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor` or `SparseTensor`. Must be one of the following types: `half`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`. | |

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.bessel_i0e(x.values, ...), x.dense_shape)`

## scipy compatibility

Equivalent to scipy.special.i0e