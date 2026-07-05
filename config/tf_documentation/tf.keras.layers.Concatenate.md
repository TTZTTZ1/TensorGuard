# tf.keras.layers.Concatenate

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Concatenate](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Concatenate)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/merging/concatenate.py#L6-L157) |

Concatenates a list of inputs.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Concatenate(
    axis=-1, **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrate `tf.feature\_column`s to Keras preprocessing layers](https://tensorflow.google.cn/guide/migrate/migrating_feature_columns) * [Migrate from TPU embedding\_columns to TPUEmbedding layer](https://tensorflow.google.cn/guide/migrate/tpu_embedding) | * [Load CSV data](https://tensorflow.google.cn/tutorials/load_data/csv) * [pix2pix: Image-to-image translation with a conditional GAN](https://tensorflow.google.cn/tutorials/generative/pix2pix) * [Image segmentation](https://tensorflow.google.cn/tutorials/images/segmentation) * [Networks](https://tensorflow.google.cn/agents/tutorials/8_networks_tutorial) * [TFX Keras Component Tutorial](https://tensorflow.google.cn/tfx/tutorials/tfx/components_keras) |

It takes as input a list of tensors, all of the same shape except
for the concatenation axis, and returns a single tensor that is the
concatenation of all inputs.

#### Examples:

```
>>> x = np.arange(20).reshape(2, 2, 5)
>>> y = np.arange(20, 30).reshape(2, 1, 5)
>>> keras.layers.Concatenate(axis=1)([x, y])
```

Usage in a Keras model:

```
>>> x1 = keras.layers.Dense(8)(np.arange(10).reshape(5, 2))
>>> x2 = keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2))
>>> y = keras.layers.Concatenate()([x1, x2])
```

| Args | |

|  |  |
| --- | --- |
| `axis` | Axis along which to concatenate. |
| `**kwargs` | Standard layer keyword arguments. |

| Returns | |
| A tensor, the concatenation of the inputs alongside axis `axis`. | |

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