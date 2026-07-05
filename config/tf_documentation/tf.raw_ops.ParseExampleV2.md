# tf.raw_ops.ParseExampleV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ParseExampleV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ParseExampleV2)

---

Transforms a vector of tf.Example protos (as strings) into typed tensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ParseExampleV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ParseExampleV2)

```
tf.raw_ops.ParseExampleV2(
    serialized,
    names,
    sparse_keys,
    dense_keys,
    ragged_keys,
    dense_defaults,
    num_sparse,
    sparse_types,
    ragged_value_types,
    ragged_split_types,
    dense_shapes,
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `serialized` | A `Tensor` of type `string`. A scalar or vector containing binary serialized Example protos. |
| `names` | A `Tensor` of type `string`. A tensor containing the names of the serialized protos. Corresponds 1:1 with the `serialized` tensor. May contain, for example, table key (descriptive) names for the corresponding serialized protos. These are purely useful for debugging purposes, and the presence of values here has no effect on the output. May also be an empty vector if no names are available. If non-empty, this tensor must have the same shape as "serialized". |
| `sparse_keys` | A `Tensor` of type `string`. Vector of strings. The keys expected in the Examples' features associated with sparse values. |
| `dense_keys` | A `Tensor` of type `string`. Vector of strings. The keys expected in the Examples' features associated with dense values. |
| `ragged_keys` | A `Tensor` of type `string`. Vector of strings. The keys expected in the Examples' features associated with ragged values. |
| `dense_defaults` | A list of `Tensor` objects with types from: `float32`, `int64`, `string`. A list of Tensors (some may be empty). Corresponds 1:1 with `dense_keys`. dense\_defaults[j] provides default values when the example's feature\_map lacks dense\_key[j]. If an empty Tensor is provided for dense\_defaults[j], then the Feature dense\_keys[j] is required. The input type is inferred from dense\_defaults[j], even when it's empty. If dense\_defaults[j] is not empty, and dense\_shapes[j] is fully defined, then the shape of dense\_defaults[j] must match that of dense\_shapes[j]. If dense\_shapes[j] has an undefined major dimension (variable strides dense feature), dense\_defaults[j] must contain a single element: the padding element. |
| `num_sparse` | An `int` that is `>= 0`. The number of sparse keys. |
| `sparse_types` | A list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. A list of `num_sparse` types; the data types of data in each Feature given in sparse\_keys. Currently the ParseExample supports DT\_FLOAT (FloatList), DT\_INT64 (Int64List), and DT\_STRING (BytesList). |
| `ragged_value_types` | A list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. A list of `num_ragged` types; the data types of data in each Feature given in ragged\_keys (where `num_ragged = sparse_keys.size()`). Currently the ParseExample supports DT\_FLOAT (FloatList), DT\_INT64 (Int64List), and DT\_STRING (BytesList). |
| `ragged_split_types` | A list of `tf.DTypes` from: `tf.int32, tf.int64`. A list of `num_ragged` types; the data types of row\_splits in each Feature given in ragged\_keys (where `num_ragged = sparse_keys.size()`). May be DT\_INT32 or DT\_INT64. |
| `dense_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`). A list of `num_dense` shapes; the shapes of data in each Feature given in dense\_keys (where `num_dense = dense_keys.size()`). The number of elements in the Feature corresponding to dense\_key[j] must always equal dense\_shapes[j].NumEntries(). If dense\_shapes[j] == (D0, D1, ..., DN) then the shape of output Tensor dense\_values[j] will be (|serialized|, D0, D1, ..., DN): The dense outputs are just the inputs row-stacked by batch. This works for dense\_shapes[j] = (-1, D1, ..., DN). In this case the shape of the output Tensor dense\_values[j] will be (|serialized|, M, D1, .., DN), where M is the maximum number of blocks of elements of length D1 \* .... \* DN, across all minibatch entries in the input. Any minibatch entry with less than M blocks of elements of length D1 \* ... \* DN will be padded with the corresponding default\_value scalar element along the second dimension. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (sparse\_indices, sparse\_values, sparse\_shapes, dense\_values, ragged\_values, ragged\_row\_splits). | |
| `sparse_indices` | A list of `num_sparse` `Tensor` objects with type `int64`. |
| `sparse_values` | A list of `Tensor` objects of type `sparse_types`. |
| `sparse_shapes` | A list of `num_sparse` `Tensor` objects with type `int64`. |
| `dense_values` | A list of `Tensor` objects. Has the same type as `dense_defaults`. |
| `ragged_values` | A list of `Tensor` objects of type `ragged_value_types`. |
| `ragged_row_splits` | A list of `Tensor` objects of type `ragged_split_types`. |