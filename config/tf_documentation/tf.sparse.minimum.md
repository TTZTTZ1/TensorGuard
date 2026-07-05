# tf.sparse.minimum

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/sparse/minimum](https://tensorflow.google.cn/api_docs/python/tf/sparse/minimum)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/sparse_ops.py#L2780-L2821) |

Returns the element-wise min of two SparseTensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.sparse.minimum`](https://tensorflow.google.cn/api_docs/python/tf/sparse/minimum), [`tf.compat.v1.sparse_minimum`](https://tensorflow.google.cn/api_docs/python/tf/sparse/minimum)

```
tf.sparse.minimum(
    sp_a, sp_b, name=None
)
```

Assumes the two SparseTensors have the same shape, i.e., no broadcasting.

| Example | |
|  | |

```
>>> sp_zero = tf.sparse.SparseTensor([[0]], [0], [7])
>>> sp_one = tf.sparse.SparseTensor([[1]], [1], [7])
>>> res = tf.sparse.minimum(sp_zero, sp_one)
>>> res.indices
<tf.Tensor: shape=(2, 1), dtype=int64, numpy=
array([[0],
       [1]])>
>>> res.values
<tf.Tensor: shape=(2,), dtype=int32, numpy=array([0, 0], dtype=int32)>
>>> res.dense_shape
<tf.Tensor: shape=(1,), dtype=int64, numpy=array([7])>
```

| Args | |

|  |  |
| --- | --- |
| `sp_a` | a `SparseTensor` operand whose dtype is real, and indices lexicographically ordered. |
| `sp_b` | the other `SparseTensor` operand with the same requirements (and the same shape). |
| `name` | optional name of the operation. |

| Returns | |

|  |  |
| --- | --- |
| `output` | the output SparseTensor. |