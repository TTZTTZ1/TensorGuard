# tf.quantization.fake_quant_with_min_max_args

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/quantization/fake_quant_with_min_max_args](https://tensorflow.google.cn/api_docs/python/tf/quantization/fake_quant_with_min_max_args)

---

Fake-quantize the 'inputs' tensor, type float to 'outputs' tensor of same shape and type.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.fake_quant_with_min_max_args`](https://tensorflow.google.cn/api_docs/python/tf/quantization/fake_quant_with_min_max_args), [`tf.compat.v1.quantization.fake_quant_with_min_max_args`](https://tensorflow.google.cn/api_docs/python/tf/quantization/fake_quant_with_min_max_args)

```
tf.quantization.fake_quant_with_min_max_args(
    inputs: Annotated[Any, _atypes.Float32],
    min: float = -6,
    max: float = 6,
    num_bits: int = 8,
    narrow_range: bool = False,
    name=None
) -> Annotated[Any, _atypes.Float32]
```

Quantization is called fake since the output is still in floating point.
The API converts inputs into values within the range [min and max] and returns
as output.

Attributes

* `[min; max]` define the clamping range for the `inputs` data.
* `inputs` values are quantized into the quantization range (
  `[0; 2^num_bits - 1]` when `narrow_range` is false and `[1; 2^num_bits - 1]`
  when it is true) and then de-quantized and output as floats in `[min; max]`
  interval.
* `num_bits` is the bitwidth of the quantization; between 2 and 16, inclusive.

Before quantization, `min` and `max` values are adjusted with the following
logic.
It is suggested to have `min <= 0 <= max`. If `0` is not in the range of values,
the behavior can be unexpected:

* If `0 < min < max`: `min_adj = 0` and `max_adj = max - min`.
* If `min < max < 0`: `min_adj = min - max` and `max_adj = 0`.
* If `min <= 0 <= max`: `scale = (max - min) / (2^num_bits - 1)`,
  `min_adj = scale * round(min / scale)` and `max_adj = max + min_adj - min`.

Examples

```
inp = tf.constant ([10.03, -10.23, 3])
out = tf.quantization.fake_quant_with_min_max_args(inp, min=-5, max=5,
                                                   num_bits=16)
print(out)

#  Output:
#  tf.Tensor([ 4.9999237 -5.0000763  3.0000763], shape=(3,), dtype=float32)
```

| Raises | |
|  | |

* InvalidArgumentError:
  + If num\_bits are outside of range [2, 16].
  + If min >= max.
* ValueError: If `inputs` are of any other type than float32.

| Args | |

|  |  |
| --- | --- |
| `inputs` | A `Tensor` of type `float32`. |
| `min` | An optional `float`. Defaults to `-6`. |
| `max` | An optional `float`. Defaults to `6`. |
| `num_bits` | An optional `int`. Defaults to `8`. |
| `narrow_range` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `float32`. | |