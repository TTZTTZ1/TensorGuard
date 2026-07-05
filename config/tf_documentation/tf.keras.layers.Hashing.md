# tf.keras.layers.Hashing

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Hashing](https://tensorflow.google.cn/api_docs/python/tf/keras/layers/Hashing)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/layers/preprocessing/hashing.py#L9-L281) |

A preprocessing layer which hashes and bins categorical features.

Inherits From: [`Layer`](https://tensorflow.google.cn/api_docs/python/tf/keras/Layer), [`Operation`](https://tensorflow.google.cn/api_docs/python/tf/keras/Operation)

```
tf.keras.layers.Hashing(
    num_bins,
    mask_value=None,
    salt=None,
    output_mode='int',
    sparse=False,
    **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Working with preprocessing layers](https://tensorflow.google.cn/guide/keras/preprocessing_layers) | * [Using side features: feature preprocessing](https://tensorflow.google.cn/recommenders/examples/featurization) |

This layer transforms categorical inputs to hashed output. It element-wise
converts a ints or strings to ints in a fixed range. The stable hash
function uses `tensorflow::ops::Fingerprint` to produce the same output
consistently across all platforms.

This layer uses [FarmHash64](https://github.com/google/farmhash) by default,
which provides a consistent hashed output across different platforms and is
stable across invocations, regardless of device and context, by mixing the
input bits thoroughly.

If you want to obfuscate the hashed output, you can also pass a random
`salt` argument in the constructor. In that case, the layer will use the
[SipHash64](https://github.com/google/highwayhash) hash function, with
the `salt` value serving as additional input to the hash function.

**Note:** This layer internally uses TensorFlow. It cannot
be used as part of the compiled computation graph of a model with
any backend other than TensorFlow.
It can however be used with any backend when running eagerly.
It can also always be used as part of an input preprocessing pipeline
with any backend (outside the model itself), which is how we recommend
to use this layer.**Note:** This layer is safe to use inside a [`tf.data`](https://tensorflow.google.cn/api_docs/python/tf/data) pipeline
(independently of which backend you're using).

**Example (FarmHash64)**

```
>>> layer = keras.layers.Hashing(num_bins=3)
>>> inp = [['A'], ['B'], ['C'], ['D'], ['E']]
>>> layer(inp)
array([[1],
        [0],
        [1],
        [1],
        [2]])>
```

**Example (FarmHash64) with a mask value**

```
>>> layer = keras.layers.Hashing(num_bins=3, mask_value='')
>>> inp = [['A'], ['B'], [''], ['C'], ['D']]
>>> layer(inp)
array([[1],
        [1],
        [0],
        [2],
        [2]])
```

**Example (SipHash64)**

```
>>> layer = keras.layers.Hashing(num_bins=3, salt=[133, 137])
>>> inp = [['A'], ['B'], ['C'], ['D'], ['E']]
>>> layer(inp)
array([[1],
        [2],
        [1],
        [0],
        [2]])
```

**Example (Siphash64 with a single integer, same as `salt=[133, 133]`)**

```
>>> layer = keras.layers.Hashing(num_bins=3, salt=133)
>>> inp = [['A'], ['B'], ['C'], ['D'], ['E']]
>>> layer(inp)
array([[0],
        [0],
        [2],
        [1],
        [0]])
```

| Args | |

|  |  |
| --- | --- |
| `num_bins` | Number of hash bins. Note that this includes the `mask_value` bin, so the effective number of bins is `(num_bins - 1)` if `mask_value` is set. |
| `mask_value` | A value that represents masked inputs, which are mapped to index 0. `None` means no mask term will be added and the hashing will start at index 0. Defaults to `None`. |
| `salt` | A single unsigned integer or None. If passed, the hash function used will be SipHash64, with these values used as an additional input (known as a "salt" in cryptography). These should be non-zero. If `None`, uses the FarmHash64 hash function. It also supports tuple/list of 2 unsigned integer numbers, see reference paper for details. Defaults to `None`. |
| `output_mode` | Specification for the output of the layer. Values can be `"int"`, `"one_hot"`, `"multi_hot"`, or `"count"` configuring the layer as follows: |

* `"int"`: Return the integer bin indices directly.
* `"one_hot"`: Encodes each individual element in the input into an
  array the same size as `num_bins`, containing a 1
  at the input's bin index. If the last dimension is size 1,
  will encode on that dimension.
  If the last dimension is not size 1, will append a new
  dimension for the encoded output.
* `"multi_hot"`: Encodes each sample in the input into a
  single array the same size as `num_bins`,
  containing a 1 for each bin index
  index present in the sample. Treats the last dimension
  as the sample dimension, if input shape is
  `(..., sample_length)`, output shape will be
  `(..., num_tokens)`.
* `"count"`: As `"multi_hot"`, but the int array contains a count of
  the number of times the bin index appeared in the sample.
  Defaults to `"int"`.| `sparse` | Boolean. Only applicable to `"one_hot"`, `"multi_hot"`, and `"count"` output modes. Only supported with TensorFlow backend. If `True`, returns a `SparseTensor` instead of a dense `Tensor`. Defaults to `False`. |
  | `**kwargs` | Keyword arguments to construct a layer. |

| Input shape | |
| A single string, a list of strings, or an `int32` or `int64` tensor of shape `(batch_size, ...,)`. | |

| Output shape | |
| An `int32` tensor of shape `(batch_size, ...)`. | |

#### Reference:

* [SipHash with salt](https://www.131002.net/siphash/siphash.pdf)

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