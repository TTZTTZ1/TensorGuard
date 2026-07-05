# tf.data.experimental.enumerate_dataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/enumerate_dataset](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/enumerate_dataset)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/enumerate_ops.py#L20-L54) |

A transformation that enumerates the elements of a dataset. (deprecated)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.enumerate_dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/enumerate_dataset)

```
tf.data.experimental.enumerate_dataset(
    start=0
)
```

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use [`tf.data.Dataset.enumerate()`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#enumerate).

It is similar to python's `enumerate`.
For example:

```
# NOTE: The following examples use `{ ... }` to represent the
# contents of a dataset.
a = { 1, 2, 3 }
b = { (7, 8), (9, 10) }

# The nested structure of the `datasets` argument determines the
# structure of elements in the resulting dataset.
a.apply(tf.data.experimental.enumerate_dataset(start=5))
=> { (5, 1), (6, 2), (7, 3) }
b.apply(tf.data.experimental.enumerate_dataset())
=> { (0, (7, 8)), (1, (9, 10)) }
```

| Args | |

|  |  |
| --- | --- |
| `start` | A [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64) scalar [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor), representing the start value for enumeration. |

| Returns | |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#apply). | |