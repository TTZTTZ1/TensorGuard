# tf.raw_ops.StringUpper

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StringUpper](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StringUpper)

---

Converts all lowercase characters into their respective uppercase replacements.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StringUpper`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StringUpper)

```
tf.raw_ops.StringUpper(
    input, encoding='', name=None
)
```

#### Example:

```
>>> tf.strings.upper("CamelCase string and ALL CAPS")
<tf.Tensor: shape=(), dtype=string, numpy=b'CAMELCASE STRING AND ALL CAPS'>
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` of type `string`. The input to be upper-cased. |
| `encoding` | An optional `string`. Defaults to `""`. Character encoding of `input`. Allowed values are '' and 'utf-8'. Value '' is interpreted as ASCII. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |