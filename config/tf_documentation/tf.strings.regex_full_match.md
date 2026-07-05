# tf.strings.regex_full_match

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/strings/regex_full_match](https://tensorflow.google.cn/api_docs/python/tf/strings/regex_full_match)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/string_ops.py#L47-L69) |

Check if the input matches the regex pattern.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.strings.regex_full_match`](https://tensorflow.google.cn/api_docs/python/tf/strings/regex_full_match)

```
tf.strings.regex_full_match(
    input, pattern, name=None
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Subword tokenizers](https://tensorflow.google.cn/text/guide/subwords_tokenizer) |

The input is a string tensor of any shape. The pattern is a scalar
string tensor which is applied to every element of the input tensor.
The boolean values (True or False) of the output tensor indicate
if the input matches the regex pattern provided.

The pattern follows the re2 syntax (<https://github.com/google/re2/wiki/Syntax>)

#### Examples:

```
>>> tf.strings.regex_full_match(["TF lib", "lib TF"], ".*lib$")
<tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True, False])>
>>> tf.strings.regex_full_match(["TF lib", "lib TF"], ".*TF$")
<tf.Tensor: shape=(2,), dtype=bool, numpy=array([False,  True])>
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` of type `string`. A string tensor of the text to be processed. |
| `pattern` | A `Tensor` of type `string`. A scalar string tensor containing the regular expression to match the input. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |