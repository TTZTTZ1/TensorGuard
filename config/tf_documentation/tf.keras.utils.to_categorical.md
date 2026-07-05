# tf.keras.utils.to_categorical

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/utils/to_categorical](https://tensorflow.google.cn/api_docs/python/tf/keras/utils/to_categorical)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/utils/numerical_utils.py#L37-L92) |

Converts a class vector (integers) to binary class matrix.

```
tf.keras.utils.to_categorical(
    x, num_classes=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Implement Differential Privacy with TensorFlow Privacy](https://tensorflow.google.cn/responsible_ai/privacy/tutorials/classification_privacy) * [Assess privacy risks with the TensorFlow Privacy Report](https://tensorflow.google.cn/responsible_ai/privacy/tutorials/privacy_report) * [On-Device Training with TensorFlow Lite](https://tensorflow.google.cn/lite/examples/on_device_training/overview) * [Human Pose Classification with MoveNet and TensorFlow Lite](https://tensorflow.google.cn/lite/tutorials/pose_classification) * [Classifying CIFAR-10 with XLA](https://tensorflow.google.cn/xla/tf2xla/tutorials/autoclustering_xla) |

E.g. for use with `categorical_crossentropy`.

| Args | |

|  |  |
| --- | --- |
| `x` | Array-like with class values to be converted into a matrix (integers from 0 to `num_classes - 1`). |
| `num_classes` | Total number of classes. If `None`, this would be inferred as `max(x) + 1`. Defaults to `None`. |

| Returns | |
| A binary matrix representation of the input as a NumPy array. The class axis is placed last. | |

#### Example:

```
>>> a = keras.utils.to_categorical([0, 1, 2, 3], num_classes=4)
>>> print(a)
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
```

```
>>> b = np.array([.9, .04, .03, .03,
...               .3, .45, .15, .13,
...               .04, .01, .94, .05,
...               .12, .21, .5, .17],
...               shape=[4, 4])
>>> loss = keras.ops.categorical_crossentropy(a, b)
>>> print(np.around(loss, 5))
[0.10536 0.82807 0.1011  1.77196]
```

```
>>> loss = keras.ops.categorical_crossentropy(a, a)
>>> print(np.around(loss, 5))
[0. 0. 0. 0.]
```