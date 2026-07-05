# tf.quantization.fake_quant_with_min_max_vars_gradient

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_gradient](https://tensorflow.google.cn/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_gradient)

---

Compute gradients for a FakeQuantWithMinMaxVars operation.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.fake_quant_with_min_max_vars_gradient`](https://tensorflow.google.cn/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_gradient), [`tf.compat.v1.quantization.fake_quant_with_min_max_vars_gradient`](https://tensorflow.google.cn/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_gradient)

```
tf.quantization.fake_quant_with_min_max_vars_gradient(
    gradients: Annotated[Any, _atypes.Float32],
    inputs: Annotated[Any, _atypes.Float32],
    min: Annotated[Any, _atypes.Float32],
    max: Annotated[Any, _atypes.Float32],
    num_bits: int = 8,
    narrow_range: bool = False,
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `gradients` | A `Tensor` of type `float32`. Backpropagated gradients above the FakeQuantWithMinMaxVars operation. |
| `inputs` | A `Tensor` of type `float32`. Values passed as inputs to the FakeQuantWithMinMaxVars operation. min, max: Quantization interval, scalar floats. |
| `min` | A `Tensor` of type `float32`. |
| `max` | A `Tensor` of type `float32`. |
| `num_bits` | An optional `int`. Defaults to `8`. The bitwidth of the quantization; between 2 and 8, inclusive. |
| `narrow_range` | An optional `bool`. Defaults to `False`. Whether to quantize into 2^num\_bits - 1 distinct values. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (backprops\_wrt\_input, backprop\_wrt\_min, backprop\_wrt\_max). | |
| `backprops_wrt_input` | A `Tensor` of type `float32`. |
| `backprop_wrt_min` | A `Tensor` of type `float32`. |
| `backprop_wrt_max` | A `Tensor` of type `float32`. |