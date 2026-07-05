# tf.keras.metrics.categorical_crossentropy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/categorical_crossentropy](https://tensorflow.google.cn/api_docs/python/tf/keras/metrics/categorical_crossentropy)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L1518-L1578) |

Computes the categorical crossentropy loss.

#### View aliases

**Main aliases**

[`tf.keras.metrics.categorical_crossentropy`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/categorical_crossentropy)

```
tf.keras.losses.categorical_crossentropy(
    y_true, y_pred, from_logits=False, label_smoothing=0.0, axis=-1
)
```

| Args | |

|  |  |
| --- | --- |
| `y_true` | Tensor of one-hot true targets. |
| `y_pred` | Tensor of predicted targets. |
| `from_logits` | Whether `y_pred` is expected to be a logits tensor. By default, we assume that `y_pred` encodes a probability distribution. |
| `label_smoothing` | Float in [0, 1]. If > `0` then smooth the labels. For example, if `0.1`, use `0.1 / num_classes` for non-target labels and `0.9 + 0.1 / num_classes` for target labels. |
| `axis` | Defaults to `-1`. The dimension along which the entropy is computed. |

| Returns | |
| Categorical crossentropy loss value. | |

#### Example:

```
>>> y_true = [[0, 1, 0], [0, 0, 1]]
>>> y_pred = [[0.05, 0.95, 0], [0.1, 0.8, 0.1]]
>>> loss = keras.losses.categorical_crossentropy(y_true, y_pred)
>>> assert loss.shape == (2,)
>>> loss
array([0.0513, 2.303], dtype=float32)
```