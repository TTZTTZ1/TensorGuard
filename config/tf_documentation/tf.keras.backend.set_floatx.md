# tf.keras.backend.set_floatx

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/backend/set_floatx](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/set_floatx)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/config.py#L37-L71) |

Set the default float dtype.

#### View aliases

**Main aliases**

[`tf.keras.config.set_floatx`](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/set_floatx)

```
tf.keras.backend.set_floatx(
    value
)
```

**Note:** It is not recommended to set this to `"float16"` for training,
as this will likely cause numeric stability issues.
Instead, mixed precision, which leverages
a mix of `float16` and `float32`. It can be configured by calling
`keras.mixed_precision.set_dtype_policy('mixed_float16')`.

| Args | |

|  |  |
| --- | --- |
| `value` | String; `'bfloat16'`, `'float16'`, `'float32'`, or `'float64'`. |

#### Examples:

```
>>> keras.config.floatx()
'float32'
```

```
>>> keras.config.set_floatx('float64')
>>> keras.config.floatx()
'float64'
```

```
>>> # Set it back to float32
>>> keras.config.set_floatx('float32')
```

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | In case of invalid value. |