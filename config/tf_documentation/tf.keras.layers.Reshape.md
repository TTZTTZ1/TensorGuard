# tf.keras.layers.Reshape

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Reshape](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Reshape)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/reshaping/reshape.py#L8-L73) |

Layer that reshapes inputs into the given shape.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Reshape(
    target_shape, **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Customizing what happens in `fit()`](https://tensorflow.google.cn/guide/keras/customizing_what_happens_in_fit) * [Using Counterfactual Logit Pairing with Keras](https://tensorflow.google.cn/responsible_ai/model_remediation/counterfactual/guide/counterfactual_keras) | * [Time series forecasting](https://tensorflow.google.cn/tutorials/structured_data/time_series) * [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://tensorflow.google.cn/tutorials/distribute/multi_worker_with_ctl) * [Multi-worker training with Keras](https://tensorflow.google.cn/tutorials/distribute/multi_worker_with_keras) * [Intro to Autoencoders](https://tensorflow.google.cn/tutorials/generative/autoencoder) * [Convolutional Variational Autoencoder](https://tensorflow.google.cn/tutorials/generative/cvae) |

| Args | |

|  |  |
| --- | --- |
| `target_shape` | Target shape. Tuple of integers, does not include the samples dimension (batch size). |

| Input shape | |
| Arbitrary, although all dimensions in the input shape must be known/fixed. Use the keyword argument `input_shape` (tuple of integers, does not include the samples/batch size axis) when using this layer as the first layer in a model. | |

| Output shape | |
| `(batch_size, *target_shape)` | |

#### Example:

```
>>> x = keras.Input(shape=(12,))
>>> y = keras.layers.Reshape((3, 4))(x)
>>> y.shape
(None, 3, 4)
```

```
>>> # also supports shape inference using `-1` as dimension
>>> y = keras.layers.Reshape((-1, 2, 2))(x)
>>> y.shape
(None, 3, 2, 2)
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