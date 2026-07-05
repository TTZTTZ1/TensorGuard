# tf.keras.layers.ELU

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/ELU](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/ELU)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/activations/elu.py#L6-L31) |

Applies an Exponential Linear Unit function to an output.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.ELU(
    alpha=1.0, **kwargs
)
```

#### Formula:

```
f(x) = alpha * (exp(x) - 1.) for x < 0
f(x) = x for x >= 0
```

| Args | |

|  |  |
| --- | --- |
| `alpha` | float, slope of negative section. Defaults to `1.0`. |
| `**kwargs` | Base layer keyword arguments, such as `name` and `dtype`. |

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