# tf.io.serialize_sparse

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/io/serialize_sparse](https://tensorflow.google.cn/api_docs/python/tf/io/serialize_sparse)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/sparse_ops.py#L2197-L2221) |

Serialize a `SparseTensor` into a 3-vector (1-D `Tensor`) object.

```
tf.io.serialize_sparse(
    sp_input,
    out_type=tf.dtypes.string,
    name=None
)

tf.dtypes.string
```

| Args | |

|  |  |
| --- | --- |
| `sp_input` | The input `SparseTensor`. |
| `out_type` | The `dtype` to use for serialization. |
| `name` | A name prefix for the returned tensors (optional). |

| Returns | |
| A 3-vector (1-D `Tensor`), with each column representing the serialized `SparseTensor`'s indices, values, and shape (respectively). | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If `sp_input` is not a `SparseTensor`. |