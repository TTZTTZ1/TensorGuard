# tf.sparse.eye

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/sparse/eye](https://tensorflow.google.cn/api_docs/python/tf/sparse/eye)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/sparse_ops.py#L249-L280) |

Creates a two-dimensional sparse tensor with ones along the diagonal.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.sparse.eye`](https://tensorflow.google.cn/api_docs/python/tf/sparse/eye)

```
tf.sparse.eye(
    num_rows,
    num_columns=None,
    dtype=tf.dtypes.float32,
    name=None
)

tf.dtypes.float32
```

| Args | |

|  |  |
| --- | --- |
| `num_rows` | Non-negative integer or `int32` scalar `tensor` giving the number of rows in the resulting matrix. |
| `num_columns` | Optional non-negative integer or `int32` scalar `tensor` giving the number of columns in the resulting matrix. Defaults to `num_rows`. |
| `dtype` | The type of element in the resulting `Tensor`. |
| `name` | A name for this `Op`. Defaults to "eye". |

| Returns | |
| A `SparseTensor` of shape [num\_rows, num\_columns] with ones along the diagonal. | |