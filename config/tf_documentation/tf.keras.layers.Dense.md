# tf.keras.layers.Dense

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Dense](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Dense)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/core/dense.py#L15-L603) |

Just your regular densely-connected NN layer.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Dense(
    units,
    activation=None,
    use_bias=True,
    kernel_initializer='glorot_uniform',
    bias_initializer='zeros',
    kernel_regularizer=None,
    bias_regularizer=None,
    activity_regularizer=None,
    kernel_constraint=None,
    bias_constraint=None,
    lora_rank=None,
    **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Advanced automatic differentiation](https://tensorflow.google.cn/guide/advanced_autodiff) * [Debug a TensorFlow 2 migrated training pipeline](https://tensorflow.google.cn/guide/migrate/migration_debugging) * [Effective Tensorflow 2](https://tensorflow.google.cn/guide/effective_tf2) * [Migration examples: Canned Estimators](https://tensorflow.google.cn/guide/migrate/canned_estimators) * [Migrate early stopping](https://tensorflow.google.cn/guide/migrate/early_stopping) | * [Overfit and underfit](https://tensorflow.google.cn/tutorials/keras/overfit_and_underfit) * [Time series forecasting](https://tensorflow.google.cn/tutorials/structured_data/time_series) * [Load a pandas DataFrame](https://tensorflow.google.cn/tutorials/load_data/pandas_dataframe) * [Using DTensors with Keras](https://tensorflow.google.cn/tutorials/distribute/dtensor_keras_tutorial) * [Intro to Autoencoders](https://tensorflow.google.cn/tutorials/generative/autoencoder) |

`Dense` implements the operation:
`output = activation(dot(input, kernel) + bias)`
where `activation` is the element-wise activation function
passed as the `activation` argument, `kernel` is a weights matrix
created by the layer, and `bias` is a bias vector created by the layer
(only applicable if `use_bias` is `True`).

**Note:** If the input to the layer has a rank greater than 2, `Dense`
computes the dot product between the `inputs` and the `kernel` along the
last axis of the `inputs` and axis 0 of the `kernel` (using [`tf.tensordot`](https://tensorflow.google.cn/api_docs/python/tf/tensordot)).
For example, if input has dimensions `(batch_size, d0, d1)`, then we create
a `kernel` with shape `(d1, units)`, and the `kernel` operates along axis 2
of the `input`, on every sub-tensor of shape `(1, 1, d1)` (there are
`batch_size * d0` such sub-tensors). The output in this case will have
shape `(batch_size, d0, units)`.

| Args | |

|  |  |
| --- | --- |
| `units` | Positive integer, dimensionality of the output space. |
| `activation` | Activation function to use. If you don't specify anything, no activation is applied (ie. "linear" activation: `a(x) = x`). |
| `use_bias` | Boolean, whether the layer uses a bias vector. |
| `kernel_initializer` | Initializer for the `kernel` weights matrix. |
| `bias_initializer` | Initializer for the bias vector. |
| `kernel_regularizer` | Regularizer function applied to the `kernel` weights matrix. |
| `bias_regularizer` | Regularizer function applied to the bias vector. |
| `activity_regularizer` | Regularizer function applied to the output of the layer (its "activation"). |
| `kernel_constraint` | Constraint function applied to the `kernel` weights matrix. |
| `bias_constraint` | Constraint function applied to the bias vector. |
| `lora_rank` | Optional integer. If set, the layer's forward pass will implement LoRA (Low-Rank Adaptation) with the provided rank. LoRA sets the layer's kernel to non-trainable and replaces it with a delta over the original kernel, obtained via multiplying two lower-rank trainable matrices. This can be useful to reduce the computation cost of fine-tuning large dense layers. You can also enable LoRA on an existing `Dense` layer by calling `layer.enable_lora(rank)`. |

| Input shape | |
| N-D tensor with shape: `(batch_size, ..., input_dim)`. The most common situation would be a 2D input with shape `(batch_size, input_dim)`. | |

| Output shape | |
| N-D tensor with shape: `(batch_size, ..., units)`. For instance, for a 2D input with shape `(batch_size, input_dim)`, the output would have shape `(batch_size, units)`. | |

| Attributes | |

|  |  |
| --- | --- |
| `input` | Retrieves the input tensor(s) of a symbolic operation. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `kernel` |  |

|  |  |
| --- | --- |
| `output` | Retrieves the output tensor(s) of a layer. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.

## Methods

### `enable_lora`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/core/dense.py#L162-L196)

```
enable_lora(
    rank, a_initializer='he_uniform', b_initializer='zeros'
)
```

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

### `quantized_build`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/core/dense.py#L321-L331)

```
quantized_build(
    input_shape, mode
)
```

### `symbolic_call`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation.py#L58-L70)

```
symbolic_call(
    *args, **kwargs
)
```

| Class Variables | |

|  |  |
| --- | --- |
| QUANTIZATION\_MODE\_ERROR\_TEMPLATE | `("Invalid quantization mode. Expected one of ('int8', 'float8'). Received: " 'quantization_mode={mode}')` |