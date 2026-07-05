# tf.keras.utils.normalize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/normalize](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/normalize)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/utils/numerical_utils.py#L7-L34) |

Normalizes an array.

```
tf.keras.utils.normalize(
    x, axis=-1, order=2
)
```

If the input is a NumPy array, a NumPy array will be returned.
If it's a backend tensor, a backend tensor will be returned.

| Args | |

|  |  |
| --- | --- |
| `x` | Array to normalize. |
| `axis` | axis along which to normalize. |
| `order` | Normalization order (e.g. `order=2` for L2 norm). |

| Returns | |
| A normalized copy of the array. | |