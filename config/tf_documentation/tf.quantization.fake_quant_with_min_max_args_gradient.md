# tf.quantization.fake_quant_with_min_max_args_gradient

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient](https://tensorflow.google.cn/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient)

---

Compute gradients for a FakeQuantWithMinMaxArgs operation.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.fake_quant_with_min_max_args_gradient`](https://tensorflow.google.cn/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient), [`tf.compat.v1.quantization.fake_quant_with_min_max_args_gradient`](https://tensorflow.google.cn/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient)

```
tf.quantization.fake_quant_with_min_max_args_gradient(
    gradients: Annotated[Any, _atypes.Float32],
    inputs: Annotated[Any, _atypes.Float32],
    min: float = -6,
    max: float = 6,
    num_bits: int = 8,
    narrow_range: bool = False,
    name=None
) -> Annotated[Any, _atypes.Float32]
```

| Args | |

|  |  |
| --- | --- |
| `gradients` | A `Tensor` of type `float32`. Backpropagated gradients above the FakeQuantWithMinMaxArgs operation. |
| `inputs` | A `Tensor` of type `float32`. Values passed as inputs to the FakeQuantWithMinMaxArgs operation. |
| `min` | An optional `float`. Defaults to `-6`. |
| `max` | An optional `float`. Defaults to `6`. |
| `num_bits` | An optional `int`. Defaults to `8`. |
| `narrow_range` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `float32`. | |