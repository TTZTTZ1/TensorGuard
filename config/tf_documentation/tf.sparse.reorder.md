# tf.sparse.reorder

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/sparse/reorder](https://tensorflow.google.cn/api_docs/python/tf/sparse/reorder)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/sparse_ops.py#L821-L873) |

Reorders a `SparseTensor` into the canonical, row-major ordering.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.sparse.reorder`](https://tensorflow.google.cn/api_docs/python/tf/sparse/reorder), [`tf.compat.v1.sparse_reorder`](https://tensorflow.google.cn/api_docs/python/tf/sparse/reorder)

```
tf.sparse.reorder(
    sp_input, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Client-efficient large-model federated learning via `federated\_select` and sparse aggregation](https://tensorflow.google.cn/federated/tutorials/sparse_federated_learning) |

Note that by convention, all sparse ops preserve the canonical ordering
along increasing dimension number. The only time ordering can be violated
is during manual manipulation of the indices and values to add entries.

Reordering does not affect the shape of the `SparseTensor`.

For example, if `sp_input` has shape `[4, 5]` and `indices` / `values`:

```
[0, 3]: b
[0, 1]: a
[3, 1]: d
[2, 0]: c
```

then the output will be a `SparseTensor` of shape `[4, 5]` and
`indices` / `values`:

```
[0, 1]: a
[0, 3]: b
[2, 0]: c
[3, 1]: d
```

| Args | |

|  |  |
| --- | --- |
| `sp_input` | The input `SparseTensor`. |
| `name` | A name prefix for the returned tensors (optional) |

| Returns | |
| A `SparseTensor` with the same shape and non-empty values, but in canonical ordering. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If `sp_input` is not a `SparseTensor`. |