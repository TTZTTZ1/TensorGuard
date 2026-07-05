# tf.nn.top_k

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/top_k](https://tensorflow.google.cn/api_docs/python/tf/nn/top_k)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_ops.py#L5815-L5879) |

Finds values and indices of the `k` largest entries for the last dimension.

#### View aliases

**Main aliases**

[`tf.nn.top_k`](https://tensorflow.google.cn/api_docs/python/tf/math/top_k)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.math.top_k`](https://tensorflow.google.cn/api_docs/python/tf/math/top_k), [`tf.compat.v1.nn.top_k`](https://tensorflow.google.cn/api_docs/python/tf/math/top_k)

```
tf.math.top_k(
    input,
    k=1,
    sorted=True,
    index_type=tf.dtypes.int32,
    name=None
)

tf.dtypes.int32
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Integrated gradients](https://tensorflow.google.cn/tutorials/interpretability/integrated_gradients) |

If the input is a vector (rank=1), finds the `k` largest entries in the vector
and outputs their values and indices as vectors. Thus `values[j]` is the
`j`-th largest entry in `input`, and its index is `indices[j]`.

```
>>> result = tf.math.top_k([1, 2, 98, 1, 1, 99, 3, 1, 3, 96, 4, 1],
...                         k=3)
>>> result.values.numpy()
array([99, 98, 96], dtype=int32)
>>> result.indices.numpy()
array([5, 2, 9], dtype=int32)
```

For matrices (resp. higher rank input), computes the top `k` entries in each
row (resp. vector along the last dimension). Thus,

```
>>> input = tf.random.normal(shape=(3,4,5,6))
>>> k = 2
>>> values, indices  = tf.math.top_k(input, k=k)
>>> values.shape.as_list()
[3, 4, 5, 2]
>>> 
>>> values.shape == indices.shape == input.shape[:-1] + [k]
True
```

The indices can be used to `gather` from a tensor who's shape matches `input`.

```
>>> gathered_values = tf.gather(input, indices, batch_dims=-1)
>>> assert tf.reduce_all(gathered_values == values)
```

If two elements are equal, the lower-index element appears first.

```
>>> result = tf.math.top_k([1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
...                        k=3)
>>> result.indices.numpy()
array([0, 1, 3], dtype=int32)
```

By default, indices are returned as type `int32`, however, this can be changed
by specifying the `index_type`.

```
>>> result = tf.math.top_k([1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
...                        k=3, index_type=tf.int16)
>>> result.indices.numpy()
array([0, 1, 3], dtype=int16)
```

| Args | |

|  |  |
| --- | --- |
| `input` | 1-D or higher `Tensor` with last dimension at least `k`. |
| `k` | 0-D `Tensor` of type `int16`, `int32` or `int64`. Number of top element to look for along the last dimension (along each row for matrices). |
| `sorted` | If true the resulting `k` elements will be sorted by the values in descending order. |
| `index_type` | Optional dtype for output indices. |
| `name` | Optional name for the operation. |

| Returns | |
| A tuple with two named fields: | |
| `values` | The `k` largest elements along each last dimensional slice. |
| `indices` | The indices of `values` within the last dimension of `input`. |