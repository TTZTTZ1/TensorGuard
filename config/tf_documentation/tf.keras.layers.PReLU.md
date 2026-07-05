# tf.keras.layers.PReLU

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/PReLU](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/PReLU)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/activations/prelu.py#L10-L99) |

Parametric Rectified Linear Unit activation layer.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.PReLU(
    alpha_initializer='Zeros',
    alpha_regularizer=None,
    alpha_constraint=None,
    shared_axes=None,
    **kwargs
)
```

#### Formula:

```
f(x) = alpha * x for x < 0
f(x) = x for x >= 0
```

where `alpha` is a learned array with the same shape as x.

| Args | |

|  |  |
| --- | --- |
| `alpha_initializer` | Initializer function for the weights. |
| `alpha_regularizer` | Regularizer for the weights. |
| `alpha_constraint` | Constraint for the weights. |
| `shared_axes` | The axes along which to share learnable parameters for the activation function. For example, if the incoming feature maps are from a 2D convolution with output shape `(batch, height, width, channels)`, and you wish to share parameters across space so that each filter only has one set of parameters, set `shared_axes=[1, 2]`. |
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