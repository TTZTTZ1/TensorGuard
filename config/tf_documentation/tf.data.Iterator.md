# tf.data.Iterator

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/Iterator](https://tensorflow.google.cn/api_docs/python/tf/data/Iterator)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/iterator_ops.py#L556-L653) |

Represents an iterator of a [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset).

[`tf.data.Iterator`](https://tensorflow.google.cn/api_docs/python/tf/data/Iterator) is the primary mechanism for enumerating elements of a
[`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset). It supports the Python Iterator protocol, which means
it can be iterated over using a for-loop:

```
>>> dataset = tf.data.Dataset.range(2)
>>> for element in dataset:
...   print(element)
tf.Tensor(0, shape=(), dtype=int64)
tf.Tensor(1, shape=(), dtype=int64)
```

or by fetching individual elements explicitly via `get_next()`:

```
>>> dataset = tf.data.Dataset.range(2)
>>> iterator = iter(dataset)
>>> print(iterator.get_next())
tf.Tensor(0, shape=(), dtype=int64)
>>> print(iterator.get_next())
tf.Tensor(1, shape=(), dtype=int64)
```

In addition, non-raising iteration is supported via `get_next_as_optional()`,
which returns the next element (if available) wrapped in a
[`tf.experimental.Optional`](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional).

```
>>> dataset = tf.data.Dataset.from_tensors(42)
>>> iterator = iter(dataset)
>>> optional = iterator.get_next_as_optional()
>>> print(optional.has_value())
tf.Tensor(True, shape=(), dtype=bool)
>>> optional = iterator.get_next_as_optional()
>>> print(optional.has_value())
tf.Tensor(False, shape=(), dtype=bool)
```

| Attributes | |

|  |  |
| --- | --- |
| `element_spec` | The type specification of an element of this iterator. |

```
>>> dataset = tf.data.Dataset.from_tensors(42)
>>> iterator = iter(dataset)
>>> iterator.element_spec
tf.TensorSpec(shape=(), dtype=tf.int32, name=None)
```

For more information,
read [this guide](https://tensorflow.google.cn/guide/data#dataset_structure).

## Methods

### `get_next`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/iterator_ops.py#L615-L630)

```
@abc.abstractmethod
get_next()
```

Returns the next element.

```
>>> dataset = tf.data.Dataset.from_tensors(42)
>>> iterator = iter(dataset)
>>> print(iterator.get_next())
tf.Tensor(42, shape=(), dtype=int32)
```

| Returns | |
| A (nested) structure of values matching [`tf.data.Iterator.element_spec`](https://tensorflow.google.cn/api_docs/python/tf/data/Iterator#element_spec). | |

| Raises | |
| [`tf.errors.OutOfRangeError`](https://tensorflow.google.cn/api_docs/python/tf/errors/OutOfRangeError): If the end of the iterator has been reached. | |

### `get_next_as_optional`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/iterator_ops.py#L632-L653)

```
@abc.abstractmethod
get_next_as_optional()
```

Returns the next element wrapped in [`tf.experimental.Optional`](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional).

If the iterator has reached the end of the sequence, the returned
[`tf.experimental.Optional`](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional) will have no value.

```
>>> dataset = tf.data.Dataset.from_tensors(42)
>>> iterator = iter(dataset)
>>> optional = iterator.get_next_as_optional()
>>> print(optional.has_value())
tf.Tensor(True, shape=(), dtype=bool)
>>> print(optional.get_value())
tf.Tensor(42, shape=(), dtype=int32)
>>> optional = iterator.get_next_as_optional()
>>> print(optional.has_value())
tf.Tensor(False, shape=(), dtype=bool)
```

| Returns | |
| A [`tf.experimental.Optional`](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional) object representing the next element. | |

### `__iter__`

```
__iter__()
```