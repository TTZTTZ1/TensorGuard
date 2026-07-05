# tf.keras.layers.StackedRNNCells

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/StackedRNNCells](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/StackedRNNCells)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/stacked_rnn_cells.py#L8-L139) |

Wrapper allowing a stack of RNN cells to behave as a single cell.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.StackedRNNCells(
    cells, **kwargs
)
```

Used to implement efficient stacked RNNs.

| Args | |

|  |  |
| --- | --- |
| `cells` | List of RNN cell instances. |

#### Example:

```
batch_size = 3
sentence_length = 5
num_features = 2
new_shape = (batch_size, sentence_length, num_features)
x = np.reshape(np.arange(30), new_shape)

rnn_cells = [keras.layers.LSTMCell(128) for _ in range(2)]
stacked_lstm = keras.layers.StackedRNNCells(rnn_cells)
lstm_layer = keras.layers.RNN(stacked_lstm)

result = lstm_layer(x)
```

| Attributes | |

|  |  |
| --- | --- |
| `input` | Retrieves the input tensor(s) of a symbolic operation. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `output` | Retrieves the output tensor(s) of a layer. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `output_size` |  |

|  |  |
| --- | --- |
| `state_size` |  |

## Methods

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/stacked_rnn_cells.py#L130-L139)

```
@classmethod
from_config(
    config, custom_objects=None
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/rnn/stacked_rnn_cells.py#L62-L85)

```
get_initial_state(
    batch_size=None
)
```

### `symbolic_call`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation.py#L58-L70)

```
symbolic_call(
    *args, **kwargs
)
```