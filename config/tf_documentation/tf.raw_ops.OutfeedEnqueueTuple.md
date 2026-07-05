# tf.raw_ops.OutfeedEnqueueTuple

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OutfeedEnqueueTuple](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OutfeedEnqueueTuple)

---

Enqueue multiple Tensor values on the computation outfeed.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.OutfeedEnqueueTuple`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OutfeedEnqueueTuple)

```
tf.raw_ops.OutfeedEnqueueTuple(
    inputs, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `inputs` | A list of `Tensor` objects. A list of tensors that will be inserted into the outfeed queue as an XLA tuple. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |