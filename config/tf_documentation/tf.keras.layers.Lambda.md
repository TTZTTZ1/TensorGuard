# tf.keras.layers.Lambda

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Lambda](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Lambda)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/core/lambda_layer.py#L12-L227) |

Wraps arbitrary expressions as a `Layer` object.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Lambda(
    function, output_shape=None, mask=None, arguments=None, **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [TensorFlow basics](https://tensorflow.google.cn/guide/basics) | * [Time series forecasting](https://tensorflow.google.cn/tutorials/structured_data/time_series) * [Data augmentation](https://tensorflow.google.cn/tutorials/images/data_augmentation) * [Graph regularization for document classification using natural graphs](https://tensorflow.google.cn/neural_structured_learning/tutorials/graph_keras_mlp_cora) * [Using TensorFlow Recommenders with TFX](https://tensorflow.google.cn/recommenders/examples/ranking_tfx) * [Parametrized Quantum Circuits for Reinforcement Learning](https://tensorflow.google.cn/quantum/tutorials/quantum_reinforcement_learning) |

The `Lambda` layer exists so that arbitrary expressions can be used
as a `Layer` when constructing Sequential
and Functional API models. `Lambda` layers are best suited for simple
operations or quick experimentation. For more advanced use cases,
prefer writing new subclasses of `Layer`.

**Warning:** `Lambda` layers have (de)serialization limitations!

The main reason to subclass `Layer` instead of using a
`Lambda` layer is saving and inspecting a model. `Lambda` layers
are saved by serializing the Python bytecode, which is fundamentally
non-portable and potentially unsafe.
They should only be loaded in the same environment where
they were saved. Subclassed layers can be saved in a more portable way
by overriding their `get_config()` method. Models that rely on
subclassed Layers are also often easier to visualize and reason about.

#### Example:

```
# add a x -> x^2 layer
model.add(Lambda(lambda x: x ** 2))
```

| Args | |

|  |  |
| --- | --- |
| `function` | The function to be evaluated. Takes input tensor as first argument. |
| `output_shape` | Expected output shape from function. This argument can usually be inferred if not explicitly provided. Can be a tuple or function. If a tuple, it only specifies the first dimension onward; sample dimension is assumed either the same as the input: `output_shape = (input_shape[0], ) + output_shape` or, the input is `None` and the sample dimension is also `None`: `output_shape = (None, ) + output_shape`. If a function, it specifies the entire shape as a function of the input shape: `output_shape = f(input_shape)`. |
| `mask` | Either None (indicating no masking) or a callable with the same signature as the `compute_mask` layer method, or a tensor that will be returned as output mask regardless of what the input is. |
| `arguments` | Optional dictionary of keyword arguments to be passed to the function. |

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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/core/lambda_layer.py#L181-L227)

```
@classmethod
from_config(
    config, custom_objects=None, safe_mode=None
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