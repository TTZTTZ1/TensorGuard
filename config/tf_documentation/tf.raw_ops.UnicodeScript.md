# tf.raw_ops.UnicodeScript

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/UnicodeScript](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/UnicodeScript)

---

Determine the script codes of a given tensor of Unicode integer code points.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.UnicodeScript`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/UnicodeScript)

```
tf.raw_ops.UnicodeScript(
    input, name=None
)
```

This operation converts Unicode code points to script codes corresponding to
each code point. Script codes correspond to International Components for
Unicode (ICU) UScriptCode values.

See
[ICU project docs](http://icu-project.org/apiref/icu4c/uscript_8h.html)
for more details on script codes.

For an example, see the unicode strings guide on [unicode scripts](https://tensorflow.google.cn/tutorials/load_data/unicode#representing_unicode).

Returns -1 (USCRIPT\_INVALID\_CODE) for invalid codepoints. Output shape will
match input shape.

#### Examples:

```
>>> tf.strings.unicode_script([1, 31, 38])
<tf.Tensor: shape=(3,), dtype=int32, numpy=array([0, 0, 0], dtype=int32)>
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` of type `int32`. A Tensor of int32 Unicode code points. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int32`. | |