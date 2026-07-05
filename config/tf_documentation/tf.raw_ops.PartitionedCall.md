# tf.raw_ops.PartitionedCall

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/PartitionedCall](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/PartitionedCall)

---

returns `f(inputs)`, where `f`'s body is placed and partitioned.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.PartitionedCall`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/PartitionedCall)

```
tf.raw_ops.PartitionedCall(
    args,
    Tout,
    f,
    config='',
    config_proto='',
    executor_type='',
    name=None
)
```

Asynchronously executes a function, potentially across multiple devices but
within a single process. The kernel places and partitions a given function's
underlying graph, and executes each of the partitioned subgraphs as a function.

| Args | |

|  |  |
| --- | --- |
| `args` | A list of `Tensor` objects. A list of input tensors. |
| `Tout` | A list of `tf.DTypes`. A list of output types. |
| `f` | A function decorated with @Defun. A function that takes 'args', a list of tensors, and returns 'output', another list of tensors. Input and output types are specified by 'Tin' and 'Tout'. The function body of f will be placed and partitioned across devices, setting this op apart from the regular Call op. |
| `config` | An optional `string`. Defaults to `""`. |
| `config_proto` | An optional `string`. Defaults to `""`. |
| `executor_type` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `Tensor` objects of type `Tout`. | |