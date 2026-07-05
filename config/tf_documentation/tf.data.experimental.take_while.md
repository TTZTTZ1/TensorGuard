# tf.data.experimental.take_while

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/take_while](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/take_while)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/take_while_ops.py#L20-L38) |

A transformation that stops dataset iteration based on a `predicate`. (deprecated)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.take_while`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/take_while)

```
tf.data.experimental.take_while(
    predicate
)
```

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `tf.data.Dataset.take\_while(...)

| Args | |

|  |  |
| --- | --- |
| `predicate` | A function that maps a nested structure of tensors (having shapes and types defined by `self.output_shapes` and `self.output_types`) to a scalar [`tf.bool`](https://tensorflow.google.cn/api_docs/python/tf#bool) tensor. |

| Returns | |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#apply). | |