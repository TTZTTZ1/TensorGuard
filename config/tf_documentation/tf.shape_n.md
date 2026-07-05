# tf.shape_n

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/shape_n](https://tensorflow.google.cn/api_docs/python/tf/shape_n)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L730-L757) |

Returns shape of a list of tensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.shape_n`](https://tensorflow.google.cn/api_docs/python/tf/shape_n)

```
tf.shape_n(
    input,
    out_type=tf.dtypes.int32,
    name=None
)

tf.dtypes.int32
```

Given a list of tensors, [`tf.shape_n`](https://tensorflow.google.cn/api_docs/python/tf/shape_n) is much faster than applying [`tf.shape`](https://tensorflow.google.cn/api_docs/python/tf/shape)
to each tensor individually.

```
>>> a = tf.ones([1, 2])
>>> b = tf.ones([2, 3])
>>> c = tf.ones([3, 4])
>>> tf.shape_n([a, b, c])
[<tf.Tensor: shape=(2,), dtype=int32, numpy=array([1, 2], dtype=int32)>,
<tf.Tensor: shape=(2,), dtype=int32, numpy=array([2, 3], dtype=int32)>,
<tf.Tensor: shape=(2,), dtype=int32, numpy=array([3, 4], dtype=int32)>]
```

| Args | |

|  |  |
| --- | --- |
| `input` | A list of at least 1 `Tensor` object with the same dtype. |
| `out_type` | The specified output type of the operation (`int32` or `int64`). Defaults to [`tf.int32`](https://tensorflow.google.cn/api_docs/python/tf#int32)(optional). |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `Tensor` specifying the shape of each input tensor with type of `out_type`. | |