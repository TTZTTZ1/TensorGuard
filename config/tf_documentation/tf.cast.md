# tf.cast

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/cast](https://tensorflow.google.cn/api_docs/python/tf/cast)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L938-L1020) |

Casts a tensor to a new type.

#### View aliases

**Main aliases**

[`tf.dtypes.cast`](https://tensorflow.google.cn/api_docs/python/tf/cast)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.cast`](https://tensorflow.google.cn/api_docs/python/tf/cast), [`tf.compat.v1.dtypes.cast`](https://tensorflow.google.cn/api_docs/python/tf/cast)

```
tf.cast(
    x, dtype, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Multilayer perceptrons for digit recognition with Core APIs](https://tensorflow.google.cn/guide/core/mlp_core) * [Logistic regression for binary classification with Core APIs](https://tensorflow.google.cn/guide/core/logistic_regression_core) * [tf.data: Build TensorFlow input pipelines](https://tensorflow.google.cn/guide/data) * [Distributed training with Core APIs and DTensor](https://tensorflow.google.cn/guide/core/distribution) * [Import a JAX model using JAX2TF](https://tensorflow.google.cn/guide/jax2tf) | * [Scalable model compression](https://tensorflow.google.cn/tutorials/optimization/compression) * [DeepDream](https://tensorflow.google.cn/tutorials/generative/deepdream) * [Parameter server training with ParameterServerStrategy](https://tensorflow.google.cn/tutorials/distribute/parameter_server_training) * [Learned data compression](https://tensorflow.google.cn/tutorials/generative/data_compression) * [Neural style transfer](https://tensorflow.google.cn/tutorials/generative/style_transfer) |

The operation casts `x` (in case of `Tensor`) or `x.values`
(in case of `SparseTensor` or `IndexedSlices`) to `dtype`.

#### For example:

```
>>> x = tf.constant([1.8, 2.2], dtype=tf.float32)
>>> tf.cast(x, tf.int32)
<tf.Tensor: shape=(2,), dtype=int32, numpy=array([1, 2], dtype=int32)>
```

Notice [`tf.cast`](https://tensorflow.google.cn/api_docs/python/tf/cast) has an alias [`tf.dtypes.cast`](https://tensorflow.google.cn/api_docs/python/tf/cast):

```
>>> x = tf.constant([1.8, 2.2], dtype=tf.float32)
>>> tf.dtypes.cast(x, tf.int32)
<tf.Tensor: shape=(2,), dtype=int32, numpy=array([1, 2], dtype=int32)>
```

The operation supports data types (for `x` and `dtype`) of
`uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`, `int64`,
`float16`, `float32`, `float64`, `complex64`, `complex128`, `bfloat16`.
In case of casting from complex types (`complex64`, `complex128`) to real
types, only the real part of `x` is returned. In case of casting from real
types to complex types (`complex64`, `complex128`), the imaginary part of the
returned value is set to `0`. The handling of complex types here matches the
behavior of numpy.

Note casting nan and inf values to integral types has undefined behavior.

Note this operation can lead to a loss of precision when converting native
Python `float` and `complex` variables to [`tf.float64`](https://tensorflow.google.cn/api_docs/python/tf#float64) or [`tf.complex128`](https://tensorflow.google.cn/api_docs/python/tf#complex128)
tensors, since the input is first converted to the `float32` data type and
then widened. It is recommended to use [`tf.convert_to_tensor`](https://tensorflow.google.cn/api_docs/python/tf/convert_to_tensor) instead of
[`tf.cast`](https://tensorflow.google.cn/api_docs/python/tf/cast) for any non-tensor inputs.

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor` or `SparseTensor` or `IndexedSlices` of numeric type. It could be `uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`, `int64`, `float16`, `float32`, `float64`, `complex64`, `complex128`, `bfloat16`. |
| `dtype` | The destination type. The list of supported dtypes is the same as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` and same type as `dtype`. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If `x` cannot be cast to the `dtype`. |