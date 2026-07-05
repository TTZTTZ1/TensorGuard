# tf.strings.regex_replace

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/strings/regex_replace](https://tensorflow.google.cn/api_docs/python/tf/strings/regex_replace)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/string_ops.py#L74-L112) |

Replace elements of `input` matching regex `pattern` with `rewrite`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.regex_replace`](https://tensorflow.google.cn/api_docs/python/tf/strings/regex_replace), [`tf.compat.v1.strings.regex_replace`](https://tensorflow.google.cn/api_docs/python/tf/strings/regex_replace)

```
tf.strings.regex_replace(
    input, pattern, rewrite, replace_global=True, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Creating a custom Counterfactual Logit Pairing Dataset](https://tensorflow.google.cn/responsible_ai/model_remediation/counterfactual/guide/creating_a_custom_counterfactual_dataset) | * [Basic text classification](https://tensorflow.google.cn/tutorials/keras/text_classification) * [Neural machine translation with attention](https://tensorflow.google.cn/text/tutorials/nmt_with_attention) * [Warm-start embedding layer matrix](https://tensorflow.google.cn/text/tutorials/warmstart_embedding_matrix) * [Word embeddings](https://tensorflow.google.cn/text/tutorials/word_embeddings) * [Graph-based Neural Structured Learning in TFX](https://tensorflow.google.cn/tfx/tutorials/tfx/neural_structured_learning) |

```
>>> tf.strings.regex_replace("Text with tags.<br /><b>contains html</b>",
...                          "<[^>]+>", " ")
<tf.Tensor: shape=(), dtype=string, numpy=b'Text with tags.  contains html '>
```

| Args | |

|  |  |
| --- | --- |
| `input` | string `Tensor`, the source strings to process. |
| `pattern` | string or scalar string `Tensor`, regular expression to use, see more details at https://github.com/google/re2/wiki/Syntax |
| `rewrite` | string or scalar string `Tensor`, value to use in match replacement, supports backslash-escaped digits (\1 to \9) can be to insert text matching corresponding parenthesized group. |
| `replace_global` | `bool`, if `True` replace all non-overlapping matches, else replace only the first match. |
| `name` | A name for the operation (optional). |

| Returns | |
| string `Tensor` of the same shape as `input` with specified replacements. | |