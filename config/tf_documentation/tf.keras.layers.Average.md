# tf.keras.layers.Average

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Average](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Average)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/merging/average.py#L6-L37) |

Averages a list of inputs element-wise..

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Average(
    **kwargs
)
```

It takes as input a list of tensors, all of the same shape,
and returns a single tensor (also of the same shape).

#### Examples:

```
>>> input_shape = (2, 3, 4)
>>> x1 = np.random.rand(*input_shape)
>>> x2 = np.random.rand(*input_shape)
>>> y = keras.layers.Average()([x1, x2])
```

Usage in a Keras model:

```
>>> input1 = keras.layers.Input(shape=(16,))
>>> x1 = keras.layers.Dense(8, activation='relu')(input1)
>>> input2 = keras.layers.Input(shape=(32,))
>>> x2 = keras.layers.Dense(8, activation='relu')(input2)
>>> # equivalent to `y = keras.layers.average([x1, x2])`
>>> y = keras.layers.Average()([x1, x2])
>>> out = keras.layers.Dense(4)(y)
>>> model = keras.models.Model(inputs=[input1, input2], outputs=out)
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