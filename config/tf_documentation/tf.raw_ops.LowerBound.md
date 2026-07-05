# tf.raw_ops.LowerBound

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LowerBound](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LowerBound)

---

Applies lower\_bound(sorted\_search\_values, values) along each row.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.LowerBound`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LowerBound)

```
tf.raw_ops.LowerBound(
    sorted_inputs,
    values,
    out_type=tf.dtypes.int32,
    name=None
)

tf.dtypes.int32
```

Each set of rows with the same index in (sorted\_inputs, values) is treated
independently. The resulting row is the equivalent of calling
`np.searchsorted(sorted_inputs, values, side='left')`.

The result is not a global index to the entire
`Tensor`, but rather just the index in the last dimension.

A 2-D example:
sorted\_sequence = [[0, 3, 9, 9, 10],
[1, 2, 3, 4, 5]]
values = [[2, 4, 9],
[0, 2, 6]]

result = LowerBound(sorted\_sequence, values)

result == [[1, 2, 2],
[0, 1, 5]]

| Args | |

|  |  |
| --- | --- |
| `sorted_inputs` | A `Tensor`. 2-D Tensor where each row is ordered. |
| `values` | A `Tensor`. Must have the same type as `sorted_inputs`. 2-D Tensor with the same numbers of rows as `sorted_search_values`. Contains the values that will be searched for in `sorted_search_values`. |
| `out_type` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.int32, tf.int64`. Defaults to [`tf.int32`](https://tensorflow.google.cn/api_docs/python/tf#int32). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `out_type`. | |