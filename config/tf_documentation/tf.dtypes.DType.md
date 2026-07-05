# tf.dtypes.DType

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/dtypes.py#L51-L288) |

Represents the type of the elements in a `Tensor`.

Inherits From: [`TraceType`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/TraceType)

#### View aliases

**Main aliases**

[`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType), [`tf.compat.v1.dtypes.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType)

```
tf.dtypes.DType(
    type_enum, handle_data=None
)
```

`DType`'s are used to specify the output data type for operations which
require it, or to inspect the data type of existing `Tensor`'s.

#### Examples:

```
>>> tf.constant(1, dtype=tf.int64)
<tf.Tensor: shape=(), dtype=int64, numpy=1>
>>> tf.constant(1.0).dtype
tf.float32
```

See [`tf.dtypes`](https://tensorflow.google.cn/api_docs/python/tf/dtypes) for a complete list of `DType`'s defined.

| Attributes | |

|  |  |
| --- | --- |
| `as_datatype_enum` | Returns a `types_pb2.DataType` enum value based on this data type. |
| `as_numpy_dtype` | Returns a Python `type` object based on this `DType`. |
| `base_dtype` | Returns a non-reference `DType` based on this `DType` (for TF1). |

Programs written for TensorFlow 2.x do not need this attribute.
It exists only for compatibility with TensorFlow 1.x, which used
reference `DType`s in the implementation of [`tf.compat.v1.Variable`](https://tensorflow.google.cn/api_docs/python/tf/compat/v1/Variable).
In TensorFlow 2.x, [`tf.Variable`](https://tensorflow.google.cn/api_docs/python/tf/Variable) is implemented without reference types.| `is_bool` | Returns whether this is a boolean data type. |
| `is_complex` | Returns whether this is a complex floating point type. |
| `is_floating` | Returns whether this is a (non-quantized, real) floating point type. |
| `is_integer` | Returns whether this is a (non-quantized) integer type. |
| `is_numeric` | Returns whether this is a numeric data type. |
| `is_numpy_compatible` | Returns whether this data type has a compatible NumPy data type. |
| `is_quantized` | Returns whether this is a quantized data type. |
| `is_unsigned` | Returns whether this type is unsigned. |

Non-numeric, unordered, and quantized types are not considered unsigned, and
this function returns `False`.| `limits` | Return intensity limits, i.e. |

(min, max) tuple, of the dtype.
Args:
clip\_negative : bool, optional If True, clip the negative range (i.e.
return 0 for min intensity) even if the image dtype allows negative
values. Returns
min, max : tuple Lower and upper intensity limits.|  |  |
| --- | --- |
| `max` | Returns the maximum representable value in this data type. |
| `min` | Returns the minimum representable value in this data type. |
| `name` |  |

|  |  |
| --- | --- |
| `real_dtype` | Returns the `DType` corresponding to this `DType`'s real part. |
| `size` |  |

## Methods

### `experimental_as_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/dtypes.py#L260-L262)

```
experimental_as_proto() -> types_pb2.SerializedDType
```

Returns a proto representation of the Dtype instance.

### `experimental_from_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/dtypes.py#L255-L258)

```
@classmethod
experimental_from_proto(
    proto: types_pb2.SerializedDType
) -> 'DType'
```

Returns a Dtype instance based on the serialized proto.

### `experimental_type_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/dtypes.py#L250-L253)

```
@classmethod
experimental_type_proto() -> Type[types_pb2.SerializedDType]
```

Returns the type of proto associated with DType serialization.

### `is_compatible_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/dtypes.py#L194-L214)

```
is_compatible_with(
    other
)
```

Returns True if the `other` DType will be converted to this DType (TF1).

Programs written for TensorFlow 2.x do not need this function.
Instead, they can do equality comparison on `DType` objects directly:
`tf.as_dtype(this) == tf.as_dtype(other)`.

This function exists only for compatibility with TensorFlow 1.x, where it
additionally allows conversion from a reference type (used by
[`tf.compat.v1.Variable`](https://tensorflow.google.cn/api_docs/python/tf/compat/v1/Variable)) to its base type.

| Args | |

|  |  |
| --- | --- |
| `other` | A `DType` (or object that may be converted to a `DType`). |

| Returns | |
| True if a Tensor of the `other` `DType` will be implicitly converted to this `DType`. | |

### `is_subtype_of`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/dtypes.py#L216-L218)

```
is_subtype_of(
    other: tf.types.experimental.TraceType
) -> bool

tf.types.experimental.TraceType
```

See tf.types.experimental.TraceType base class.

### `most_specific_common_supertype`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/dtypes.py#L220-L223)

```
most_specific_common_supertype(
    types: Sequence[tf.types.experimental.TraceType]
) -> Optional['DType']

tf.types.experimental.TraceType
```

See tf.types.experimental.TraceType base class.

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/dtypes.py#L264-L275)

```
__eq__(
    other
)
```

Returns True iff this DType refers to the same type as `other`.

### `__ne__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/dtypes.py#L277-L279)

```
__ne__(
    other
)
```

Returns True iff self != other.