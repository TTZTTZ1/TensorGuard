# tf.raw_ops.QuantizeAndDequantizeV4

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QuantizeAndDequantizeV4](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QuantizeAndDequantizeV4)

---

Quantizes then dequantizes a tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.QuantizeAndDequantizeV4`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QuantizeAndDequantizeV4)

```
tf.raw_ops.QuantizeAndDequantizeV4(
    input,
    input_min,
    input_max,
    signed_input=True,
    num_bits=8,
    range_given=False,
    round_mode='HALF_TO_EVEN',
    narrow_range=False,
    axis=-1,
    name=None
)
```

This is almost identical to QuantizeAndDequantizeV2, except that it returns a
gradient of 1 for inputs that are within the quantization range, or 0 otherwise.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. Tensor to quantize and then dequantize. |
| `input_min` | A `Tensor`. Must have the same type as `input`. If `range_given == True`, this specifies the minimum input value that needs to be represented, otherwise it is determined from the min value of the `input` tensor. |
| `input_max` | A `Tensor`. Must have the same type as `input`. If `range_given == True`, this specifies the maximum input value that needs to be represented, otherwise it is determined from the max value of the `input` tensor. |
| `signed_input` | An optional `bool`. Defaults to `True`. Whether the quantization is signed or unsigned. (actually this parameter should have been called **`signed_output`**) |
| `num_bits` | An optional `int`. Defaults to `8`. The bitwidth of the quantization. |
| `range_given` | An optional `bool`. Defaults to `False`. Whether the range is given or should be determined from the `input` tensor. |
| `round_mode` | An optional `string` from: `"HALF_TO_EVEN", "HALF_UP"`. Defaults to `"HALF_TO_EVEN"`. The 'round\_mode' attribute controls which rounding tie-breaking algorithm is used when rounding float values to their quantized equivalents. The following rounding modes are currently supported: |

* HALF\_TO\_EVEN: this is the default round\_mode.
* HALF\_UP: round towards positive. In this mode 7.5 rounds up to 8 and -7.5
  rounds up to -7.|  |  |
  | --- | --- |
  | `narrow_range` | An optional `bool`. Defaults to `False`. If True, then the absolute value of the quantized minimum value is the same as the quantized maximum value, instead of 1 greater. i.e. for 8 bit quantization, the minimum value is -127 instead of -128. |
  | `axis` | An optional `int`. Defaults to `-1`. If specified, this axis is treated as a channel or slice axis, and a separate quantization range is used for each channel or slice along this axis. |
  | `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |