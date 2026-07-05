# tf.keras.layers.Dot

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Dot](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Dot)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/merging/dot.py#L197-L356) |

Computes element-wise dot product of two tensors.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Dot(
    axes, normalize=False, **kwargs
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Federated Reconstruction for Matrix Factorization](https://tensorflow.google.cn/federated/tutorials/federated_reconstruction_for_matrix_factorization) |

It takes a list of inputs of size 2, and the axes
corresponding to each input along with the dot product
is to be performed.

Let's say `x` and `y` are the two input tensors with shapes
`(2, 3, 5)` and `(2, 10, 3)`. The batch dimension should be
of same size for both the inputs, and `axes` should correspond
to the dimensions that have the same size in the corresponding
inputs. e.g. with `axes=(1, 2)`, the dot product of `x`, and `y`
will result in a tensor with shape `(2, 5, 10)`

#### Example:

```
>>> x = np.arange(10).reshape(1, 5, 2)
>>> y = np.arange(10, 20).reshape(1, 2, 5)
>>> keras.layers.Dot(axes=(1, 2))([x, y])
```

Usage in a Keras model:

```
>>> x1 = keras.layers.Dense(8)(np.arange(10).reshape(5, 2))
>>> x2 = keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2))
>>> y = keras.layers.Dot(axes=1)([x1, x2])
```

| Args | |

|  |  |
| --- | --- |
| `axes` | Integer or tuple of integers, axis or axes along which to take the dot product. If a tuple, should be two integers corresponding to the desired axis from the first input and the desired axis from the second input, respectively. Note that the size of the two selected axes must match. |
| `normalize` | Whether to L2-normalize samples along the dot product axis before taking the dot product. If set to `True`, then the output of the dot product is the cosine proximity between the two samples. |
| `**kwargs` | Standard layer keyword arguments. |

| Returns | |
| A tensor, the dot product of the samples from the inputs. | |

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