# tf.lite.TargetSpec

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/lite/TargetSpec](https://tensorflow.google.cn/api_docs/python/tf/lite/TargetSpec)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/lite.py#L185-L230) |

Specification of target device used to optimize the model.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.lite.TargetSpec`](https://tensorflow.google.cn/api_docs/python/tf/lite/TargetSpec)

```
tf.lite.TargetSpec(
    supported_ops=None,
    supported_types=None,
    experimental_select_user_tf_ops=None,
    experimental_supported_backends=None
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [TFLite Authoring Tool](https://tensorflow.google.cn/lite/guide/authoring) |

| Attributes | |

|  |  |
| --- | --- |
| `supported_ops` | Experimental flag, subject to change. Set of [`tf.lite.OpsSet`](https://tensorflow.google.cn/api_docs/python/tf/lite/OpsSet) options, where each option represents a set of operators supported by the target device. (default {tf.lite.OpsSet.TFLITE\_BUILTINS})) |
| `supported_types` | Set of [`tf.dtypes.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) data types supported on the target device. If initialized, optimization might be driven by the smallest type in this set. (default set()) |
| `experimental_select_user_tf_ops` | Experimental flag, subject to change. Set of user's TensorFlow operators' names that are required in the TensorFlow Lite runtime. These ops will be exported as select TensorFlow ops in the model (in conjunction with the tf.lite.OpsSet.SELECT\_TF\_OPS flag). This is an advanced feature that should only be used if the client is using TF ops that may not be linked in by default with the TF ops that are provided when using the SELECT\_TF\_OPS path. The client is responsible for linking these ops into the target runtime. |
| `experimental_supported_backends` | Experimental flag, subject to change. Set containing names of supported backends. Currently only "GPU" is supported, more options will be available later. |