# tf.lite.experimental.OpResolverType

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/lite/experimental/OpResolverType](https://tensorflow.google.cn/api_docs/python/tf/lite/experimental/OpResolverType)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/lite/python/interpreter.py#L303-L331) |

Different types of op resolvers for Tensorflow Lite.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.lite.experimental.OpResolverType`](https://tensorflow.google.cn/api_docs/python/tf/lite/experimental/OpResolverType)

* `AUTO`: Indicates the op resolver that is chosen by default in TfLite
  Python, which is the "BUILTIN" as described below.
* `BUILTIN`: Indicates the op resolver for built-in ops with optimized kernel
  implementation.
* `BUILTIN_REF`: Indicates the op resolver for built-in ops with reference
  kernel implementation. It's generally used for testing and debugging.
* `BUILTIN_WITHOUT_DEFAULT_DELEGATES`: Indicates the op resolver for
  built-in ops with optimized kernel implementation, but it will disable
  the application of default TfLite delegates (like the XNNPACK delegate) to
  the model graph. Generally this should not be used unless there are issues
  with the default configuration.

| Class Variables | |

|  |  |
| --- | --- |
| AUTO | `<OpResolverType.AUTO: 0>` |
| BUILTIN | `<OpResolverType.BUILTIN: 1>` |
| BUILTIN\_REF | `<OpResolverType.BUILTIN_REF: 2>` |
| BUILTIN\_WITHOUT\_DEFAULT\_DELEGATES | `<OpResolverType.BUILTIN_WITHOUT_DEFAULT_DELEGATES: 3>` |