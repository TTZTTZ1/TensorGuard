# tf.raw_ops.UnbatchGrad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/UnbatchGrad](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/UnbatchGrad)

---

Gradient of Unbatch.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.UnbatchGrad`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/UnbatchGrad)

```
tf.raw_ops.UnbatchGrad(
    original_input,
    batch_index,
    grad,
    id,
    container='',
    shared_name='',
    name=None
)
```

Acts like Batch but using the given batch\_index index of batching things as they
become available. This ensures that the gradients are propagated back in the
same session which did the forward pass.

original\_input: The input to the Unbatch operation this is the gradient of.
batch\_index: The batch\_index given to the Unbatch operation this is the gradient
of.
grad: The downstream gradient.
id: The id scalar emitted by Batch.
batched\_grad: The return value, either an empty tensor or the batched gradient.
container: Container to control resource sharing.
shared\_name: Instances of UnbatchGrad with the same container and shared\_name
are assumed to possibly belong to the same batch. If left empty, the op name
will be used as the shared name.

| Args | |

|  |  |
| --- | --- |
| `original_input` | A `Tensor`. |
| `batch_index` | A `Tensor` of type `int64`. |
| `grad` | A `Tensor`. Must have the same type as `original_input`. |
| `id` | A `Tensor` of type `int64`. |
| `container` | An optional `string`. Defaults to `""`. |
| `shared_name` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `original_input`. | |