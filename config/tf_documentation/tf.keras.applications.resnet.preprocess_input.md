# tf.keras.applications.resnet.preprocess_input

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/applications/resnet/preprocess_input](https://tensorflow.google.cn/api_docs/python/tf/keras/applications/resnet/preprocess_input)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/applications/resnet.py#L497-L506) |

Preprocesses a tensor or Numpy array encoding a batch of images.

#### View aliases

**Main aliases**

[`tf.keras.applications.resnet50.preprocess_input`](https://tensorflow.google.cn/api_docs/python/tf/keras/applications/resnet/preprocess_input)

```
tf.keras.applications.resnet.preprocess_input(
    x, data_format=None
)
```

Usage example with [`applications.MobileNet`](https://tensorflow.google.cn/api_docs/python/tf/keras/applications/MobileNet):

```
i = keras.layers.Input([None, None, 3], dtype="uint8")
x = ops.cast(i, "float32")
x = keras.applications.mobilenet.preprocess_input(x)
core = keras.applications.MobileNet()
x = core(x)
model = keras.Model(inputs=[i], outputs=[x])
result = model(image)
```

| Args | |

|  |  |
| --- | --- |
| `x` | A floating point [`numpy.array`](https://tensorflow.google.cn/api_docs/python/tf/keras/ops/array) or a backend-native tensor, 3D or 4D with 3 color channels, with values in the range [0, 255]. The preprocessed data are written over the input data if the data types are compatible. To avoid this behaviour, [`numpy.copy(x)`](https://tensorflow.google.cn/api_docs/python/tf/keras/ops/copy) can be used. |
| `data_format` | Optional data format of the image tensor/array. None, means the global setting [`keras.backend.image_data_format()`](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/image_data_format) is used (unless you changed it, it uses "channels\_last"). Defaults to `None`. |

| Returns | |
| Preprocessed array with type `float32`. | |

The images are converted from RGB to BGR, then each color channel is
zero-centered with respect to the ImageNet dataset, without scaling.

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | In case of unknown `data_format` argument. |