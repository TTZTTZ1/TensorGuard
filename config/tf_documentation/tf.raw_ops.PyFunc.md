# tf.raw_ops.PyFunc

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/PyFunc](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/PyFunc)

---

Invokes a python function to compute func(input)->output.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.PyFunc`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/PyFunc)

```
tf.raw_ops.PyFunc(
    input, token, Tout, name=None
)
```

This operation is considered stateful. For a stateless version, see
PyFuncStateless.

| Args | |

|  |  |
| --- | --- |
| `input` | A list of `Tensor` objects. List of Tensors that will provide input to the Op. |
| `token` | A `string`. A token representing a registered python function in this address space. |
| `Tout` | A list of `tf.DTypes`. Data types of the outputs from the op. The length of the list specifies the number of outputs. |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `Tensor` objects of type `Tout`. | |