# tf.quantization.quantize_and_dequantize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/quantization/quantize_and_dequantize](https://tensorflow.google.cn/api_docs/python/tf/quantization/quantize_and_dequantize)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L5896-L5960) |

Quantizes then dequantizes a tensor. (deprecated)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.quantization.quantize_and_dequantize`](https://tensorflow.google.cn/api_docs/python/tf/quantization/quantize_and_dequantize)

```
tf.quantization.quantize_and_dequantize(
    input,
    input_min,
    input_max,
    signed_input=True,
    num_bits=8,
    range_given=False,
    round_mode='HALF_TO_EVEN',
    name=None,
    narrow_range=False,
    axis=None
)
```

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
This Op has been deprecated, use`quantize_and_dequantize_v2` instead. To To simulate the V1 the behavior of tf.quantization.quantize\_and\_dequantize(...) use tf.grad\_pass\_through(tf.quantization.quantize\_and\_dequantize\_v2)(...).

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` to quantize and dequantize. |
| `input_min` | If range\_given=True, the minimum input value, that needs to be represented in the quantized representation. If axis is specified, this should be a vector of minimum values for each slice along axis. |
| `input_max` | If range\_given=True, the maximum input value that needs to be represented in the quantized representation. If axis is specified, this should be a vector of maximum values for each slice along axis. |
| `signed_input` | True if the quantization is signed or unsigned. |
| `num_bits` | The bitwidth of the quantization. |
| `range_given` | If true use `input_min` and `input_max` for the range of the input, otherwise determine min and max from the input `Tensor`. |
| `round_mode` | Rounding mode when rounding from float values to quantized ones. one of ['HALF\_TO\_EVEN', 'HALF\_UP'] |
| `name` | Optional name for the operation. |
| `narrow_range` | If true, then the absolute value of the quantized minimum value is the same as the quantized maximum value, instead of 1 greater. i.e. for 8 bit quantization, the minimum value is -127 instead of -128. |
| `axis` | Integer. If specified, refers to a dimension of the input tensor, such that quantization will be per slice along that dimension. |

| Returns | |
| A `Tensor`. Each element is the result of quantizing and dequantizing the corresponding element of `input`. | |