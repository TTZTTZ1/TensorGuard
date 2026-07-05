# tf.data.experimental.get_next_as_optional

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/get_next_as_optional](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/get_next_as_optional)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/iterator_ops.py#L996-L1012) |

Returns a [`tf.experimental.Optional`](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional) with the next element of the iterator. (deprecated)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.get_next_as_optional`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/get_next_as_optional)

```
tf.data.experimental.get_next_as_optional(
    iterator
)
```

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use [`tf.data.Iterator.get_next_as_optional()`](https://tensorflow.google.cn/api_docs/python/tf/data/Iterator#get_next_as_optional) instead.

If the iterator has reached the end of the sequence, the returned
[`tf.experimental.Optional`](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional) will have no value.

| Args | |

|  |  |
| --- | --- |
| `iterator` | A [`tf.data.Iterator`](https://tensorflow.google.cn/api_docs/python/tf/data/Iterator). |

| Returns | |
| A [`tf.experimental.Optional`](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional) object which either contains the next element of the iterator (if it exists) or no value. | |