# tf.keras.preprocessing.image.apply_brightness_shift

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/apply_brightness_shift](https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/apply_brightness_shift)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L1710-L1738) |

Performs a brightness shift.

```
tf.keras.preprocessing.image.apply_brightness_shift(
    x, brightness, scale=True
)
```

DEPRECATED.

| Args | |

|  |  |
| --- | --- |
| `x` | Input tensor. Must be 3D. |
| `brightness` | Float. The new brightness value. |
| `scale` | Whether to rescale the image such that minimum and maximum values are 0 and 255 respectively. Default: True. |

| Returns | |
| Numpy image tensor. | |

| Raises | |

|  |  |
| --- | --- |
| `ImportError` | if PIL is not available. |