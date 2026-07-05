# tf.keras.losses.MeanSquaredError

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MeanSquaredError](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/MeanSquaredError)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L37-L60) |

Computes the mean of squares of errors between labels and predictions.

Inherits From: [`Loss`](https://tensorflow.google.cn/api_docs/python/tf/keras/Loss)

```
tf.keras.losses.MeanSquaredError(
    reduction='sum_over_batch_size',
    name='mean_squared_error'
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Time series forecasting](https://tensorflow.google.cn/tutorials/structured_data/time_series) * [Intro to Autoencoders](https://tensorflow.google.cn/tutorials/generative/autoencoder) * [Load CSV data](https://tensorflow.google.cn/tutorials/load_data/csv) * [Hello, many worlds](https://tensorflow.google.cn/quantum/tutorials/hello_many_worlds) * [Recommending movies: ranking](https://tensorflow.google.cn/recommenders/examples/basic_ranking) |

#### Formula:

```
loss = mean(square(y_true - y_pred))
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L59-L60)

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