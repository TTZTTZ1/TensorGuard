# tf.compat.as_str_any

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/compat/as_str_any](https://tensorflow.google.cn/api_docs/python/tf/compat/as_str_any)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/util/compat.py#L119-L136) |

Converts input to `str` type.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.compat.as_str_any`](https://tensorflow.google.cn/api_docs/python/tf/compat/as_str_any)

```
tf.compat.as_str_any(
    value, encoding='utf-8'
)
```

Uses `str(value)`, except for `bytes` typed inputs, which are converted
using `as_str`.

| Args | |

|  |  |
| --- | --- |
| `value` | A object that can be converted to `str`. |
| `encoding` | Encoding for `bytes` typed inputs. |

| Returns | |
| A `str` object. | |