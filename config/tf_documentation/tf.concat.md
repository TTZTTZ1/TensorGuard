# tf.concat

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/concat](https://tensorflow.google.cn/api_docs/python/tf/concat)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L1316-L1408) |

Concatenates tensors along one dimension.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.concat`](https://tensorflow.google.cn/api_docs/python/tf/concat)

```
tf.concat(
    values, axis, name='concat'
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Better performance with the tf.data API](https://tensorflow.google.cn/guide/data_performance) * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) * [TensorFlow basics](https://tensorflow.google.cn/guide/basics) * [Quickstart for the TensorFlow Core APIs](https://tensorflow.google.cn/guide/core/quickstart_core) * [Customizing what happens in `fit()` with TensorFlow](https://tensorflow.google.cn/guide/keras/custom_train_step_in_tensorflow) | * [Simple audio recognition: Recognizing keywords](https://tensorflow.google.cn/tutorials/audio/simple_audio) * [Learned data compression](https://tensorflow.google.cn/tutorials/generative/data_compression) * [Integrated gradients](https://tensorflow.google.cn/tutorials/interpretability/integrated_gradients) * [Load a pandas DataFrame](https://tensorflow.google.cn/tutorials/load_data/pandas_dataframe) * [Transfer learning for video classification with MoViNet](https://tensorflow.google.cn/tutorials/video/transfer_learning_with_movinet) |

See also [`tf.tile`](https://tensorflow.google.cn/api_docs/python/tf/tile), [`tf.stack`](https://tensorflow.google.cn/api_docs/python/tf/stack), [`tf.repeat`](https://tensorflow.google.cn/api_docs/python/tf/repeat).

Concatenates the list of tensors `values` along dimension `axis`. If
`values[i].shape = [D0, D1, ... Daxis(i), ...Dn]`, the concatenated
result has shape

```
[D0, D1, ... Raxis, ...Dn]
```

where

```
Raxis = sum(Daxis(i))
```

That is, the data from the input tensors is joined along the `axis`
dimension.

The number of dimensions of the input tensors must match, and all dimensions
except `axis` must be equal.

#### For example:

```
>>> t1 = [[1, 2, 3], [4, 5, 6]]
>>> t2 = [[7, 8, 9], [10, 11, 12]]
>>> tf.concat([t1, t2], 0)
<tf.Tensor: shape=(4, 3), dtype=int32, numpy=
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [10, 11, 12]], dtype=int32)>
```

```
>>> tf.concat([t1, t2], 1)
<tf.Tensor: shape=(2, 6), dtype=int32, numpy=
array([[ 1,  2,  3,  7,  8,  9],
       [ 4,  5,  6, 10, 11, 12]], dtype=int32)>
```

As in Python, the `axis` could also be negative numbers. Negative `axis`
are interpreted as counting from the end of the rank, i.e.,
`axis + rank(values)`-th dimension.

#### For example:

```
>>> t1 = [[[1, 2], [2, 3]], [[4, 4], [5, 3]]]
>>> t2 = [[[7, 4], [8, 4]], [[2, 10], [15, 11]]]
>>> tf.concat([t1, t2], -1)
<tf.Tensor: shape=(2, 2, 4), dtype=int32, numpy=
  array([[[ 1,  2,  7,  4],
          [ 2,  3,  8,  4]],
         [[ 4,  4,  2, 10],
          [ 5,  3, 15, 11]]], dtype=int32)>
```

**Note:** If you are concatenating along a new axis consider using stack.
E.g.

```
tf.concat([tf.expand_dims(t, axis) for t in tensors], axis)
```

can be rewritten as

```
tf.stack(tensors, axis=axis)
```

| Args | |

|  |  |
| --- | --- |
| `values` | A list of `Tensor` objects or a single `Tensor`. |
| `axis` | 0-D `int32` `Tensor`. Dimension along which to concatenate. Must be in the range `[-rank(values), rank(values))`. As in Python, indexing for axis is 0-based. Positive axis in the rage of `[0, rank(values))` refers to `axis`-th dimension. And negative axis refers to `axis + rank(values)`-th dimension. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` resulting from concatenation of the input tensors. | |