# tf.strings.join

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/strings/join](https://tensorflow.google.cn/api_docs/python/tf/strings/join)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/string_ops.py#L551-L583) |

Perform element-wise concatenation of a list of string tensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.string_join`](https://tensorflow.google.cn/api_docs/python/tf/strings/join), [`tf.compat.v1.strings.join`](https://tensorflow.google.cn/api_docs/python/tf/strings/join)

```
tf.strings.join(
    inputs, separator='', name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) | * [Text generation with an RNN](https://tensorflow.google.cn/text/tutorials/text_generation) * [Sending Different Data To Particular Clients With tff.federated\_select](https://tensorflow.google.cn/federated/tutorials/federated_select) * [Client-efficient large-model federated learning via `federated\_select` and sparse aggregation](https://tensorflow.google.cn/federated/tutorials/sparse_federated_learning) * [Image captioning with visual attention](https://tensorflow.google.cn/text/tutorials/image_captioning) * [Neural machine translation with attention](https://tensorflow.google.cn/text/tutorials/nmt_with_attention) |

Given a list of string tensors of same shape, performs element-wise
concatenation of the strings of the same index in all tensors.

```
>>> tf.strings.join(['abc','def']).numpy()
b'abcdef'
>>> tf.strings.join([['abc','123'],
...                  ['def','456'],
...                  ['ghi','789']]).numpy()
array([b'abcdefghi', b'123456789'], dtype=object)
>>> tf.strings.join([['abc','123'],
...                  ['def','456']],
...                  separator=" ").numpy()
array([b'abc def', b'123 456'], dtype=object)
```

The reduction version of this elementwise operation is
[`tf.strings.reduce_join`](https://tensorflow.google.cn/api_docs/python/tf/strings/reduce_join)

| Args | |

|  |  |
| --- | --- |
| `inputs` | A list of [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) objects of same size and [`tf.string`](https://tensorflow.google.cn/api_docs/python/tf#string) dtype. |
| `separator` | A string added between each string being joined. |
| `name` | A name for the operation (optional). |

| Returns | |
| A [`tf.string`](https://tensorflow.google.cn/api_docs/python/tf#string) tensor. | |