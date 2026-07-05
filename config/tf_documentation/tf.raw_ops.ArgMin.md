# tf.raw_ops.ArgMin

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ArgMin](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ArgMin)

---

Returns the index with the smallest value across dimensions of a tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ArgMin`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ArgMin)

```
tf.raw_ops.ArgMin(
    input,
    dimension,
    output_type=tf.dtypes.int64,
    name=None
)

tf.dtypes.int64
```

Note that in case of ties the identity of the return value is not guaranteed.

| Usage | |
|  | |

```
import tensorflow as tf
a = [1, 10, 26.9, 2.8, 166.32, 62.3]
b = tf.math.argmin(input = a)
c = tf.keras.backend.eval(b)
# c = 0
# here a[0] = 1 which is the smallest element of a across axis 0
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`, `qint8`, `quint8`, `qint32`, `qint16`, `quint16`, `bool`. |
| `dimension` | A `Tensor`. Must be one of the following types: `int32`, `int64`. int32 or int64, must be in the range `[-rank(input), rank(input))`. Describes which dimension of the input Tensor to reduce across. For vectors, use dimension = 0. |
| `output_type` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.int32, tf.int64`. Defaults to [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `output_type`. | |