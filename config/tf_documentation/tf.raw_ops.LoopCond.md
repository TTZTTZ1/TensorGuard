# tf.raw_ops.LoopCond

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LoopCond](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LoopCond)

---

Forwards the input to the output.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.LoopCond`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LoopCond)

```
tf.raw_ops.LoopCond(
    input, name=None
)
```

This operator represents the loop termination condition used by the
"pivot" switches of a loop.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` of type `bool`. A boolean scalar, representing the branch predicate of the Switch op. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |