# tf.lookup.TextFileIndex

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/lookup/TextFileIndex](https://tensorflow.google.cn/api_docs/python/tf/lookup/TextFileIndex)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/lookup_ops.py#L589-L606) |

The key and value content to get from each line.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.lookup.TextFileIndex`](https://tensorflow.google.cn/api_docs/python/tf/lookup/TextFileIndex)

This class defines the key and value used for [`tf.lookup.TextFileInitializer`](https://tensorflow.google.cn/api_docs/python/tf/lookup/TextFileInitializer).

The key and value content to get from each line is specified either
by the following, or a value `>=0`.

* [`TextFileIndex.LINE_NUMBER`](https://tensorflow.google.cn/api_docs/python/tf/lookup/TextFileIndex#LINE_NUMBER) means use the line number starting from zero,
  expects data type int64.
* [`TextFileIndex.WHOLE_LINE`](https://tensorflow.google.cn/api_docs/python/tf/lookup/TextFileIndex#WHOLE_LINE) means use the whole line content, expects data
  type string.

A value `>=0` means use the index (starting at zero) of the split line based
on `delimiter`.

| Class Variables | |

|  |  |
| --- | --- |
| LINE\_NUMBER | `-1` |
| WHOLE\_LINE | `-2` |