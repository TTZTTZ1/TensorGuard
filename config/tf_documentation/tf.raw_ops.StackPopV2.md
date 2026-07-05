# tf.raw_ops.StackPopV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StackPopV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StackPopV2)

---

Pop the element at the top of the stack.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.StackPopV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/StackPopV2)

```
tf.raw_ops.StackPopV2(
    handle, elem_type, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `handle` | A `Tensor` of type `resource`. The handle to a stack. |
| `elem_type` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). The type of the elem that is popped. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `elem_type`. | |