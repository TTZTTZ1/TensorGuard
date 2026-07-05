# tf.raw_ops.If

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/If](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/If)

---

output = cond ? then\_branch(input) : else\_branch(input)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.If`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/If)

```
tf.raw_ops.If(
    cond, input, Tout, then_branch, else_branch, output_shapes=[], name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `cond` | A `Tensor`. A Tensor. If the tensor is a scalar of non-boolean type, the scalar is converted to a boolean according to the following rule: if the scalar is a numerical value, non-zero means `True` and zero means False; if the scalar is a string, non-empty means `True` and empty means `False`. If the tensor is not a scalar, being empty means False and being non-empty means True. |
| `input` | A list of `Tensor` objects. A list of input tensors. |
| `Tout` | A list of `tf.DTypes`. A list of output types. |
| `then_branch` | A function decorated with @Defun. A function that takes 'inputs' and returns a list of tensors, whose types are the same as what else\_branch returns. |
| `else_branch` | A function decorated with @Defun. A function that takes 'inputs' and returns a list of tensors, whose types are the same as what then\_branch returns. |
| `output_shapes` | An optional list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`). Defaults to `[]`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `Tensor` objects of type `Tout`. | |