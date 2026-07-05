# tf.raw_ops.RequantizePerChannel

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RequantizePerChannel](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RequantizePerChannel)

---

Requantizes input with min and max values known per channel.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.RequantizePerChannel`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RequantizePerChannel)

```
tf.raw_ops.RequantizePerChannel(
    input,
    input_min,
    input_max,
    requested_output_min,
    requested_output_max,
    out_type=tf.dtypes.quint8,
    name=None
)

tf.dtypes.quint8
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`. The original input tensor. |
| `input_min` | A `Tensor` of type `float32`. The minimum value of the input tensor |
| `input_max` | A `Tensor` of type `float32`. The maximum value of the input tensor. |
| `requested_output_min` | A `Tensor` of type `float32`. The minimum value of the output tensor requested. |
| `requested_output_max` | A `Tensor` of type `float32`. The maximum value of the output tensor requested. |
| `out_type` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`. Defaults to [`tf.quint8`](https://tensorflow.google.cn/api_docs/python/tf#quint8). The quantized type of output tensor that needs to be converted. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (output, output\_min, output\_max). | |
| `output` | A `Tensor` of type `out_type`. |
| `output_min` | A `Tensor` of type `float32`. |
| `output_max` | A `Tensor` of type `float32`. |