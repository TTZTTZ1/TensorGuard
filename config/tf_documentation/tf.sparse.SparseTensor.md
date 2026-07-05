# tf.sparse.SparseTensor

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/sparse/SparseTensor](https://tensorflow.google.cn/api_docs/python/tf/sparse/SparseTensor)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/sparse_tensor.py#L48-L369) |

Represents a sparse tensor.

#### View aliases

**Main aliases**

[`tf.SparseTensor`](https://tensorflow.google.cn/api_docs/python/tf/sparse/SparseTensor)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.SparseTensor`](https://tensorflow.google.cn/api_docs/python/tf/sparse/SparseTensor), [`tf.compat.v1.sparse.SparseTensor`](https://tensorflow.google.cn/api_docs/python/tf/sparse/SparseTensor)

```
tf.sparse.SparseTensor(
    indices, values, dense_shape
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Working with sparse tensors](https://tensorflow.google.cn/guide/sparse_tensor) * [Migrate from TPU embedding\_columns to TPUEmbedding layer](https://tensorflow.google.cn/guide/migrate/tpu_embedding) * [tf.data: Build TensorFlow input pipelines](https://tensorflow.google.cn/guide/data) * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) * [Introduction to Tensors](https://tensorflow.google.cn/guide/tensor) | * [Client-efficient large-model federated learning via `federated\_select` and sparse aggregation](https://tensorflow.google.cn/federated/tutorials/sparse_federated_learning) * [Text generation with an RNN](https://tensorflow.google.cn/text/tutorials/text_generation) * [TFX Estimator Component Tutorial](https://tensorflow.google.cn/tfx/tutorials/tfx/components) * [TFX Keras Component Tutorial](https://tensorflow.google.cn/tfx/tutorials/tfx/components_keras) * [Graph-based Neural Structured Learning in TFX](https://tensorflow.google.cn/tfx/tutorials/tfx/neural_structured_learning) |

TensorFlow represents a sparse tensor as three separate dense tensors:
`indices`, `values`, and `dense_shape`. In Python, the three tensors are
collected into a `SparseTensor` class for ease of use. If you have separate
`indices`, `values`, and `dense_shape` tensors, wrap them in a `SparseTensor`
object before passing to the ops below.

Concretely, the sparse tensor `SparseTensor(indices, values, dense_shape)`
comprises the following components, where `N` and `ndims` are the number
of values and number of dimensions in the `SparseTensor`, respectively:

* `indices`: A 2-D int64 tensor of shape `[N, ndims]`, which specifies the
  indices of the elements in the sparse tensor that contain nonzero values
  (elements are zero-indexed). For example, `indices=[[1,3], [2,4]]` specifies
  that the elements with indexes of [1,3] and [2,4] have nonzero values.
* `values`: A 1-D tensor of any type and shape `[N]`, which supplies the
  values for each element in `indices`. For example, given `indices=[[1,3],
  [2,4]]`, the parameter `values=[18, 3.6]` specifies that element [1,3] of
  the sparse tensor has a value of 18, and element [2,4] of the tensor has a
  value of 3.6.
* `dense_shape`: A 1-D int64 tensor of shape `[ndims]`, which specifies the
  dense\_shape of the sparse tensor. Takes a list indicating the number of
  elements in each dimension. For example, `dense_shape=[3,6]` specifies a
  two-dimensional 3x6 tensor, `dense_shape=[2,3,4]` specifies a
  three-dimensional 2x3x4 tensor, and `dense_shape=[9]` specifies a
  one-dimensional tensor with 9 elements.

The corresponding dense tensor satisfies:

```
dense.shape = dense_shape
dense[tuple(indices[i])] = values[i]
```

By convention, `indices` should be sorted in row-major order (or equivalently
lexicographic order on the tuples `indices[i]`). This is not enforced when
`SparseTensor` objects are constructed, but most ops assume correct ordering.
If the ordering of sparse tensor `st` is wrong, a fixed version can be
obtained by calling [`tf.sparse.reorder(st)`](https://tensorflow.google.cn/api_docs/python/tf/sparse/reorder).

Example: The sparse tensor

```
SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
```

represents the dense tensor

```
[[1, 0, 0, 0]
 [0, 0, 2, 0]
 [0, 0, 0, 0]]
```

| Args | |

|  |  |
| --- | --- |
| `indices` | A 2-D int64 tensor of shape `[N, ndims]`. |
| `values` | A 1-D tensor of any type and shape `[N]`. |
| `dense_shape` | A 1-D int64 tensor of shape `[ndims]`. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | When building an eager SparseTensor if `dense_shape` is unknown or contains unknown elements (None or -1). |

| Attributes | |

|  |  |
| --- | --- |
| `dense_shape` | A 1-D Tensor of int64 representing the shape of the dense tensor. |
| `dtype` | The `DType` of elements in this tensor. |
| `graph` | The `Graph` that contains the index, value, and dense\_shape tensors. |
| `indices` | The indices of non-zero values in the represented dense tensor. |
| `op` | The `Operation` that produces `values` as an output. |
| `shape` | Get the `TensorShape` representing the shape of the dense tensor. |
| `values` | The non-zero values in the represented dense tensor. |

## Methods

### `consumers`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/sparse_tensor.py#L344-L345)

```
consumers()
```

### `eval`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/sparse_tensor.py#L298-L321)

```
eval(
    feed_dict=None, session=None
)
```

Evaluates this sparse tensor in a `Session`.

Calling this method will execute all preceding operations that
produce the inputs needed for the operation that produces this
tensor.

**Note:** Before invoking [`SparseTensor.eval()`](https://tensorflow.google.cn/api_docs/python/tf/sparse/SparseTensor#eval), its graph must have been
launched in a session, and either a default session must be
available, or `session` must be specified explicitly.

| Args | |

|  |  |
| --- | --- |
| `feed_dict` | A dictionary that maps `Tensor` objects to feed values. See `tf.Session.run` for a description of the valid feed values. |
| `session` | (Optional.) The `Session` to be used to evaluate this sparse tensor. If none, the default session will be used. |

| Returns | |
| A `SparseTensorValue` object. | |

### `from_value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/sparse_tensor.py#L108-L116)

```
@classmethod
from_value(
    sparse_tensor_value
)
```

### `get_shape`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/sparse_tensor.py#L156-L162)

```
get_shape() -> tf.TensorShape

tf.TensorShape
```

Get the `TensorShape` representing the shape of the dense tensor.

| Returns | |
| A `TensorShape` object. | |

### `set_shape`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/sparse_tensor.py#L232-L287)

```
set_shape(
    shape
)
```

Updates the `TensorShape` representing the shape of the dense tensor.

With eager execution this operates as a shape assertion.
Here the shapes match:

```
>>> st = tf.SparseTensor(
...   indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
>>> st.set_shape([3, 4])
```

Passing a `None` in the new shape allows any value for that axis:

```
>>> st.set_shape([3, None])
```

An error is raised if an incompatible shape is passed.

```
>>> st.set_shape([1, 4])
Traceback (most recent call last):
... 
ValueError: Tensor's shape (3, 4) is not compatible with supplied
shape [1, 4]
```

When executing in a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function), or building a model using
[`tf.keras.Input`](https://tensorflow.google.cn/api_docs/python/tf/keras/Input), [`SparseTensor.set_shape`](https://tensorflow.google.cn/api_docs/python/tf/sparse/SparseTensor#set_shape) will *merge* the given `shape`
with the current shape of this tensor, and set the tensor's shape to the
merged value (see [`tf.TensorShape.merge_with`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape#merge_with) for details):

```
>>> st = tf.keras.Input(shape=[None, None, 3], sparse=True)
>>> print(st.shape)
(None, None, None, 3)
```

Dimensions set to `None` are not updated:

```
>>> st.set_shape([None, 224, 224, None])
>>> print(st.shape)
(None, 224, 224, 3)
```

The main use case for this is to provide additional shape information
that cannot be inferred from the graph alone.

**Caution:** `set_shape` ensures that the applied shape is compatible with
the existing shape, but it does not check at runtime. Setting
incorrect shapes can result in inconsistencies between the
statically-known graph and the runtime value of tensors.

| Args | |

|  |  |
| --- | --- |
| `shape` | A `TensorShape` representing the shape of this tensor, a `TensorShapeProto`, a list, a tuple, or None. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `shape` is not compatible with the current shape of this tensor. |

### `with_values`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/sparse_tensor.py#L183-L206)

```
with_values(
    new_values
)
```

Returns a copy of `self` with `values` replaced by `new_values`.

This method produces a new `SparseTensor` that has the same nonzero
`indices` and same `dense_shape`, but updated values.

| Args | |

|  |  |
| --- | --- |
| `new_values` | The values of the new `SparseTensor`. Needs to have the same shape as the current `.values` `Tensor`. May have a different type than the current `values`. |

| Returns | |
| A `SparseTensor` with identical indices and shape but updated values. | |

#### Example usage:

```
>>> st = tf.sparse.from_dense([[1, 0, 2, 0], [3, 0, 0, 4]])
>>> tf.sparse.to_dense(st.with_values([10, 20, 30, 40]))  # 4 nonzero values
<tf.Tensor: shape=(2, 4), dtype=int32, numpy=
array([[10,  0, 20,  0],
       [30,  0,  0, 40]], dtype=int32)>
```

### `__div__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L133-L142)

```
__div__(
    y
)
```

Component-wise divides a SparseTensor by a dense Tensor.

*Limitation*: this Op only broadcasts the dense side to the sparse side, but not
the other direction.

| Args | |

|  |  |
| --- | --- |
| `sp_indices` | A `Tensor` of type `int64`. 2-D. `N x R` matrix with the indices of non-empty values in a SparseTensor, possibly not in canonical ordering. |
| `sp_values` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. 1-D. `N` non-empty values corresponding to `sp_indices`. |
| `sp_shape` | A `Tensor` of type `int64`. 1-D. Shape of the input SparseTensor. |
| `dense` | A `Tensor`. Must have the same type as `sp_values`. `R`-D. The dense Tensor operand. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `sp_values`. | |

### `__mul__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L133-L142)

```
__mul__(
    y
)
```

Component-wise multiplies a SparseTensor by a dense Tensor.

The output locations corresponding to the implicitly zero elements in the sparse
tensor will be zero (i.e., will not take up storage space), regardless of the
contents of the dense tensor (even if it's +/-INF and that INF\*0 == NaN).

*Limitation*: this Op only broadcasts the dense side to the sparse side, but not
the other direction.

| Args | |

|  |  |
| --- | --- |
| `sp_indices` | A `Tensor` of type `int64`. 2-D. `N x R` matrix with the indices of non-empty values in a SparseTensor, possibly not in canonical ordering. |
| `sp_values` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`. 1-D. `N` non-empty values corresponding to `sp_indices`. |
| `sp_shape` | A `Tensor` of type `int64`. 1-D. Shape of the input SparseTensor. |
| `dense` | A `Tensor`. Must have the same type as `sp_values`. `R`-D. The dense Tensor operand. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `sp_values`. | |

### `__truediv__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/override_binary_operator.py#L133-L142)

```
__truediv__(
    y
)
```

Internal helper function for 'sp\_t / dense\_t'.