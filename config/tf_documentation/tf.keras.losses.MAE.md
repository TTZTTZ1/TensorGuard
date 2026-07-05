# tf.keras.losses.MAE

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MAE](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MAE)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L1161-L1195) |

Computes the mean absolute error between labels and predictions.

#### View aliases

**Main aliases**

[`tf.keras.losses.mae`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MAE), [`tf.keras.metrics.MAE`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MAE), [`tf.keras.metrics.mae`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MAE)

```
tf.keras.losses.MAE(
    y_true, y_pred
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Intro to Autoencoders](https://tensorflow.google.cn/tutorials/generative/autoencoder) |

```
loss = mean(abs(y_true - y_pred), axis=-1)
```

| Args | |

|  |  |
| --- | --- |
| `y_true` | Ground truth values with shape = `[batch_size, d0, .. dN]`. |
| `y_pred` | The predicted values with shape = `[batch_size, d0, .. dN]`. |

| Returns | |
| Mean absolute error values with shape = `[batch_size, d0, .. dN-1]`. | |

#### Example:

```
>>> y_true = np.random.randint(0, 2, size=(2, 3))
>>> y_pred = np.random.random(size=(2, 3))
>>> loss = keras.losses.mean_absolute_error(y_true, y_pred)
```