# tf.sparse.from_dense

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/sparse/from_dense](https://tensorflow.google.cn/api_docs/python/tf/sparse/from_dense)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/sparse_ops.py#L111-L140) |

Converts a dense tensor into a sparse tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.sparse.from_dense`](https://tensorflow.google.cn/api_docs/python/tf/sparse/from_dense)

```
tf.sparse.from_dense(
    tensor, name=None
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Working with sparse tensors](https://tensorflow.google.cn/guide/sparse_tensor) |

Only elements not equal to zero will be present in the result. The resulting
`SparseTensor` has the same dtype and shape as the input.

```
>>> sp = tf.sparse.from_dense([0, 0, 3, 0, 1])
>>> sp.shape.as_list()
[5]
>>> sp.values.numpy()
array([3, 1], dtype=int32)
>>> sp.indices.numpy()
array([[2],
       [4]])
```

| Args | |

|  |  |
| --- | --- |
| `tensor` | A dense `Tensor` to be converted to a `SparseTensor`. |
| `name` | Optional name for the op. |

| Returns | |
| The `SparseTensor`. | |