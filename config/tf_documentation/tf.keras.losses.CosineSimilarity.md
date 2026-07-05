# tf.keras.losses.CosineSimilarity

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/CosineSimilarity](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/CosineSimilarity)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L149-L186) |

Computes the cosine similarity between `y_true` & `y_pred`.

Inherits From: [`Loss`](https://tensorflow.google.cn/api_docs/python/tf/keras/Loss)

```
tf.keras.losses.CosineSimilarity(
    axis=-1,
    reduction='sum_over_batch_size',
    name='cosine_similarity'
)
```

Note that it is a number between -1 and 1. When it is a negative number
between -1 and 0, 0 indicates orthogonality and values closer to -1
indicate greater similarity. This makes it usable as a loss function in a
setting where you try to maximize the proximity between predictions and
targets. If either `y_true` or `y_pred` is a zero vector, cosine similarity
will be 0 regardless of the proximity between predictions and targets.

#### Formula:

```
loss = -sum(l2_norm(y_true) * l2_norm(y_pred))
```

| Args | |

|  |  |
| --- | --- |
| `axis` | The axis along which the cosine similarity is computed (the features axis). Defaults to `-1`. |
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L185-L186)

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