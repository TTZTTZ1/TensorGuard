# tf.raw_ops.StaticRegexReplace

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StaticRegexReplace](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StaticRegexReplace)

---

Replaces the match of pattern in input with rewrite.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StaticRegexReplace`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StaticRegexReplace)

```
tf.raw_ops.StaticRegexReplace(
    input, pattern, rewrite, replace_global=True, name=None
)
```

It follows the re2 syntax (<https://github.com/google/re2/wiki/Syntax>)

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` of type `string`. The text to be processed. |
| `pattern` | A `string`. The regular expression to match the input. |
| `rewrite` | A `string`. The rewrite to be applied to the matched expression. |
| `replace_global` | An optional `bool`. Defaults to `True`. If True, the replacement is global, otherwise the replacement is done only on the first match. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |