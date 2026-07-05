# tf.raw_ops.StackPop

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StackPop](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StackPop)

---

Deprecated, use StackPopV2.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StackPop`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StackPop)

```
tf.raw_ops.StackPop(
    handle, elem_type, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type mutable `string`. |
| `elem_type` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `elem_type`. | |