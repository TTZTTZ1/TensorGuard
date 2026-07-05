# tf.keras.layers.Activation

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Activation](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Activation)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/activations/activation.py#L6-L39) |

Applies an activation function to an output.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Activation(
    activation, **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Mixed precision](https://tensorflow.google.cn/guide/mixed_precision) * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) | * [Basic text classification](https://tensorflow.google.cn/tutorials/keras/text_classification) * [Load text](https://tensorflow.google.cn/tutorials/load_data/text) * [Classifying CIFAR-10 with XLA](https://tensorflow.google.cn/xla/tf2xla/tutorials/autoclustering_xla) * [TFF simulations with accelerators](https://tensorflow.google.cn/federated/tutorials/simulations_with_accelerators) * [Parametrized Quantum Circuits for Reinforcement Learning](https://tensorflow.google.cn/quantum/tutorials/quantum_reinforcement_learning) |

| Args | |

|  |  |
| --- | --- |
| `activation` | Activation function. It could be a callable, or the name of an activation from the [`keras.activations`](https://tensorflow.google.cn/api_docs/python/tf/keras/activations) namespace. |
| `**kwargs` | Base layer keyword arguments, such as `name` and `dtype`. |

#### Example:

```
>>> layer = keras.layers.Activation('relu')
>>> layer([-3.0, -1.0, 0.0, 2.0])
[0.0, 0.0, 0.0, 2.0]
>>> layer = keras.layers.Activation(keras.activations.relu)
>>> layer([-3.0, -1.0, 0.0, 2.0])
[0.0, 0.0, 0.0, 2.0]
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

### `symbolic_call`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation.py#L58-L70)

```
symbolic_call(
    *args, **kwargs
)
```