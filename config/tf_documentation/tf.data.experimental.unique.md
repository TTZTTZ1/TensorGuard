# tf.data.experimental.unique

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/unique](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/unique)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/unique.py#L20-L43) |

Creates a `Dataset` from another `Dataset`, discarding duplicates. (deprecated)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.unique`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/unique)

```
tf.data.experimental.unique()
```

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `tf.data.Dataset.unique(...)

Use this transformation to produce a dataset that contains one instance of
each unique element in the input. For example:

```
dataset = tf.data.Dataset.from_tensor_slices([1, 37, 2, 37, 2, 1])

# Using `unique()` will drop the duplicate elements.
dataset = dataset.apply(tf.data.experimental.unique())  # ==> { 1, 37, 2 }
```

| Returns | |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#apply). | |