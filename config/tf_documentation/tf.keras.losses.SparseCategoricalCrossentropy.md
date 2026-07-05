# tf.keras.losses.SparseCategoricalCrossentropy

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/SparseCategoricalCrossentropy](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/SparseCategoricalCrossentropy)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L903-L983) |

Computes the crossentropy loss between the labels and predictions.

Inherits From: [`Loss`](https://tensorflow.google.cn/api_docs/python/tf/keras/Loss)

```
tf.keras.losses.SparseCategoricalCrossentropy(
    from_logits=False,
    ignore_class=None,
    reduction='sum_over_batch_size',
    name='sparse_categorical_crossentropy'
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Effective Tensorflow 2](https://tensorflow.google.cn/guide/effective_tf2) * [Migrate early stopping](https://tensorflow.google.cn/guide/migrate/early_stopping) * [Migrate the fault tolerance mechanism](https://tensorflow.google.cn/guide/migrate/fault_tolerance) * [Use TPUs](https://tensorflow.google.cn/guide/tpu) * [tf.data: Build TensorFlow input pipelines](https://tensorflow.google.cn/guide/data) | * [Load text](https://tensorflow.google.cn/tutorials/load_data/text) * [Distributed training with Keras](https://tensorflow.google.cn/tutorials/distribute/keras) * [Image segmentation](https://tensorflow.google.cn/tutorials/images/segmentation) * [Save and load a model using a distribution strategy](https://tensorflow.google.cn/tutorials/distribute/save_and_load) * [Image classification](https://tensorflow.google.cn/tutorials/images/classification) |

Use this crossentropy loss function when there are two or more label
classes. We expect labels to be provided as integers. If you want to
provide labels using `one-hot` representation, please use
`CategoricalCrossentropy` loss. There should be `# classes` floating point
values per feature for `y_pred` and a single floating point value per
feature for `y_true`.

In the snippet below, there is a single floating point value per example for
`y_true` and `num_classes` floating pointing values per example for
`y_pred`. The shape of `y_true` is `[batch_size]` and the shape of `y_pred`
is `[batch_size, num_classes]`.

| Args | |

|  |  |
| --- | --- |
| `from_logits` | Whether `y_pred` is expected to be a logits tensor. By default, we assume that `y_pred` encodes a probability distribution. |
| `reduction` | Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"` or `None`. |
| `name` | Optional name for the loss instance. |

#### Examples:

```
>>> y_true = [1, 2]
>>> y_pred = [[0.05, 0.95, 0], [0.1, 0.8, 0.1]]
>>> # Using 'auto'/'sum_over_batch_size' reduction type.
>>> scce = keras.losses.SparseCategoricalCrossentropy()
>>> scce(y_true, y_pred)
1.177
```

```
>>> # Calling with 'sample_weight'.
>>> scce(y_true, y_pred, sample_weight=np.array([0.3, 0.7]))
0.814
```

```
>>> # Using 'sum' reduction type.
>>> scce = keras.losses.SparseCategoricalCrossentropy(
...     reduction="sum")
>>> scce(y_true, y_pred)
2.354
```

```
>>> # Using 'none' reduction type.
>>> scce = keras.losses.SparseCategoricalCrossentropy(
...     reduction=None)
>>> scce(y_true, y_pred)
array([0.0513, 2.303], dtype=float32)
```

Usage with the `compile()` API:

```
model.compile(optimizer='sgd',
              loss=keras.losses.SparseCategoricalCrossentropy())
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L977-L983)

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