# tf.math.reduce_any

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/reduce_any](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_any)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L3189-L3234) |

Computes [`tf.math.logical_or`](https://tensorflow.google.cn/api_docs/python/tf/math/logical_or) of elements across dimensions of a tensor.

#### View aliases

**Main aliases**

[`tf.reduce_any`](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_any)

```
tf.math.reduce_any(
    input_tensor, axis=None, keepdims=False, name=None
)
```

This is the reduction operation for the elementwise [`tf.math.logical_or`](https://tensorflow.google.cn/api_docs/python/tf/math/logical_or) op.

Reduces `input_tensor` along the dimensions given in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
of the entries in `axis`, which must be unique. If `keepdims` is true, the
reduced dimensions are retained with length 1.

If `axis` is None, all dimensions are reduced, and a
tensor with a single element is returned.

| For example | |
|  | |

```
>>> x = tf.constant([[True,  True], [False, False]])
>>> tf.reduce_any(x)
<tf.Tensor: shape=(), dtype=bool, numpy=True>
>>> tf.reduce_any(x, 0)
<tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True,  True])>
>>> tf.reduce_any(x, 1)
<tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True, False])>
```

| Args | |

|  |  |
| --- | --- |
| `input_tensor` | The boolean tensor to reduce. |
| `axis` | The dimensions to reduce. If `None` (the default), reduces all dimensions. Must be in the range `[-rank(input_tensor), rank(input_tensor))`. |
| `keepdims` | If true, retains reduced dimensions with length 1. |
| `name` | A name for the operation (optional). |

| Returns | |
| The reduced tensor. | |

## numpy compatibility

Equivalent to np.any