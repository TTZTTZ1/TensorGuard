# tf.sparse.map_values

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/sparse/map_values](https://tensorflow.google.cn/api_docs/python/tf/sparse/map_values)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/sparse_ops.py#L2932-L2996) |

Applies `op` to the `.values` tensor of one or more `SparseTensor`s.

```
tf.sparse.map_values(
    op, *args, **kwargs
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Working with sparse tensors](https://tensorflow.google.cn/guide/sparse_tensor) |

Replaces any `SparseTensor` in `args` or `kwargs` with its `values`
tensor (which contains the non-default values for the SparseTensor),
and then calls `op`. Returns a `SparseTensor` that is constructed
from the input `SparseTensor`s' `indices`, `dense_shape`, and the
value returned by the `op`.

If the input arguments contain multiple `SparseTensor`s, then they must have
equal `indices` and dense shapes.

#### Examples:

```
>>> s = tf.sparse.from_dense([[1, 2, 0],
...                           [0, 4, 0],
...                           [1, 0, 0]])
>>> tf.sparse.to_dense(tf.sparse.map_values(tf.ones_like, s)).numpy()
array([[1, 1, 0],
       [0, 1, 0],
       [1, 0, 0]], dtype=int32)
```

```
>>> tf.sparse.to_dense(tf.sparse.map_values(tf.multiply, s, s)).numpy()
array([[ 1,  4,  0],
       [ 0, 16,  0],
       [ 1,  0,  0]], dtype=int32)
```

```
>>> tf.sparse.to_dense(tf.sparse.map_values(tf.add, s, 5)).numpy()
array([[6, 7, 0],
       [0, 9, 0],
       [6, 0, 0]], dtype=int32)
```

**Note:** even though `tf.add(0, 5) != 0`, implicit zeros
will remain unchanged. However, if the sparse tensor contains any explicit
zeros, these will be affected by the mapping!

| Args | |

|  |  |
| --- | --- |
| `op` | The operation that should be applied to the SparseTensor `values`. `op` is typically an element-wise operation (such as math\_ops.add), but any operation that preserves the shape can be used. |
| `*args` | Arguments for `op`. |
| `**kwargs` | Keyword arguments for `op`. |

| Returns | |
| A `SparseTensor` whose `indices` and `dense_shape` matches the `indices` and `dense_shape` of all input `SparseTensor`s. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If args contains no `SparseTensor`, or if the `indices` or `dense_shape`s of the input `SparseTensor`s are not equal. |