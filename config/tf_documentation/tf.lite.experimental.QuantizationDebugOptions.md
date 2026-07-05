# tf.lite.experimental.QuantizationDebugOptions

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/lite/experimental/QuantizationDebugOptions](https://tensorflow.google.cn/api_docs/python/tf/lite/experimental/QuantizationDebugOptions)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/tools/optimize/debugging/python/debugger.py#L56-L117) |

Debug options to set up a given QuantizationDebugger.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.lite.experimental.QuantizationDebugOptions`](https://tensorflow.google.cn/api_docs/python/tf/lite/experimental/QuantizationDebugOptions)

```
tf.lite.experimental.QuantizationDebugOptions(
    layer_debug_metrics: Optional[Mapping[str, Callable[[np.ndarray], float]]] = None,
    model_debug_metrics: Optional[Mapping[str, Callable[[Sequence[np.ndarray], Sequence[np.ndarray]],
        float]]] = None,
    layer_direct_compare_metrics: Optional[Mapping[str, Callable[[Sequence[np.ndarray], Sequence[np.ndarray],
        float, int], float]]] = None,
    denylisted_ops: Optional[List[str]] = None,
    denylisted_nodes: Optional[List[str]] = None,
    fully_quantize: bool = False
) -> None
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Inspecting Quantization Errors with Quantization Debugger](https://tensorflow.google.cn/lite/performance/quantization_debugger) |

| Args | |

|  |  |
| --- | --- |
| `layer_debug_metrics` | a dict to specify layer debug functions {function\_name\_str: function} where the function accepts result of NumericVerify Op, which is value difference between float and dequantized op results. The function returns single scalar value. |
| `model_debug_metrics` | a dict to specify model debug functions {function\_name\_str: function} where the function accepts outputs from two models, and returns single scalar value for a metric. (e.g. accuracy, IoU) |
| `layer_direct_compare_metrics` | a dict to specify layer debug functions {function\_name\_str: function}. The signature is different from that of `layer_debug_metrics`, and this one gets passed (original float value, original quantized value, scale, zero point). The function's implementation is responsible for correctly dequantize the quantized value to compare. Use this one when comparing diff is not enough. (Note) quantized value is passed as int8, so cast to int32 is needed. |
| `denylisted_ops` | a list of op names which is expected to be removed from quantization. |
| `denylisted_nodes` | a list of op's output tensor names to be removed from quantization. |
| `fully_quantize` | Bool indicating whether to fully quantize the model. Besides model body, the input/output will be quantized as well. Corresponding to mlir\_quantize's fully\_quantize parameter. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | when there are duplicate keys |