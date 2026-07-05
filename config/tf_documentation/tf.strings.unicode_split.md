# tf.strings.unicode_split

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/strings/unicode_split](https://tensorflow.google.cn/api_docs/python/tf/strings/unicode_split)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/ragged/ragged_string_ops.py#L294-L339) |

Splits each string in `input` into a sequence of Unicode code points.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.strings.unicode_split`](https://tensorflow.google.cn/api_docs/python/tf/strings/unicode_split)

```
tf.strings.unicode_split(
    input,
    input_encoding,
    errors='replace',
    replacement_char=65533,
    name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Introduction to Tensors](https://tensorflow.google.cn/guide/tensor) * [Unicode strings](https://tensorflow.google.cn/text/guide/unicode) | * [Text generation with an RNN](https://tensorflow.google.cn/text/tutorials/text_generation) |

`result[i1...iN, j]` is the substring of `input[i1...iN]` that encodes its
`j`th character, when decoded using `input_encoding`.

| Args | |

|  |  |
| --- | --- |
| `input` | An `N` dimensional potentially ragged `string` tensor with shape `[D1...DN]`. `N` must be statically known. |
| `input_encoding` | String name for the unicode encoding that should be used to decode each string. |
| `errors` | Specifies the response when an input string can't be converted using the indicated encoding. One of: |

* `'strict'`: Raise an exception for any illegal substrings.
* `'replace'`: Replace illegal substrings with `replacement_char`.
* `'ignore'`: Skip illegal substrings.| `replacement_char` | The replacement codepoint to be used in place of invalid substrings in `input` when `errors='replace'`. |
  | `name` | A name for the operation (optional). |

| Returns | |
| A `N+1` dimensional `int32` tensor with shape `[D1...DN, (num_chars)]`. The returned tensor is a [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) if `input` is a scalar, or a [`tf.RaggedTensor`](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensor) otherwise. | |

#### Example:

```
>>> input = [s.encode('utf8') for s in (u'G\xf6\xf6dnight', u'\U0001f60a')]
>>> tf.strings.unicode_split(input, 'UTF-8').to_list()
[[b'G', b'\xc3\xb6', b'\xc3\xb6', b'd', b'n', b'i', b'g', b'h', b't'],
 [b'\xf0\x9f\x98\x8a']]
```