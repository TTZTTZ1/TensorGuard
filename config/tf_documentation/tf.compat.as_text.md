# tf.compat.as_text

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/compat/as_text](https://tensorflow.google.cn/api_docs/python/tf/compat/as_text)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/util/compat.py#L85-L108) |

Converts any string-like python input types to unicode.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.compat.as_text`](https://tensorflow.google.cn/api_docs/python/tf/compat/as_text)

```
tf.compat.as_text(
    bytes_or_text, encoding='utf-8'
)
```

Returns the input as a unicode string. Uses utf-8 encoding for text
by default.

| Args | |

|  |  |
| --- | --- |
| `bytes_or_text` | A `bytes`, `str`, or `unicode` object. |
| `encoding` | A string indicating the charset for decoding unicode. |

| Returns | |
| A `unicode` (Python 2) or `str` (Python 3) object. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If `bytes_or_text` is not a binary or unicode string. |