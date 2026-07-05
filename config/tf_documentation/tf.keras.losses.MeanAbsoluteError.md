# tf.keras.losses.MeanAbsoluteError

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MeanAbsoluteError](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MeanAbsoluteError)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L63-L86) |

Computes the mean of absolute difference between labels and predictions.

Inherits From: [`Loss`](https://tensorflow.google.cn/api_docs/python/tf/keras/Loss)

```
tf.keras.losses.MeanAbsoluteError(
    reduction='sum_over_batch_size',
    name='mean_absolute_error'
)
```

#### Formula:

```
loss = mean(abs(y_true - y_pred))
```

| Args | |

|  |  |
| --- | --- |
| `reduction` | Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"` or `None`. |
| `name` | Optional name for the loss instance. |

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L85-L86)

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