# tf.strings.split

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/strings/split](https://tensorflow.google.cn/api_docs/python/tf/strings/split)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/ragged/ragged_string_ops.py#L466-L525) |

Split elements of `input` based on `sep` into a `RaggedTensor`.

```
tf.strings.split(
    input, sep=None, maxsplit=-1, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Introduction to Tensors](https://tensorflow.google.cn/guide/tensor) * [tf.data: Build TensorFlow input pipelines](https://tensorflow.google.cn/guide/data) * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) | * [Load and preprocess images](https://tensorflow.google.cn/tutorials/load_data/images) * [Client-efficient large-model federated learning via `federated\_select` and sparse aggregation](https://tensorflow.google.cn/federated/tutorials/sparse_federated_learning) * [Using text and neural network features](https://tensorflow.google.cn/decision_forests/tutorials/intermediate_colab) * [Sending Different Data To Particular Clients With tff.federated\_select](https://tensorflow.google.cn/federated/tutorials/federated_select) * [Graph-based Neural Structured Learning in TFX](https://tensorflow.google.cn/tfx/tutorials/tfx/neural_structured_learning) |

Let N be the size of `input` (typically N will be the batch size). Split each
element of `input` based on `sep` and return a `RaggedTensor` containing the
split tokens. Empty tokens are ignored.

#### Example:

```
>>> tf.strings.split('hello world').numpy()
 array([b'hello', b'world'], dtype=object)
>>> tf.strings.split(['hello world', 'a b c'])
<tf.RaggedTensor [[b'hello', b'world'], [b'a', b'b', b'c']]>
```

If `sep` is given, consecutive delimiters are not grouped together and are
deemed to delimit empty strings. For example, `input` of `"1<>2<><>3"` and
`sep` of `"<>"` returns `["1", "2", "", "3"]`. If `sep` is None or an empty
string, consecutive whitespace are regarded as a single separator, and the
result will contain no empty strings at the start or end if the string has
leading or trailing whitespace.

Note that the above mentioned behavior matches python's str.split.

| Args | |

|  |  |
| --- | --- |
| `input` | A string `Tensor` of rank `N`, the strings to split. If `rank(input)` is not known statically, then it is assumed to be `1`. |
| `sep` | `0-D` string `Tensor`, the delimiter string. |
| `maxsplit` | An `int`. If `maxsplit > 0`, limit of the split of the result. |
| `name` | A name for the operation (optional). |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If sep is not a string. |

| Returns | |
| A `RaggedTensor` of rank `N+1`, the strings split according to the delimiter. | |