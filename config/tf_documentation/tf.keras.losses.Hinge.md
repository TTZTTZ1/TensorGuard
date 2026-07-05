# tf.keras.losses.Hinge

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/Hinge](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/Hinge)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L253-L277) |

Computes the hinge loss between `y_true` & `y_pred`.

Inherits From: [`Loss`](https://tensorflow.google.cn/api_docs/python/tf/keras/Loss)

```
tf.keras.losses.Hinge(
    reduction='sum_over_batch_size', name='hinge'
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [MNIST classification](https://tensorflow.google.cn/quantum/tutorials/mnist) |

#### Formula:

```
loss = maximum(1 - y_true * y_pred, 0)
```

`y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are
provided we will convert them to -1 or 1.

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L276-L277)

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