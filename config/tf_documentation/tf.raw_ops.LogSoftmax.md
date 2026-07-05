# tf.raw_ops.LogSoftmax

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LogSoftmax](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LogSoftmax)

---

Computes log softmax activations.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.LogSoftmax`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LogSoftmax)

```
tf.raw_ops.LogSoftmax(
    logits, name=None
)
```

For each batch `i` and class `j` we have

```
logsoftmax[i, j] = logits[i, j] - log(sum(exp(logits[i])))
```

| Args | |

|  |  |
| --- | --- |
| `logits` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. 2-D with shape `[batch_size, num_classes]`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `logits`. | |