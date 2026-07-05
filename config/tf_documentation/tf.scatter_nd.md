# tf.scatter_nd

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/scatter_nd](https://tensorflow.google.cn/api_docs/python/tf/scatter_nd)

---

Scatters `updates` into a tensor of shape `shape` according to `indices`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.manip.scatter_nd`](https://tensorflow.google.cn/api_docs/python/tf/scatter_nd), [`tf.compat.v1.scatter_nd`](https://tensorflow.google.cn/api_docs/python/tf/scatter_nd)

```
tf.scatter_nd(
    indices: Annotated[Any, TV_ScatterNd_Tindices],
    updates: Annotated[Any, TV_ScatterNd_T],
    shape: Annotated[Any, TV_ScatterNd_Tindices],
    name=None
) -> Annotated[Any, TV_ScatterNd_T]
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Introduction to tensor slicing](https://tensorflow.google.cn/guide/tensor_slicing) |

Scatter sparse `updates` according to individual values at the specified
`indices`. This op returns an output tensor with the `shape` you specify. This
op is the inverse of the [`tf.gather_nd`](https://tensorflow.google.cn/api_docs/python/tf/gather_nd) operator which extracts values or slices
from a given tensor.

This operation is similar to [`tf.tensor_scatter_nd_add`](https://tensorflow.google.cn/api_docs/python/tf/tensor_scatter_nd_add), except that the tensor
is zero-initialized. Calling [`tf.scatter_nd(indices, updates, shape)`](https://tensorflow.google.cn/api_docs/python/tf/scatter_nd)
is identical to calling
`tf.tensor_scatter_nd_add(tf.zeros(shape, updates.dtype), indices, updates)`

If `indices` contains duplicates, the associated `updates` are accumulated
(summed) into the output tensor.

**Warning:** For floating-point data types, the output may be nondeterministic.
This is because the order in which the updates are applied is nondeterministic
and when floating-point numbers are added in different orders the resulting
numerical approximation error can be slightly different. However, the output
will be deterministic if op determinism is enabled via
[`tf.config.experimental.enable_op_determinism`](https://tensorflow.google.cn/api_docs/python/tf/config/experimental/enable_op_determinism).

`indices` is an integer tensor containing indices into the output tensor. The
last dimension of `indices` can be at most the rank of `shape`:

```
indices.shape[-1] <= shape.rank
```

The last dimension of `indices` corresponds to indices of elements
(if `indices.shape[-1] = shape.rank`) or slices
(if `indices.shape[-1] < shape.rank`) along dimension `indices.shape[-1]` of
`shape`.

`updates` is a tensor with shape:

```
indices.shape[:-1] + shape[indices.shape[-1]:]
```

The simplest form of the scatter op is to insert individual elements in
a tensor by index. Consider an example where you want to insert 4 scattered
elements in a rank-1 tensor with 8 elements.

![](https://tensorflow.google.cn/images/ScatterNd1.png)

In Python, this scatter operation would look like this:

```
    indices = tf.constant([[4], [3], [1], [7]])
    updates = tf.constant([9, 10, 11, 12])
    shape = tf.constant([8])
    scatter = tf.scatter_nd(indices, updates, shape)
    print(scatter)
```

The resulting tensor would look like this:

```
[0, 11, 0, 10, 9, 0, 0, 12]
```

You can also insert entire slices of a higher rank tensor all at once. For
example, you can insert two slices in the first dimension of a rank-3 tensor
with two matrices of new values.

![](https://tensorflow.google.cn/images/ScatterNd2.png)

In Python, this scatter operation would look like this:

```
    indices = tf.constant([[1], [3]])
    updates = tf.constant([[[5, 5, 5, 5], [6, 6, 6, 6],
                            [7, 7, 7, 7], [8, 8, 8, 8]],
                           [[5, 5, 5, 5], [6, 6, 6, 6],
                            [7, 7, 7, 7], [8, 8, 8, 8]]])
    shape = tf.constant([4, 4, 4])
    scatter = tf.scatter_nd(indices, updates, shape)
    print(scatter)
```

The resulting tensor would look like this:

```
[[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
 [[5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8]],
 [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
 [[5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8]]]
```

Note that on CPU, if an out of bound index is found, an error is returned.
On GPU, if an out of bound index is found, the index is ignored.

| Args | |

|  |  |
| --- | --- |
| `indices` | A `Tensor`. Must be one of the following types: `int16`, `int32`, `int64`. Tensor of indices. |
| `updates` | A `Tensor`. Values to scatter into the output tensor. |
| `shape` | A `Tensor`. Must have the same type as `indices`. 1-D. The shape of the output tensor. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `updates`. | |