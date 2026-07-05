# tf.keras.layers.SimpleRNN

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/SimpleRNN](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/SimpleRNN)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/simple_rnn.py#L212-L450) |

Fully-connected RNN where the output is to be fed back as the new input.

Inherits From: [`RNN`](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/RNN), [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.SimpleRNN(
    units,
    activation='tanh',
    use_bias=True,
    kernel_initializer='glorot_uniform',
    recurrent_initializer='orthogonal',
    bias_initializer='zeros',
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    return_sequences=False,
    return_state=False,
    go_backwards=False,
    stateful=False,
    unroll=False,
    seed=None,
    **kwargs
)
```

| Args | |

|  |  |
| --- | --- |
| `units` | Positive integer, dimensionality of the output space. |
| `activation` | Activation function to use. Default: hyperbolic tangent (`tanh`). If you pass None, no activation is applied (ie. "linear" activation: `a(x) = x`). |
| `use_bias` | Boolean, (default `True`), whether the layer uses a bias vector. |
| `kernel_initializer` | Initializer for the `kernel` weights matrix, used for the linear transformation of the inputs. Default: `"glorot_uniform"`. |
| `recurrent_initializer` | Initializer for the `recurrent_kernel` weights matrix, used for the linear transformation of the recurrent state. Default: `"orthogonal"`. |
| `bias_initializer` | Initializer for the bias vector. Default: `"zeros"`. |
| `kernel_regularizer` | Regularizer function applied to the `kernel` weights matrix. Default: `None`. |
| `recurrent_regularizer` | Regularizer function applied to the `recurrent_kernel` weights matrix. Default: `None`. |
| `bias_regularizer` | Regularizer function applied to the bias vector. Default: `None`. |
| `activity_regularizer` | Regularizer function applied to the output of the layer (its "activation"). Default: `None`. |
| `kernel_constraint` | Constraint function applied to the `kernel` weights matrix. Default: `None`. |
| `recurrent_constraint` | Constraint function applied to the `recurrent_kernel` weights matrix. Default: `None`. |
| `bias_constraint` | Constraint function applied to the bias vector. Default: `None`. |
| `dropout` | Float between 0 and 1. Fraction of the units to drop for the linear transformation of the inputs. Default: 0. |
| `recurrent_dropout` | Float between 0 and 1. Fraction of the units to drop for the linear transformation of the recurrent state. Default: 0. |
| `return_sequences` | Boolean. Whether to return the last output in the output sequence, or the full sequence. Default: `False`. |
| `return_state` | Boolean. Whether to return the last state in addition to the output. Default: `False`. |
| `go_backwards` | Boolean (default: `False`). If `True`, process the input sequence backwards and return the reversed sequence. |
| `stateful` | Boolean (default: `False`). If `True`, the last state for each sample at index i in a batch will be used as initial state for the sample of index i in the following batch. |
| `unroll` | Boolean (default: `False`). If `True`, the network will be unrolled, else a symbolic loop will be used. Unrolling can speed-up a RNN, although it tends to be more memory-intensive. Unrolling is only suitable for short sequences. |

| Call arguments | |

|  |  |
| --- | --- |
| `sequence` | A 3D tensor, with shape `[batch, timesteps, feature]`. |
| `mask` | Binary tensor of shape `[batch, timesteps]` indicating whether a given timestep should be masked. An individual `True` entry indicates that the corresponding timestep should be utilized, while a `False` entry indicates that the corresponding timestep should be ignored. |
| `training` | Python boolean indicating whether the layer should behave in training mode or in inference mode. This argument is passed to the cell when calling it. This is only relevant if `dropout` or `recurrent_dropout` is used. |
| `initial_state` | List of initial state tensors to be passed to the first call of the cell. |

#### Example:

```
inputs = np.random.random((32, 10, 8))
simple_rnn = keras.layers.SimpleRNN(4)
output = simple_rnn(inputs)  # The output has shape `(32, 4)`.
simple_rnn = keras.layers.SimpleRNN(
    4, return_sequences=True, return_state=True
)
# whole_sequence_output has shape `(32, 10, 4)`.
# final_state has shape `(32, 4)`.
whole_sequence_output, final_state = simple_rnn(inputs)
```

| Attributes | |

|  |  |
| --- | --- |
| `activation` |  |

|  |  |
| --- | --- |
| `bias_constraint` |  |

|  |  |
| --- | --- |
| `bias_initializer` |  |

|  |  |
| --- | --- |
| `bias_regularizer` |  |

|  |  |
| --- | --- |
| `dropout` |  |

|  |  |
| --- | --- |
| `input` | Retrieves the input tensor(s) of a symbolic operation. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `kernel_constraint` |  |

|  |  |
| --- | --- |
| `kernel_initializer` |  |

|  |  |
| --- | --- |
| `kernel_regularizer` |  |

|  |  |
| --- | --- |
| `output` | Retrieves the output tensor(s) of a layer. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `recurrent_constraint` |  |

|  |  |
| --- | --- |
| `recurrent_dropout` |  |

|  |  |
| --- | --- |
| `recurrent_initializer` |  |

|  |  |
| --- | --- |
| `recurrent_regularizer` |  |

|  |  |
| --- | --- |
| `units` |  |

|  |  |
| --- | --- |
| `use_bias` |  |

## Methods

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/simple_rnn.py#L448-L450)

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

### `get_initial_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/rnn.py#L306-L321)

```
get_initial_state(
    batch_size
)
```

### `inner_loop`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/rnn.py#L332-L356)

```
inner_loop(
    sequences, initial_state, mask, training=False
)
```

### `reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/rnn.py#L327-L330)

```
reset_state()
```

### `reset_states`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/rnn.py#L323-L325)

```
reset_states()
```

### `symbolic_call`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation.py#L58-L70)

```
symbolic_call(
    *args, **kwargs
)
```