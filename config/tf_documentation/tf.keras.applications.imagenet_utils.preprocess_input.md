# tf.keras.applications.imagenet_utils.preprocess_input

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/applications/imagenet_utils/preprocess_input](https://tensorflow.google.cn/api_docs/python/tf/keras/applications/imagenet_utils/preprocess_input)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/applications/imagenet_utils.py#L86-L106) |

Preprocesses a tensor or Numpy array encoding a batch of images.

```
tf.keras.applications.imagenet_utils.preprocess_input(
    x, data_format=None, mode='caffe'
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
| x: A floating point [`numpy.array`](https://tensorflow.google.cn/api_docs/python/tf/keras/ops/array) or a backend-native tensor, 3D or 4D with 3 color channels, with values in the range [0, 255]. The preprocessed data are written over the input data if the data types are compatible. To avoid this behaviour, [`numpy.copy(x)`](https://tensorflow.google.cn/api_docs/python/tf/keras/ops/copy) can be used. data\_format: Optional data format of the image tensor/array. None, means the global setting [`keras.backend.image_data_format()`](https://tensorflow.google.cn/api_docs/python/tf/keras/backend/image_data_format) is used (unless you changed it, it uses "channels\_last"). | |
| `mode` | One of "caffe", "tf" or "torch". |

* caffe: will convert the images from RGB to BGR,
  then will zero-center each color channel with
  respect to the ImageNet dataset,
  without scaling.
* tf: will scale pixels between -1 and 1,
  sample-wise.
* torch: will scale pixels between 0 and 1 and then
  will normalize each channel with respect to the
  ImageNet dataset.
  Defaults to `"caffe"`.

  Defaults to `None`.

| Returns | |
| Preprocessed array with type `float32`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | In case of unknown `mode` or `data_format` argument. |