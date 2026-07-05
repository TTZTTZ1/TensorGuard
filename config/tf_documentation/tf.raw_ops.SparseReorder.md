# tf.raw_ops.SparseReorder

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseReorder](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseReorder)

---

Reorders a SparseTensor into the canonical, row-major ordering.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseReorder`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseReorder)

```
tf.raw_ops.SparseReorder(
    input_indices, input_values, input_shape, name=None
)
```

Note that by convention, all sparse ops preserve the canonical ordering along
increasing dimension number. The only time ordering can be violated is during
manual manipulation of the indices and values vectors to add entries.

Reordering does not affect the shape of the SparseTensor.

If the tensor has rank `R` and `N` non-empty values, `input_indices` has
shape `[N, R]`, input\_values has length `N`, and input\_shape has length `R`.

| Args | |

|  |  |
| --- | --- |
| `input_indices` | A `Tensor` of type `int64`. 2-D. `N x R` matrix with the indices of non-empty values in a SparseTensor, possibly not in canonical ordering. |
| `input_values` | A `Tensor`. 1-D. `N` non-empty values corresponding to `input_indices`. |
| `input_shape` | A `Tensor` of type `int64`. 1-D. Shape of the input SparseTensor. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (output\_indices, output\_values). | |
| `output_indices` | A `Tensor` of type `int64`. |
| `output_values` | A `Tensor`. Has the same type as `input_values`. |