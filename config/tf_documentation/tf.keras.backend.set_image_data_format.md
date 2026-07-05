# tf.keras.backend.set_image_data_format

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/backend/set_image_data_format](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/set_image_data_format)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/backend/config.py#L134-L167) |

Set the value of the image data format convention.

#### View aliases

**Main aliases**

[`tf.keras.config.set_image_data_format`](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/set_image_data_format)

```
tf.keras.backend.set_image_data_format(
    data_format
)
```

| Args | |

|  |  |
| --- | --- |
| `data_format` | string. `'channels_first'` or `'channels_last'`. |

#### Examples:

```
>>> keras.config.image_data_format()
'channels_last'
```

```
>>> keras.config.set_image_data_format('channels_first')
>>> keras.config.image_data_format()
'channels_first'
```

```
>>> # Set it back to `'channels_last'`
>>> keras.config.set_image_data_format('channels_last')
```