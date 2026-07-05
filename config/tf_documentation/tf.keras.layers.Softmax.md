# tf.keras.layers.Softmax

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Softmax](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Softmax)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/activations/softmax.py#L14-L75) |

Softmax activation layer.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Softmax(
    axis=-1, **kwargs
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Basic classification: Classify images of clothing](https://tensorflow.google.cn/tutorials/keras/classification) * [TensorFlow 2 quickstart for beginners](https://tensorflow.google.cn/tutorials/quickstart/beginner) * [Building Your Own Federated Learning Algorithm](https://tensorflow.google.cn/federated/tutorials/building_your_own_federated_learning_algorithm) * [Composing Learning Algorithms](https://tensorflow.google.cn/federated/tutorials/composing_learning_algorithms) * [Federated Learning for Image Classification](https://tensorflow.google.cn/federated/tutorials/federated_learning_for_image_classification) |

#### Formula:

```
exp_x = exp(x - max(x))
f(x) = exp_x / sum(exp_x)
```

#### Example:

```
>>> oftmax_layer = keras.layers.activations.Softmax()
>>> nput = np.array([1.0, 2.0, 1.0])
>>> esult = softmax_layer(input)
[0.21194157, 0.5761169, 0.21194157]
```

| Args | |

|  |  |
| --- | --- |
| `axis` | Integer, or list of Integers, axis along which the softmax normalization is applied. |
| `**kwargs` | Base layer keyword arguments, such as `name` and `dtype`. |

| Call arguments | |

|  |  |
| --- | --- |
| `inputs` | The inputs (logits) to the softmax layer. |
| `mask` | A boolean mask of the same shape as `inputs`. The mask specifies 1 to keep and 0 to mask. Defaults to `None`. |

| Returns | |
| Softmaxed output with the same shape as `inputs`. | |

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