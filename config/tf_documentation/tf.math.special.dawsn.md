# tf.math.special.dawsn

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/special/dawsn](https://tensorflow.google.cn/api_docs/python/tf/math/special/dawsn)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/special_math_ops.py#L101-L129) |

Computes Dawson's integral of `x` element-wise.

```
tf.math.special.dawsn(
    x, name=None
)
```

Dawson's integral is defined as `exp(-x**2)` times the integral of
`exp(t**2)` from `0` to `x`, with the domain of definition all real numbers.

Dawson's function is odd.

```
>>> tf.math.special.dawsn([-1., -0.5, 0.5, 1.]).numpy()
array([-0.5380795, -0.4244364, 0.4244364,  0.5380795], dtype=float32)
```

This implementation is based off of the Cephes math library.

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor` or `SparseTensor`. Must be one of the following types: `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`. | |

## scipy compatibility

Equivalent to scipy.special.dawsn