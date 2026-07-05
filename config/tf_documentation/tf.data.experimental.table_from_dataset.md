# tf.data.experimental.table_from_dataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/table_from_dataset](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/table_from_dataset)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/lookup_ops.py#L102-L187) |

Returns a lookup table based on the given dataset.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.table_from_dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/table_from_dataset)

```
tf.data.experimental.table_from_dataset(
    dataset=None,
    num_oov_buckets=0,
    vocab_size=None,
    default_value=None,
    hasher_spec=lookup_ops.FastHashSpec,
    key_dtype=tf.dtypes.string,
    name=None
)

tf.dtypes.string
```

This operation constructs a lookup table based on the given dataset of pairs
of (key, value).

Any lookup of an out-of-vocabulary token will return a bucket ID based on its
hash if `num_oov_buckets` is greater than zero. Otherwise it is assigned the
`default_value`.
The bucket ID range is
`[vocabulary size, vocabulary size + num_oov_buckets - 1]`.

#### Sample Usages:

```
>>> keys = tf.data.Dataset.range(100)
>>> values = tf.data.Dataset.range(100).map(
...     lambda x: tf.strings.as_string(x * 2))
>>> ds = tf.data.Dataset.zip((keys, values))
>>> table = tf.data.experimental.table_from_dataset(
...                               ds, default_value='n/a', key_dtype=tf.int64)
>>> table.lookup(tf.constant([0, 1, 2], dtype=tf.int64)).numpy()
array([b'0', b'2', b'4'], dtype=object)
```

| Args | |

|  |  |
| --- | --- |
| `dataset` | A dataset containing (key, value) pairs. |
| `num_oov_buckets` | The number of out-of-vocabulary buckets. |
| `vocab_size` | Number of the elements in the vocabulary, if known. |
| `default_value` | The value to use for out-of-vocabulary feature values. Defaults to -1. |
| `hasher_spec` | A `HasherSpec` to specify the hash function to use for assignation of out-of-vocabulary buckets. |
| `key_dtype` | The `key` data type. |
| `name` | A name for this op (optional). |

| Returns | |
| The lookup table based on the given dataset. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If |

* `dataset` does not contain pairs
* The 2nd item in the `dataset` pairs has a dtype which is incompatible
  with `default_value`
* `num_oov_buckets` is negative
* `vocab_size` is not greater than zero
* The `key_dtype` is not integer or string