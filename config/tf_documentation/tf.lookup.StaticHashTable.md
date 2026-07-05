# tf.lookup.StaticHashTable

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/lookup/StaticHashTable](https://tensorflow.google.cn/api_docs/python/tf/lookup/StaticHashTable)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L281-L413) |

A generic hash table that is immutable once initialized.

Inherits From: [`TrackableResource`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/experimental/TrackableResource)

```
tf.lookup.StaticHashTable(
    initializer, default_value, name=None, experimental_is_anonymous=False
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Federated Learning for Text Generation](https://tensorflow.google.cn/federated/tutorials/federated_learning_for_text_generation) * [Client-efficient large-model federated learning via `federated\_select` and sparse aggregation](https://tensorflow.google.cn/federated/tutorials/sparse_federated_learning) * [Feature Engineering using TFX Pipeline and TensorFlow Transform](https://tensorflow.google.cn/tfx/tutorials/tfx/penguin_tft) * [Preprocessing data with TensorFlow Transform](https://tensorflow.google.cn/tfx/tutorials/transform/census) |

#### Example usage:

```
>>> keys_tensor = tf.constant(['a', 'b', 'c'])
>>> vals_tensor = tf.constant([7, 8, 9])
>>> input_tensor = tf.constant(['a', 'f'])
>>> table = tf.lookup.StaticHashTable(
...     tf.lookup.KeyValueTensorInitializer(keys_tensor, vals_tensor),
...     default_value=-1)
>>> table.lookup(input_tensor).numpy()
array([ 7, -1], dtype=int32)
```

Or for more pythonic code:

```
>>> table[input_tensor].numpy()
array([ 7, -1], dtype=int32)
```

The result of a lookup operation has the same shape as the argument:

```
>>> input_tensor = tf.constant([['a', 'b'], ['c', 'd']])
>>> table[input_tensor].numpy()
array([[ 7,  8],
       [ 9, -1]], dtype=int32)
```

| Args | |

|  |  |
| --- | --- |
| `initializer` | The table initializer to use. See `HashTable` kernel for supported key and value types. |
| `default_value` | The value to use if a key is missing in the table. |
| `name` | A name for the operation (optional). |
| `experimental_is_anonymous` | Whether to use anonymous mode for the table (default is False). In anonymous mode, the table resource can only be accessed via a resource handle. It can't be looked up by a name. When all resource handles pointing to that resource are gone, the resource will be deleted automatically. |

| Attributes | |

|  |  |
| --- | --- |
| `default_value` | The default value of the table. |
| `key_dtype` | The table key dtype. |
| `name` | The name of the table. |
| `resource_handle` | Returns the resource handle associated with this Resource. |
| `value_dtype` | The table value dtype. |

## Methods

### `export`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L378-L394)

```
export(
    name=None
)
```

Returns tensors of all keys and values in the table.

| Args | |

|  |  |
| --- | --- |
| `name` | A name for the operation (optional). |

| Returns | |
| A pair of tensors with the first tensor containing all keys and the second tensors containing all values in the table. | |

### `lookup`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L229-L271)

```
lookup(
    keys, name=None
)
```

Looks up `keys` in a table, outputs the corresponding values.

The `default_value` is used for keys not present in the table.

| Args | |

|  |  |
| --- | --- |
| `keys` | Keys to look up. May be either a `SparseTensor` or dense `Tensor`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `SparseTensor` if keys are sparse, a `RaggedTensor` if keys are ragged, otherwise a dense `Tensor`. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | when `keys` or `default_value` doesn't match the table data types. |

### `size`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L217-L227)

```
size(
    name=None
)
```

Compute the number of elements in this table.

| Args | |

|  |  |
| --- | --- |
| `name` | A name for the operation (optional). |

| Returns | |
| A scalar tensor containing the number of elements in this table. | |

### `__getitem__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L171-L173)

```
__getitem__(
    keys
)
```

Looks up `keys` in a table, outputs the corresponding values.