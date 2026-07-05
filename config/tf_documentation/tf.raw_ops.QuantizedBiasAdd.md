# tf.raw_ops.QuantizedBiasAdd

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QuantizedBiasAdd](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QuantizedBiasAdd)

---

Adds Tensor 'bias' to Tensor 'input' for Quantized types.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.QuantizedBiasAdd`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QuantizedBiasAdd)

```
tf.raw_ops.QuantizedBiasAdd(
    input, bias, min_input, max_input, min_bias, max_bias, out_type, name=None
)
```

Broadcasts the values of bias on dimensions 0..N-2 of 'input'.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`. |
| `bias` | A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`. A 1D bias Tensor with size matching the last dimension of 'input'. |
| `min_input` | A `Tensor` of type `float32`. The float value that the lowest quantized input value represents. |
| `max_input` | A `Tensor` of type `float32`. The float value that the highest quantized input value represents. |
| `min_bias` | A `Tensor` of type `float32`. The float value that the lowest quantized bias value represents. |
| `max_bias` | A `Tensor` of type `float32`. The float value that the highest quantized bias value represents. |
| `out_type` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (output, min\_out, max\_out). | |
| `output` | A `Tensor` of type `out_type`. |
| `min_out` | A `Tensor` of type `float32`. |
| `max_out` | A `Tensor` of type `float32`. |