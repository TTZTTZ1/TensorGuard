# tf.raw_ops.SparseSlice

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSlice](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSlice)

---

Slice a `SparseTensor` based on the `start` and `size`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseSlice`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSlice)

```
tf.raw_ops.SparseSlice(
    indices, values, shape, start, size, name=None
)
```

For example, if the input is

```
input_tensor = shape = [2, 7]
[    a   d e  ]
[b c          ]
```

Graphically the output tensors are:

```
sparse_slice([0, 0], [2, 4]) = shape = [2, 4]
[    a  ]
[b c    ]

sparse_slice([0, 4], [2, 3]) = shape = [2, 3]
[ d e  ]
[      ]
```

| Args | |

|  |  |
| --- | --- |
| `indices` | A `Tensor` of type `int64`. 2-D tensor represents the indices of the sparse tensor. |
| `values` | A `Tensor`. 1-D tensor represents the values of the sparse tensor. |
| `shape` | A `Tensor` of type `int64`. 1-D. tensor represents the shape of the sparse tensor. |
| `start` | A `Tensor` of type `int64`. 1-D. tensor represents the start of the slice. |
| `size` | A `Tensor` of type `int64`. 1-D. tensor represents the size of the slice. output indices: A list of 1-D tensors represents the indices of the output sparse tensors. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (output\_indices, output\_values, output\_shape). | |
| `output_indices` | A `Tensor` of type `int64`. |
| `output_values` | A `Tensor`. Has the same type as `values`. |
| `output_shape` | A `Tensor` of type `int64`. |