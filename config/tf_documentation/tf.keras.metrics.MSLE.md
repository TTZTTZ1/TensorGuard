# tf.keras.metrics.MSLE

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/MSLE](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/MSLE)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L1244-L1288) |

Computes the mean squared logarithmic error between `y_true` & `y_pred`.

#### View aliases

**Main aliases**

[`tf.keras.losses.msle`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MSLE), [`tf.keras.metrics.MSLE`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MSLE), [`tf.keras.metrics.msle`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MSLE)

```
tf.keras.losses.MSLE(
    y_true, y_pred
)
```

#### Formula:

```
loss = mean(square(log(y_true + 1) - log(y_pred + 1)), axis=-1)
```

Note that `y_pred` and `y_true` cannot be less or equal to 0. Negative
values and 0 values will be replaced with [`keras.backend.epsilon()`](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/epsilon)
(default to `1e-7`).

| Args | |

|  |  |
| --- | --- |
| `y_true` | Ground truth values with shape = `[batch_size, d0, .. dN]`. |
| `y_pred` | The predicted values with shape = `[batch_size, d0, .. dN]`. |

| Returns | |
| Mean squared logarithmic error values with shape = `[batch_size, d0, .. dN-1]`. | |

#### Example:

```
>>> y_true = np.random.randint(0, 2, size=(2, 3))
>>> y_pred = np.random.random(size=(2, 3))
>>> loss = keras.losses.mean_squared_logarithmic_error(y_true, y_pred)
```