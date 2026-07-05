# tf.keras.losses.MAPE

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MAPE](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MAPE)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L1198-L1241) |

Computes the mean absolute percentage error between `y_true` & `y_pred`.

#### View aliases

**Main aliases**

[`tf.keras.losses.mape`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MAPE), [`tf.keras.metrics.MAPE`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MAPE), [`tf.keras.metrics.mape`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MAPE)

```
tf.keras.losses.MAPE(
    y_true, y_pred
)
```

#### Formula:

```
loss = 100 * mean(abs((y_true - y_pred) / y_true), axis=-1)
```

Division by zero is prevented by dividing by `maximum(y_true, epsilon)`
where `epsilon = keras.backend.epsilon()`
(default to `1e-7`).

| Args | |

|  |  |
| --- | --- |
| `y_true` | Ground truth values with shape = `[batch_size, d0, .. dN]`. |
| `y_pred` | The predicted values with shape = `[batch_size, d0, .. dN]`. |

| Returns | |
| Mean absolute percentage error values with shape = `[batch_size, d0, .. dN-1]`. | |

#### Example:

```
>>> y_true = np.random.random(size=(2, 3))
>>> y_pred = np.random.random(size=(2, 3))
>>> loss = keras.losses.mean_absolute_percentage_error(y_true, y_pred)
```