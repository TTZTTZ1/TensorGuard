# tf.keras.losses.sparse_categorical_crossentropy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/sparse_categorical_crossentropy](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/sparse_categorical_crossentropy)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L1677-L1738) |

Computes the sparse categorical crossentropy loss.

#### View aliases

**Main aliases**

[`tf.keras.metrics.sparse_categorical_crossentropy`](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/sparse_categorical_crossentropy)

```
tf.keras.losses.sparse_categorical_crossentropy(
    y_true, y_pred, from_logits=False, ignore_class=None, axis=-1
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Use TPUs](https://tensorflow.google.cn/guide/tpu) | * [Using DTensors with Keras](https://tensorflow.google.cn/tutorials/distribute/dtensor_keras_tutorial) * [Introduction to the TensorFlow Models NLP library](https://tensorflow.google.cn/tfmodels/nlp/index) |

| Args | |

|  |  |
| --- | --- |
| `y_true` | Ground truth values. |
| `y_pred` | The predicted values. |
| `from_logits` | Whether `y_pred` is expected to be a logits tensor. By default, we assume that `y_pred` encodes a probability distribution. |
| `ignore_class` | Optional integer. The ID of a class to be ignored during loss computation. This is useful, for example, in segmentation problems featuring a "void" class (commonly -1 or 255) in segmentation maps. By default (`ignore_class=None`), all classes are considered. |
| `axis` | Defaults to `-1`. The dimension along which the entropy is computed. |

| Returns | |
| Sparse categorical crossentropy loss value. | |

#### Examples:

```
>>> y_true = [1, 2]
>>> y_pred = [[0.05, 0.95, 0], [0.1, 0.8, 0.1]]
>>> loss = keras.losses.sparse_categorical_crossentropy(y_true, y_pred)
>>> assert loss.shape == (2,)
>>> loss
array([0.0513, 2.303], dtype=float32)
```