# tf.keras.preprocessing.image.save_img

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/save_img](https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/save_img)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/utils/image_utils.py#L162-L184) |

Saves an image stored as a NumPy array to a path or file object.

#### View aliases

**Main aliases**

[`tf.keras.preprocessing.image.save_img`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/save_img)

```
tf.keras.utils.save_img(
    path, x, data_format=None, file_format=None, scale=True, **kwargs
)
```

| Args | |

|  |  |
| --- | --- |
| `path` | Path or file object. |
| `x` | NumPy array. |
| `data_format` | Image data format, either `"channels_first"` or `"channels_last"`. |
| `file_format` | Optional file format override. If omitted, the format to use is determined from the filename extension. If a file object was used instead of a filename, this parameter should always be used. |
| `scale` | Whether to rescale image values to be within `[0, 255]`. |
| `**kwargs` | Additional keyword arguments passed to `PIL.Image.save()`. |