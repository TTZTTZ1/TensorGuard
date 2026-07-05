# tf.raw_ops.PyFuncStateless

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/PyFuncStateless](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/PyFuncStateless)

---

A stateless version of PyFunc.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.PyFuncStateless`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/PyFuncStateless)

```
tf.raw_ops.PyFuncStateless(
    input, token, Tout, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input` | A list of `Tensor` objects. |
| `token` | A `string`. |
| `Tout` | A list of `tf.DTypes`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `Tensor` objects of type `Tout`. | |