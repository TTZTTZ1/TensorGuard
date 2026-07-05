# tf.raw_ops.Unbatch

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Unbatch](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Unbatch)

---

Reverses the operation of Batch for a single output Tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Unbatch`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Unbatch)

```
tf.raw_ops.Unbatch(
    batched_tensor,
    batch_index,
    id,
    timeout_micros,
    container='',
    shared_name='',
    name=None
)
```

An instance of Unbatch either receives an empty batched\_tensor, in which case it
asynchronously waits until the values become available from a concurrently
running instance of Unbatch with the same container and shared\_name, or receives
a non-empty batched\_tensor in which case it finalizes all other concurrently
running instances and outputs its own element from the batch.

batched\_tensor: The possibly transformed output of Batch. The size of the first
dimension should remain unchanged by the transformations for the operation to
work.
batch\_index: The matching batch\_index obtained from Batch.
id: The id scalar emitted by Batch.
unbatched\_tensor: The Tensor corresponding to this execution.
timeout\_micros: Maximum amount of time (in microseconds) to wait to receive the
batched input tensor associated with a given invocation of the op.
container: Container to control resource sharing.
shared\_name: Instances of Unbatch with the same container and shared\_name are
assumed to possibly belong to the same batch. If left empty, the op name will
be used as the shared name.

| Args | |

|  |  |
| --- | --- |
| `batched_tensor` | A `Tensor`. |
| `batch_index` | A `Tensor` of type `int64`. |
| `id` | A `Tensor` of type `int64`. |
| `timeout_micros` | An `int`. |
| `container` | An optional `string`. Defaults to `""`. |
| `shared_name` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `batched_tensor`. | |