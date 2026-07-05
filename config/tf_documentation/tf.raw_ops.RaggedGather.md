# tf.raw_ops.RaggedGather

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RaggedGather](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RaggedGather)

---

Gather ragged slices from `params` axis `0` according to `indices`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.RaggedGather`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RaggedGather)

```
tf.raw_ops.RaggedGather(
    params_nested_splits,
    params_dense_values,
    indices,
    OUTPUT_RAGGED_RANK,
    name=None
)
```

Outputs a `RaggedTensor` output composed from `output_dense_values` and
`output_nested_splits`, such that:

```
output.shape = indices.shape + params.shape[1:]
output.ragged_rank = indices.shape.ndims + params.ragged_rank
output[i...j, d0...dn] = params[indices[i...j], d0...dn]
```

where

* `params =
  ragged.from_nested_row_splits(params_dense_values, params_nested_splits)`
  provides the values that should be gathered.
* `indices` ia a dense tensor with dtype `int32` or `int64`, indicating which
  values should be gathered.
* `output =
  ragged.from_nested_row_splits(output_dense_values, output_nested_splits)`
  is the output tensor.

(Note: This c++ op is used to implement the higher-level python
`tf.ragged.gather` op, which also supports ragged indices.)

| Args | |

|  |  |
| --- | --- |
| `params_nested_splits` | A list of at least 1 `Tensor` objects with the same type in: `int32`, `int64`. The `nested_row_splits` tensors that define the row-partitioning for the `params` RaggedTensor input. |
| `params_dense_values` | A `Tensor`. The `flat_values` for the `params` RaggedTensor. There was a terminology change at the python level from dense\_values to flat\_values, so dense\_values is the deprecated name. |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. Indices in the outermost dimension of `params` of the values that should be gathered. |
| `OUTPUT_RAGGED_RANK` | An `int` that is `>= 0`. The ragged rank of the output RaggedTensor. `output_nested_splits` will contain this number of `row_splits` tensors. This value should equal `indices.shape.ndims + params.ragged_rank - 1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (output\_nested\_splits, output\_dense\_values). | |
| `output_nested_splits` | A list of `OUTPUT_RAGGED_RANK` `Tensor` objects with the same type as `params_nested_splits`. |
| `output_dense_values` | A `Tensor`. Has the same type as `params_dense_values`. |