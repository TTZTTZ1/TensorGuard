# tf.keras.activations.gelu

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/activations/gelu](https://tensorflow.google.cn/api_docs/python/tf/keras/activations/gelu)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/activations/activations.py#L280-L300) |

Gaussian error linear unit (GELU) activation function.

```
tf.keras.activations.gelu(
    x, approximate=False
)
```

The Gaussian error linear unit (GELU) is defined as:

`gelu(x) = x * P(X <= x)` where `P(X) ~ N(0, 1)`,
i.e. `gelu(x) = 0.5 * x * (1 + erf(x / sqrt(2)))`.

GELU weights inputs by their value, rather than gating
inputs by their sign as in ReLU.

| Args | |

|  |  |
| --- | --- |
| `x` | Input tensor. |
| `approximate` | A `bool`, whether to enable approximation. |

#### Reference:

* [Hendrycks et al., 2016](https://arxiv.org/abs/1606.08415)