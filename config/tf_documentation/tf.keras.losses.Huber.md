# tf.keras.losses.Huber

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/losses/Huber](https://tensorflow.google.cn/api_docs/python/tf/keras/losses/Huber)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L189-L224) |

Computes the Huber loss between `y_true` & `y_pred`.

Inherits From: [`Loss`](https://tensorflow.google.cn/api_docs/python/tf/keras/Loss)

```
tf.keras.losses.Huber(
    delta=1.0,
    reduction='sum_over_batch_size',
    name='huber_loss'
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Playing CartPole with the Actor-Critic method](https://tensorflow.google.cn/tutorials/reinforcement_learning/actor_critic) * [Parametrized Quantum Circuits for Reinforcement Learning](https://tensorflow.google.cn/quantum/tutorials/quantum_reinforcement_learning) |

#### Formula:

```
for x in error:
    if abs(x) <= delta:
        loss.append(0.5 * x^2)
    elif abs(x) > delta:
        loss.append(delta * abs(x) - 0.5 * delta^2)

loss = mean(loss, axis=-1)
```

See: [Huber loss](https://en.wikipedia.org/wiki/Huber_loss).

| Args | |

|  |  |
| --- | --- |
| `delta` | A float, the point where the Huber loss function changes from a quadratic to linear. |
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/losses/losses.py#L223-L224)

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