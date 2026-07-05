# tf.sparse.slice

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/sparse/slice](https://tensorflow.google.cn/api_docs/python/tf/sparse/slice)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/sparse_ops.py#L1136-L1183) |

Slice a `SparseTensor` based on the `start` and `size`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.sparse.slice`](https://tensorflow.google.cn/api_docs/python/tf/sparse/slice), [`tf.compat.v1.sparse_slice`](https://tensorflow.google.cn/api_docs/python/tf/sparse/slice)

```
tf.sparse.slice(
    sp_input, start, size, name=None
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Working with sparse tensors](https://tensorflow.google.cn/guide/sparse_tensor) |

For example, if the input is

```
input_tensor = shape = [2, 7]
[    a   d e  ]
[b c          ]
```

Graphically the output tensors are:

```
sparse.slice([0, 0], [2, 4]) = shape = [2, 4]
[    a  ]
[b c    ]

sparse.slice([0, 4], [2, 3]) = shape = [2, 3]
[ d e  ]
[      ]
```

| Args | |

|  |  |
| --- | --- |
| `sp_input` | The `SparseTensor` to split. |
| `start` | 1-D. tensor represents the start of the slice. |
| `size` | 1-D. tensor represents the size of the slice. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `SparseTensor` objects resulting from splicing. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If `sp_input` is not a `SparseTensor`. |