# tf.raw_ops.DecodeJSONExample

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DecodeJSONExample](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DecodeJSONExample)

---

Convert JSON-encoded Example records to binary protocol buffer strings.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.DecodeJSONExample`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DecodeJSONExample)

```
tf.raw_ops.DecodeJSONExample(
    json_examples, name=None
)
```

**Note:** This is **not** a general purpose JSON parsing op.

This op converts JSON-serialized
[`tf.train.Example`](https://tensorflow.google.cn/api_docs/python/tf/train/Example) (created with `json_format.MessageToJson`, following the
[standard JSON mapping](https://developers.google.cn/protocol-buffers/docs/proto3#json))
to a binary-serialized [`tf.train.Example`](https://tensorflow.google.cn/api_docs/python/tf/train/Example) (equivalent to
[`Example.SerializeToString()`](https://tensorflow.google.cn/api_docs/python/tf/train/BytesList#SerializeToString)) suitable for conversion to tensors with
[`tf.io.parse_example`](https://tensorflow.google.cn/api_docs/python/tf/io/parse_example).

| Args | |

|  |  |
| --- | --- |
| `json_examples` | A `Tensor` of type `string`. Each string is a JSON object serialized according to the JSON mapping of the Example proto. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |