# tf.raw_ops.RemoteCall

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RemoteCall](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RemoteCall)

---

Runs function `f` on a remote device indicated by `target`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.RemoteCall`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RemoteCall)

```
tf.raw_ops.RemoteCall(
    target, args, Tout, f, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `target` | A `Tensor` of type `string`. A fully specified device name where we want to run the function. |
| `args` | A list of `Tensor` objects. A list of arguments for the function. |
| `Tout` | A list of `tf.DTypes` that has length `>= 1`. The type list for the return values. |
| `f` | A function decorated with @Defun. The function to run remotely. |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `Tensor` objects of type `Tout`. | |