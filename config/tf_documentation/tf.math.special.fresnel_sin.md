# tf.math.special.fresnel_sin

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/special/fresnel_sin](https://tensorflow.google.cn/api_docs/python/tf/math/special/fresnel_sin)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/special_math_ops.py#L193-L220) |

Computes Fresnel's sine integral of `x` element-wise.

```
tf.math.special.fresnel_sin(
    x, name=None
)
```

The Fresnel sine integral is defined as the integral of `sin(t^2)` from
`0` to `x`, with the domain of definition all real numbers.

```
>>> tf.math.special.fresnel_sin([-1., -0.1, 0.1, 1.]).numpy()
array([-0.43825912, -0.00052359,  0.00052359,  0.43825912], dtype=float32)
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

Equivalent to scipy.special.fresnel first output.