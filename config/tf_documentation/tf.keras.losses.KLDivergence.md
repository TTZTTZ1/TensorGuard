# tf.keras.losses.KLDivergence

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/KLDivergence](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/KLDivergence)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L335-L360) |

Computes Kullback-Leibler divergence loss between `y_true` & `y_pred`.

Inherits From: [`Loss`](https://tensorflow.google.cn/api_docs/python/tf/keras/Loss)

```
tf.keras.losses.KLDivergence(
    reduction='sum_over_batch_size', name='kl_divergence'
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L359-L360)

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