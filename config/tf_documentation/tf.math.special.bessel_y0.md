# tf.math.special.bessel_y0

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/special/bessel_y0](https://tensorflow.google.cn/api_docs/python/tf/math/special/bessel_y0)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/special_math_ops.py#L531-L555) |

Computes the Bessel y0 function of `x` element-wise.

```
tf.math.special.bessel_y0(
    x, name=None
)
```

Modified Bessel function of order 0.

```
>>> tf.math.special.bessel_y0([0.5, 1., 2., 4.]).numpy()
array([-0.44451873,  0.08825696,  0.51037567, -0.01694074], dtype=float32)
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor` or `SparseTensor`. Must be one of the following types: `half`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`. | |

## scipy compatibility

Equivalent to scipy.special.y0