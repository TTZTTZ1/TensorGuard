# tf.lookup.StaticVocabularyTable

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/lookup/StaticVocabularyTable](https://tensorflow.google.cn/api_docs/python/tf/lookup/StaticVocabularyTable)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L1190-L1408) |

String to Id table that assigns out-of-vocabulary keys to hash buckets.

Inherits From: [`TrackableResource`](https://tensorflow.google.cn/api_docs/python/tf/saved_model/experimental/TrackableResource)

```
tf.lookup.StaticVocabularyTable(
    initializer,
    num_oov_buckets,
    lookup_key_dtype=None,
    name=None,
    experimental_is_anonymous=False
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Subword tokenizers](https://tensorflow.google.cn/text/guide/subwords_tokenizer) * [BERT Preprocessing with TF Text](https://tensorflow.google.cn/text/guide/bert_preprocessing_guide) | * [Load text](https://tensorflow.google.cn/tutorials/load_data/text) * [Client-efficient large-model federated learning via `federated\_select` and sparse aggregation](https://tensorflow.google.cn/federated/tutorials/sparse_federated_learning) * [Apache ORC Reader](https://tensorflow.google.cn/io/tutorials/orc) |

For example, if an instance of `StaticVocabularyTable` is initialized with a
string-to-id initializer that maps:

```
>>> init = tf.lookup.KeyValueTensorInitializer(
...     keys=tf.constant(['emerson', 'lake', 'palmer']),
...     values=tf.constant([0, 1, 2], dtype=tf.int64))
>>> table = tf.lookup.StaticVocabularyTable(
...    init,
...    num_oov_buckets=5)
```

The `Vocabulary` object will performs the following mapping:

* `emerson -> 0`
* `lake -> 1`
* `palmer -> 2`
* `<other term> -> bucket_id`, where `bucket_id` will be between `3` and
  `3 + num_oov_buckets - 1 = 7`, calculated by:
  `hash(<term>) % num_oov_buckets + vocab_size`

#### If input\_tensor is:

```
>>> input_tensor = tf.constant(["emerson", "lake", "palmer",
...                             "king", "crimson"])
>>> table[input_tensor].numpy()
array([0, 1, 2, 6, 7])
```

If `initializer` is None, only out-of-vocabulary buckets are used.

#### Example usage:

```
>>> num_oov_buckets = 3
>>> vocab = ["emerson", "lake", "palmer", "crimnson"]
>>> import tempfile
>>> f = tempfile.NamedTemporaryFile(delete=False)
>>> f.write('\n'.join(vocab).encode('utf-8'))
>>> f.close()
```

```
>>> init = tf.lookup.TextFileInitializer(
...     f.name,
...     key_dtype=tf.string, key_index=tf.lookup.TextFileIndex.WHOLE_LINE,
...     value_dtype=tf.int64, value_index=tf.lookup.TextFileIndex.LINE_NUMBER)
>>> table = tf.lookup.StaticVocabularyTable(init, num_oov_buckets)
>>> table.lookup(tf.constant(["palmer", "crimnson" , "king",
...                           "tarkus", "black", "moon"])).numpy()
array([2, 3, 5, 6, 6, 4])
```

The hash function used for generating out-of-vocabulary buckets ID is
Fingerprint64.

Note that the out-of-vocabulary bucket IDs always range from the table `size`
up to `size + num_oov_buckets - 1` regardless of the table values, which could
cause unexpected collisions:

```
>>> init = tf.lookup.KeyValueTensorInitializer(
...     keys=tf.constant(["emerson", "lake", "palmer"]),
...     values=tf.constant([1, 2, 3], dtype=tf.int64))
>>> table = tf.lookup.StaticVocabularyTable(
...     init,
...     num_oov_buckets=1)
>>> input_tensor = tf.constant(["emerson", "lake", "palmer", "king"])
>>> table[input_tensor].numpy()
array([1, 2, 3, 3])
```

| Args | |

|  |  |
| --- | --- |
| `initializer` | A `TableInitializerBase` object that contains the data used to initialize the table. If None, then we only use out-of-vocab buckets. |
| `num_oov_buckets` | Number of buckets to use for out-of-vocabulary keys. Must be greater than zero. If out-of-vocab buckets are not required, use `StaticHashTable` instead. |
| `lookup_key_dtype` | Data type of keys passed to `lookup`. Defaults to `initializer.key_dtype` if `initializer` is specified, otherwise [`tf.string`](https://tensorflow.google.cn/api_docs/python/tf#string). Must be string or integer, and must be castable to `initializer.key_dtype`. |
| `name` | A name for the operation (optional). |
| `experimental_is_anonymous` | Whether to use anonymous mode for the table (default is False). In anonymous mode, the table resource can only be accessed via a resource handle. It can't be looked up by a name. When all resource handles pointing to that resource are gone, the resource will be deleted automatically. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | when `num_oov_buckets` is not positive. |
| `TypeError` | when lookup\_key\_dtype or initializer.key\_dtype are not integer or string. Also when initializer.value\_dtype != int64. |

| Attributes | |

|  |  |
| --- | --- |
| `key_dtype` | The table key dtype. |
| `name` | The name of the table. |
| `resource_handle` | Returns the resource handle associated with this Resource. |
| `value_dtype` | The table value dtype. |

## Methods

### `lookup`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L1362-L1408)

```
lookup(
    keys, name=None
)
```

Looks up `keys` in the table, outputs the corresponding values.

It assigns out-of-vocabulary keys to buckets based in their hashes.

| Args | |

|  |  |
| --- | --- |
| `keys` | Keys to look up. May be either a `SparseTensor` or dense `Tensor`. |
| `name` | Optional name for the op. |

| Returns | |
| A `SparseTensor` if keys are sparse, a `RaggedTensor` if keys are ragged, otherwise a dense `Tensor`. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | when `keys` doesn't match the table key data type. |

### `size`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L1353-L1360)

```
size(
    name=None
)
```

Compute the number of elements in this table.

### `__getitem__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L171-L173)

```
__getitem__(
    keys
)
```

Looks up `keys` in a table, outputs the corresponding values.