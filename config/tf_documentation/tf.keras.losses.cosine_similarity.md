# tf.keras.losses.cosine_similarity

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/cosine_similarity](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/cosine_similarity)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L1291-L1328) |

Computes the cosine similarity between labels and predictions.

```
tf.keras.losses.cosine_similarity(
    y_true, y_pred, axis=-1
)
```

#### Formula:

```
loss = -sum(l2_norm(y_true) * l2_norm(y_pred))
```

Note that it is a number between -1 and 1. When it is a negative number
between -1 and 0, 0 indicates orthogonality and values closer to -1
indicate greater similarity. This makes it usable as a loss function in a
setting where you try to maximize the proximity between predictions and
targets. If either `y_true` or `y_pred` is a zero vector, cosine
similarity will be 0 regardless of the proximity between predictions
and targets.

| Args | |

|  |  |
| --- | --- |
| `y_true` | Tensor of true targets. |
| `y_pred` | Tensor of predicted targets. |
| `axis` | Axis along which to determine similarity. Defaults to `-1`. |

| Returns | |
| Cosine similarity tensor. | |

#### Example:

```
>>> y_true = [[0., 1.], [1., 1.], [1., 1.]]
>>> y_pred = [[1., 0.], [1., 1.], [-1., -1.]]
>>> loss = keras.losses.cosine_similarity(y_true, y_pred, axis=-1)
[-0., -0.99999994, 0.99999994]
```