# tf.keras.layers.InputSpec

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/InputSpec](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/InputSpec)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/input_spec.py#L6-L114) |

Specifies the rank, dtype and shape of every input to a layer.

#### View aliases

**Main aliases**

[`tf.keras.layers.InputSpec`](https://tensorflow.google.cn/api_docs/python/tf/keras/InputSpec)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.keras.InputSpec`](https://tensorflow.google.cn/api_docs/python/tf/keras/InputSpec)

```
tf.keras.InputSpec(
    dtype=None,
    shape=None,
    ndim=None,
    max_ndim=None,
    min_ndim=None,
    axes=None,
    allow_last_axis_squeeze=False,
    name=None
)
```

Layers can expose (if appropriate) an `input_spec` attribute:
an instance of `InputSpec`, or a nested structure of `InputSpec` instances
(one per input tensor). These objects enable the layer to run input
compatibility checks for input structure, input rank, input shape, and
input dtype for the first argument of [`Layer.call`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer#__call__).

A `None` entry in a shape is compatible with any dimension.

| Args | |

|  |  |
| --- | --- |
| `dtype` | Expected dtype of the input. |
| `shape` | Shape tuple, expected shape of the input (may include `None` for dynamic axes). Includes the batch size. |
| `ndim` | Integer, expected rank of the input. |
| `max_ndim` | Integer, maximum rank of the input. |
| `min_ndim` | Integer, minimum rank of the input. |
| `axes` | Dictionary mapping integer axes to a specific dimension value. |
| `allow_last_axis_squeeze` | If `True`, allow inputs of rank N+1 as long as the last axis of the input is 1, as well as inputs of rank N-1 as long as the last axis of the spec is 1. |
| `name` | Expected key corresponding to this input when passing data as a dictionary. |

#### Example:

```
class MyLayer(Layer):
    def __init__(self):
        super().__init__()
        # The layer will accept inputs with
        # shape (*, 28, 28) & (*, 28, 28, 1)
        # and raise an appropriate error message otherwise.
        self.input_spec = InputSpec(
            shape=(None, 28, 28, 1),
            allow_last_axis_squeeze=True)
```

## Methods

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/input_spec.py#L112-L114)

```
@classmethod
from_config(
    config
)
```

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/input_spec.py#L102-L110)

```
get_config()
```