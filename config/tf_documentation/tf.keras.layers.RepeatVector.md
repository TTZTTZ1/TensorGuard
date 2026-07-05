# tf.keras.layers.RepeatVector

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/RepeatVector](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/RepeatVector)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/reshaping/repeat_vector.py#L7-L48) |

Repeats the input n times.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.RepeatVector(
    n, **kwargs
)
```

#### Example:

```
>>> x = keras.Input(shape=(32,))
>>> y = keras.layers.RepeatVector(3)(x)
>>> y.shape
(None, 3, 32)
```

| Args | |

|  |  |
| --- | --- |
| `n` | Integer, repetition factor. |

| Input shape | |
| 2D tensor with shape `(batch_size, features)`. | |

| Output shape | |
| 3D tensor with shape `(batch_size, n, features)`. | |

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