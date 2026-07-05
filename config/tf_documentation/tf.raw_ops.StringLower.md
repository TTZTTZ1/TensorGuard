# tf.raw_ops.StringLower

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StringLower](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StringLower)

---

Converts all uppercase characters into their respective lowercase replacements.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StringLower`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StringLower)

```
tf.raw_ops.StringLower(
    input, encoding='', name=None
)
```

#### Example:

```
>>> tf.strings.lower("CamelCase string and ALL CAPS")
<tf.Tensor: shape=(), dtype=string, numpy=b'camelcase string and all caps'>
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` of type `string`. The input to be lower-cased. |
| `encoding` | An optional `string`. Defaults to `""`. Character encoding of `input`. Allowed values are '' and 'utf-8'. Value '' is interpreted as ASCII. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |