# tf.get_logger

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/get_logger](https://tensorflow.google.cn/api_docs/python/tf/get_logger)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/platform/tf_logging.py#L93-L179) |

Return TF logger instance.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.get_logger`](https://tensorflow.google.cn/api_docs/python/tf/get_logger)

```
tf.get_logger()
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrating your TFLite code to TF2](https://tensorflow.google.cn/guide/migrate/tflite) * [Customizing MinDiffModel](https://tensorflow.google.cn/responsible_ai/model_remediation/min_diff/guide/customizing_min_diff_model) * [Integrating MinDiff with MinDiffModel](https://tensorflow.google.cn/responsible_ai/model_remediation/min_diff/guide/integrating_min_diff_with_min_diff_model) * [Integrating MinDiff without MinDiffModel](https://tensorflow.google.cn/responsible_ai/model_remediation/min_diff/guide/integrating_min_diff_without_min_diff_model) * [Subword tokenizers](https://tensorflow.google.cn/text/guide/subwords_tokenizer) | * [TensorFlow Hub Object Detection Colab](https://tensorflow.google.cn/hub/tutorials/tf2_object_detection) * [Implement Differential Privacy with TensorFlow Privacy](https://tensorflow.google.cn/responsible_ai/privacy/tutorials/classification_privacy) * [Parametrized Quantum Circuits for Reinforcement Learning](https://tensorflow.google.cn/quantum/tutorials/quantum_reinforcement_learning) * [Object Detection with TensorFlow Lite Model Maker](https://tensorflow.google.cn/lite/models/modify/model_maker/object_detection) * [Text classification with TensorFlow Lite Model Maker](https://tensorflow.google.cn/lite/models/modify/model_maker/text_classification) |

| Returns | |
| An instance of the Python logging library Logger. | |

See Python documentation (<https://docs.python.org/3/library/logging.html>)
for detailed API. Below is only a summary.

The logger has 5 levels of logging from the most serious to the least:

1. FATAL
2. ERROR
3. WARN
4. INFO
5. DEBUG

The logger has the following methods, based on these logging levels:

1. fatal(msg, \*args, \*\*kwargs)
2. error(msg, \*args, \*\*kwargs)
3. warn(msg, \*args, \*\*kwargs)
4. info(msg, \*args, \*\*kwargs)
5. debug(msg, \*args, \*\*kwargs)

The `msg` can contain string formatting. An example of logging at the `ERROR`
level
using string formating is:

```
>>> tf.get_logger().error("The value %d is invalid.", 3)
```

You can also specify the logging verbosity. In this case, the
WARN level log will not be emitted:

```
>>> tf.get_logger().setLevel(ERROR)
>>> tf.get_logger().warn("This is a warning.")
```