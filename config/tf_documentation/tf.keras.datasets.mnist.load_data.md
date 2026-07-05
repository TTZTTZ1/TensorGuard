# tf.keras.datasets.mnist.load_data

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/datasets/mnist/load_data](https://tensorflow.google.cn/api_docs/python/tf/keras/datasets/mnist/load_data)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/datasets/mnist.py#L9-L71) |

Loads the MNIST dataset.

```
tf.keras.datasets.mnist.load_data(
    path='mnist.npz'
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Import a JAX model using JAX2TF](https://tensorflow.google.cn/guide/jax2tf) * [Mixed precision](https://tensorflow.google.cn/guide/mixed_precision) * [Multi-GPU and distributed training](https://tensorflow.google.cn/guide/keras/distributed_training) * [Weight clustering in Keras example](https://tensorflow.google.cn/model_optimization/guide/clustering/clustering_example) * [Pruning in Keras example](https://tensorflow.google.cn/model_optimization/guide/pruning/pruning_with_keras) | * [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://tensorflow.google.cn/tutorials/distribute/multi_worker_with_ctl) * [Multi-worker training with Keras](https://tensorflow.google.cn/tutorials/distribute/multi_worker_with_keras) * [Convolutional Variational Autoencoder](https://tensorflow.google.cn/tutorials/generative/cvae) * [Deep Convolutional Generative Adversarial Network](https://tensorflow.google.cn/tutorials/generative/dcgan) * [Save and load models](https://tensorflow.google.cn/tutorials/keras/save_and_load) |

This is a dataset of 60,000 28x28 grayscale images of the 10 digits,
along with a test set of 10,000 images.
More info can be found at the
[MNIST homepage](http://yann.lecun.com/exdb/mnist/).

| Args | |

|  |  |
| --- | --- |
| `path` | path where to cache the dataset locally (relative to `~/.keras/datasets`). |

| Returns | |
| Tuple of NumPy arrays: `(x_train, y_train), (x_test, y_test)`. | |

**`x_train`**: `uint8` NumPy array of grayscale image data with shapes
`(60000, 28, 28)`, containing the training data. Pixel values range
from 0 to 255.

**`y_train`**: `uint8` NumPy array of digit labels (integers in range 0-9)
with shape `(60000,)` for the training data.

**`x_test`**: `uint8` NumPy array of grayscale image data with shapes
`(10000, 28, 28)`, containing the test data. Pixel values range
from 0 to 255.

**`y_test`**: `uint8` NumPy array of digit labels (integers in range 0-9)
with shape `(10000,)` for the test data.

#### Example:

```
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
assert x_train.shape == (60000, 28, 28)
assert x_test.shape == (10000, 28, 28)
assert y_train.shape == (60000,)
assert y_test.shape == (10000,)
```

#### License:

Yann LeCun and Corinna Cortes hold the copyright of MNIST dataset,
which is a derivative work from original NIST datasets.
MNIST dataset is made available under the terms of the
[Creative Commons Attribution-Share Alike 3.0 license.](https://creativecommons.org/licenses/by-sa/3.0/)