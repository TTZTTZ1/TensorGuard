# tf.keras.losses.categorical_hinge

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/categorical_hinge](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/categorical_hinge)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L1081-L1119) |

Computes the categorical hinge loss between `y_true` & `y_pred`.

#### View aliases

**Main aliases**

[`tf.keras.metrics.categorical_hinge`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/categorical_hinge)

```
tf.keras.losses.categorical_hinge(
    y_true, y_pred
)
```

#### Formula:

```
loss = maximum(neg - pos + 1, 0)
```

where `neg=maximum((1-y_true)*y_pred)` and `pos=sum(y_true*y_pred)`

| Args | |

|  |  |
| --- | --- |
| `y_true` | The ground truth values. `y_true` values are expected to be either `{-1, +1}` or `{0, 1}` (i.e. a one-hot-encoded tensor) with shape = `[batch_size, d0, .. dN]`. |
| `y_pred` | The predicted values with shape = `[batch_size, d0, .. dN]`. |

| Returns | |
| Categorical hinge loss values with shape = `[batch_size, d0, .. dN-1]`. | |

#### Example:

```
>>> y_true = np.random.randint(0, 3, size=(2,))
>>> y_true = np.eye(np.max(y_true) + 1)[y_true]
>>> y_pred = np.random.random(size=(2, 3))
>>> loss = keras.losses.categorical_hinge(y_true, y_pred)
```