# tf.raw_ops.For

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/For](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/For)

---

Applies a for loop.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.For`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/For)

```
tf.raw_ops.For(
    start, limit, delta, input, body, name=None
)
```

```
   output = input;
   for i in range(start, limit, delta)
     output = body(i, output);
```

| Args | |

|  |  |
| --- | --- |
| `start` | A `Tensor` of type `int32`. The lower bound. An int32 |
| `limit` | A `Tensor` of type `int32`. The upper bound. An int32 |
| `delta` | A `Tensor` of type `int32`. The increment. An int32 |
| `input` | A list of `Tensor` objects. A list of input tensors whose types are T. |
| `body` | A function decorated with @Defun. A function that takes a list of tensors (int32, T) and returns another list of tensors (T). |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `Tensor` objects. Has the same type as `input`. | |