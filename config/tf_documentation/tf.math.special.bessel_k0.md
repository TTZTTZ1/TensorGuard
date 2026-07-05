# tf.math.special.bessel_k0

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/special/bessel_k0](https://tensorflow.google.cn/api_docs/python/tf/math/special/bessel_k0)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/special_math_ops.py#L365-L391) |

Computes the Bessel k0 function of `x` element-wise.

```
tf.math.special.bessel_k0(
    x, name=None
)
```

Modified Bessel function of order 0.

It is preferable to use the numerically stabler function `k0e(x)` instead.

```
>>> tf.math.special.bessel_k0([0.5, 1., 2., 4.]).numpy()
array([0.92441907, 0.42102444, 0.11389387, 0.01115968], dtype=float32)
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor` or `SparseTensor`. Must be one of the following types: `half`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`. | |

## scipy compatibility

Equivalent to scipy.special.k0