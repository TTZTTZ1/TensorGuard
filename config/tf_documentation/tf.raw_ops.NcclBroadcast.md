# tf.raw_ops.NcclBroadcast

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NcclBroadcast](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NcclBroadcast)

---

Sends `input` to all devices that are connected to the output.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.NcclBroadcast`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NcclBroadcast)

```
tf.raw_ops.NcclBroadcast(
    input, shape, name=None
)
```

Sends `input` to all devices that are connected to the output.

The graph should be constructed so that all ops connected to the output have a
valid device assignment, and the op itself is assigned one of these devices.

input: The input to the broadcast.
output: The same as input.
shape: The shape of the input tensor.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `int32`, `int64`. |
| `shape` | A [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |