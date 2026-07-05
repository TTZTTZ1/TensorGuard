# tf.compat.as_bytes

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/compat/as_bytes](https://tensorflow.google.cn/api_docs/python/tf/compat/as_bytes)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/util/compat.py#L57-L82) |

Converts `bytearray`, `bytes`, or unicode python input types to `bytes`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.compat.as_bytes`](https://tensorflow.google.cn/api_docs/python/tf/compat/as_bytes)

```
tf.compat.as_bytes(
    bytes_or_text, encoding='utf-8'
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [TFX Python function component tutorial](https://tensorflow.google.cn/tfx/tutorials/tfx/python_function_component) |

Uses utf-8 encoding for text by default.

| Args | |

|  |  |
| --- | --- |
| `bytes_or_text` | A `bytearray`, `bytes`, `str`, or `unicode` object. |
| `encoding` | A string indicating the charset for encoding unicode. |

| Returns | |
| A `bytes` object. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If `bytes_or_text` is not a binary or unicode string. |