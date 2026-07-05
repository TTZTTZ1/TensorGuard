# tf.IndexedSlices

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/indexed_slices.py#L54-L196) |

A sparse representation of a set of tensor slices at given indices.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices)

```
tf.IndexedSlices(
    values, indices, dense_shape=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Client-efficient large-model federated learning via `federated\_select` and sparse aggregation](https://tensorflow.google.cn/federated/tutorials/sparse_federated_learning) |

This class is a simple wrapper for a pair of `Tensor` objects:

* `values`: A `Tensor` of any dtype with shape `[D0, D1, ..., Dn]`.
* `indices`: A 1-D integer `Tensor` with shape `[D0]`.

An `IndexedSlices` is typically used to represent a subset of a larger
tensor `dense` of shape `[LARGE0, D1, .. , DN]` where `LARGE0 >> D0`.
The values in `indices` are the indices in the first dimension of
the slices that have been extracted from the larger tensor.

The dense tensor `dense` represented by an `IndexedSlices` `slices` has

```
dense[slices.indices[i], :, :, :, ...] = slices.values[i, :, :, :, ...]
```

The `IndexedSlices` class is used principally in the definition of
gradients for operations that have sparse gradients
(e.g. [`tf.gather`](https://tensorflow.google.cn/api_docs/python/tf/gather)).

```
>>> v = tf.Variable([[0.,1, 2], [2, 3, 4], [4, 5, 6], [6, 7, 8]])
>>> with tf.GradientTape() as tape:
...   r = tf.gather(v, [1,3])
>>> index_slices = tape.gradient(r,v)
>>> index_slices
<...IndexedSlices object ...>
>>> index_slices.indices.numpy()
array([1, 3], dtype=int32)
>>> index_slices.values.numpy()
array([[1., 1., 1.],
       [1., 1., 1.]], dtype=float32)
```

Contrast this representation with
[`tf.sparse.SparseTensor`](https://tensorflow.google.cn/api_docs/python/tf/sparse/SparseTensor),
which uses multi-dimensional indices and scalar values.

| Attributes | |

|  |  |
| --- | --- |
| `dense_shape` | A 1-D `Tensor` containing the shape of the corresponding dense tensor. |
| `device` | The name of the device on which `values` will be produced, or `None`. |
| `dtype` | The `DType` of elements in this tensor. |
| `graph` | The `Graph` that contains the values, indices, and shape tensors. |
| `indices` | A 1-D `Tensor` containing the indices of the slices. |
| `name` | The name of this `IndexedSlices`. |
| `op` | The `Operation` that produces `values` as an output. |
| `shape` | Gets the [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) representing the shape of the dense tensor. |
| `values` | A `Tensor` containing the values of the slices. |

## Methods

### `consumers`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/indexed_slices.py#L195-L196)

```
consumers()
```

### `__neg__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/indexed_slices.py#L162-L163)

```
__neg__()
```