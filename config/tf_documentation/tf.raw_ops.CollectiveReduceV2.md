# tf.raw_ops.CollectiveReduceV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveReduceV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveReduceV2)

---

Mutually reduces multiple tensors of identical type and shape.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CollectiveReduceV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveReduceV2)

```
tf.raw_ops.CollectiveReduceV2(
    input,
    group_size,
    group_key,
    instance_key,
    ordering_token,
    merge_op,
    final_op,
    communication_hint='auto',
    timeout_seconds=0,
    is_stateless=False,
    max_subdivs_per_device=-1,
    name=None
)
```

`is_stateless` means each op does not need control dependencies to other
collective ops. In this case, keys that are unique at runtime
(e.g. `instance_key`) should be used to distinguish collective groups.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `bfloat16`, `float32`, `half`, `float64`, `int32`, `int64`. |
| `group_size` | A `Tensor` of type `int32`. |
| `group_key` | A `Tensor` of type `int32`. |
| `instance_key` | A `Tensor` of type `int32`. |
| `ordering_token` | A list of `Tensor` objects with type `resource`. |
| `merge_op` | A `string` from: `"Min", "Max", "Mul", "Add"`. |
| `final_op` | A `string` from: `"Id", "Div"`. |
| `communication_hint` | An optional `string`. Defaults to `"auto"`. |
| `timeout_seconds` | An optional `float`. Defaults to `0`. |
| `is_stateless` | An optional `bool`. Defaults to `False`. |
| `max_subdivs_per_device` | An optional `int`. Defaults to `-1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |