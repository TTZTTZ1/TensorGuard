# tf.raw_ops.CollectiveGatherV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveGatherV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveGatherV2)

---

Mutually accumulates multiple tensors of identical type and shape.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CollectiveGatherV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CollectiveGatherV2)

```
tf.raw_ops.CollectiveGatherV2(
    input,
    group_size,
    group_key,
    instance_key,
    ordering_token,
    communication_hint='auto',
    timeout_seconds=0,
    is_stateless=False,
    name=None
)
```

`is_stateless` means each op does not need control dependencies to other
collective ops. In this case, keys that are unique at runtime
(e.g. `instance_key`) should be used to distinguish collective groups.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `float32`, `half`, `float64`, `int32`, `int64`. |
| `group_size` | A `Tensor` of type `int32`. |
| `group_key` | A `Tensor` of type `int32`. |
| `instance_key` | A `Tensor` of type `int32`. |
| `ordering_token` | A list of `Tensor` objects with type `resource`. |
| `communication_hint` | An optional `string`. Defaults to `"auto"`. |
| `timeout_seconds` | An optional `float`. Defaults to `0`. |
| `is_stateless` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |