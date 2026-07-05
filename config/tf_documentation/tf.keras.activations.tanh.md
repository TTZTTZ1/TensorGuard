# tf.keras.activations.tanh

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/activations/tanh](https://tensorflow.google.cn/api_docs/python/tf/keras/activations/tanh)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/activations/activations.py#L303-L314) |

Hyperbolic tangent activation function.

```
tf.keras.activations.tanh(
    x
)
```

#### It is defined as:

`tanh(x) = sinh(x) / cosh(x)`, i.e.
`tanh(x) = ((exp(x) - exp(-x)) / (exp(x) + exp(-x)))`.

| Args | |

|  |  |
| --- | --- |
| `x` | Input tensor. |