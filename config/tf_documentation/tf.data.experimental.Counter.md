# tf.data.experimental.Counter

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/Counter](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/Counter)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/counter.py#L24-L59) |

Creates a `Dataset` that counts from `start` in steps of size `step`. (deprecated)

```
tf.data.experimental.Counter(
    start=0,
    step=1,
    dtype=tf.dtypes.int64
)

tf.dtypes.int64
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [tf.data: Build TensorFlow input pipelines](https://tensorflow.google.cn/guide/data) | * [Data augmentation](https://tensorflow.google.cn/tutorials/images/data_augmentation) |

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use [`tf.data.Dataset.counter(...)`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#counter) instead.

Unlike [`tf.data.Dataset.range`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#range) which will stop at some ending number,
`Counter` will produce elements indefinitely.

```
>>> dataset = tf.data.experimental.Counter().take(5)
>>> list(dataset.as_numpy_iterator())
[0, 1, 2, 3, 4]
>>> dataset.element_spec
TensorSpec(shape=(), dtype=tf.int64, name=None)
>>> dataset = tf.data.experimental.Counter(dtype=tf.int32)
>>> dataset.element_spec
TensorSpec(shape=(), dtype=tf.int32, name=None)
>>> dataset = tf.data.experimental.Counter(start=2).take(5)
>>> list(dataset.as_numpy_iterator())
[2, 3, 4, 5, 6]
>>> dataset = tf.data.experimental.Counter(start=2, step=5).take(5)
>>> list(dataset.as_numpy_iterator())
[2, 7, 12, 17, 22]
>>> dataset = tf.data.experimental.Counter(start=10, step=-1).take(5)
>>> list(dataset.as_numpy_iterator())
[10, 9, 8, 7, 6]
```

| Args | |

|  |  |
| --- | --- |
| `start` | (Optional.) The starting value for the counter. Defaults to 0. |
| `step` | (Optional.) The step size for the counter. Defaults to 1. |
| `dtype` | (Optional.) The data type for counter elements. Defaults to [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64). |

| Returns | |
| A `Dataset` of scalar `dtype` elements. | |