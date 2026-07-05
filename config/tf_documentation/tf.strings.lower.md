# tf.strings.lower

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/strings/lower](https://tensorflow.google.cn/api_docs/python/tf/strings/lower)

---

Converts all uppercase characters into their respective lowercase replacements.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.strings.lower`](https://tensorflow.google.cn/api_docs/python/tf/strings/lower)

```
tf.strings.lower(
    input: Annotated[Any, _atypes.String],
    encoding: str = '',
    name=None
) -> Annotated[Any, _atypes.String]
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Basic text classification](https://tensorflow.google.cn/tutorials/keras/text_classification) * [Image captioning with visual attention](https://tensorflow.google.cn/text/tutorials/image_captioning) * [Neural machine translation with attention](https://tensorflow.google.cn/text/tutorials/nmt_with_attention) * [Warm-start embedding layer matrix](https://tensorflow.google.cn/text/tutorials/warmstart_embedding_matrix) * [word2vec](https://tensorflow.google.cn/text/tutorials/word2vec) |

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