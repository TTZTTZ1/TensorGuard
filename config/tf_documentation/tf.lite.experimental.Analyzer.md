# tf.lite.experimental.Analyzer

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/lite/experimental/Analyzer](https://tensorflow.google.cn/api_docs/python/tf/lite/experimental/Analyzer)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/analyzer.py#L35-L105) |

Provides a collection of TFLite model analyzer tools.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.lite.experimental.Analyzer`](https://tensorflow.google.cn/api_docs/python/tf/lite/experimental/Analyzer)

### Used in the notebooks

| Used in the guide |
| --- |
| * [TensorFlow Lite Model Analyzer](https://tensorflow.google.cn/lite/guide/model_analyzer) |

#### Example:

```
model = tf.keras.applications.MobileNetV3Large()
fb_model = tf.lite.TFLiteConverterV2.from_keras_model(model).convert()
tf.lite.experimental.Analyzer.analyze(model_content=fb_model)
# === TFLite ModelAnalyzer ===
#
# Your TFLite model has ‘1’ subgraph(s). In the subgraph description below,
# T# represents the Tensor numbers. For example, in Subgraph#0, the MUL op
# takes tensor #0 and tensor #19 as input and produces tensor #136 as output.
#
# Subgraph#0 main(T#0) -> [T#263]
#   Op#0 MUL(T#0, T#19) -> [T#136]
#   Op#1 ADD(T#136, T#18) -> [T#137]
#   Op#2 CONV_2D(T#137, T#44, T#93) -> [T#138]
#   Op#3 HARD_SWISH(T#138) -> [T#139]
#   Op#4 DEPTHWISE_CONV_2D(T#139, T#94, T#24) -> [T#140]
#   ...
```

**Warning:** Experimental interface, subject to change.

## Methods

### `analyze`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/analyzer.py#L63-L105)

```
@staticmethod
analyze(
    model_path=None, model_content=None, gpu_compatibility=False, **kwargs
)
```

Analyzes the given tflite\_model with dumping model structure.

This tool provides a way to understand users' TFLite flatbuffer model by
dumping internal graph structure. It also provides additional features
like checking GPU delegate compatibility.

**Warning:** Experimental interface, subject to change.
The output format is not guaranteed to stay stable, so don't
write scripts to this.

| Args | |

|  |  |
| --- | --- |
| `model_path` | TFLite flatbuffer model path. |
| `model_content` | TFLite flatbuffer model object. |
| `gpu_compatibility` | Whether to check GPU delegate compatibility. |
| `**kwargs` | Experimental keyword arguments to analyze API. |

| Returns | |
| Print analyzed report via console output. | |