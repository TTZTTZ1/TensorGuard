# tf.data.experimental.DatasetInitializer

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/DatasetInitializer](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/DatasetInitializer)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/lookup_ops.py#L54-L99) |

Creates a table initializer from a [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.DatasetInitializer`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/DatasetInitializer)

```
tf.data.experimental.DatasetInitializer(
    dataset
)
```

#### Sample usage:

```
>>> keys = tf.data.Dataset.range(100)
>>> values = tf.data.Dataset.range(100).map(
...     lambda x: tf.strings.as_string(x * 2))
>>> ds = tf.data.Dataset.zip((keys, values))
>>> init = tf.data.experimental.DatasetInitializer(ds)
>>> table = tf.lookup.StaticHashTable(init, "")
>>> table.lookup(tf.constant([0, 1, 2], dtype=tf.int64)).numpy()
array([b'0', b'2', b'4'], dtype=object)
```

Raises: ValueError if `dataset` doesn't conform to specifications.

| Args | |

|  |  |
| --- | --- |
| `dataset` | A [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) object that produces tuples of scalars. The first scalar is treated as a key and the second as value. |

| Attributes | |

|  |  |
| --- | --- |
| `dataset` | A [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) object that produces tuples of scalars. The first scalar is treated as a key and the second as value. |
| `key_dtype` | The expected table key dtype. |
| `value_dtype` | The expected table value dtype. |

## Methods

### `initialize`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/lookup_ops.py#L94-L99)

```
initialize(
    table
)
```

Returns the table initialization op.