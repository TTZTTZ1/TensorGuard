# tf.keras.metrics.logcosh

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/logcosh](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/logcosh)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L1381-L1425) |

Logarithm of the hyperbolic cosine of the prediction error.

#### View aliases

**Main aliases**

[`tf.keras.metrics.logcosh`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/logcosh)

```
tf.keras.losses.logcosh(
    y_true, y_pred
)
```

#### Formula:

```
loss = mean(log(cosh(y_pred - y_true)), axis=-1)
```

Note that `log(cosh(x))` is approximately equal to `(x ** 2) / 2` for small
`x` and to `abs(x) - log(2)` for large `x`. This means that 'logcosh' works
mostly like the mean squared error, but will not be so strongly affected by
the occasional wildly incorrect prediction.

#### Example:

```
>>> y_true = [[0., 1.], [0., 0.]]
>>> y_pred = [[1., 1.], [0., 0.]]
>>> loss = keras.losses.log_cosh(y_true, y_pred)
0.108
```

| Args | |

|  |  |
| --- | --- |
| `y_true` | Ground truth values with shape = `[batch_size, d0, .. dN]`. |
| `y_pred` | The predicted values with shape = `[batch_size, d0, .. dN]`. |

| Returns | |
| Logcosh error values with shape = `[batch_size, d0, .. dN-1]`. | |