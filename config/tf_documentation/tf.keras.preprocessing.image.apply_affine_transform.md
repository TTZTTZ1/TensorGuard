# tf.keras.preprocessing.image.apply_affine_transform

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/apply_affine_transform](https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/image/apply_affine_transform)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/image.py#L1778-L1892) |

Applies an affine transformation specified by the parameters given.

```
tf.keras.preprocessing.image.apply_affine_transform(
    x,
    theta=0,
    tx=0,
    ty=0,
    shear=0,
    zx=1,
    zy=1,
    row_axis=1,
    col_axis=2,
    channel_axis=0,
    fill_mode='nearest',
    cval=0.0,
    order=1
)
```

DEPRECATED.