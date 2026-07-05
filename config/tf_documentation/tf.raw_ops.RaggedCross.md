# tf.raw_ops.RaggedCross

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RaggedCross](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RaggedCross)

---

Generates a feature cross from a list of tensors, and returns it as a RaggedTensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.RaggedCross`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RaggedCross)

```
tf.raw_ops.RaggedCross(
    ragged_values,
    ragged_row_splits,
    sparse_indices,
    sparse_values,
    sparse_shape,
    dense_inputs,
    input_order,
    hashed_output,
    num_buckets,
    hash_key,
    out_values_type,
    out_row_splits_type,
    name=None
)
```

See [`tf.ragged.cross`](https://tensorflow.google.cn/api_docs/python/tf/ragged/cross) for more details.

Args:
ragged\_values: A list of `Tensor` objects with types from: `int64`, `string`.
The values tensor for each RaggedTensor input.
ragged\_row\_splits: A list of `Tensor` objects with types from: `int32`, `int64`.
The row\_splits tensor for each RaggedTensor input.
sparse\_indices: A list of `Tensor` objects with type `int64`.
The indices tensor for each SparseTensor input.
sparse\_values: A list of `Tensor` objects with types from: `int64`, `string`.
The values tensor for each SparseTensor input.
sparse\_shape: A list with the same length as `sparse_indices` of `Tensor` objects with type `int64`.
The dense\_shape tensor for each SparseTensor input.
dense\_inputs: A list of `Tensor` objects with types from: `int64`, `string`.
The tf.Tensor inputs.
input\_order: A `string`.
String specifying the tensor type for each input. The `i`th character in
this string specifies the type of the `i`th input, and is one of: 'R' (ragged),
'D' (dense), or 'S' (sparse). This attr is used to ensure that the crossed
values are combined in the order of the inputs from the call to tf.ragged.cross.
hashed\_output: A `bool`.
num\_buckets: An `int` that is `>= 0`.
hash\_key: An `int`.
out\_values\_type: A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.int64, tf.string`.
out\_row\_splits\_type: A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.int32, tf.int64`.
name: A name for the operation (optional).

Returns:
A tuple of `Tensor` objects (output\_values, output\_row\_splits).

```
output_values: A `Tensor` of type `out_values_type`.
output_row_splits: A `Tensor` of type `out_row_splits_type`.
```