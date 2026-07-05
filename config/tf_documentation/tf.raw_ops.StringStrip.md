# tf.raw_ops.StringStrip

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StringStrip](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StringStrip)

---

Strip leading and trailing whitespaces from the Tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StringStrip`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StringStrip)

```
tf.raw_ops.StringStrip(
    input, name=None
)
```

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