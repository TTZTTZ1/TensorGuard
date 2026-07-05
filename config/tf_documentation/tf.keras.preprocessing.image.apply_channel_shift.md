# tf.keras.preprocessing.image.apply_channel_shift

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/apply_channel_shift](https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/apply_channel_shift)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L1668-L1689) |

Performs a channel shift.

```
tf.keras.preprocessing.image.apply_channel_shift(
    x, intensity, channel_axis=0
)
```

DEPRECATED.

| Args | |

|  |  |
| --- | --- |
| `x` | Input tensor. Must be 3D. |
| `intensity` | Transformation intensity. |
| `channel_axis` | Index of axis for channels in the input tensor. |

| Returns | |
| Numpy image tensor. | |