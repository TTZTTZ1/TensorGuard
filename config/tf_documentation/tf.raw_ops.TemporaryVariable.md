# tf.raw_ops.TemporaryVariable

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TemporaryVariable](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TemporaryVariable)

---

Returns a tensor that may be mutated, but only persists within a single step.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TemporaryVariable`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TemporaryVariable)

```
tf.raw_ops.TemporaryVariable(
    shape, dtype, var_name='', name=None
)
```

This is an experimental op for internal use only and it is possible to use this
op in unsafe ways. DO NOT USE unless you fully understand the risks.

It is the caller's responsibility to ensure that 'ref' is eventually passed to a
matching 'DestroyTemporaryVariable' op after all other uses have completed.

Outputs a ref to the tensor state so it may be read or modified.

E.g.
var = state\_ops.\_temporary*variable([1, 2], types.float*)
var\_name = var.op.name
var = state\_ops.assign(var, [[4.0, 5.0]])
var = state\_ops.assign\_add(var, [[6.0, 7.0]])
final = state\_ops.\_destroy\_temporary\_variable(var, var\_name=var\_name)

| Args | |

|  |  |
| --- | --- |
| `shape` | A [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. The shape of the variable tensor. |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). The type of elements in the variable tensor. |
| `var_name` | An optional `string`. Defaults to `""`. Overrides the name used for the temporary variable resource. Default value is the name of the 'TemporaryVariable' op (which is guaranteed unique). |
| `name` | A name for the operation (optional). |

| Returns | |
| A mutable `Tensor` of type `dtype`. | |