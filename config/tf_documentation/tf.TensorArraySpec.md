# tf.TensorArraySpec

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/TensorArraySpec](https://tensorflow.google.cn/api_docs/python/tf/TensorArraySpec)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/tensor_array_ops.py#L1363-L1491) |

Type specification for a [`tf.TensorArray`](https://tensorflow.google.cn/api_docs/python/tf/TensorArray).

Inherits From: [`TypeSpec`](https://tensorflow.google.cn/api_docs/python/tf/TypeSpec), [`TraceType`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/TraceType)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.TensorArraySpec`](https://tensorflow.google.cn/api_docs/python/tf/TensorArraySpec)

```
tf.TensorArraySpec(
    element_shape=None,
    dtype=tf.dtypes.float32,
    dynamic_size=False,
    infer_shape=True
)

tf.dtypes.float32
```

| Args | |

|  |  |
| --- | --- |
| `element_shape` | The shape of each element in the `TensorArray`. |
| `dtype` | Data type of the `TensorArray`. |
| `dynamic_size` | Whether the `TensorArray` can grow past its initial size. |
| `infer_shape` | Whether shape inference is enabled. |

| Attributes | |

|  |  |
| --- | --- |
| `value_type` |  |

## Methods

### `experimental_as_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/type_spec.py#L217-L222)

```
experimental_as_proto() -> struct_pb2.TypeSpecProto
```

Returns a proto representation of the TypeSpec instance.

Do NOT override for custom non-TF types.

### `experimental_from_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/type_spec.py#L204-L215)

```
@classmethod
experimental_from_proto(
    proto: struct_pb2.TypeSpecProto
) -> 'TypeSpec'
```

Returns a TypeSpec instance based on the serialized proto.

Do NOT override for custom non-TF types.

| Args | |

|  |  |
| --- | --- |
| `proto` | Proto generated using 'experimental\_as\_proto'. |

### `experimental_type_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/type_spec.py#L196-L202)

```
@classmethod
experimental_type_proto() -> Type[struct_pb2.TypeSpecProto]
```

Returns the type of proto associated with TypeSpec serialization.

Do NOT override for custom non-TF types.

### `from_value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/tensor_array_ops.py#L1470-L1480)

```
@staticmethod
from_value(
    value
)
```

### `is_compatible_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/tensor_array_ops.py#L1425-L1434)

```
is_compatible_with(
    other
)
```

Returns true if `spec_or_value` is compatible with this TypeSpec.

Prefer using "is\_subtype\_of" and "most\_specific\_common\_supertype" wherever
possible.

| Args | |

|  |  |
| --- | --- |
| `spec_or_value` | A TypeSpec or TypeSpec associated value to compare against. |

### `is_subtype_of`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/tensor_array_ops.py#L1390-L1394)

```
is_subtype_of(
    other
)
```

Returns True if `self` is a subtype of `other`.

Implements the tf.types.experimental.func.TraceType interface.

If not overridden by a subclass, the default behavior is to assume the
TypeSpec is covariant upon attributes that implement TraceType and
invariant upon rest of the attributes as well as the structure and type
of the TypeSpec.

| Args | |

|  |  |
| --- | --- |
| `other` | A TraceType object. |

### `most_specific_common_supertype`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/tensor_array_ops.py#L1396-L1423)

```
most_specific_common_supertype(
    others
)
```

Returns the most specific supertype of `self` and `others`.

| Args | |

|  |  |
| --- | --- |
| `others` | A Sequence of `TypeSpec`. |

Returns `None` if a supertype does not exist.

### `most_specific_compatible_type`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/type_spec.py#L323-L341)

```
most_specific_compatible_type(
    other: 'TypeSpec'
) -> 'TypeSpec'
```

Returns the most specific TypeSpec compatible with `self` and `other`. (deprecated)

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use most\_specific\_common\_supertype instead.

Deprecated. Please use `most_specific_common_supertype` instead.
Do not override this function.

| Args | |

|  |  |
| --- | --- |
| `other` | A `TypeSpec`. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If there is no TypeSpec that is compatible with both `self` and `other`. |

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/type_spec.py#L545-L548)

```
__eq__(
    other
) -> bool
```

Return self==value.

### `__ne__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/type_spec.py#L550-L551)

```
__ne__(
    other
) -> bool
```

Return self!=value.