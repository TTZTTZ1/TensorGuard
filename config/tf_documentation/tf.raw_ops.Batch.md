# tf.raw_ops.Batch

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Batch](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Batch)

---

Batches all input tensors nondeterministically.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Batch`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Batch)

```
tf.raw_ops.Batch(
    in_tensors,
    num_batch_threads,
    max_batch_size,
    batch_timeout_micros,
    grad_timeout_micros,
    max_enqueued_batches=10,
    allowed_batch_sizes=[],
    container='',
    shared_name='',
    batching_queue='',
    name=None
)
```

When many instances of this Op are being run concurrently with the same
container/shared\_name in the same device, some will output zero-shaped Tensors
and others will output Tensors of size up to max\_batch\_size.

All Tensors in in\_tensors are batched together (so, for example, labels and
features should be batched with a single instance of this operation.

Each invocation of batch emits an `id` scalar which will be used to identify
this particular invocation when doing unbatch or its gradient.

Each op which emits a non-empty batch will also emit a non-empty batch\_index
Tensor, which, is a [K, 3] matrix where each row contains the invocation's id,
start, and length of elements of each set of Tensors present in batched\_tensors.

Batched tensors are concatenated along the first dimension, and all tensors in
in\_tensors must have the first dimension of the same size.

in\_tensors: The tensors to be batched.
num\_batch\_threads: Number of scheduling threads for processing batches of work.
Determines the number of batches processed in parallel.
max\_batch\_size: Batch sizes will never be bigger than this.
batch\_timeout\_micros: Maximum number of microseconds to wait before outputting
an incomplete batch.
allowed\_batch\_sizes: Optional list of allowed batch sizes. If left empty, does
nothing. Otherwise, supplies a list of batch sizes, causing the op to pad
batches up to one of those sizes. The entries must increase monotonically, and
the final entry must equal max\_batch\_size.
grad\_timeout\_micros: The timeout to use for the gradient. See Unbatch.
batched\_tensors: Either empty tensors or a batch of concatenated Tensors.
batch\_index: If out\_tensors is non-empty, has information to invert it.
container: Controls the scope of sharing of this batch.
id: always contains a scalar with a unique ID for this invocation of Batch.
shared\_name: Concurrently running instances of batch in the same device with the
same container and shared\_name will batch their elements together. If left
empty, the op name will be used as the shared name.
T: the types of tensors to be batched.

| Args | |

|  |  |
| --- | --- |
| `in_tensors` | A list of `Tensor` objects. |
| `num_batch_threads` | An `int`. |
| `max_batch_size` | An `int`. |
| `batch_timeout_micros` | An `int`. |
| `grad_timeout_micros` | An `int`. |
| `max_enqueued_batches` | An optional `int`. Defaults to `10`. |
| `allowed_batch_sizes` | An optional list of `ints`. Defaults to `[]`. |
| `container` | An optional `string`. Defaults to `""`. |
| `shared_name` | An optional `string`. Defaults to `""`. |
| `batching_queue` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (batched\_tensors, batch\_index, id). | |
| `batched_tensors` | A list of `Tensor` objects. Has the same type as `in_tensors`. |
| `batch_index` | A `Tensor` of type `int64`. |
| `id` | A `Tensor` of type `int64`. |