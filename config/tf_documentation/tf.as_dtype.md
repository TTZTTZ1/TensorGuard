# tf.as_dtype

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/as_dtype](https://tensorflow.google.cn/api_docs/python/tf/as_dtype)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/dtypes.py#L793-L853) |

Converts the given `type_value` to a [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType).

#### View aliases

**Main aliases**

[`tf.as_dtype`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/as_dtype)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.as_dtype`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/as_dtype), [`tf.compat.v1.dtypes.as_dtype`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/as_dtype)

```
tf.dtypes.as_dtype(
    type_value
)
```

Inputs can be existing [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) objects, a [`DataType`
enum](https://tensorflow.google.cn/code/tensorflow/core/framework/types.proto),
a string type name, or a
[`numpy.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html).

#### Examples:

```
>>> tf.as_dtype(2)  # Enum value for float64.
tf.float64
```

```
>>> tf.as_dtype('float')
tf.float32
```

```
>>> tf.as_dtype(np.int32)
tf.int32
```

**Note:** `DType` values are interned (i.e. a single instance of each dtype is
stored in a map). When passed a new `DType` object, `as_dtype` always returns
the interned value.

| Args | |

|  |  |
| --- | --- |
| `type_value` | A value that can be converted to a [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) object. |

| Returns | |
| A `DType` corresponding to `type_value`. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If `type_value` cannot be converted to a `DType`. |