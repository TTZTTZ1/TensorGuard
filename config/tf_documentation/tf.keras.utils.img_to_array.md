# tf.keras.utils.img_to_array

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/img_to_array](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/img_to_array)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/utils/image_utils.py#L110-L159) |

Converts a PIL Image instance to a NumPy array.

#### View aliases

**Main aliases**

[`tf.keras.preprocessing.image.img_to_array`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/img_to_array)

```
tf.keras.utils.img_to_array(
    img, data_format=None, dtype=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Using the SavedModel format](https://tensorflow.google.cn/guide/saved_model) | * [DeepDream](https://tensorflow.google.cn/tutorials/generative/deepdream) * [Image classification](https://tensorflow.google.cn/tutorials/images/classification) |

#### Example:

```
from PIL import Image
img_data = np.random.random(size=(100, 100, 3))
img = keras.utils.array_to_img(img_data)
array = keras.utils.image.img_to_array(img)
```

| Args | |

|  |  |
| --- | --- |
| `img` | Input PIL Image instance. |
| `data_format` | Image data format, can be either `"channels_first"` or `"channels_last"`. Defaults to `None`, in which case the global setting [`keras.backend.image_data_format()`](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/image_data_format) is used (unless you changed it, it defaults to `"channels_last"`). |
| `dtype` | Dtype to use. `None` means the global setting [`keras.backend.floatx()`](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/floatx) is used (unless you changed it, it defaults to `"float32"`). |

| Returns | |
| A 3D NumPy array. | |