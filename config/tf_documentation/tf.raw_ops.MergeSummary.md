# tf.raw_ops.MergeSummary

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MergeSummary](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MergeSummary)

---

Merges summaries.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.MergeSummary`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MergeSummary)

```
tf.raw_ops.MergeSummary(
    inputs, name=None
)
```

This op creates a
[`Summary`](https://tensorflow.google.cn/code/tensorflow/core/framework/summary.proto)
protocol buffer that contains the union of all the values in the input
summaries.

When the Op is run, it reports an `InvalidArgument` error if multiple values
in the summaries to merge use the same tag.

| Args | |

|  |  |
| --- | --- |
| `inputs` | A list of at least 1 `Tensor` objects with type `string`. Can be of any shape. Each must contain serialized `Summary` protocol buffers. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |