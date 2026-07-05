# tf.keras.activations.swish

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/activations/swish](https://tensorflow.google.cn/api_docs/python/tf/keras/activations/swish)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/activations/activations.py#L260-L277) |

Swish (or Silu) activation function.

#### View aliases

**Main aliases**

[`tf.keras.activations.swish`](https://tensorflow.google.cn/api_docs/python/tf/keras/activations/silu)

```
tf.keras.activations.silu(
    x
)
```

It is defined as: `swish(x) = x * sigmoid(x)`.

The Swish (or Silu) activation function is a smooth,
non-monotonic function that is unbounded above and
bounded below.

| Args | |

|  |  |
| --- | --- |
| `x` | Input tensor. |

#### Reference:

* [Ramachandran et al., 2017](https://arxiv.org/abs/1710.05941)