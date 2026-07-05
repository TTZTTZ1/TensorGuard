# tf.keras.losses.Loss

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/Loss](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/Loss)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/loss.py#L9-L74) |

Loss base class.

#### View aliases

**Main aliases**

[`tf.keras.losses.Loss`](https://tensorflow.google.cn/api_docs/python/tf/keras/Loss)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.keras.Loss`](https://tensorflow.google.cn/api_docs/python/tf/keras/Loss)

```
tf.keras.Loss(
    name=None, reduction='sum_over_batch_size', dtype=None
)
```

To be implemented by subclasses:

* `call()`: Contains the logic for loss calculation using `y_true`,
  `y_pred`.

Example subclass implementation:

```
class MeanSquaredError(Loss):
    def call(self, y_true, y_pred):
        return ops.mean(ops.square(y_pred - y_true), axis=-1)
```

## Methods

### `call`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/loss.py#L63-L64)

```
call(
    y_true, y_pred
)
```

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/loss.py#L69-L71)

```
@classmethod
from_config(
    config
)
```

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/loss.py#L66-L67)

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