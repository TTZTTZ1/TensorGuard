# tf.keras.losses.CategoricalCrossentropy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/CategoricalCrossentropy](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/CategoricalCrossentropy)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L673-L760) |

Computes the crossentropy loss between the labels and predictions.

Inherits From: [`Loss`](https://tensorflow.google.cn/api_docs/python/tf/keras/Loss)

```
tf.keras.losses.CategoricalCrossentropy(
    from_logits=False,
    label_smoothing=0.0,
    axis=-1,
    reduction='sum_over_batch_size',
    name='categorical_crossentropy'
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Effective Tensorflow 2](https://tensorflow.google.cn/guide/effective_tf2) * [Debug a TensorFlow 2 migrated training pipeline](https://tensorflow.google.cn/guide/migrate/migration_debugging) | * [Adversarial example using FGSM](https://tensorflow.google.cn/tutorials/generative/adversarial_fgsm) * [Retraining an Image Classifier](https://tensorflow.google.cn/hub/tutorials/tf2_image_retraining) * [Implement Differential Privacy with TensorFlow Privacy](https://tensorflow.google.cn/responsible_ai/privacy/tutorials/classification_privacy) * [Assess privacy risks with the TensorFlow Privacy Report](https://tensorflow.google.cn/responsible_ai/privacy/tutorials/privacy_report) * [On-Device Training with TensorFlow Lite](https://tensorflow.google.cn/lite/examples/on_device_training/overview) |

Use this crossentropy loss function when there are two or more label
classes. We expect labels to be provided in a `one_hot` representation. If
you want to provide labels as integers, please use
`SparseCategoricalCrossentropy` loss. There should be `num_classes` floating
point values per feature, i.e., the shape of both `y_pred` and `y_true` are
`[batch_size, num_classes]`.

| Args | |

|  |  |
| --- | --- |
| `from_logits` | Whether `y_pred` is expected to be a logits tensor. By default, we assume that `y_pred` encodes a probability distribution. |
| `label_smoothing` | Float in [0, 1]. When > 0, label values are smoothed, meaning the confidence on label values are relaxed. For example, if `0.1`, use `0.1 / num_classes` for non-target labels and `0.9 + 0.1 / num_classes` for target labels. |
| `axis` | The axis along which to compute crossentropy (the features axis). Defaults to `-1`. |
| `reduction` | Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"` or `None`. |
| `name` | Optional name for the loss instance. |

#### Examples:

#### Standalone usage:

```
>>> y_true = [[0, 1, 0], [0, 0, 1]]
>>> y_pred = [[0.05, 0.95, 0], [0.1, 0.8, 0.1]]
>>> # Using 'auto'/'sum_over_batch_size' reduction type.
>>> cce = keras.losses.CategoricalCrossentropy()
>>> cce(y_true, y_pred)
1.177
```

```
>>> # Calling with 'sample_weight'.
>>> cce(y_true, y_pred, sample_weight=np.array([0.3, 0.7]))
0.814
```

```
>>> # Using 'sum' reduction type.
>>> cce = keras.losses.CategoricalCrossentropy(
...     reduction="sum")
>>> cce(y_true, y_pred)
2.354
```

```
>>> # Using 'none' reduction type.
>>> cce = keras.losses.CategoricalCrossentropy(
...     reduction=None)
>>> cce(y_true, y_pred)
array([0.0513, 2.303], dtype=float32)
```

Usage with the `compile()` API:

```
model.compile(optimizer='sgd',
              loss=keras.losses.CategoricalCrossentropy())
```

## Methods

### `call`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L20-L22)

```
call(
    y_true, y_pred
)
```

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L30-L34)

```
@classmethod
from_config(
    config
)
```

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L753-L760)

```
get_config()
```

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/loss.py#L32-L61)

```
__call__(
    y_true, y_pred, sample_weight=None
)
```

Call self as a function.