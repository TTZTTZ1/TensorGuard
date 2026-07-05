# tf.keras.activations.hard_sigmoid

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/activations/hard_sigmoid](https://tensorflow.google.cn/api_docs/python/tf/keras/activations/hard_sigmoid)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/activations/activations.py#L354-L374) |

Hard sigmoid activation function.

```
tf.keras.activations.hard_sigmoid(
    x
)
```

The hard sigmoid activation is defined as:

* `0` if `if x <= -3`
* `1` if `x >= 3`
* `(x/6) + 0.5` if `-3 < x < 3`

It's a faster, piecewise linear approximation
of the sigmoid activation.

| Args | |

|  |  |
| --- | --- |
| `x` | Input tensor. |

#### Reference:

* [Wikipedia "Hard sigmoid"](https://en.wikipedia.org/wiki/Hard_sigmoid)