# tf.sparse.transpose

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/sparse/transpose](https://tensorflow.google.cn/api_docs/python/tf/sparse/transpose)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/sparse_ops.py#L2824-L2929) |

Transposes a `SparseTensor`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.sparse.transpose`](https://tensorflow.google.cn/api_docs/python/tf/sparse/transpose), [`tf.compat.v1.sparse_transpose`](https://tensorflow.google.cn/api_docs/python/tf/sparse/transpose)

```
tf.sparse.transpose(
    sp_input, perm=None, name=None
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Working with sparse tensors](https://tensorflow.google.cn/guide/sparse_tensor) |

Permutes the dimensions according to the value of `perm`. This is the sparse
version of [`tf.transpose`](https://tensorflow.google.cn/api_docs/python/tf/transpose).

The returned tensor's dimension `i` will correspond to the input dimension
`perm[i]`. If `perm` is not given, it is set to (n-1...0), where n is the rank
of the input tensor. Hence, by default, this operation performs a regular
matrix transpose on 2-D input Tensors.

#### For example:

```
>>> x = tf.SparseTensor(indices=[[0, 1], [0, 3], [2, 3], [3, 1]],
...                     values=[1.1, 2.2, 3.3, 4.4],
...                     dense_shape=[4, 5])
>>> print('x =', tf.sparse.to_dense(x))
x = tf.Tensor(
[[0.  1.1 0.  2.2 0. ]
[0.  0.  0.  0.  0. ]
[0.  0.  0.  3.3 0. ]
[0.  4.4 0.  0.  0. ]], shape=(4, 5), dtype=float32)
```

```
>>> x_transpose = tf.sparse.transpose(x)
>>> print('x_transpose =', tf.sparse.to_dense(x_transpose))
x_transpose = tf.Tensor(
[[0.  0.  0.  0. ]
[1.1 0.  0.  4.4]
[0.  0.  0.  0. ]
[2.2 0.  3.3 0. ]
[0.  0.  0.  0. ]], shape=(5, 4), dtype=float32)
```

Equivalently, you could call `tf.sparse.transpose(x, perm=[1, 0])`. The
`perm` argument is more useful for n-dimensional tensors where n > 2.

```
>>> x = tf.SparseTensor(indices=[[0, 0, 1], [0, 0, 3], [1, 2, 3], [1, 3, 1]],
...                     values=[1.1, 2.2, 3.3, 4.4],
...                     dense_shape=[2, 4, 5])
>>> print('x =', tf.sparse.to_dense(x))
x = tf.Tensor(
[[[0.  1.1 0.  2.2 0. ]
  [0.  0.  0.  0.  0. ]
  [0.  0.  0.  0.  0. ]
  [0.  0.  0.  0.  0. ]]
[[0.  0.  0.  0.  0. ]
  [0.  0.  0.  0.  0. ]
  [0.  0.  0.  3.3 0. ]
  [0.  4.4 0.  0.  0. ]]], shape=(2, 4, 5), dtype=float32)
```

As above, simply calling [`tf.sparse.transpose`](https://tensorflow.google.cn/api_docs/python/tf/sparse/transpose) will default to `perm=[2,1,0]`.

To take the transpose of a batch of sparse matrices, where 0 is the batch
dimension, you would set `perm=[0,2,1]`.

```
>>> x_transpose = tf.sparse.transpose(x, perm=[0, 2, 1])
>>> print('x_transpose =', tf.sparse.to_dense(x_transpose))
x_transpose = tf.Tensor(
[[[0.  0.  0.  0. ]
  [1.1 0.  0.  0. ]
  [0.  0.  0.  0. ]
  [2.2 0.  0.  0. ]
  [0.  0.  0.  0. ]]
[[0.  0.  0.  0. ]
  [0.  0.  0.  4.4]
  [0.  0.  0.  0. ]
  [0.  0.  3.3 0. ]
  [0.  0.  0.  0. ]]], shape=(2, 5, 4), dtype=float32)
```

| Args | |

|  |  |
| --- | --- |
| `sp_input` | The input `SparseTensor`. |
| `perm` | A permutation vector of the dimensions of `sp_input`. |
| `name` | A name prefix for the returned tensors (optional). |

| Returns | |
| A transposed `SparseTensor`. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If `sp_input` is not a `SparseTensor`. |