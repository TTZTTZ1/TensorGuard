# tf.keras.layers.GaussianNoise

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/GaussianNoise](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/GaussianNoise)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/regularization/gaussian_noise.py#L7-L62) |

Apply additive zero-centered Gaussian noise.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.GaussianNoise(
    stddev, seed=None, **kwargs
)
```

This is useful to mitigate overfitting
(you could see it as a form of random data augmentation).
Gaussian Noise (GS) is a natural choice as corruption process
for real valued inputs.

As it is a regularization layer, it is only active at training time.

| Args | |

|  |  |
| --- | --- |
| `stddev` | Float, standard deviation of the noise distribution. |
| `seed` | Integer, optional random seed to enable deterministic behavior. |

| Call arguments | |

|  |  |
| --- | --- |
| `inputs` | Input tensor (of any rank). |
| `training` | Python boolean indicating whether the layer should behave in training mode (adding noise) or in inference mode (doing nothing). |

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