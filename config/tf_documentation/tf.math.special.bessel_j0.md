# tf.math.special.bessel_j0

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/special/bessel_j0](https://tensorflow.google.cn/api_docs/python/tf/math/special/bessel_j0)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/special_math_ops.py#L477-L501) |

Computes the Bessel j0 function of `x` element-wise.

```
tf.math.special.bessel_j0(
    x, name=None
)
```

Modified Bessel function of order 0.

```
>>> tf.math.special.bessel_j0([0.5, 1., 2., 4.]).numpy()
array([ 0.93846981,  0.76519769,  0.22389078, -0.39714981], dtype=float32)
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor` or `SparseTensor`. Must be one of the following types: `half`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`. | |

## scipy compatibility

Equivalent to scipy.special.j0