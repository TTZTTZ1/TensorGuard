# tf.raw_ops.VarHandleOp

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/VarHandleOp](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/VarHandleOp)

---

Creates a handle to a Variable resource.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.VarHandleOp`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/VarHandleOp)

```
tf.raw_ops.VarHandleOp(
    dtype,
    shape,
    container='',
    shared_name='',
    debug_name='',
    allowed_devices=[],
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). the type of this variable. Must agree with the dtypes of all ops using this variable. |
| `shape` | A [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. The (possibly partially specified) shape of this variable. |
| `container` | An optional `string`. Defaults to `""`. the container this variable is placed in. |
| `shared_name` | An optional `string`. Defaults to `""`. the name by which this variable is referred to. |
| `debug_name` | An optional `string`. Defaults to `""`. the user-given name, which still applies in anonymous mode. |
| `allowed_devices` | An optional list of `strings`. Defaults to `[]`. DEPRECATED. The allowed devices containing the resource variable. Set when the output ResourceHandle represents a per-replica/partitioned resource variable. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `resource`. | |