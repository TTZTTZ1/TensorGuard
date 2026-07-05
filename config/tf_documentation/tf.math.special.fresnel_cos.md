# tf.math.special.fresnel_cos

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/special/fresnel_cos](https://tensorflow.google.cn/api_docs/python/tf/math/special/fresnel_cos)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/special_math_ops.py#L162-L190) |

Computes Fresnel's cosine integral of `x` element-wise.

```
tf.math.special.fresnel_cos(
    x, name=None
)
```

The Fresnel cosine integral is defined as the integral of `cos(t^2)` from
`0` to `x`, with the domain of definition all real numbers.

The Fresnel cosine integral is odd.

```
>>> tf.math.special.fresnel_cos([-1., -0.1, 0.1, 1.]).numpy()
array([-0.7798934 , -0.09999753,  0.09999753,  0.7798934 ], dtype=float32)
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

Equivalent to scipy.special.fresnel second output.