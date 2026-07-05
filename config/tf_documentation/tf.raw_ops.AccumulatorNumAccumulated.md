# tf.raw_ops.AccumulatorNumAccumulated

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AccumulatorNumAccumulated](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AccumulatorNumAccumulated)

---

Returns the number of gradients aggregated in the given accumulators.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.AccumulatorNumAccumulated`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AccumulatorNumAccumulated)

```
tf.raw_ops.AccumulatorNumAccumulated(
    handle, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type mutable `string`. The handle to an accumulator. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int32`. | |