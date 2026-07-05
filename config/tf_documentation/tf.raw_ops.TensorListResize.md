# tf.raw_ops.TensorListResize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListResize](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListResize)

---

Resizes the list.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TensorListResize`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TensorListResize)

```
tf.raw_ops.TensorListResize(
    input_handle, size, name=None
)
```

input\_handle: the input list
size: size of the output list

| Args | |

|  |  |
| --- | --- |
| `input_handle` | A `Tensor` of type `variant`. |
| `size` | A `Tensor` of type `int32`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |