# tf.keras.layers.Permute

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Permute](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Permute)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/reshaping/permute.py#L8-L64) |

Permutes the dimensions of the input according to a given pattern.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Permute(
    dims, **kwargs
)
```

Useful e.g. connecting RNNs and convnets.

| Args | |

|  |  |
| --- | --- |
| `dims` | Tuple of integers. Permutation pattern does not include the batch dimension. Indexing starts at 1. For instance, `(2, 1)` permutes the first and second dimensions of the input. |

| Input shape | |
| Arbitrary. | |

| Output shape | |
| Same as the input shape, but with the dimensions re-ordered according to the specified pattern. | |

#### Example:

```
>>> x = keras.Input(shape=(10, 64))
>>> y = keras.layers.Permute((2, 1))(x)
>>> y.shape
(None, 64, 10)
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