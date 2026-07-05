# tf.keras.layers.CategoryEncoding

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/CategoryEncoding](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/CategoryEncoding)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/category_encoding.py#L7-L206) |

A preprocessing layer which encodes integer features.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.CategoryEncoding(
    num_tokens=None, output_mode='multi_hot', sparse=False, **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrate `tf.feature\_column`s to Keras preprocessing layers](https://tensorflow.google.cn/guide/migrate/migrating_feature_columns) * [Working with preprocessing layers](https://tensorflow.google.cn/guide/keras/preprocessing_layers) | * [Load CSV data](https://tensorflow.google.cn/tutorials/load_data/csv) * [Classify structured data using Keras preprocessing layers](https://tensorflow.google.cn/tutorials/structured_data/preprocessing_layers) |

This layer provides options for condensing data into a categorical encoding
when the total number of tokens are known in advance. It accepts integer
values as inputs, and it outputs a dense or sparse representation of those
inputs. For integer inputs where the total number of tokens is not known,
use [`keras.layers.IntegerLookup`](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/IntegerLookup) instead.

**Note:** This layer is safe to use inside a [`tf.data`](https://tensorflow.google.cn/api_docs/python/tf/data) pipeline
(independently of which backend you're using).

#### Examples:

**One-hot encoding data**

```
>>> layer = keras.layers.CategoryEncoding(
...           num_tokens=4, output_mode="one_hot")
>>> layer([3, 2, 0, 1])
array([[0., 0., 0., 1.],
        [0., 0., 1., 0.],
        [1., 0., 0., 0.],
        [0., 1., 0., 0.]]>
```

**Multi-hot encoding data**

```
>>> layer = keras.layers.CategoryEncoding(
...           num_tokens=4, output_mode="multi_hot")
>>> layer([[0, 1], [0, 0], [1, 2], [3, 1]])
array([[1., 1., 0., 0.],
        [1., 0., 0., 0.],
        [0., 1., 1., 0.],
        [0., 1., 0., 1.]]>
```

**Using weighted inputs in `"count"` mode**

```
>>> layer = keras.layers.CategoryEncoding(
...           num_tokens=4, output_mode="count")
>>> count_weights = np.array([[.1, .2], [.1, .1], [.2, .3], [.4, .2]])
>>> layer([[0, 1], [0, 0], [1, 2], [3, 1]], count_weights=count_weights)
  array([[0.1, 0.2, 0. , 0. ],
         [0.2, 0. , 0. , 0. ],
         [0. , 0.2, 0.3, 0. ],
         [0. , 0.2, 0. , 0.4]]>
```

| Args | |

|  |  |
| --- | --- |
| `num_tokens` | The total number of tokens the layer should support. All inputs to the layer must integers in the range `0 <= value < num_tokens`, or an error will be thrown. |
| `output_mode` | Specification for the output of the layer. Values can be `"one_hot"`, `"multi_hot"` or `"count"`, configuring the layer as follows: |

```
- `"one_hot"`: Encodes each individual element in the input
    into an array of `num_tokens` size, containing a 1 at the
    element index. If the last dimension is size 1, will encode
    on that dimension. If the last dimension is not size 1,
    will append a new dimension for the encoded output.
- `"multi_hot"`: Encodes each sample in the input into a single
    array of `num_tokens` size, containing a 1 for each
    vocabulary term present in the sample. Treats the last
    dimension as the sample dimension, if input shape is
    `(..., sample_length)`, output shape will be
    `(..., num_tokens)`.
- `"count"`: Like `"multi_hot"`, but the int array contains a
    count of the number of times the token at that index
    appeared in the sample.
```

For all output modes, currently only output up to rank 2 is
supported.
Defaults to `"multi_hot"`.| `sparse` | Whether to return a sparse tensor; for backends that support sparse tensors. |

| Call arguments | |

|  |  |
| --- | --- |
| `inputs` | A 1D or 2D tensor of integer inputs. |
| `count_weights` | A tensor in the same shape as `inputs` indicating the weight for each sample value when summing up in `count` mode. Not used in `"multi_hot"` or `"one_hot"` modes. |

| Attributes | |

|  |  |
| --- | --- |
| `input` | Retrieves the input tensor(s) of a symbolic operation. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.| `output` | Retrieves the output tensor(s) of a layer. |

Only returns the tensor(s) corresponding to the *first time*
the operation was called.

## Methods

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