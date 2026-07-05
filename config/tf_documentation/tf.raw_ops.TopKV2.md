# tf.raw_ops.TopKV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TopKV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TopKV2)

---

Finds values and indices of the `k` largest elements for the last dimension.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TopKV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TopKV2)

```
tf.raw_ops.TopKV2(
    input,
    k,
    sorted=True,
    index_type=tf.dtypes.int32,
    name=None
)

tf.dtypes.int32
```

If the input is a vector (rank-1), finds the `k` largest entries in the vector
and outputs their values and indices as vectors. Thus `values[j]` is the
`j`-th largest entry in `input`, and its index is `indices[j]`.

For matrices (resp. higher rank input), computes the top `k` entries in each
row (resp. vector along the last dimension). Thus,

```
values.shape = indices.shape = input.shape[:-1] + [k]
```

If two elements are equal, the lower-index element appears first.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. 1-D or higher with last dimension at least `k`. |
| `k` | A `Tensor`. Must be one of the following types: `int16`, `int32`, `int64`. 0-D. Number of top elements to look for along the last dimension (along each row for matrices). |
| `sorted` | An optional `bool`. Defaults to `True`. If true the resulting `k` elements will be sorted by the values in descending order. |
| `index_type` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.int16, tf.int32, tf.int64`. Defaults to [`tf.int32`](https://tensorflow.google.cn/api_docs/python/tf#int32). |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (values, indices). | |
| `values` | A `Tensor`. Has the same type as `input`. |
| `indices` | A `Tensor` of type `index_type`. |