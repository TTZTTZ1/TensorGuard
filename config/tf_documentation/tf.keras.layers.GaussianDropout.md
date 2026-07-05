# tf.keras.layers.GaussianDropout

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/GaussianDropout](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/GaussianDropout)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/regularization/gaussian_dropout.py#L9-L62) |

Apply multiplicative 1-centered Gaussian noise.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.GaussianDropout(
    rate, seed=None, **kwargs
)
```

As it is a regularization layer, it is only active at training time.

| Args | |

|  |  |
| --- | --- |
| `rate` | Float, drop probability (as with `Dropout`). The multiplicative noise will have standard deviation `sqrt(rate / (1 - rate))`. |
| `seed` | Integer, optional random seed to enable deterministic behavior. |

| Call arguments | |

|  |  |
| --- | --- |
| `inputs` | Input tensor (of any rank). |
| `training` | Python boolean indicating whether the layer should behave in training mode (adding dropout) or in inference mode (doing nothing). |

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