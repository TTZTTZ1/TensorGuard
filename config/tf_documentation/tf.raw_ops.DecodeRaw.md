# tf.raw_ops.DecodeRaw

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DecodeRaw](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DecodeRaw)

---

Reinterpret the bytes of a string as a vector of numbers.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.DecodeRaw`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DecodeRaw)

```
tf.raw_ops.DecodeRaw(
    bytes, out_type, little_endian=True, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `bytes` | A `Tensor` of type `string`. All the elements must have the same length. |
| `out_type` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.half, tf.float32, tf.float64, tf.int32, tf.uint16, tf.uint8, tf.int16, tf.int8, tf.int64, tf.complex64, tf.complex128, tf.bool, tf.bfloat16`. |
| `little_endian` | An optional `bool`. Defaults to `True`. Whether the input `bytes` are in little-endian order. Ignored for `out_type` values that are stored in a single byte like `uint8`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `out_type`. | |