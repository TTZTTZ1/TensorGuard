# tf.nn.gelu

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/gelu](https://tensorflow.google.cn/api_docs/python/tf/nn/gelu)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_ops.py#L3702-L3753) |

Compute the Gaussian Error Linear Unit (GELU) activation function.

```
tf.nn.gelu(
    features, approximate=False, name=None
)
```

Gaussian error linear unit (GELU) computes
`x * P(X <= x)`, where `P(X) ~ N(0, 1)`.
The (GELU) nonlinearity weights inputs by their value, rather than gates
inputs by their sign as in ReLU.

#### For example:

```
>>> x = tf.constant([-3.0, -1.0, 0.0, 1.0, 3.0], dtype=tf.float32)
>>> y = tf.nn.gelu(x)
>>> y.numpy()
array([-0.00404951, -0.15865529,  0.        ,  0.8413447 ,  2.9959507 ],
    dtype=float32)
>>> y = tf.nn.gelu(x, approximate=True)
>>> y.numpy()
array([-0.00363752, -0.15880796,  0.        ,  0.841192  ,  2.9963627 ],
    dtype=float32)
```

| Args | |

|  |  |
| --- | --- |
| `features` | A `float Tensor` representing preactivation values. |
| `approximate` | An optional `bool`. Defaults to `False`. Whether to enable approximation. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` with the same type as `features`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if `features` is not a floating point `Tensor`. |

| References | |
| [Gaussian Error Linear Units (GELUs)](https://arxiv.org/abs/1606.08415). | |