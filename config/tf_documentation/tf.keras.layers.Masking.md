# tf.keras.layers.Masking

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Masking](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Masking)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/core/masking.py#L7-L74) |

Masks a sequence by using a mask value to skip timesteps.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Masking(
    mask_value=0.0, **kwargs
)
```

For each timestep in the input tensor (dimension #1 in the tensor),
if all values in the input tensor at that timestep
are equal to `mask_value`, then the timestep will be masked (skipped)
in all downstream layers (as long as they support masking).

If any downstream layer does not support masking yet receives such
an input mask, an exception will be raised.

#### Example:

Consider a NumPy data array `x` of shape `(samples, timesteps, features)`,
to be fed to an LSTM layer. You want to mask timestep #3 and #5 because you
lack data for these timesteps. You can:

* Set `x[:, 3, :] = 0.` and `x[:, 5, :] = 0.`
* Insert a `Masking` layer with `mask_value=0.` before the LSTM layer:

```
samples, timesteps, features = 32, 10, 8
inputs = np.random.random([samples, timesteps, features]).astype(np.float32)
inputs[:, 3, :] = 0.
inputs[:, 5, :] = 0.

model = keras.models.Sequential()
model.add(keras.layers.Masking(mask_value=0.)
model.add(keras.layers.LSTM(32))
output = model(inputs)
# The time step 3 and 5 will be skipped from LSTM calculation.
```

**Note:** in the Keras masking convention, a masked timestep is denoted by
a mask value of `False`, while a non-masked (i.e. usable) timestep
is denoted by a mask value of `True`.

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