# tf.keras.activations.softmax

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/activations/softmax](https://tensorflow.google.cn/api_docs/python/tf/keras/activations/softmax)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/activations/activations.py#L135-L165) |

Softmax converts a vector of values to a probability distribution.

```
tf.keras.activations.softmax(
    x, axis=-1
)
```

The elements of the output vector are in range `[0, 1]` and sum to 1.

Each input vector is handled independently.
The `axis` argument sets which axis of the input the function
is applied along.

Softmax is often used as the activation for the last
layer of a classification network because the result could be interpreted as
a probability distribution.

The softmax of each vector x is computed as
`exp(x) / sum(exp(x))`.

The input values in are the log-odds of the resulting probability.

| Args | |

|  |  |
| --- | --- |
| `x` | Input tensor. |
| `axis` | Integer, axis along which the softmax is applied. |