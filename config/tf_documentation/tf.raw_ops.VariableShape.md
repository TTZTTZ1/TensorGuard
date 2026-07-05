# tf.raw_ops.VariableShape

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/VariableShape](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/VariableShape)

---

Returns the shape of the variable pointed to by `resource`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.VariableShape`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/VariableShape)

```
tf.raw_ops.VariableShape(
    input,
    out_type=tf.dtypes.int32,
    name=None
)

tf.dtypes.int32
```

This operation returns a 1-D integer tensor representing the shape of `input`.

#### For example:

```
# 't' is [[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]]
shape(t) ==> [2, 2, 3]
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` of type `resource`. |
| `out_type` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.int32, tf.int64`. Defaults to [`tf.int32`](https://tensorflow.google.cn/api_docs/python/tf#int32). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `out_type`. | |