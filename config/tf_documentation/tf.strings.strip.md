# tf.strings.strip

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/strings/strip](https://tensorflow.google.cn/api_docs/python/tf/strings/strip)

---

Strip leading and trailing whitespaces from the Tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.string_strip`](https://tensorflow.google.cn/api_docs/python/tf/strings/strip), [`tf.compat.v1.strings.strip`](https://tensorflow.google.cn/api_docs/python/tf/strings/strip)

```
tf.strings.strip(
    input: Annotated[Any, _atypes.String], name=None
) -> Annotated[Any, _atypes.String]
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [End to end example for BigQuery TensorFlow reader](https://tensorflow.google.cn/io/tutorials/bigquery) * [Preprocessing data with TensorFlow Transform](https://tensorflow.google.cn/tfx/tutorials/transform/census) * [Neural machine translation with attention](https://tensorflow.google.cn/text/tutorials/nmt_with_attention) * [TFX Keras Component Tutorial](https://tensorflow.google.cn/tfx/tutorials/tfx/components_keras) |

#### Examples:

```
>>> tf.strings.strip(["\nTensorFlow", "     The python library    "]).numpy()
array([b'TensorFlow', b'The python library'], dtype=object)
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` of type `string`. A string `Tensor` of any shape. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |