# tf.IndexedSlicesSpec

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/IndexedSlicesSpec](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlicesSpec)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/indexed_slices.py#L203-L267) |

Type specification for a [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices).

Inherits From: [`TypeSpec`](https://tensorflow.google.cn/api_docs/python/tf/TypeSpec), [`TraceType`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/TraceType)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.IndexedSlicesSpec`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlicesSpec)

```
tf.IndexedSlicesSpec(
    shape=None,
    dtype=tf.dtypes.float32,
    indices_dtype=tf.dtypes.int64,
    dense_shape_dtype=None,
    indices_shape=None
)

tf.dtypes.float32
tf.dtypes.int64
```

| Args | |

|  |  |
| --- | --- |
| `shape` | The dense shape of the `IndexedSlices`, or `None` to allow any dense shape. |
| `dtype` | [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) of values in the `IndexedSlices`. |
| `indices_dtype` | [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) of the `indices` in the `IndexedSlices`. One of [`tf.int32`](https://tensorflow.google.cn/api_docs/python/tf#int32) or [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64). |
| `dense_shape_dtype` | [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) of the `dense_shape` in the `IndexedSlices`. One of [`tf.int32`](https://tensorflow.google.cn/api_docs/python/tf#int32), [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64), or `None` (if the `IndexedSlices` has no `dense_shape` tensor). |
| `indices_shape` | The shape of the `indices` component, which indicates how many slices are in the `IndexedSlices`. |

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

### `is_compatible_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/type_spec.py#L300-L321)

```
is_compatible_with(
    spec_or_value
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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/type_spec.py#L109-L146)

```
is_subtype_of(
    other: tf.types.experimental.TraceType
) -> bool

tf.types.experimental.TraceType
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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/type_spec.py#L148-L194)

```
most_specific_common_supertype(
    others: Sequence[tf.types.experimental.TraceType]
) -> Optional['TypeSpec']

tf.types.experimental.TraceType
```

Returns the most specific supertype TypeSpec of `self` and `others`.

Implements the tf.types.experimental.func.TraceType interface.

If not overridden by a subclass, the default behavior is to assume the
TypeSpec is covariant upon attributes that implement TraceType and
invariant upon rest of the attributes as well as the structure and type
of the TypeSpec.

| Args | |

|  |  |
| --- | --- |
| `others` | A sequence of TraceTypes. |

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