# tf.math.reduce_all

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/reduce_all](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_all)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L3083-L3128) |

Computes [`tf.math.logical_and`](https://tensorflow.google.cn/api_docs/python/tf/math/logical_and) of elements across dimensions of a tensor.

#### View aliases

**Main aliases**

[`tf.reduce_all`](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_all)

```
tf.math.reduce_all(
    input_tensor, axis=None, keepdims=False, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Extension types](https://tensorflow.google.cn/guide/extension_type) | * [Neural machine translation with attention](https://tensorflow.google.cn/text/tutorials/nmt_with_attention) |

This is the reduction operation for the elementwise [`tf.math.logical_and`](https://tensorflow.google.cn/api_docs/python/tf/math/logical_and) op.

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
>>> tf.math.reduce_all(x)
<tf.Tensor: shape=(), dtype=bool, numpy=False>
>>> tf.math.reduce_all(x, 0)
<tf.Tensor: shape=(2,), dtype=bool, numpy=array([False, False])>
>>> tf.math.reduce_all(x, 1)
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

Equivalent to np.all