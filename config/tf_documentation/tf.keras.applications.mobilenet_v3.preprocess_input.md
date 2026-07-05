# tf.keras.applications.mobilenet_v3.preprocess_input

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/applications/mobilenet_v3/preprocess_input](https://tensorflow.google.cn/api_docs/python/tf/keras/applications/mobilenet_v3/preprocess_input)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/applications/mobilenet_v3.py#L652-L672) |

A placeholder method for backward compatibility.

```
tf.keras.applications.mobilenet_v3.preprocess_input(
    x, data_format=None
)
```

The preprocessing logic has been included in the mobilenet\_v3 model
implementation. Users are no longer required to call this method to
normalize the input data. This method does nothing and only kept as a
placeholder to align the API surface between old and new version of model.

| Args | |

|  |  |
| --- | --- |
| `x` | A floating point [`numpy.array`](https://tensorflow.google.cn/api_docs/python/tf/keras/ops/array) or a tensor. |
| `data_format` | Optional data format of the image tensor/array. `None` means the global setting [`keras.config.image_data_format()`](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/image_data_format) is used (unless you changed it, it uses `"channels_last"`). Defaults to `None`. |

| Returns | |
| Unchanged [`numpy.array`](https://tensorflow.google.cn/api_docs/python/tf/keras/ops/array) or tensor. | |