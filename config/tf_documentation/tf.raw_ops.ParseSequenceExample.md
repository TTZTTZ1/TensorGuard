# tf.raw_ops.ParseSequenceExample

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ParseSequenceExample](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ParseSequenceExample)

---

Transforms a vector of brain.SequenceExample protos (as strings) into typed tensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ParseSequenceExample`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ParseSequenceExample)

```
tf.raw_ops.ParseSequenceExample(
    serialized,
    debug_name,
    context_dense_defaults,
    feature_list_dense_missing_assumed_empty,
    context_sparse_keys,
    context_dense_keys,
    feature_list_sparse_keys,
    feature_list_dense_keys,
    Ncontext_sparse=0,
    Ncontext_dense=0,
    Nfeature_list_sparse=0,
    Nfeature_list_dense=0,
    context_sparse_types=[],
    feature_list_dense_types=[],
    context_dense_shapes=[],
    feature_list_sparse_types=[],
    feature_list_dense_shapes=[],
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `serialized` | A `Tensor` of type `string`. A vector containing binary serialized SequenceExample protos. |
| `debug_name` | A `Tensor` of type `string`. A vector containing the names of the serialized protos. May contain, for example, table key (descriptive) name for the corresponding serialized proto. This is purely useful for debugging purposes, and the presence of values here has no effect on the output. May also be an empty vector if no name is available. |
| `context_dense_defaults` | A list of `Tensor` objects with types from: `float32`, `int64`, `string`. A list of Ncontext\_dense Tensors (some may be empty). context\_dense\_defaults[j] provides default values when the SequenceExample's context map lacks context\_dense\_key[j]. If an empty Tensor is provided for context\_dense\_defaults[j], then the Feature context\_dense\_keys[j] is required. The input type is inferred from context\_dense\_defaults[j], even when it's empty. If context\_dense\_defaults[j] is not empty, its shape must match context\_dense\_shapes[j]. |
| `feature_list_dense_missing_assumed_empty` | A list of `strings`. A vector listing the FeatureList keys which may be missing from the SequenceExamples. If the associated FeatureList is missing, it is treated as empty. By default, any FeatureList not listed in this vector must exist in the SequenceExamples. |
| `context_sparse_keys` | A list of `strings`. A list of Ncontext\_sparse string Tensors (scalars). The keys expected in the Examples' features associated with context\_sparse values. |
| `context_dense_keys` | A list of `strings`. A list of Ncontext\_dense string Tensors (scalars). The keys expected in the SequenceExamples' context features associated with dense values. |
| `feature_list_sparse_keys` | A list of `strings`. A list of Nfeature\_list\_sparse string Tensors (scalars). The keys expected in the FeatureLists associated with sparse values. |
| `feature_list_dense_keys` | A list of `strings`. A list of Nfeature\_list\_dense string Tensors (scalars). The keys expected in the SequenceExamples' feature\_lists associated with lists of dense values. |
| `Ncontext_sparse` | An optional `int` that is `>= 0`. Defaults to `0`. |
| `Ncontext_dense` | An optional `int` that is `>= 0`. Defaults to `0`. |
| `Nfeature_list_sparse` | An optional `int` that is `>= 0`. Defaults to `0`. |
| `Nfeature_list_dense` | An optional `int` that is `>= 0`. Defaults to `0`. |
| `context_sparse_types` | An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`. A list of Ncontext\_sparse types; the data types of data in each context Feature given in context\_sparse\_keys. Currently the ParseSingleSequenceExample supports DT\_FLOAT (FloatList), DT\_INT64 (Int64List), and DT\_STRING (BytesList). |
| `feature_list_dense_types` | An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`. |
| `context_dense_shapes` | An optional list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`). Defaults to `[]`. A list of Ncontext\_dense shapes; the shapes of data in each context Feature given in context\_dense\_keys. The number of elements in the Feature corresponding to context\_dense\_key[j] must always equal context\_dense\_shapes[j].NumEntries(). The shape of context\_dense\_values[j] will match context\_dense\_shapes[j]. |
| `feature_list_sparse_types` | An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`. A list of Nfeature\_list\_sparse types; the data types of data in each FeatureList given in feature\_list\_sparse\_keys. Currently the ParseSingleSequenceExample supports DT\_FLOAT (FloatList), DT\_INT64 (Int64List), and DT\_STRING (BytesList). |
| `feature_list_dense_shapes` | An optional list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`). Defaults to `[]`. A list of Nfeature\_list\_dense shapes; the shapes of data in each FeatureList given in feature\_list\_dense\_keys. The shape of each Feature in the FeatureList corresponding to feature\_list\_dense\_key[j] must always equal feature\_list\_dense\_shapes[j].NumEntries(). |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (context\_sparse\_indices, context\_sparse\_values, context\_sparse\_shapes, context\_dense\_values, feature\_list\_sparse\_indices, feature\_list\_sparse\_values, feature\_list\_sparse\_shapes, feature\_list\_dense\_values, feature\_list\_dense\_lengths). | |
| `context_sparse_indices` | A list of `Ncontext_sparse` `Tensor` objects with type `int64`. |
| `context_sparse_values` | A list of `Tensor` objects of type `context_sparse_types`. |
| `context_sparse_shapes` | A list of `Ncontext_sparse` `Tensor` objects with type `int64`. |
| `context_dense_values` | A list of `Tensor` objects. Has the same type as `context_dense_defaults`. |
| `feature_list_sparse_indices` | A list of `Nfeature_list_sparse` `Tensor` objects with type `int64`. |
| `feature_list_sparse_values` | A list of `Tensor` objects of type `feature_list_sparse_types`. |
| `feature_list_sparse_shapes` | A list of `Nfeature_list_sparse` `Tensor` objects with type `int64`. |
| `feature_list_dense_values` | A list of `Tensor` objects of type `feature_list_dense_types`. |
| `feature_list_dense_lengths` | A list of `Nfeature_list_dense` `Tensor` objects with type `int64`. |