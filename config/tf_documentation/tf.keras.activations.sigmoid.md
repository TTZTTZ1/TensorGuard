# tf.keras.activations.sigmoid

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/activations/sigmoid](https://tensorflow.google.cn/api_docs/python/tf/keras/activations/sigmoid)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/activations/activations.py#L317-L341) |

Sigmoid activation function.

```
tf.keras.activations.sigmoid(
    x
)
```

It is defined as: `sigmoid(x) = 1 / (1 + exp(-x))`.

For small values (<-5),
`sigmoid` returns a value close to zero, and for large values (>5)
the result of the function gets close to 1.

Sigmoid is equivalent to a 2-element softmax, where the second element is
assumed to be zero. The sigmoid function always returns a value between
0 and 1.

| Args | |

|  |  |
| --- | --- |
| `x` | Input tensor. |