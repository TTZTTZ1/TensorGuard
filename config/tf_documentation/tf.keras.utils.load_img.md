# tf.keras.utils.load_img

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/load_img](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/load_img)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/utils/image_utils.py#L187-L293) |

Loads an image into PIL format.

#### View aliases

**Main aliases**

[`tf.keras.preprocessing.image.load_img`](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/load_img)

```
tf.keras.utils.load_img(
    path,
    color_mode='rgb',
    target_size=None,
    interpolation='nearest',
    keep_aspect_ratio=False
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Using the SavedModel format](https://tensorflow.google.cn/guide/saved_model) | * [Image classification](https://tensorflow.google.cn/tutorials/images/classification) |

#### Example:

```
image = keras.utils.load_img(image_path)
input_arr = keras.utils.img_to_array(image)
input_arr = np.array([input_arr])  # Convert single image to a batch.
predictions = model.predict(input_arr)
```

| Args | |

|  |  |
| --- | --- |
| `path` | Path to image file. |
| `color_mode` | One of `"grayscale"`, `"rgb"`, `"rgba"`. Default: `"rgb"`. The desired image format. |
| `target_size` | Either `None` (default to original size) or tuple of ints `(img_height, img_width)`. |
| `interpolation` | Interpolation method used to resample the image if the target size is different from that of the loaded image. Supported methods are `"nearest"`, `"bilinear"`, and `"bicubic"`. If PIL version 1.1.3 or newer is installed, `"lanczos"` is also supported. If PIL version 3.4.0 or newer is installed, `"box"` and `"hamming"` are also supported. By default, `"nearest"` is used. |
| `keep_aspect_ratio` | Boolean, whether to resize images to a target size without aspect ratio distortion. The image is cropped in the center with target aspect ratio before resizing. |

| Returns | |
| A PIL Image instance. | |