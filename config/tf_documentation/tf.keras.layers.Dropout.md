# tf.keras.layers.Dropout

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Dropout](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Dropout)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/regularization/dropout.py#L6-L76) |

Applies dropout to the input.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Dropout(
    rate, noise_shape=None, seed=None, **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Effective Tensorflow 2](https://tensorflow.google.cn/guide/effective_tf2) * [Migrate checkpoint saving](https://tensorflow.google.cn/guide/migrate/checkpoint_saver) * [Migrate evaluation](https://tensorflow.google.cn/guide/migrate/evaluator) * [Migrate the fault tolerance mechanism](https://tensorflow.google.cn/guide/migrate/fault_tolerance) * [Migrate TensorBoard: TensorFlow's visualization toolkit](https://tensorflow.google.cn/guide/migrate/tensorboard) | * [Overfit and underfit](https://tensorflow.google.cn/tutorials/keras/overfit_and_underfit) * [Using DTensors with Keras](https://tensorflow.google.cn/tutorials/distribute/dtensor_keras_tutorial) * [Simple audio recognition: Recognizing keywords](https://tensorflow.google.cn/tutorials/audio/simple_audio) * [Deep Convolutional Generative Adversarial Network](https://tensorflow.google.cn/tutorials/generative/dcgan) * [Basic text classification](https://tensorflow.google.cn/tutorials/keras/text_classification) |

The `Dropout` layer randomly sets input units to 0 with a frequency of
`rate` at each step during training time, which helps prevent overfitting.
Inputs not set to 0 are scaled up by `1 / (1 - rate)` such that the sum over
all inputs is unchanged.

Note that the `Dropout` layer only applies when `training` is set to `True`
in `call()`, such that no values are dropped during inference.
When using `model.fit`, `training` will be appropriately set to `True`
automatically. In other contexts, you can set the argument explicitly
to `True` when calling the layer.

(This is in contrast to setting `trainable=False` for a `Dropout` layer.
`trainable` does not affect the layer's behavior, as `Dropout` does
not have any variables/weights that can be frozen during training.)

| Args | |

|  |  |
| --- | --- |
| `rate` | Float between 0 and 1. Fraction of the input units to drop. |
| `noise_shape` | 1D integer tensor representing the shape of the binary dropout mask that will be multiplied with the input. For instance, if your inputs have shape `(batch_size, timesteps, features)` and you want the dropout mask to be the same for all timesteps, you can use `noise_shape=(batch_size, 1, features)`. |
| `seed` | A Python integer to use as random seed. |

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