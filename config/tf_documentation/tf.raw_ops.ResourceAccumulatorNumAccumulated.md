# tf.raw_ops.ResourceAccumulatorNumAccumulated

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceAccumulatorNumAccumulated](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceAccumulatorNumAccumulated)

---

Returns the number of gradients aggregated in the given accumulators.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ResourceAccumulatorNumAccumulated`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ResourceAccumulatorNumAccumulated)

```
tf.raw_ops.ResourceAccumulatorNumAccumulated(
    handle, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type `resource`. The handle to an accumulator. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int32`. | |