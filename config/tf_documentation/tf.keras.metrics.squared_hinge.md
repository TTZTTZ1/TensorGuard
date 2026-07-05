# tf.keras.metrics.squared_hinge

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/squared_hinge](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/squared_hinge)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L1043-L1078) |

Computes the squared hinge loss between `y_true` & `y_pred`.

#### View aliases

**Main aliases**

[`tf.keras.metrics.squared_hinge`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/squared_hinge)

```
tf.keras.losses.squared_hinge(
    y_true, y_pred
)
```

#### Formula:

```
loss = mean(square(maximum(1 - y_true * y_pred, 0)), axis=-1)
```

| Args | |

|  |  |
| --- | --- |
| `y_true` | The ground truth values. `y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are provided we will convert them to -1 or 1 with shape = `[batch_size, d0, .. dN]`. |
| `y_pred` | The predicted values with shape = `[batch_size, d0, .. dN]`. |

| Returns | |
| Squared hinge loss values with shape = `[batch_size, d0, .. dN-1]`. | |

#### Example:

```
>>> y_true = np.random.choice([-1, 1], size=(2, 3))
>>> y_pred = np.random.random(size=(2, 3))
>>> loss = keras.losses.squared_hinge(y_true, y_pred)
```