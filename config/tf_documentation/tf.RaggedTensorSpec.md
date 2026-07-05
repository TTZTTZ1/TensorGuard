# tf.RaggedTensorSpec

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/RaggedTensorSpec](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensorSpec)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/ragged/ragged_tensor.py#L2319-L2661) |

Type specification for a [`tf.RaggedTensor`](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensor).

Inherits From: [`TypeSpec`](https://tensorflow.google.cn/api_docs/python/tf/TypeSpec), [`TraceType`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/TraceType)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.RaggedTensorSpec`](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensorSpec)

```
tf.RaggedTensorSpec(
    shape=None,
    dtype=tf.dtypes.float32,
    ragged_rank=None,
    row_splits_dtype=tf.dtypes.int64,
    flat_values_spec=None
)

tf.dtypes.float32
tf.dtypes.int64
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) * [Subword tokenizers](https://tensorflow.google.cn/text/guide/subwords_tokenizer) |

| Args | |

|  |  |
| --- | --- |
| `shape` | The shape of the RaggedTensor, or `None` to allow any shape. If a shape is specified, then all ragged dimensions must have size `None`. |
| `dtype` | [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) of values in the RaggedTensor. |
| `ragged_rank` | Python integer, the number of times the RaggedTensor's flat\_values is partitioned. Defaults to `shape.ndims - 1`. |
| `row_splits_dtype` | `dtype` for the RaggedTensor's `row_splits` tensor. One of [`tf.int32`](https://tensorflow.google.cn/api_docs/python/tf#int32) or [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64). |
| `flat_values_spec` | TypeSpec for flat\_value of the RaggedTensor. It shall be provided when the flat\_values is a CompositeTensor rather then Tensor. If both `dtype` and `flat_values_spec` and are provided, `dtype` must be the same as `flat_values_spec.dtype`. (experimental) |

| Attributes | |

|  |  |
| --- | --- |
| `dtype` | The [`tf.dtypes.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) specified by this type for the RaggedTensor. |

```
>>> rt = tf.ragged.constant([["a"], ["b", "c"]], dtype=tf.string)
>>> tf.type_spec_from_value(rt).dtype
tf.string
```

|  |  |
| --- | --- |
| `flat_values_spec` | The `TypeSpec` of the flat\_values of RaggedTensor. |
| `ragged_rank` | The number of times the RaggedTensor's flat\_values is partitioned. |

Defaults to `shape.ndims - 1`.

```
>>> values = tf.ragged.constant([[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]])
>>> tf.type_spec_from_value(values).ragged_rank
1
```

```
>>> rt1 = tf.RaggedTensor.from_uniform_row_length(values, 2)
>>> tf.type_spec_from_value(rt1).ragged_rank
2
```

|  |  |
| --- | --- |
| `row_splits_dtype` | The [`tf.dtypes.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) of the RaggedTensor's `row_splits`. |

```
>>> rt = tf.ragged.constant([[1, 2, 3], [4]], row_splits_dtype=tf.int64)
>>> tf.type_spec_from_value(rt).row_splits_dtype
tf.int64
```

|  |  |
| --- | --- |
| `shape` | The statically known shape of the RaggedTensor. |

```
>>> rt = tf.ragged.constant([[0], [1, 2]])
>>> tf.type_spec_from_value(rt).shape
TensorShape([2, None])
```

```
>>> rt = tf.ragged.constant([[[0, 1]], [[1, 2], [3, 4]]], ragged_rank=1)
>>> tf.type_spec_from_value(rt).shape
TensorShape([2, None, 2])
```

|  |  |
| --- | --- |
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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/ragged/ragged_tensor.py#L2643-L2661)

```
@classmethod
from_value(
    value
)
```

### `is_compatible_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/ragged/ragged_tensor.py#L2468-L2478)

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