# tf.TensorSpec

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/TensorSpec](https://tensorflow.google.cn/api_docs/python/tf/TensorSpec)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L917-L1219) |

Describes the type of a tf.Tensor.

Inherits From: [`TypeSpec`](https://tensorflow.google.cn/api_docs/python/tf/TypeSpec), [`TraceType`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/TraceType)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.TensorSpec`](https://tensorflow.google.cn/api_docs/python/tf/TensorSpec)

```
tf.TensorSpec(
    shape,
    dtype=tf.dtypes.float32,
    name=None
)

tf.dtypes.float32
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Extension types](https://tensorflow.google.cn/guide/extension_type) * [Import a JAX model using JAX2TF](https://tensorflow.google.cn/guide/jax2tf) * [Using the SavedModel format](https://tensorflow.google.cn/guide/saved_model) * [Better performance with tf.function](https://tensorflow.google.cn/guide/function) * [Migrate the SavedModel workflow](https://tensorflow.google.cn/guide/migrate/saved_model) | * [DeepDream](https://tensorflow.google.cn/tutorials/generative/deepdream) * [Simple audio recognition: Recognizing keywords](https://tensorflow.google.cn/tutorials/audio/simple_audio) * [Load video data](https://tensorflow.google.cn/tutorials/load_data/video) * [Transfer learning for video classification with MoViNet](https://tensorflow.google.cn/tutorials/video/transfer_learning_with_movinet) * [Video classification with a 3D convolutional neural network](https://tensorflow.google.cn/tutorials/video/video_classification) |

```
>>> t = tf.constant([[1,2,3],[4,5,6]])
>>> tf.TensorSpec.from_tensor(t)
TensorSpec(shape=(2, 3), dtype=tf.int32, name=None)
```

Contains metadata for describing the nature of [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) objects
accepted or returned by some TensorFlow APIs.

For example, it can be used to constrain the type of inputs accepted by
a tf.function:

```
>>> @tf.function(input_signature=[tf.TensorSpec([1, None])])
... def constrained_foo(t):
...   print("tracing...")
...   return t
```

Now the [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) is able to assume that `t` is always of the type
`tf.TensorSpec([1, None])` which will avoid retracing as well as enforce the
type restriction on inputs.

As a result, the following call with tensor of type `tf.TensorSpec([1, 2])`
triggers a trace and succeeds:

```
>>> constrained_foo(tf.constant([[1., 2]])).numpy()
tracing...
array([[1., 2.]], dtype=float32)
```

The following subsequent call with tensor of type `tf.TensorSpec([1, 4])`
does not trigger a trace and succeeds:

```
>>> constrained_foo(tf.constant([[1., 2, 3, 4]])).numpy()
array([[1., 2., 3., 4.], dtype=float32)
```

But the following call with tensor of type `tf.TensorSpec([2, 2])` fails:

```
>>> constrained_foo(tf.constant([[1., 2], [3, 4]])).numpy()
Traceback (most recent call last):
...
TypeError: Binding inputs to tf.function `constrained_foo` failed ...
```

| Args | |

|  |  |
| --- | --- |
| `shape` | Value convertible to [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape). The shape of the tensor. |
| `dtype` | Value convertible to [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). The type of the tensor values. |
| `name` | Optional name for the Tensor. |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If shape is not convertible to a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape), or dtype is not convertible to a [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |

| Attributes | |

|  |  |
| --- | --- |
| `dtype` | Returns the `dtype` of elements in the tensor. |
| `name` | Returns the (optionally provided) name of the described tensor. |
| `shape` | Returns the `TensorShape` that represents the shape of the tensor. |
| `value_type` | The Python type for values that are compatible with this TypeSpec. |

## Methods

### `experimental_as_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L977-L982)

```
experimental_as_proto() -> struct_pb2.TensorSpecProto
```

Returns a proto representation of the TensorSpec instance.

### `experimental_from_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L968-L975)

```
@classmethod
experimental_from_proto(
    proto: struct_pb2.TensorSpecProto
) -> 'TensorSpec'
```

Returns a TensorSpec instance based on the serialized proto.

### `experimental_type_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L963-L966)

```
@classmethod
experimental_type_proto() -> Type[struct_pb2.TensorSpecProto]
```

Returns the type of proto associated with TensorSpec serialization.

### `from_spec`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L1126-L1138)

```
@classmethod
from_spec(
    spec, name=None
)
```

Returns a `TensorSpec` with the same shape and dtype as `spec`.

```
>>> spec = tf.TensorSpec(shape=[8, 3], dtype=tf.int32, name="OriginalName")
>>> tf.TensorSpec.from_spec(spec, "NewName")
TensorSpec(shape=(8, 3), dtype=tf.int32, name='NewName')
```

| Args | |

|  |  |
| --- | --- |
| `spec` | The `TypeSpec` used to create the new `TensorSpec`. |
| `name` | The name for the new `TensorSpec`. Defaults to `spec.name`. |

### `from_tensor`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L1140-L1161)

```
@classmethod
from_tensor(
    tensor, name=None
)
```

Returns a `TensorSpec` that describes `tensor`.

```
>>> tf.TensorSpec.from_tensor(tf.constant([1, 2, 3]))
TensorSpec(shape=(3,), dtype=tf.int32, name=None)
```

| Args | |

|  |  |
| --- | --- |
| `tensor` | The [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) that should be described. |
| `name` | A name for the `TensorSpec`. Defaults to `tensor.op.name`. |

| Returns | |
| A `TensorSpec` that describes `tensor`. | |

### `is_compatible_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L984-L996)

```
is_compatible_with(
    spec_or_tensor
)
```

Returns True if spec\_or\_tensor is compatible with this TensorSpec.

Two tensors are considered compatible if they have the same dtype
and their shapes are compatible (see [`tf.TensorShape.is_compatible_with`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape#is_compatible_with)).

| Args | |

|  |  |
| --- | --- |
| `spec_or_tensor` | A tf.TensorSpec or a tf.Tensor |

| Returns | |
| True if spec\_or\_tensor is compatible with self. | |

### `is_subtype_of`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L998-L1006)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L896-L899)

```
__eq__(
    other
)
```

Return self==value.

### `__ne__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor.py#L901-L902)

```
__ne__(
    other
)
```

Return self!=value.