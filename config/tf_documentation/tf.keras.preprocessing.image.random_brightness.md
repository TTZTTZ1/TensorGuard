# tf.keras.preprocessing.image.random_brightness

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/random_brightness](https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/random_brightness)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L1741-L1766) |

Performs a random brightness shift.

```
tf.keras.preprocessing.image.random_brightness(
    x, brightness_range, scale=True
)
```

DEPRECATED.

| Args | |

|  |  |
| --- | --- |
| `x` | Input tensor. Must be 3D. |
| `brightness_range` | Tuple of floats; brightness range. |
| `scale` | Whether to rescale the image such that minimum and maximum values are 0 and 255 respectively. Default: True. |

| Returns | |
| Numpy image tensor. | |

| Raises | |
| ValueError if `brightness_range` isn't a tuple. | |