# tf.strings.upper

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/strings/upper](https://tensorflow.google.cn/api_docs/python/tf/strings/upper)

---

Converts all lowercase characters into their respective uppercase replacements.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.strings.upper`](https://tensorflow.google.cn/api_docs/python/tf/strings/upper)

```
tf.strings.upper(
    input: Annotated[Any, _atypes.String],
    encoding: str = '',
    name=None
) -> Annotated[Any, _atypes.String]
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