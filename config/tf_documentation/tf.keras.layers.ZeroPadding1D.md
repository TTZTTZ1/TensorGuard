# tf.keras.layers.ZeroPadding1D

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/ZeroPadding1D](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/ZeroPadding1D)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/reshaping/zero_padding1d.py#L8-L70) |

Zero-padding layer for 1D input (e.g. temporal sequence).

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.ZeroPadding1D(
    padding=1, **kwargs
)
```

#### Example:

```
>>> input_shape = (2, 2, 3)
>>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
>>> x
[[[ 0  1  2]
  [ 3  4  5]]
 [[ 6  7  8]
  [ 9 10 11]]]
>>> y = keras.layers.ZeroPadding1D(padding=2)(x)
>>> y
[[[ 0  0  0]
  [ 0  0  0]
  [ 0  1  2]
  [ 3  4  5]
  [ 0  0  0]
  [ 0  0  0]]
 [[ 0  0  0]
  [ 0  0  0]
  [ 6  7  8]
  [ 9 10 11]
  [ 0  0  0]
  [ 0  0  0]]]
```

| Args | |

|  |  |
| --- | --- |
| `padding` | Int, or tuple of int (length 2), or dictionary. |

* If int: how many zeros to add at the beginning and end of
  the padding dimension (axis 1).
* If tuple of 2 ints: how many zeros to add at the beginning and the
  end of the padding dimension (`(left_pad, right_pad)`).

| Input shape | |
| 3D tensor with shape `(batch_size, axis_to_pad, features)` | |

| Output shape | |
| 3D tensor with shape `(batch_size, padded_axis, features)` | |

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