# tf.math.special.bessel_j1

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/special/bessel_j1](https://tensorflow.google.cn/api_docs/python/tf/math/special/bessel_j1)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/special_math_ops.py#L504-L528) |

Computes the Bessel j1 function of `x` element-wise.

```
tf.math.special.bessel_j1(
    x, name=None
)
```

Modified Bessel function of order 1.

```
>>> tf.math.special.bessel_j1([0.5, 1., 2., 4.]).numpy()
array([ 0.24226846,  0.44005059,  0.57672481, -0.06604333], dtype=float32)
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor` or `SparseTensor`. Must be one of the following types: `half`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`. | |

## scipy compatibility

Equivalent to scipy.special.j1