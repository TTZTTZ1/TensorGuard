# tf.keras.layers.Embedding

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Embedding](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Embedding)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/core/embedding.py#L14-L427) |

Turns positive integers (indexes) into dense vectors of fixed size.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Embedding(
    input_dim,
    output_dim,
    embeddings_initializer='uniform',
    embeddings_regularizer=None,
    embeddings_constraint=None,
    mask_zero=False,
    weights=None,
    lora_rank=None,
    **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrate `tf.feature\_column`s to Keras preprocessing layers](https://tensorflow.google.cn/guide/migrate/migrating_feature_columns) * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) * [Working with preprocessing layers](https://tensorflow.google.cn/guide/keras/preprocessing_layers) | * [Parameter server training with ParameterServerStrategy](https://tensorflow.google.cn/tutorials/distribute/parameter_server_training) * [Basic text classification](https://tensorflow.google.cn/tutorials/keras/text_classification) * [Load text](https://tensorflow.google.cn/tutorials/load_data/text) * [Using side features: feature preprocessing](https://tensorflow.google.cn/recommenders/examples/featurization) * [Taking advantage of context features](https://tensorflow.google.cn/recommenders/examples/context_features) |

e.g. `[[4], [20]] -> [[0.25, 0.1], [0.6, -0.2]]`

This layer can only be used on positive integer inputs of a fixed range.

#### Example:

```
>>> model = keras.Sequential()
>>> model.add(keras.layers.Embedding(1000, 64))
>>> # The model will take as input an integer matrix of size (batch,
>>> # input_length), and the largest integer (i.e. word index) in the input
>>> # should be no larger than 999 (vocabulary size).
>>> # Now model.output_shape is (None, 10, 64), where `None` is the batch
>>> # dimension.
>>> input_array = np.random.randint(1000, size=(32, 10))
>>> model.compile('rmsprop', 'mse')
>>> output_array = model.predict(input_array)
>>> print(output_array.shape)
(32, 10, 64)
```

| Args | |

|  |  |
| --- | --- |
| `input_dim` | Integer. Size of the vocabulary, i.e. maximum integer index + 1. |
| `output_dim` | Integer. Dimension of the dense embedding. |
| `embeddings_initializer` | Initializer for the `embeddings` matrix (see [`keras.initializers`](https://tensorflow.google.cn/api_docs/python/tf/keras/initializers)). |
| `embeddings_regularizer` | Regularizer function applied to the `embeddings` matrix (see [`keras.regularizers`](https://tensorflow.google.cn/api_docs/python/tf/keras/regularizers)). |
| `embeddings_constraint` | Constraint function applied to the `embeddings` matrix (see [`keras.constraints`](https://tensorflow.google.cn/api_docs/python/tf/keras/constraints)). |
| `mask_zero` | Boolean, whether or not the input value 0 is a special "padding" value that should be masked out. This is useful when using recurrent layers which may take variable length input. If this is `True`, then all subsequent layers in the model need to support masking or an exception will be raised. If `mask_zero` is set to `True`, as a consequence, index 0 cannot be used in the vocabulary (`input_dim` should equal size of vocabulary + 1). |
| `weights` | Optional floating-point matrix of size `(input_dim, output_dim)`. The initial embeddings values to use. |
| `lora_rank` | Optional integer. If set, the layer's forward pass will implement LoRA (Low-Rank Adaptation) with the provided rank. LoRA sets the layer's embeddings matrix to non-trainable and replaces it with a delta over the original matrix, obtained via multiplying two lower-rank trainable matrices. This can be useful to reduce the computation cost of fine-tuning large embedding layers. You can also enable LoRA on an existing `Embedding` layer by calling `layer.enable_lora(rank)`. |

| Input shape | |
| 2D tensor with shape: `(batch_size, input_length)`. | |

| Output shape | |
| 3D tensor with shape: `(batch_size, input_length, output_dim)`. | |

| Attributes | |

|  |  |
| --- | --- |
| `embeddings` |  |

|  |  |
| --- | --- |
| `input` | Retrieves the input tensor(s) of a symbolic operation. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `output` | Retrieves the output tensor(s) of a layer. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.

## Methods

### `enable_lora`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/core/embedding.py#L157-L191)

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/core/embedding.py#L305-L311)

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
| QUANTIZATION\_MODE\_ERROR\_TEMPLATE | `"Invalid quantization mode. Expected 'int8'. Received: quantization_mode={mode}"` |