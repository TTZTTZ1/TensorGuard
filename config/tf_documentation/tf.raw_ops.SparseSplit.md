# tf.raw_ops.SparseSplit

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSplit](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSplit)

---

Split a `SparseTensor` into `num_split` tensors along one dimension.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseSplit`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSplit)

```
tf.raw_ops.SparseSplit(
    split_dim, indices, values, shape, num_split, name=None
)
```

If the `shape[split_dim]` is not an integer multiple of `num_split`. Slices
`[0 : shape[split_dim] % num_split]` gets one extra dimension.
For example, if `split_dim = 1` and `num_split = 2` and the input is

```
input_tensor = shape = [2, 7]
[    a   d e  ]
[b c          ]
```

Graphically the output tensors are:

```
output_tensor[0] = shape = [2, 4]
[    a  ]
[b c    ]

output_tensor[1] = shape = [2, 3]
[ d e  ]
[      ]
```

| Args | |

|  |  |
| --- | --- |
| `split_dim` | A `Tensor` of type `int64`. 0-D. The dimension along which to split. Must be in the range `[0, rank(shape))`. |
| `indices` | A `Tensor` of type `int64`. 2-D tensor represents the indices of the sparse tensor. |
| `values` | A `Tensor`. 1-D tensor represents the values of the sparse tensor. |
| `shape` | A `Tensor` of type `int64`. 1-D. tensor represents the shape of the sparse tensor. output indices: A list of 1-D tensors represents the indices of the output sparse tensors. |
| `num_split` | An `int` that is `>= 1`. The number of ways to split. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (output\_indices, output\_values, output\_shape). | |
| `output_indices` | A list of `num_split` `Tensor` objects with type `int64`. |
| `output_values` | A list of `num_split` `Tensor` objects with the same type as `values`. |
| `output_shape` | A list of `num_split` `Tensor` objects with type `int64`. |