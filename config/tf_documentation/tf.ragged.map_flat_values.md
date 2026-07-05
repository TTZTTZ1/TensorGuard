# tf.ragged.map_flat_values

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/ragged/map_flat_values](https://tensorflow.google.cn/api_docs/python/tf/ragged/map_flat_values)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/ragged/ragged_functional_ops.py#L25-L136) |

Applies `op` to the `flat_values` of one or more RaggedTensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.ragged.map_flat_values`](https://tensorflow.google.cn/api_docs/python/tf/ragged/map_flat_values)

```
tf.ragged.map_flat_values(
    op, *args, **kwargs
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) |

Replaces any `RaggedTensor` in `args` or `kwargs` with its `flat_values`
tensor (which collapses all ragged dimensions), and then calls `op`. Returns
a `RaggedTensor` that is constructed from the input `RaggedTensor`s'
`nested_row_splits` and the value returned by the `op`.

If the input arguments contain multiple `RaggedTensor`s, then they must have
identical `nested_row_splits`.

This operation is generally used to apply elementwise operations to each value
in a `RaggedTensor`.

**Warning:** [`tf.ragged.map_flat_values`](https://tensorflow.google.cn/api_docs/python/tf/ragged/map_flat_values) does *not* apply `op` to each row of a
ragged tensor. This difference is important for non-elementwise operations,
such as [`tf.reduce_sum`](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_sum). If you wish to apply a non-elementwise operation to
each row of a ragged tensor, use [`tf.map_fn`](https://tensorflow.google.cn/api_docs/python/tf/map_fn) instead. (You may need to
specify an `output_signature` when using [`tf.map_fn`](https://tensorflow.google.cn/api_docs/python/tf/map_fn) with ragged tensors.)

#### Examples:

```
>>> rt = tf.ragged.constant([[1, 2, 3], [], [4, 5], [6]])
>>> tf.ragged.map_flat_values(tf.ones_like, rt)
<tf.RaggedTensor [[1, 1, 1], [], [1, 1], [1]]>
>>> tf.ragged.map_flat_values(tf.multiply, rt, rt)
<tf.RaggedTensor [[1, 4, 9], [], [16, 25], [36]]>
>>> tf.ragged.map_flat_values(tf.add, rt, 5)
<tf.RaggedTensor [[6, 7, 8], [], [9, 10], [11]]>
```

Example with a non-elementwise operation (note that `map_flat_values` and
`map_fn` return different results):

```
>>> rt = tf.ragged.constant([[1.0, 3.0], [], [3.0, 6.0, 3.0]])
>>> def normalized(x):
...   return x / tf.reduce_sum(x)
>>> tf.ragged.map_flat_values(normalized, rt)
<tf.RaggedTensor [[0.0625, 0.1875], [], [0.1875, 0.375, 0.1875]]>
>>> tf.map_fn(normalized, rt)
<tf.RaggedTensor [[0.25, 0.75], [], [0.25, 0.5, 0.25]]>
```

| Args | |

|  |  |
| --- | --- |
| `op` | The operation that should be applied to the RaggedTensor `flat_values`. `op` is typically an element-wise operation (such as math\_ops.add), but any operation that preserves the size of the outermost dimension can be used. I.e., `shape[0]` of the value returned by `op` must match `shape[0]` of the `RaggedTensor`s' `flat_values` tensors. |
| `*args` | Arguments for `op`. |
| `**kwargs` | Keyword arguments for `op`. |

| Returns | |
| A `RaggedTensor` whose `ragged_rank` matches the `ragged_rank` of all input `RaggedTensor`s. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If args contains no `RaggedTensors`, or if the `nested_splits` of the input `RaggedTensor`s are not identical. |