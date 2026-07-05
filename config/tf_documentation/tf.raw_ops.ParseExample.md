# tf.raw_ops.ParseExample

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ParseExample](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ParseExample)

---

Transforms a vector of brain.Example protos (as strings) into typed tensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ParseExample`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ParseExample)

```
tf.raw_ops.ParseExample(
    serialized,
    names,
    sparse_keys,
    dense_keys,
    dense_defaults,
    sparse_types,
    dense_shapes,
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `serialized` | A `Tensor` of type `string`. A vector containing a batch of binary serialized Example protos. |
| `names` | A `Tensor` of type `string`. A vector containing the names of the serialized protos. May contain, for example, table key (descriptive) names for the corresponding serialized protos. These are purely useful for debugging purposes, and the presence of values here has no effect on the output. May also be an empty vector if no names are available. If non-empty, this vector must be the same length as "serialized". |
| `sparse_keys` | A list of `Tensor` objects with type `string`. A list of Nsparse string Tensors (scalars). The keys expected in the Examples' features associated with sparse values. |
| `dense_keys` | A list of `Tensor` objects with type `string`. A list of Ndense string Tensors (scalars). The keys expected in the Examples' features associated with dense values. |
| `dense_defaults` | A list of `Tensor` objects with types from: `float32`, `int64`, `string`. A list of Ndense Tensors (some may be empty). dense\_defaults[j] provides default values when the example's feature\_map lacks dense\_key[j]. If an empty Tensor is provided for dense\_defaults[j], then the Feature dense\_keys[j] is required. The input type is inferred from dense\_defaults[j], even when it's empty. If dense\_defaults[j] is not empty, and dense\_shapes[j] is fully defined, then the shape of dense\_defaults[j] must match that of dense\_shapes[j]. If dense\_shapes[j] has an undefined major dimension (variable strides dense feature), dense\_defaults[j] must contain a single element: the padding element. |
| `sparse_types` | A list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. A list of Nsparse types; the data types of data in each Feature given in sparse\_keys. Currently the ParseExample supports DT\_FLOAT (FloatList), DT\_INT64 (Int64List), and DT\_STRING (BytesList). |
| `dense_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`). A list of Ndense shapes; the shapes of data in each Feature given in dense\_keys. The number of elements in the Feature corresponding to dense\_key[j] must always equal dense\_shapes[j].NumEntries(). If dense\_shapes[j] == (D0, D1, ..., DN) then the shape of output Tensor dense\_values[j] will be (|serialized|, D0, D1, ..., DN): The dense outputs are just the inputs row-stacked by batch. This works for dense\_shapes[j] = (-1, D1, ..., DN). In this case the shape of the output Tensor dense\_values[j] will be (|serialized|, M, D1, .., DN), where M is the maximum number of blocks of elements of length D1 \* .... \* DN, across all minibatch entries in the input. Any minibatch entry with less than M blocks of elements of length D1 \* ... \* DN will be padded with the corresponding default\_value scalar element along the second dimension. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (sparse\_indices, sparse\_values, sparse\_shapes, dense\_values). | |
| `sparse_indices` | A list with the same length as `sparse_keys` of `Tensor` objects with type `int64`. |
| `sparse_values` | A list of `Tensor` objects of type `sparse_types`. |
| `sparse_shapes` | A list with the same length as `sparse_keys` of `Tensor` objects with type `int64`. |
| `dense_values` | A list of `Tensor` objects. Has the same type as `dense_defaults`. |