# tf.sparse.mask

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/sparse/mask](https://tensorflow.google.cn/api_docs/python/tf/sparse/mask)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L1565-L1606) |

Masks elements of `IndexedSlices`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.sparse.mask`](https://tensorflow.google.cn/api_docs/python/tf/sparse/mask), [`tf.compat.v1.sparse_mask`](https://tensorflow.google.cn/api_docs/python/tf/sparse/mask)

```
tf.sparse.mask(
    a, mask_indices, name=None
)
```

Given an `IndexedSlices` instance `a`, returns another `IndexedSlices` that
contains a subset of the slices of `a`. Only the slices at indices not
specified in `mask_indices` are returned.

This is useful when you need to extract a subset of slices in an
`IndexedSlices` object.

#### For example:

```
# `a` contains slices at indices [12, 26, 37, 45] from a large tensor
# with shape [1000, 10]
a.indices  # [12, 26, 37, 45]
tf.shape(a.values)  # [4, 10]

# `b` will be the subset of `a` slices at its second and third indices, so
# we want to mask its first and last indices (which are at absolute
# indices 12, 45)
b = tf.sparse.mask(a, [12, 45])

b.indices  # [26, 37]
tf.shape(b.values)  # [2, 10]
```

| Args | |

|  |  |
| --- | --- |
| `a` | An `IndexedSlices` instance. |
| `mask_indices` | Indices of elements to mask. |
| `name` | A name for the operation (optional). |

| Returns | |
| The masked `IndexedSlices` instance. | |