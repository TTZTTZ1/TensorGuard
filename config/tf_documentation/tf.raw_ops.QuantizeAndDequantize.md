# tf.raw_ops.QuantizeAndDequantize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QuantizeAndDequantize](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QuantizeAndDequantize)

---

Use QuantizeAndDequantizeV2 instead.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.QuantizeAndDequantize`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QuantizeAndDequantize)

```
tf.raw_ops.QuantizeAndDequantize(
    input,
    signed_input=True,
    num_bits=8,
    range_given=False,
    input_min=0,
    input_max=0,
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `signed_input` | An optional `bool`. Defaults to `True`. |
| `num_bits` | An optional `int`. Defaults to `8`. |
| `range_given` | An optional `bool`. Defaults to `False`. |
| `input_min` | An optional `float`. Defaults to `0`. |
| `input_max` | An optional `float`. Defaults to `0`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |