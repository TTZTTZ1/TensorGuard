# tf.raw_ops.QuantizeAndDequantizeV4Grad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QuantizeAndDequantizeV4Grad](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QuantizeAndDequantizeV4Grad)

---

Returns the gradient of `QuantizeAndDequantizeV4`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.QuantizeAndDequantizeV4Grad`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/QuantizeAndDequantizeV4Grad)

```
tf.raw_ops.QuantizeAndDequantizeV4Grad(
    gradients, input, input_min, input_max, axis=-1, name=None
)
```

Returns a gradient of 1 for inputs that are within the quantization range,
or 0 otherwise.

| Args | |

|  |  |
| --- | --- |
| `gradients` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `input` | A `Tensor`. Must have the same type as `gradients`. |
| `input_min` | A `Tensor`. Must have the same type as `gradients`. |
| `input_max` | A `Tensor`. Must have the same type as `gradients`. |
| `axis` | An optional `int`. Defaults to `-1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (input\_backprop, input\_min\_backprop, input\_max\_backprop). | |
| `input_backprop` | A `Tensor`. Has the same type as `gradients`. |
| `input_min_backprop` | A `Tensor`. Has the same type as `gradients`. |
| `input_max_backprop` | A `Tensor`. Has the same type as `gradients`. |