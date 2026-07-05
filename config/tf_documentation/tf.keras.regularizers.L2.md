# tf.keras.regularizers.L2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/regularizers/L2](https://tensorflow.google.cn/api_docs/python/tf/keras/regularizers/L2)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/regularizers/regularizers.py#L242-L268) |

A regularizer that applies a L2 regularization penalty.

Inherits From: [`Regularizer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Regularizer)

#### View aliases

**Main aliases**

[`tf.keras.regularizers.l2`](https://tensorflow.google.cn/api_docs/python/tf/keras/regularizers/L2)

```
tf.keras.regularizers.L2(
    l2=0.01
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Distributed training with TensorFlow](https://tensorflow.google.cn/guide/distributed_training) * [Effective Tensorflow 2](https://tensorflow.google.cn/guide/effective_tf2) * [Use TF1.x models in TF2 workflows](https://tensorflow.google.cn/guide/migrate/model_mapping) | * [Overfit and underfit](https://tensorflow.google.cn/tutorials/keras/overfit_and_underfit) * [Custom training with tf.distribute.Strategy](https://tensorflow.google.cn/tutorials/distribute/custom_training) * [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://tensorflow.google.cn/tutorials/distribute/multi_worker_with_ctl) * [Parameter server training with ParameterServerStrategy](https://tensorflow.google.cn/tutorials/distribute/parameter_server_training) * [Retraining an Image Classifier](https://tensorflow.google.cn/hub/tutorials/tf2_image_retraining) |

The L2 regularization penalty is computed as:
`loss = l2 * reduce_sum(square(x))`

L2 may be passed to a layer as a string identifier:

```
>>> dense = Dense(3, kernel_regularizer='l2')
```

In this case, the default value used is `l2=0.01`.

| Arguments | |

|  |  |
| --- | --- |
| `l2` | float, L2 regularization factor. |

## Methods

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/regularizers/regularizers.py#L127-L145)

```
@classmethod
from_config(
    config
)
```

Creates a regularizer from its config.

This method is the reverse of `get_config`,
capable of instantiating the same regularizer from the config
dictionary.

This method is used by Keras `model_to_estimator`, saving and
loading models to HDF5 formats, Keras model cloning, some visualization
utilities, and exporting models to and from JSON.

| Args | |

|  |  |
| --- | --- |
| `config` | A Python dictionary, typically the output of get\_config. |

| Returns | |
| A regularizer instance. | |

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/regularizers/regularizers.py#L267-L268)

```
get_config()
```

Returns the config of the regularizer.

An regularizer config is a Python dictionary (serializable)
containing all configuration parameters of the regularizer.
The same regularizer can be reinstantiated later
(without any saved state) from this configuration.

This method is optional if you are just training and executing models,
exporting to and from SavedModels, or using weight checkpoints.

This method is required for Keras `model_to_estimator`, saving and
loading models to HDF5 formats, Keras model cloning, some visualization
utilities, and exporting models to and from JSON.

| Returns | |
| Python dictionary. | |

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/regularizers/regularizers.py#L264-L265)

```
__call__(
    x
)
```

Compute a regularization penalty from an input tensor.