# tf.keras.losses.MSE

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MSE](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MSE)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L1122-L1158) |

Computes the mean squared error between labels and predictions.

#### View aliases

**Main aliases**

[`tf.keras.losses.mse`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MSE), [`tf.keras.metrics.MSE`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MSE), [`tf.keras.metrics.mse`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MSE)

```
tf.keras.losses.MSE(
    y_true, y_pred
)
```

#### Formula:

```
loss = mean(square(y_true - y_pred), axis=-1)
```

#### Example:

```
>>> y_true = np.random.randint(0, 2, size=(2, 3))
>>> y_pred = np.random.random(size=(2, 3))
>>> loss = keras.losses.mean_squared_error(y_true, y_pred)
```

| Args | |

|  |  |
| --- | --- |
| `y_true` | Ground truth values with shape = `[batch_size, d0, .. dN]`. |
| `y_pred` | The predicted values with shape = `[batch_size, d0, .. dN]`. |

| Returns | |
| Mean squared error values with shape = `[batch_size, d0, .. dN-1]`. | |