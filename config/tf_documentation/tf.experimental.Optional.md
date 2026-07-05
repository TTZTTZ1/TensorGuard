# tf.experimental.Optional

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/optional_ops.py#L31-L159) |

Represents a value that may or may not be present.

#### View aliases

**Main aliases**

[`tf.data.experimental.Optional`](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.Optional`](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional), [`tf.compat.v1.experimental.Optional`](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional)

A [`tf.experimental.Optional`](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional) can represent the result of an operation that may
fail as a value, rather than raising an exception and halting execution. For
example, [`tf.data.Iterator.get_next_as_optional()`](https://tensorflow.google.cn/api_docs/python/tf/data/Iterator#get_next_as_optional) returns a
[`tf.experimental.Optional`](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional) that either contains the next element of an
iterator if one exists, or an "empty" value that indicates the end of the
sequence has been reached.

[`tf.experimental.Optional`](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional) can only be used with values that are convertible
to [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) or `tf.CompositeTensor`.

One can create a [`tf.experimental.Optional`](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional) from a value using the
`from_value()` method:

```
>>> optional = tf.experimental.Optional.from_value(42)
>>> print(optional.has_value())
tf.Tensor(True, shape=(), dtype=bool)
>>> print(optional.get_value())
tf.Tensor(42, shape=(), dtype=int32)
```

or without a value using the `empty()` method:

```
>>> optional = tf.experimental.Optional.empty(
...   tf.TensorSpec(shape=(), dtype=tf.int32, name=None))
>>> print(optional.has_value())
tf.Tensor(False, shape=(), dtype=bool)
```

| Attributes | |

|  |  |
| --- | --- |
| `element_spec` | The type specification of an element of this optional. |

```
>>> optional = tf.experimental.Optional.from_value(42)
>>> print(optional.element_spec)
tf.TensorSpec(shape=(), dtype=tf.int32, name=None)
```

## Methods

### `empty`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/optional_ops.py#L113-L132)

```
@staticmethod
empty(
    element_spec
)
```

Returns an `Optional` that has no value.

**Note:** This method takes an argument that defines the structure of the value
that would be contained in the returned `Optional` if it had a value.

```
>>> optional = tf.experimental.Optional.empty(
...   tf.TensorSpec(shape=(), dtype=tf.int32, name=None))
>>> print(optional.has_value())
tf.Tensor(False, shape=(), dtype=bool)
```

| Args | |

|  |  |
| --- | --- |
| `element_spec` | A (nested) structure of [`tf.TypeSpec`](https://tensorflow.google.cn/api_docs/python/tf/TypeSpec) objects matching the structure of an element of this optional. |

| Returns | |
| A [`tf.experimental.Optional`](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional) with no value. | |

### `from_value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/optional_ops.py#L134-L159)

```
@staticmethod
from_value(
    value
)
```

Returns a [`tf.experimental.Optional`](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional) that wraps the given value.

```
>>> optional = tf.experimental.Optional.from_value(42)
>>> print(optional.has_value())
tf.Tensor(True, shape=(), dtype=bool)
>>> print(optional.get_value())
tf.Tensor(42, shape=(), dtype=int32)
```

| Args | |

|  |  |
| --- | --- |
| `value` | A value to wrap. The value must be convertible to [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) or `tf.CompositeTensor`. |

| Returns | |
| A [`tf.experimental.Optional`](https://tensorflow.google.cn/api_docs/python/tf/experimental/Optional) that wraps `value`. | |

### `get_value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/optional_ops.py#L79-L97)

```
@abc.abstractmethod
get_value(
    name=None
)
```

Returns the value wrapped by this optional.

If this optional does not have a value (i.e. `self.has_value()` evaluates to
`False`), this operation will raise [`tf.errors.InvalidArgumentError`](https://tensorflow.google.cn/api_docs/python/tf/errors/InvalidArgumentError) at
runtime.

```
>>> optional = tf.experimental.Optional.from_value(42)
>>> print(optional.get_value())
tf.Tensor(42, shape=(), dtype=int32)
```

| Args | |

|  |  |
| --- | --- |
| `name` | (Optional.) A name for the created operation. |

| Returns | |
| The wrapped value. | |

### `has_value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/optional_ops.py#L63-L77)

```
@abc.abstractmethod
has_value(
    name=None
)
```

Returns a tensor that evaluates to `True` if this optional has a value.

```
>>> optional = tf.experimental.Optional.from_value(42)
>>> print(optional.has_value())
tf.Tensor(True, shape=(), dtype=bool)
```

| Args | |

|  |  |
| --- | --- |
| `name` | (Optional.) A name for the created operation. |

| Returns | |
| A scalar [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) of type [`tf.bool`](https://tensorflow.google.cn/api_docs/python/tf#bool). | |