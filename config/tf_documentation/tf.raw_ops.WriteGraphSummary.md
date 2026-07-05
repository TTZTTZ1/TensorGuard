# tf.raw_ops.WriteGraphSummary

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/WriteGraphSummary](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/WriteGraphSummary)

---

Writes a graph summary.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.WriteGraphSummary`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/WriteGraphSummary)

```
tf.raw_ops.WriteGraphSummary(
    writer, step, tensor, name=None
)
```

Writes TensorFlow graph `tensor` at `step` using summary `writer`.

| Args | |

|  |  |
| --- | --- |
| `writer` | A `Tensor` of type `resource`. |
| `step` | A `Tensor` of type `int64`. |
| `tensor` | A `Tensor` of type `string`. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |