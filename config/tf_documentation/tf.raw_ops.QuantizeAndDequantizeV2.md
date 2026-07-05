# tf.raw_ops.QuantizeAndDequantizeV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QuantizeAndDequantizeV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QuantizeAndDequantizeV2)

---

Quantizes then dequantizes a tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.QuantizeAndDequantizeV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QuantizeAndDequantizeV2)

```
tf.raw_ops.QuantizeAndDequantizeV2(
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

This op simulates the precision loss from the quantized forward pass by:

1. Quantizing the tensor to fixed point numbers, which should match the target
   quantization method when it is used in inference.
2. Dequantizing it back to floating point numbers for the following ops, most
   likely matmul.

There are different ways to quantize. This version uses only scaling, so 0.0
maps to 0.

From the specified 'num\_bits' in the quantized output type, it determines
minimum and maximum representable quantized values.

e.g.

* [-128, 127] for signed, num\_bits = 8, or
* [0, 255] for unsigned, num\_bits = 8.

If range\_given == False, the initial input\_min, input\_max will be determined
automatically as the minimum and maximum values in the input tensor, otherwise
the specified values of input\_min, input\_max are used.

**Note:** If the input\_min, input\_max are specified, they do not need to equal the
actual minimum and maximum values in the tensor. e.g. in some cases it may be
beneficial to specify these values such that the low probability extremes of the
input distribution are clipped.

This op determines the maximum scale\_factor that would map the initial
[input\_min, input\_max] range to a range that lies within the representable
quantized range.

It determines the scale from one of input\_min and input\_max, then updates the
other one to maximize the representable range.

e.g.

* if the output is signed, num\_bits = 8, [input\_min, input\_max] = [-10.0,
  5.0]: it would use a scale\_factor of -128 / -10.0 = 12.8 In this case, it
  would update input\_max to be 127 / 12.8 = 9.921875
* if the output is signed, num\_bits = 8, [input\_min, input\_max] = [-10.0,
  10.0]: it would use a scale\_factor of 127 / 10.0 = 12.7 In this case, it
  would update input\_min to be 128.0 / 12.7 = -10.07874
* if the output is unsigned, input\_min is forced to be 0, and only the
  specified input\_max is used.

After determining the scale\_factor and updating the input range, it applies the
following to each value in the 'input' tensor.

output = round(clamp(value, input\_min, input\_max) \* scale\_factor) / scale\_factor.

The above round function rounds the value based on the given round\_mode.

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