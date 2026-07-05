# tf.keras.layers.LeakyReLU

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/LeakyReLU](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/LeakyReLU)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/activations/leaky_relu.py#L8-L66) |

Leaky version of a Rectified Linear Unit activation layer.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.LeakyReLU(
    negative_slope=0.3, **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Customizing what happens in `fit()`](https://tensorflow.google.cn/guide/keras/customizing_what_happens_in_fit) | * [Deep Convolutional Generative Adversarial Network](https://tensorflow.google.cn/tutorials/generative/dcgan) * [pix2pix: Image-to-image translation with a conditional GAN](https://tensorflow.google.cn/tutorials/generative/pix2pix) |

This layer allows a small gradient when the unit is not active.

#### Formula:

```
f(x) = alpha * x if x < 0
f(x) = x if x >= 0
```

#### Example:

```
leaky_relu_layer = LeakyReLU(negative_slope=0.5)
input = np.array([-10, -5, 0.0, 5, 10])
result = leaky_relu_layer(input)
# result = [-5. , -2.5,  0. ,  5. , 10.]
```

| Args | |

|  |  |
| --- | --- |
| `negative_slope` | Float >= 0.0. Negative slope coefficient. Defaults to `0.3`. |
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