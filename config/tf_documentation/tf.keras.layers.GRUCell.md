# tf.keras.layers.GRUCell

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/GRUCell](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/GRUCell)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/gru.py#L15-L327) |

Cell class for the GRU layer.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.GRUCell(
    units,
    activation='tanh',
    recurrent_activation='sigmoid',
    use_bias=True,
    kernel_initializer='glorot_uniform',
    recurrent_initializer='orthogonal',
    bias_initializer='zeros',
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    reset_after=True,
    seed=None,
    **kwargs
)
```

This class processes one step within the whole time sequence input, whereas
`keras.layer.GRU` processes the whole sequence.

| Args | |

|  |  |
| --- | --- |
| `units` | Positive integer, dimensionality of the output space. |
| `activation` | Activation function to use. Default: hyperbolic tangent (`tanh`). If you pass None, no activation is applied (ie. "linear" activation: `a(x) = x`). |
| `recurrent_activation` | Activation function to use for the recurrent step. Default: sigmoid (`sigmoid`). If you pass `None`, no activation is applied (ie. "linear" activation: `a(x) = x`). |
| `use_bias` | Boolean, (default `True`), whether the layer should use a bias vector. |
| `kernel_initializer` | Initializer for the `kernel` weights matrix, used for the linear transformation of the inputs. Default: `"glorot_uniform"`. |
| `recurrent_initializer` | Initializer for the `recurrent_kernel` weights matrix, used for the linear transformation of the recurrent state. Default: `"orthogonal"`. |
| `bias_initializer` | Initializer for the bias vector. Default: `"zeros"`. |
| `kernel_regularizer` | Regularizer function applied to the `kernel` weights matrix. Default: `None`. |
| `recurrent_regularizer` | Regularizer function applied to the `recurrent_kernel` weights matrix. Default: `None`. |
| `bias_regularizer` | Regularizer function applied to the bias vector. Default: `None`. |
| `kernel_constraint` | Constraint function applied to the `kernel` weights matrix. Default: `None`. |
| `recurrent_constraint` | Constraint function applied to the `recurrent_kernel` weights matrix. Default: `None`. |
| `bias_constraint` | Constraint function applied to the bias vector. Default: `None`. |
| `dropout` | Float between 0 and 1. Fraction of the units to drop for the linear transformation of the inputs. Default: 0. |
| `recurrent_dropout` | Float between 0 and 1. Fraction of the units to drop for the linear transformation of the recurrent state. Default: 0. |
| `reset_after` | GRU convention (whether to apply reset gate after or before matrix multiplication). False = "before", True = "after" (default and cuDNN compatible). |
| `seed` | Random seed for dropout. |

| Call arguments | |

|  |  |
| --- | --- |
| `inputs` | A 2D tensor, with shape `(batch, features)`. |
| `states` | A 2D tensor with shape `(batch, units)`, which is the state from the previous time step. |
| `training` | Python boolean indicating whether the layer should behave in training mode or in inference mode. Only relevant when `dropout` or `recurrent_dropout` is used. |

#### Example:

```
>>> inputs = np.random.random((32, 10, 8))
>>> rnn = keras.layers.RNN(keras.layers.GRUCell(4))
>>> output = rnn(inputs)
>>> output.shape
(32, 4)
>>> rnn = keras.layers.RNN(
...    keras.layers.GRUCell(4),
...    return_sequences=True,
...    return_state=True)
>>> whole_sequence_output, final_state = rnn(inputs)
>>> whole_sequence_output.shape
(32, 10, 4)
>>> final_state.shape
(32, 4)
```

| Attributes | |

|  |  |
| --- | --- |
| `input` | Retrieves the input tensor(s) of a symbolic operation. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `output` | Retrieves the output tensor(s) of a layer. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.

## Methods

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation.py#L191-L213)

```
@classmethod
from_config(
    config
)
```

Creates a layer from its config.

This method is the reverse of `get_config`,
capable of instantiating the same layer from the config
dictionary. It does not handle layer connectivity
(handled by Network), nor weights (handled by `set_weights`).

| Args | |

|  |  |
| --- | --- |
| `config` | A Python dictionary, typically the output of get\_config. |

| Returns | |
| A layer instance. | |

### `get_dropout_mask`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/dropout_rnn_cell.py#L22-L30)

```
get_dropout_mask(
    step_input
)
```

### `get_initial_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/gru.py#L324-L327)

```
get_initial_state(
    batch_size=None
)
```

### `get_recurrent_dropout_mask`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/dropout_rnn_cell.py#L32-L40)

```
get_recurrent_dropout_mask(
    step_input
)
```

### `reset_dropout_mask`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/dropout_rnn_cell.py#L42-L50)

```
reset_dropout_mask()
```

Reset the cached dropout mask if any.

The RNN layer invokes this in the `call()` method
so that the cached mask is cleared after calling `cell.call()`. The
mask should be cached across all timestep within the same batch, but
shouldn't be cached between batches.

### `reset_recurrent_dropout_mask`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/dropout_rnn_cell.py#L52-L53)

```
reset_recurrent_dropout_mask()
```

### `symbolic_call`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation.py#L58-L70)

```
symbolic_call(
    *args, **kwargs
)
```