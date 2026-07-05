# tf.raw_ops.WriteSummary

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/WriteSummary](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/WriteSummary)

---

Writes a tensor summary.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.WriteSummary`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/WriteSummary)

```
tf.raw_ops.WriteSummary(
    writer, step, tensor, tag, summary_metadata, name=None
)
```

Writes `tensor` at `step` with `tag` using summary `writer`.

| Args | |

|  |  |
| --- | --- |
| `writer` | A `Tensor` of type `resource`. |
| `step` | A `Tensor` of type `int64`. |
| `tensor` | A `Tensor`. |
| `tag` | A `Tensor` of type `string`. |
| `summary_metadata` | A `Tensor` of type `string`. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |