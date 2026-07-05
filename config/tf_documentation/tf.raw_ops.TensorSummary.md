# tf.raw_ops.TensorSummary

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorSummary](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorSummary)

---

Outputs a `Summary` protocol buffer with a tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorSummary`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorSummary)

```
tf.raw_ops.TensorSummary(
    tensor,
    description='',
    labels=[],
    display_name='',
    name=None
)
```

This op is being phased out in favor of TensorSummaryV2, which lets callers pass
a tag as well as a serialized SummaryMetadata proto string that contains
plugin-specific data. We will keep this op to maintain backwards compatibility.

| Args | |

|  |  |
| --- | --- |
| `tensor` | A `Tensor`. A tensor to serialize. |
| `description` | An optional `string`. Defaults to `""`. A json-encoded SummaryDescription proto. |
| `labels` | An optional list of `strings`. Defaults to `[]`. An unused list of strings. |
| `display_name` | An optional `string`. Defaults to `""`. An unused string. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |