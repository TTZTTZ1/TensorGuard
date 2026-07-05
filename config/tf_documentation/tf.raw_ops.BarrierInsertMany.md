# tf.raw_ops.BarrierInsertMany

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BarrierInsertMany](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BarrierInsertMany)

---

For each key, assigns the respective value to the specified component.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.BarrierInsertMany`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BarrierInsertMany)

```
tf.raw_ops.BarrierInsertMany(
    handle, keys, values, component_index, name=None
)
```

If a key is not found in the barrier, this operation will create a new
incomplete element. If a key is found in the barrier, and the element
already has a value at component\_index, this operation will fail with
INVALID\_ARGUMENT, and leave the barrier in an undefined state.

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type mutable `string`. The handle to a barrier. |
| `keys` | A `Tensor` of type `string`. A one-dimensional tensor of keys, with length n. |
| `values` | A `Tensor`. An any-dimensional tensor of values, which are associated with the respective keys. The 0th dimension must have length n. |
| `component_index` | An `int`. The component of the barrier elements that is being assigned. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |