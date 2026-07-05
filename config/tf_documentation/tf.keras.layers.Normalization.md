# tf.keras.layers.Normalization

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Normalization](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Normalization)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/normalization.py#L12-L336) |

A preprocessing layer that normalizes continuous features.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Normalization(
    axis=-1, mean=None, variance=None, invert=False, **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrate `tf.feature\_column`s to Keras preprocessing layers](https://tensorflow.google.cn/guide/migrate/migrating_feature_columns) * [Working with preprocessing layers](https://tensorflow.google.cn/guide/keras/preprocessing_layers) | * [Load a pandas DataFrame](https://tensorflow.google.cn/tutorials/load_data/pandas_dataframe) * [Basic regression: Predict fuel efficiency](https://tensorflow.google.cn/tutorials/keras/regression) * [Load CSV data](https://tensorflow.google.cn/tutorials/load_data/csv) * [Simple audio recognition: Recognizing keywords](https://tensorflow.google.cn/tutorials/audio/simple_audio) * [Classify structured data using Keras preprocessing layers](https://tensorflow.google.cn/tutorials/structured_data/preprocessing_layers) |

This layer will shift and scale inputs into a distribution centered around
0 with standard deviation 1. It accomplishes this by precomputing the mean
and variance of the data, and calling `(input - mean) / sqrt(var)` at
runtime.

The mean and variance values for the layer must be either supplied on
construction or learned via `adapt()`. `adapt()` will compute the mean and
variance of the data and store them as the layer's weights. `adapt()` should
be called before `fit()`, `evaluate()`, or `predict()`.

| Args | |

|  |  |
| --- | --- |
| `axis` | Integer, tuple of integers, or None. The axis or axes that should have a separate mean and variance for each index in the shape. For example, if shape is `(None, 5)` and `axis=1`, the layer will track 5 separate mean and variance values for the last axis. If `axis` is set to `None`, the layer will normalize all elements in the input by a scalar mean and variance. When `-1`, the last axis of the input is assumed to be a feature dimension and is normalized per index. Note that in the specific case of batched scalar inputs where the only axis is the batch axis, the default will normalize each index in the batch separately. In this case, consider passing `axis=None`. Defaults to `-1`. |
| `mean` | The mean value(s) to use during normalization. The passed value(s) will be broadcast to the shape of the kept axes above; if the value(s) cannot be broadcast, an error will be raised when this layer's `build()` method is called. |
| `variance` | The variance value(s) to use during normalization. The passed value(s) will be broadcast to the shape of the kept axes above; if the value(s) cannot be broadcast, an error will be raised when this layer's `build()` method is called. |
| `invert` | If `True`, this layer will apply the inverse transformation to its inputs: it would turn a normalized input back into its original form. |

#### Examples:

Calculate a global mean and variance by analyzing the dataset in `adapt()`.

```
>>> adapt_data = np.array([1., 2., 3., 4., 5.], dtype='float32')
>>> input_data = np.array([1., 2., 3.], dtype='float32')
>>> layer = keras.layers.Normalization(axis=None)
>>> layer.adapt(adapt_data)
>>> layer(input_data)
array([-1.4142135, -0.70710677, 0.], dtype=float32)
```

Calculate a mean and variance for each index on the last axis.

```
>>> adapt_data = np.array([[0., 7., 4.],
...                        [2., 9., 6.],
...                        [0., 7., 4.],
...                        [2., 9., 6.]], dtype='float32')
>>> input_data = np.array([[0., 7., 4.]], dtype='float32')
>>> layer = keras.layers.Normalization(axis=-1)
>>> layer.adapt(adapt_data)
>>> layer(input_data)
array([-1., -1., -1.], dtype=float32)
```

Pass the mean and variance directly.

```
>>> input_data = np.array([[1.], [2.], [3.]], dtype='float32')
>>> layer = keras.layers.Normalization(mean=3., variance=2.)
>>> layer(input_data)
array([[-1.4142135 ],
       [-0.70710677],
       [ 0.        ]], dtype=float32)
```

Use the layer to de-normalize inputs (after adapting the layer).

```
>>> adapt_data = np.array([[0., 7., 4.],
...                        [2., 9., 6.],
...                        [0., 7., 4.],
...                        [2., 9., 6.]], dtype='float32')
>>> input_data = np.array([[1., 2., 3.]], dtype='float32')
>>> layer = keras.layers.Normalization(axis=-1, invert=True)
>>> layer.adapt(adapt_data)
>>> layer(input_data)
array([2., 10., 8.], dtype=float32)
```

| Attributes | |

|  |  |
| --- | --- |
| `input` | Retrieves the input tensor(s) of a symbolic operation. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `output` | Retrieves the output tensor(s) of a layer. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.

## Methods

### `adapt`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/normalization.py#L197-L281)

```
adapt(
    data
)
```

Computes the mean and variance of values in a dataset.

Calling `adapt()` on a `Normalization` layer is an alternative to
passing in `mean` and `variance` arguments during layer construction. A
`Normalization` layer should always either be adapted over a dataset or
passed `mean` and `variance`.

During `adapt()`, the layer will compute a `mean` and `variance`
separately for each position in each axis specified by the `axis`
argument. To calculate a single `mean` and `variance` over the input
data, simply pass `axis=None` to the layer.

| Arg | |

|  |  |
| --- | --- |
| `data` | The data to train on. It can be passed either as a [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset), as a NumPy array, or as a backend-native eager tensor. If a dataset, *it must be batched*. Keras will assume that the data is batched, and if that assumption doesn't hold, the mean and variance may be incorrectly computed. |

### `finalize_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/normalization.py#L283-L292)

```
finalize_state()
```

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation.py#L191-L213)

```
@classmethod
from_config(
    config
)
```

Creates a layer from its config.

This method is the reverse of `get_config`,
capable of instantiating the same layer from the config
dictionary. It does not handle layer connectivity
(handled by Network), nor weights (handled by `set_weights`).

| Args | |

|  |  |
| --- | --- |
| `config` | A Python dictionary, typically the output of get\_config. |

| Returns | |
| A layer instance. | |

### `symbolic_call`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation.py#L58-L70)

```
symbolic_call(
    *args, **kwargs
)
```