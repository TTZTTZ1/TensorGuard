# tf.raw_ops.EnqueueTPUEmbeddingRaggedTensorBatch

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/EnqueueTPUEmbeddingRaggedTensorBatch](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/EnqueueTPUEmbeddingRaggedTensorBatch)

---

Eases the porting of code that uses tf.nn.embedding\_lookup().

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.EnqueueTPUEmbeddingRaggedTensorBatch`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/EnqueueTPUEmbeddingRaggedTensorBatch)

```
tf.raw_ops.EnqueueTPUEmbeddingRaggedTensorBatch(
    sample_splits,
    embedding_indices,
    aggregation_weights,
    mode_override,
    table_ids,
    device_ordinal=-1,
    combiners=[],
    max_sequence_lengths=[],
    num_features=[],
    name=None
)
```

sample\_splits[i], embedding\_indices[i] and aggregation\_weights[i] correspond
to the ith feature. table\_ids[i] indicates which embedding table to look up ith
feature.

The tensors at corresponding positions in two of the input lists,
embedding\_indices and aggregation\_weights, must have the same shape, i.e. rank 1
with dim\_size() equal to the total number of lookups into the table described by
the corresponding feature.

| Args | |

|  |  |
| --- | --- |
| `sample_splits` | A list of at least 1 `Tensor` objects with the same type in: `int32`, `int64`. A list of rank 1 Tensors specifying the break points for splitting embedding\_indices and aggregation\_weights into rows. It corresponds to ids.row\_splits in embedding\_lookup(), when ids is a RaggedTensor. |
| `embedding_indices` | A list with the same length as `sample_splits` of `Tensor` objects with the same type in: `int32`, `int64`. A list of rank 1 Tensors, indices into the embedding tables. It corresponds to ids.values in embedding\_lookup(), when ids is a RaggedTensor. |
| `aggregation_weights` | A list with the same length as `sample_splits` of `Tensor` objects with the same type in: `float32`, `float64`. A list of rank 1 Tensors containing per training example aggregation weights. It corresponds to the values field of a RaggedTensor with the same row\_splits as ids in embedding\_lookup(), when ids is a RaggedTensor. |
| `mode_override` | A `Tensor` of type `string`. A string input that overrides the mode specified in the TPUEmbeddingConfiguration. Supported values are {'unspecified', 'inference', 'training', 'backward\_pass\_only'}. When set to 'unspecified', the mode set in TPUEmbeddingConfiguration is used, otherwise mode\_override is used. |
| `table_ids` | A list of `ints`. A list of integers specifying the identifier of the embedding table (offset of TableDescriptor in the TPUEmbeddingConfiguration) to lookup the corresponding input. The ith input is looked up using table\_ids[i]. The size of the table\_ids list must be equal to that of sample\_indices, embedding\_indices and aggregation\_weights. |
| `device_ordinal` | An optional `int`. Defaults to `-1`. The TPU device to use. Should be >= 0 and less than the number of TPU cores in the task on which the node is placed. |
| `combiners` | An optional list of `strings`. Defaults to `[]`. A list of string scalars, one for each embedding table that specify how to normalize the embedding activations after weighted summation. Supported combiners are 'mean', 'sum', or 'sqrtn'. It is invalid to have the sum of the weights be 0 for 'mean' or the sum of the squared weights be 0 for 'sqrtn'. If combiners isn't passed, the default is to use 'sum' for all tables. |
| `max_sequence_lengths` | An optional list of `ints`. Defaults to `[]`. |
| `num_features` | An optional list of `ints`. Defaults to `[]`. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |