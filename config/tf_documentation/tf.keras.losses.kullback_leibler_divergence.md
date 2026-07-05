# tf.keras.losses.kullback_leibler_divergence

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/kullback_leibler_divergence](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/kullback_leibler_divergence)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L1428-L1476) |

Computes Kullback-Leibler divergence loss between `y_true` & `y_pred`.

#### View aliases

**Main aliases**

[`tf.keras.losses.kld`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/KLD), [`tf.keras.losses.kullback_leibler_divergence`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/KLD), [`tf.keras.metrics.KLD`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/KLD), [`tf.keras.metrics.kld`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/KLD), [`tf.keras.metrics.kullback_leibler_divergence`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/KLD)

```
tf.keras.losses.KLD(
    y_true, y_pred
)
```

#### Formula:

```
loss = y_true * log(y_true / y_pred)
```

`y_true` and `y_pred` are expected to be probability
distributions, with values between 0 and 1. They will get
clipped to the `[0, 1]` range.

| Args | |

|  |  |
| --- | --- |
| `y_true` | Tensor of true targets. |
| `y_pred` | Tensor of predicted targets. |

| Returns | |
| KL Divergence loss values with shape = `[batch_size, d0, .. dN-1]`. | |

#### Example:

```
>>> y_true = np.random.randint(0, 2, size=(2, 3)).astype(np.float32)
>>> y_pred = np.random.random(size=(2, 3))
>>> loss = keras.losses.kl_divergence(y_true, y_pred)
>>> assert loss.shape == (2,)
>>> y_true = ops.clip(y_true, 1e-7, 1)
>>> y_pred = ops.clip(y_pred, 1e-7, 1)
>>> assert np.array_equal(
...     loss, np.sum(y_true * np.log(y_true / y_pred), axis=-1))
```