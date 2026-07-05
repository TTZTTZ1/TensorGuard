# tf.data.experimental.get_structure

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/get_structure](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/get_structure)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/dataset_ops.py#L4339-L4377) |

Returns the type signature for elements of the input dataset / iterator.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.get_structure`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/get_structure)

```
tf.data.experimental.get_structure(
    dataset_or_iterator
)
```

For example, to get the structure of a [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset):

```
>>> dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])
>>> tf.data.experimental.get_structure(dataset)
TensorSpec(shape=(), dtype=tf.int32, name=None)
```

```
>>> dataset = tf.data.experimental.from_list([(1, 'a'), (2, 'b'), (3, 'c')])
>>> tf.data.experimental.get_structure(dataset)
(TensorSpec(shape=(), dtype=tf.int32, name=None),
 TensorSpec(shape=(), dtype=tf.string, name=None))
```

To get the structure of an [`tf.data.Iterator`](https://tensorflow.google.cn/api_docs/python/tf/data/Iterator):

```
>>> dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])
>>> tf.data.experimental.get_structure(iter(dataset))
TensorSpec(shape=(), dtype=tf.int32, name=None)
```

| Args | |

|  |  |
| --- | --- |
| `dataset_or_iterator` | A [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) or an [`tf.data.Iterator`](https://tensorflow.google.cn/api_docs/python/tf/data/Iterator). |

| Returns | |
| A (nested) structure of [`tf.TypeSpec`](https://tensorflow.google.cn/api_docs/python/tf/TypeSpec) objects matching the structure of an element of `dataset_or_iterator` and specifying the type of individual components. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If input is not a [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) or an [`tf.data.Iterator`](https://tensorflow.google.cn/api_docs/python/tf/data/Iterator) object. |