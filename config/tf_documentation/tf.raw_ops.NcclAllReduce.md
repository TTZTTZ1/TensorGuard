# tf.raw_ops.NcclAllReduce

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NcclAllReduce](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NcclAllReduce)

---

Outputs a tensor containing the reduction across all input tensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.NcclAllReduce`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NcclAllReduce)

```
tf.raw_ops.NcclAllReduce(
    input, reduction, num_devices, shared_name, name=None
)
```

Outputs a tensor containing the reduction across all input tensors passed to ops
within the same `shared\_name.

The graph should be constructed so if one op runs with shared\_name value `c`,
then `num_devices` ops will run with shared\_name value `c`. Failure to do so
will cause the graph execution to fail to complete.

input: the input to the reduction
data: the value of the reduction across all `num_devices` devices.
reduction: the reduction operation to perform.
num\_devices: The number of devices participating in this reduction.
shared\_name: Identifier that shared between ops of the same reduction.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `int32`, `int64`. |
| `reduction` | A `string` from: `"min", "max", "prod", "sum"`. |
| `num_devices` | An `int`. |
| `shared_name` | A `string`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |