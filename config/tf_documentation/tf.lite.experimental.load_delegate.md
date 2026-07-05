# tf.lite.experimental.load_delegate

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/lite/experimental/load_delegate](https://tensorflow.google.cn/api_docs/python/tf/lite/experimental/load_delegate)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/interpreter.py#L125-L170) |

Returns loaded Delegate object.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.lite.experimental.load_delegate`](https://tensorflow.google.cn/api_docs/python/tf/lite/experimental/load_delegate)

```
tf.lite.experimental.load_delegate(
    library, options=None
)
```

#### Example usage:

```
import tensorflow as tf

try:
  delegate = tf.lite.experimental.load_delegate('delegate.so')
except ValueError:
  // Fallback to CPU

if delegate:
  interpreter = tf.lite.Interpreter(
      model_path='model.tflite',
      experimental_delegates=[delegate])
else:
  interpreter = tf.lite.Interpreter(model_path='model.tflite')
```

This is typically used to leverage EdgeTPU for running TensorFlow Lite models.
For more information see: <https://coral.ai/docs/edgetpu/tflite-python/>

| Args | |

|  |  |
| --- | --- |
| `library` | Name of shared library containing the [TfLiteDelegate](https://tensorflow.google.cn/lite/performance/delegates). |
| `options` | Dictionary of options that are required to load the delegate. All keys and values in the dictionary should be convertible to str. Consult the documentation of the specific delegate for required and legal options. (default None) |

| Returns | |
| Delegate object. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | Delegate failed to load. |
| `RuntimeError` | If delegate loading is used on unsupported platform. |