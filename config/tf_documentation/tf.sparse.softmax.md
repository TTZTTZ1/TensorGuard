# tf.sparse.softmax

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/sparse/softmax](https://tensorflow.google.cn/api_docs/python/tf/sparse/softmax)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/sparse_ops.py#L2671-L2731) |

Applies softmax to a batched N-D `SparseTensor`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.sparse.softmax`](https://tensorflow.google.cn/api_docs/python/tf/sparse/softmax), [`tf.compat.v1.sparse_softmax`](https://tensorflow.google.cn/api_docs/python/tf/sparse/softmax)

```
tf.sparse.softmax(
    sp_input, name=None
)
```

The inputs represent an N-D SparseTensor with logical shape `[..., B, C]`
(where `N >= 2`), and with indices sorted in the canonical lexicographic
order.

This op is equivalent to applying the normal [`tf.nn.softmax()`](https://tensorflow.google.cn/api_docs/python/tf/nn/softmax) to each
innermost logical submatrix with shape `[B, C]`, but with the catch that *the
implicitly zero elements do not participate*. Specifically, the algorithm is
equivalent to:

(1) Applies [`tf.nn.softmax()`](https://tensorflow.google.cn/api_docs/python/tf/nn/softmax) to a densified view of each innermost
submatrix with shape `[B, C]`, along the size-C dimension;
(2) Masks out the original implicitly-zero locations;
(3) Renormalizes the remaining elements.

Hence, the `SparseTensor` result has exactly the same non-zero indices and
shape.

Example using a 3-D SparseTensor:

```
>>> st = tf.sparse.from_dense(
...   [[[0., np.e],
...     [1., 0.]],
... 
...    [[np.e, 0.],
...     [np.e, np.e]]])
>>> res = tf.sparse.softmax(st)
>>> res.indices
  <tf.Tensor: shape=(5, 3), dtype=int64, numpy=
  array([[0, 0, 1],
         [0, 1, 0],
         [1, 0, 0],
         [1, 1, 0],
         [1, 1, 1]])>
>>> res.values
  <tf.Tensor: ... numpy=array([1. , 1. , 1. , 0.5, 0.5], dtype=float32)>
>>> res.dense_shape
  <tf.Tensor: shape=(3,), dtype=int64, numpy=array([2, 2, 2])>
>>> tf.sparse.to_dense(res)
  <tf.Tensor: shape=(2, 2, 2), dtype=float32, numpy=
  array([[[0. , 1. ],
          [1. , 0. ]],
         [[1. , 0. ],
          [0.5, 0.5]]], dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `sp_input` | N-D `SparseTensor`, where `N >= 2`. |
| `name` | optional name of the operation. |

| Returns | |

|  |  |
| --- | --- |
| `output` | N-D `SparseTensor` representing the results. |