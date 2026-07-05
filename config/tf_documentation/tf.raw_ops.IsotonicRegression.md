# tf.raw_ops.IsotonicRegression

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IsotonicRegression](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IsotonicRegression)

---

Solves a batch of isotonic regression problems.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.IsotonicRegression`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/IsotonicRegression)

```
tf.raw_ops.IsotonicRegression(
    input,
    output_dtype=tf.dtypes.float32,
    name=None
)

tf.dtypes.float32
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. A (batch\_size, dim)-tensor holding a batch of inputs. |
| `output_dtype` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.half, tf.bfloat16, tf.float32, tf.float64`. Defaults to [`tf.float32`](https://tensorflow.google.cn/api_docs/python/tf#float32). Dtype of output. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (output, segments). | |
| `output` | A `Tensor` of type `output_dtype`. |
| `segments` | A `Tensor` of type `int32`. |