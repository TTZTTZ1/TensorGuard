# tf.lookup.experimental.MutableHashTable

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/lookup/experimental/MutableHashTable](https://tensorflow.google.cn/api_docs/python/tf/lookup/experimental/MutableHashTable)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L1798-L2107) |

A generic mutable hash table implementation.

Inherits From: [`TrackableResource`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/experimental/TrackableResource)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.lookup.experimental.MutableHashTable`](https://tensorflow.google.cn/api_docs/python/tf/lookup/experimental/MutableHashTable)

```
tf.lookup.experimental.MutableHashTable(
    key_dtype,
    value_dtype,
    default_value,
    name='MutableHashTable',
    checkpoint=True,
    experimental_is_anonymous=False
)
```

Data can be inserted by calling the `insert` method and removed by calling the
`remove` method. It does not support initialization via the init method.

`MutableHashTable` requires additional memory during checkpointing and restore
operations to create temporary key and value tensors.

#### Example usage:

```
>>> table = tf.lookup.experimental.MutableHashTable(key_dtype=tf.string,
...                                                 value_dtype=tf.int64,
...                                                 default_value=-1)
>>> keys_tensor = tf.constant(['a', 'b', 'c'])
>>> vals_tensor = tf.constant([7, 8, 9], dtype=tf.int64)
>>> input_tensor = tf.constant(['a', 'f'])
>>> table.insert(keys_tensor, vals_tensor)
>>> table.lookup(input_tensor).numpy()
array([ 7, -1])
>>> table.remove(tf.constant(['c']))
>>> table.lookup(keys_tensor).numpy()
array([ 7, 8, -1])
>>> sorted(table.export()[0].numpy())
[b'a', b'b']
>>> sorted(table.export()[1].numpy())
[7, 8]
```

| Args | |

|  |  |
| --- | --- |
| `key_dtype` | the type of the key tensors. |
| `value_dtype` | the type of the value tensors. |
| `default_value` | The value to use if a key is missing in the table. |
| `name` | A name for the operation (optional). |
| `checkpoint` | if True, the contents of the table are saved to and restored from checkpoints. If `shared_name` is empty for a checkpointed table, it is shared using the table node name. |
| `experimental_is_anonymous` | Whether to use anonymous mode for the table (default is False). In anonymous mode, the table resource can only be accessed via a resource handle. It can't be looked up by a name. When all resource handles pointing to that resource are gone, the resource will be deleted automatically. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If checkpoint is True and no name was specified. |

| Attributes | |

|  |  |
| --- | --- |
| `key_dtype` | The table key dtype. |
| `name` | The name of the table. |
| `resource_handle` | Returns the resource handle associated with this Resource. |
| `value_dtype` | The table value dtype. |

## Methods

### `export`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L2038-L2053)

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

### `insert`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L2011-L2036)

```
insert(
    keys, values, name=None
)
```

Associates `keys` with `values`.

| Args | |

|  |  |
| --- | --- |
| `keys` | Keys to insert. Can be a tensor of any shape. Must match the table's key type. |
| `values` | Values to be associated with keys. Must be a tensor of the same shape as `keys` and match the table's value type. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | when `keys` or `values` doesn't match the table data types. |

### `lookup`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L1968-L2009)

```
lookup(
    keys, dynamic_default_values=None, name=None
)
```

Looks up `keys` in a table, outputs the corresponding values.

The `default_value` is used for keys not present in the table.

| Args | |

|  |  |
| --- | --- |
| `keys` | Keys to look up. Can be a tensor of any shape. Must match the table's key\_dtype. |
| `dynamic_default_values` | The values to use if a key is missing in the table. If None (by default), the `table.default_value` will be used. Shape of `dynamic_default_values` must be same with `table.default_value` or the lookup result tensor. In the latter case, each key will have a different default value. |

For example:

```
  keys = [0, 1, 3]
  dynamic_default_values = [[1, 3, 4], [2, 3, 9], [8, 3, 0]]

  # The key '0' will use [1, 3, 4] as default value.
  # The key '1' will use [2, 3, 9] as default value.
  # The key '3' will use [8, 3, 0] as default value.
```

|  |  |
| --- | --- |
| `name` | A name for the operation (optional). |

| Returns | |
| A tensor containing the values in the same shape as `keys` using the table's value type. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | when `keys` do not match the table data types. |

### `remove`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L1942-L1966)

```
remove(
    keys, name=None
)
```

Removes `keys` and its associated values from the table.

If a key is not present in the table, it is silently ignored.

| Args | |

|  |  |
| --- | --- |
| `keys` | Keys to remove. Can be a tensor of any shape. Must match the table's key type. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | when `keys` do not match the table data types. |

### `size`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L1929-L1940)

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