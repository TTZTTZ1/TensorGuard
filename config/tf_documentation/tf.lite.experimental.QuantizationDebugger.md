# tf.lite.experimental.QuantizationDebugger

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/lite/experimental/QuantizationDebugger](https://tensorflow.google.cn/api_docs/python/tf/lite/experimental/QuantizationDebugger)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/tools/optimize/debugging/python/debugger.py#L120-L549) |

Debugger for Quantized TensorFlow Lite debug mode models.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.lite.experimental.QuantizationDebugger`](https://tensorflow.google.cn/api_docs/python/tf/lite/experimental/QuantizationDebugger)

```
tf.lite.experimental.QuantizationDebugger(
    quant_debug_model_path: Optional[str] = None,
    quant_debug_model_content: Optional[bytes] = None,
    float_model_path: Optional[str] = None,
    float_model_content: Optional[bytes] = None,
    debug_dataset: Optional[Callable[[], Iterable[Sequence[np.ndarray]]]] = None,
    debug_options: Optional[tf.lite.experimental.QuantizationDebugOptions] = None,
    converter: Optional[TFLiteConverter] = None
) -> None

tf.lite.experimental.QuantizationDebugOptions
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Inspecting Quantization Errors with Quantization Debugger](https://tensorflow.google.cn/lite/performance/quantization_debugger) |

This can run the TensorFlow Lite converted models equipped with debug ops and
collect debug information. This debugger calculates statistics from
user-defined post-processing functions as well as default ones.

| Args | |

|  |  |
| --- | --- |
| `quant_debug_model_path` | Path to the quantized debug TFLite model file. |
| `quant_debug_model_content` | Content of the quantized debug TFLite model. |
| `float_model_path` | Path to float TFLite model file. |
| `float_model_content` | Content of the float TFLite model. |
| `debug_dataset` | a factory function that returns dataset generator which is used to generate input samples (list of np.ndarray) for the model. The generated elements must have same types and shape as inputs to the model. |
| `debug_options` | Debug options to debug the given model. |
| `converter` | Optional, use converter instead of quantized model. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If the debugger was unable to be created. |

| Attributes | |

|  |  |
| --- | --- |
| `options` |  |

## Methods

### `get_debug_quantized_model`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/tools/optimize/debugging/python/debugger.py#L261-L273)

```
get_debug_quantized_model() -> bytes
```

Returns an instrumented quantized model.

Convert the quantized model with the initialized converter and
return bytes for model. The model will be instrumented with numeric
verification operations and should only be used for debugging.

| Returns | |
| Model bytes corresponding to the model. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if converter is not passed to the debugger. |

### `get_nondebug_quantized_model`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/tools/optimize/debugging/python/debugger.py#L247-L259)

```
get_nondebug_quantized_model() -> bytes
```

Returns a non-instrumented quantized model.

Convert the quantized model with the initialized converter and
return bytes for nondebug model. The model will not be instrumented with
numeric verification operations.

| Returns | |
| Model bytes corresponding to the model. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if converter is not passed to the debugger. |

### `layer_statistics_dump`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/tools/optimize/debugging/python/debugger.py#L524-L549)

```
layer_statistics_dump(
    file: IO[str]
) -> None
```

Dumps layer statistics into file, in csv format.

| Args | |

|  |  |
| --- | --- |
| `file` | file, or file-like object to write. |

### `run`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/tools/optimize/debugging/python/debugger.py#L326-L330)

```
run() -> None
```

Runs models and gets metrics.