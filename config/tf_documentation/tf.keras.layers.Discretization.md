# tf.keras.layers.Discretization

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Discretization](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Discretization)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/discretization.py#L11-L249) |

A preprocessing layer which buckets continuous features by ranges.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Discretization(
    bin_boundaries=None,
    num_bins=None,
    epsilon=0.01,
    output_mode='int',
    sparse=False,
    dtype=None,
    name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrate `tf.feature\_column`s to Keras preprocessing layers](https://tensorflow.google.cn/guide/migrate/migrating_feature_columns) | * [Using side features: feature preprocessing](https://tensorflow.google.cn/recommenders/examples/featurization) * [Taking advantage of context features](https://tensorflow.google.cn/recommenders/examples/context_features) * [Building deep retrieval models](https://tensorflow.google.cn/recommenders/examples/deep_recommenders) |

This layer will place each element of its input data into one of several
contiguous ranges and output an integer index indicating which range each
element was placed in.

**Note:** This layer is safe to use inside a [`tf.data`](https://tensorflow.google.cn/api_docs/python/tf/data) pipeline
(independently of which backend you're using).

| Input shape | |
| Any array of dimension 2 or higher. | |

| Output shape | |
| Same as input shape. | |

| Arguments | |

|  |  |
| --- | --- |
| `bin_boundaries` | A list of bin boundaries. The leftmost and rightmost bins will always extend to `-inf` and `inf`, so `bin_boundaries=[0., 1., 2.]` generates bins `(-inf, 0.)`, `[0., 1.)`, `[1., 2.)`, and `[2., +inf)`. If this option is set, `adapt()` should not be called. |
| `num_bins` | The integer number of bins to compute. If this option is set, `adapt()` should be called to learn the bin boundaries. |
| `epsilon` | Error tolerance, typically a small fraction close to zero (e.g. 0.01). Higher values of epsilon increase the quantile approximation, and hence result in more unequal buckets, but could improve performance and resource consumption. |
| `output_mode` | Specification for the output of the layer. Values can be `"int"`, `"one_hot"`, `"multi_hot"`, or `"count"` configuring the layer as follows: |

* `"int"`: Return the discretized bin indices directly.
* `"one_hot"`: Encodes each individual element in the
  input into an array the same size as `num_bins`,
  containing a 1 at the input's bin
  index. If the last dimension is size 1, will encode on that
  dimension. If the last dimension is not size 1,
  will append a new dimension for the encoded output.
* `"multi_hot"`: Encodes each sample in the input into a
  single array the same size as `num_bins`,
  containing a 1 for each bin index
  index present in the sample.
  Treats the last dimension as the sample
  dimension, if input shape is `(..., sample_length)`,
  output shape will be `(..., num_tokens)`.
* `"count"`: As `"multi_hot"`, but the int array contains
  a count of the number of times the bin index appeared
  in the sample.
  Defaults to `"int"`.| `sparse` | Boolean. Only applicable to `"one_hot"`, `"multi_hot"`, and `"count"` output modes. Only supported with TensorFlow backend. If `True`, returns a `SparseTensor` instead of a dense `Tensor`. Defaults to `False`. |

#### Examples:

Discretize float values based on provided buckets.

```
>>> input = np.array([[-1.5, 1.0, 3.4, .5], [0.0, 3.0, 1.3, 0.0]])
>>> layer = Discretization(bin_boundaries=[0., 1., 2.])
>>> layer(input)
array([[0, 2, 3, 1],
       [1, 3, 2, 1]])
```

Discretize float values based on a number of buckets to compute.

```
>>> input = np.array([[-1.5, 1.0, 3.4, .5], [0.0, 3.0, 1.3, 0.0]])
>>> layer = Discretization(num_bins=4, epsilon=0.01)
>>> layer.adapt(input)
>>> layer(input)
array([[0, 2, 3, 2],
       [1, 3, 3, 1]])
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

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/discretization.py#L161-L199)

```
adapt(
    data, steps=None
)
```

Computes bin boundaries from quantiles in a input dataset.

Calling `adapt()` on a `Discretization` layer is an alternative to
passing in a `bin_boundaries` argument during construction. A
`Discretization` layer should always be either adapted over a dataset or
passed `bin_boundaries`.

During `adapt()`, the layer will estimate the quantile boundaries of the
input dataset. The number of quantiles can be controlled via the
`num_bins` argument, and the error tolerance for quantile boundaries can
be controlled via the `epsilon` argument.

| Arguments | |

|  |  |
| --- | --- |
| `data` | The data to train on. It can be passed either as a batched [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset), or as a NumPy array. |
| `steps` | Integer or `None`. Total number of steps (batches of samples) to process. If `data` is a [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset), and `steps` is `None`, `adapt()` will run until the input dataset is exhausted. When passing an infinitely repeating dataset, you must specify the `steps` argument. This argument is not supported with array inputs or list inputs. |

### `finalize_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/discretization.py#L206-L211)

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

### `reset_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/discretization.py#L213-L216)

```
reset_state()
```

### `symbolic_call`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/ops/operation.py#L58-L70)

```
symbolic_call(
    *args, **kwargs
)
```

### `update_state`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/discretization.py#L201-L204)

```
update_state(
    data
)
```