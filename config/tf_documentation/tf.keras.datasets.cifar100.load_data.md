# tf.keras.datasets.cifar100.load_data

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/datasets/cifar100/load_data](https://tensorflow.google.cn/api_docs/python/tf/keras/datasets/cifar100/load_data)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/datasets/cifar100.py#L13-L85) |

Loads the CIFAR100 dataset.

```
tf.keras.datasets.cifar100.load_data(
    label_mode='fine'
)
```

This is a dataset of 50,000 32x32 color training images and
10,000 test images, labeled over 100 fine-grained classes that are
grouped into 20 coarse-grained classes. See more info at the
[CIFAR homepage](https://www.cs.toronto.edu/%7Ekriz/cifar.html).

| Args | |

|  |  |
| --- | --- |
| `label_mode` | one of `"fine"`, `"coarse"`. If it is `"fine"`, the category labels are the fine-grained labels, and if it is `"coarse"`, the output labels are the coarse-grained superclasses. |

| Returns | |
| Tuple of NumPy arrays: `(x_train, y_train), (x_test, y_test)`. | |

**`x_train`**: `uint8` NumPy array of grayscale image data with shapes
`(50000, 32, 32, 3)`, containing the training data. Pixel values range
from 0 to 255.

**`y_train`**: `uint8` NumPy array of labels (integers in range 0-99)
with shape `(50000, 1)` for the training data.

**`x_test`**: `uint8` NumPy array of grayscale image data with shapes
`(10000, 32, 32, 3)`, containing the test data. Pixel values range
from 0 to 255.

**`y_test`**: `uint8` NumPy array of labels (integers in range 0-99)
with shape `(10000, 1)` for the test data.

#### Example:

```
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar100.load_data()
assert x_train.shape == (50000, 32, 32, 3)
assert x_test.shape == (10000, 32, 32, 3)
assert y_train.shape == (50000, 1)
assert y_test.shape == (10000, 1)
```