# tf.raw_ops.EagerPyFunc

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/EagerPyFunc](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/EagerPyFunc)

---

Eagerly executes a python function to compute func(input)->output.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.EagerPyFunc`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/EagerPyFunc)

```
tf.raw_ops.EagerPyFunc(
    input, token, Tout, is_async=False, name=None
)
```

The

semantics of the input, output, and attributes are the same as those for
PyFunc.

| Args | |

|  |  |
| --- | --- |
| `input` | A list of `Tensor` objects. |
| `token` | A `string`. |
| `Tout` | A list of `tf.DTypes`. |
| `is_async` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `Tensor` objects of type `Tout`. | |