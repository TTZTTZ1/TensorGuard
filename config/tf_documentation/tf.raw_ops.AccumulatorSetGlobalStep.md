# tf.raw_ops.AccumulatorSetGlobalStep

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AccumulatorSetGlobalStep](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AccumulatorSetGlobalStep)

---

Updates the accumulator with a new value for global\_step.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.AccumulatorSetGlobalStep`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AccumulatorSetGlobalStep)

```
tf.raw_ops.AccumulatorSetGlobalStep(
    handle, new_global_step, name=None
)
```

Logs warning if the accumulator's value is already higher than
new\_global\_step.

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type mutable `string`. The handle to an accumulator. |
| `new_global_step` | A `Tensor` of type `int64`. The new global\_step value to set. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |