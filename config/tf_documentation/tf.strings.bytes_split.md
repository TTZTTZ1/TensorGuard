# tf.strings.bytes_split

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/strings/bytes_split](https://tensorflow.google.cn/api_docs/python/tf/strings/bytes_split)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/ragged/ragged_string_ops.py#L40-L84) |

Split string elements of `input` into bytes.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.strings.bytes_split`](https://tensorflow.google.cn/api_docs/python/tf/strings/bytes_split)

```
tf.strings.bytes_split(
    input, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Introduction to Tensors](https://tensorflow.google.cn/guide/tensor) | * [Federated Learning for Text Generation](https://tensorflow.google.cn/federated/tutorials/federated_learning_for_text_generation) |

#### Examples:

```
>>> tf.strings.bytes_split('hello').numpy()
array([b'h', b'e', b'l', b'l', b'o'], dtype=object)
>>> tf.strings.bytes_split(['hello', '123'])
<tf.RaggedTensor [[b'h', b'e', b'l', b'l', b'o'], [b'1', b'2', b'3']]>
```

Note that this op splits strings into bytes, not unicode characters. To
split strings into unicode characters, use [`tf.strings.unicode_split`](https://tensorflow.google.cn/api_docs/python/tf/strings/unicode_split).

See also: [`tf.io.decode_raw`](https://tensorflow.google.cn/api_docs/python/tf/io/decode_raw), [`tf.strings.split`](https://tensorflow.google.cn/api_docs/python/tf/strings/split), [`tf.strings.unicode_split`](https://tensorflow.google.cn/api_docs/python/tf/strings/unicode_split).

| Args | |

|  |  |
| --- | --- |
| `input` | A string `Tensor` or `RaggedTensor`: the strings to split. Must have a statically known rank (`N`). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `RaggedTensor` of rank `N+1`: the bytes that make up the source strings. | |