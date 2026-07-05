# tf.keras.layers.ReLU

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/ReLU](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/ReLU)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/activations/relu.py#L6-L85) |

Rectified Linear Unit activation function layer.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.ReLU(
    max_value=None, negative_slope=0.0, threshold=0.0, **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Pruning for on-device inference w/ XNNPACK](https://tensorflow.google.cn/model_optimization/guide/pruning/pruning_for_on_device_inference) * [Sparse weights using structural pruning](https://tensorflow.google.cn/model_optimization/guide/pruning/pruning_with_sparsity_2_by_4) | * [pix2pix: Image-to-image translation with a conditional GAN](https://tensorflow.google.cn/tutorials/generative/pix2pix) |

#### Formula:

```
f(x) = max(x,0)
f(x) = max_value if x >= max_value
f(x) = x if threshold <= x < max_value
f(x) = negative_slope * (x - threshold) otherwise
```

#### Example:

```
relu_layer = keras.layers.activations.ReLU(
    max_value=10,
    negative_slope=0.5,
    threshold=0,
)
input = np.array([-10, -5, 0.0, 5, 10])
result = relu_layer(input)
# result = [-5. , -2.5,  0. ,  5. , 10.]
```

| Args | |

|  |  |
| --- | --- |
| `max_value` | Float >= 0. Maximum activation value. None means unlimited. Defaults to `None`. |
| `negative_slope` | Float >= 0. Negative slope coefficient. Defaults to `0.0`. |
| `threshold` | Float >= 0. Threshold value for thresholded activation. Defaults to `0.0`. |
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