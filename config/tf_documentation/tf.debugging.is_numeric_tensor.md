# tf.debugging.is_numeric_tensor

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/debugging/is_numeric_tensor](https://tensorflow.google.cn/api_docs/python/tf/debugging/is_numeric_tensor)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/check_ops.py#L1954-L1986) |

Returns `True` if the elements of `tensor` are numbers.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.debugging.is_numeric_tensor`](https://tensorflow.google.cn/api_docs/python/tf/debugging/is_numeric_tensor), [`tf.compat.v1.is_numeric_tensor`](https://tensorflow.google.cn/api_docs/python/tf/debugging/is_numeric_tensor)

```
tf.debugging.is_numeric_tensor(
    tensor
)
```

Specifically, returns `True` if the dtype of `tensor` is one of the following:

* [`tf.float16`](https://tensorflow.google.cn/api_docs/python/tf#float16)
* [`tf.float32`](https://tensorflow.google.cn/api_docs/python/tf#float32)
* [`tf.float64`](https://tensorflow.google.cn/api_docs/python/tf#float64)
* [`tf.int8`](https://tensorflow.google.cn/api_docs/python/tf#int8)
* [`tf.int16`](https://tensorflow.google.cn/api_docs/python/tf#int16)
* [`tf.int32`](https://tensorflow.google.cn/api_docs/python/tf#int32)
* [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64)
* [`tf.uint8`](https://tensorflow.google.cn/api_docs/python/tf#uint8)
* [`tf.uint16`](https://tensorflow.google.cn/api_docs/python/tf#uint16)
* [`tf.uint32`](https://tensorflow.google.cn/api_docs/python/tf#uint32)
* [`tf.uint64`](https://tensorflow.google.cn/api_docs/python/tf#uint64)
* [`tf.qint8`](https://tensorflow.google.cn/api_docs/python/tf#qint8)
* [`tf.qint16`](https://tensorflow.google.cn/api_docs/python/tf#qint16)
* [`tf.qint32`](https://tensorflow.google.cn/api_docs/python/tf#qint32)
* [`tf.quint8`](https://tensorflow.google.cn/api_docs/python/tf#quint8)
* [`tf.quint16`](https://tensorflow.google.cn/api_docs/python/tf#quint16)
* [`tf.complex64`](https://tensorflow.google.cn/api_docs/python/tf#complex64)
* [`tf.complex128`](https://tensorflow.google.cn/api_docs/python/tf#complex128)
* [`tf.bfloat16`](https://tensorflow.google.cn/api_docs/python/tf#bfloat16)

Returns `False` if `tensor` is of a non-numeric type or if `tensor` is not
a [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) object.