# tf.keras.losses.LogCosh

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/LogCosh](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/LogCosh)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L227-L250) |

Computes the logarithm of the hyperbolic cosine of the prediction error.

Inherits From: [`Loss`](https://tensorflow.google.cn/api_docs/python/tf/keras/Loss)

```
tf.keras.losses.LogCosh(
    reduction='sum_over_batch_size', name='log_cosh'
)
```

#### Formula:

```
error = y_pred - y_true
logcosh = mean(log((exp(error) + exp(-error))/2), axis=-1)`
```

where x is the error `y_pred - y_true`.

| Args | |

|  |  |
| --- | --- |
| `reduction` | Type of reduction to apply to loss. Options are `"sum"`, `"sum_over_batch_size"` or `None`. Defaults to `"sum_over_batch_size"`. |
| `name` | Optional name for the instance. |

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L249-L250)

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