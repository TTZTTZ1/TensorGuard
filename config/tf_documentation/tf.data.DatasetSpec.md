# tf.data.DatasetSpec

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/DatasetSpec](https://tensorflow.google.cn/api_docs/python/tf/data/DatasetSpec)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/dataset_ops.py#L4532-L4687) |

Type specification for [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset).

Inherits From: [`TypeSpec`](https://tensorflow.google.cn/api_docs/python/tf/TypeSpec), [`TraceType`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/TraceType)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.DatasetSpec`](https://tensorflow.google.cn/api_docs/python/tf/data/DatasetSpec), [`tf.compat.v1.data.experimental.DatasetStructure`](https://tensorflow.google.cn/api_docs/python/tf/data/DatasetSpec)

```
tf.data.DatasetSpec(
    element_spec, dataset_shape=()
)
```

See [`tf.TypeSpec`](https://tensorflow.google.cn/api_docs/python/tf/TypeSpec) for more information about TensorFlow type specifications.

```
>>> dataset = tf.data.Dataset.range(3)
>>> tf.data.DatasetSpec.from_value(dataset)
DatasetSpec(TensorSpec(shape=(), dtype=tf.int64, name=None), TensorShape([]))
```

| Attributes | |

|  |  |
| --- | --- |
| `element_spec` | The inner element spec. |
| `value_type` | The Python type for values that are compatible with this TypeSpec. |

In particular, all values that are compatible with this TypeSpec must be an
instance of this type.

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/dataset_ops.py#L4651-L4654)

```
@staticmethod
from_value(
    value
)
```

Creates a `DatasetSpec` for the given [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) value.

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/dataset_ops.py#L4560-L4584)

```
is_subtype_of(
    other
)
```

See base class.

### `most_specific_common_supertype`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/dataset_ops.py#L4586-L4623)

```
most_specific_common_supertype(
    others
)
```

See base class.

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/dataset_ops.py#L4684-L4687)

```
__eq__(
    other
)
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