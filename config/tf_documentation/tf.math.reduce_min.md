# tf.math.reduce_min

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/reduce_min](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_min)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L2836-L2897) |

Computes the [`tf.math.minimum`](https://tensorflow.google.cn/api_docs/python/tf/math/minimum) of elements across dimensions of a tensor.

#### View aliases

**Main aliases**

[`tf.reduce_min`](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_min)

```
tf.math.reduce_min(
    input_tensor, axis=None, keepdims=False, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) | * [Integrated gradients](https://tensorflow.google.cn/tutorials/interpretability/integrated_gradients) * [Intro to Autoencoders](https://tensorflow.google.cn/tutorials/generative/autoencoder) * [MoViNet for streaming action recognition](https://tensorflow.google.cn/hub/tutorials/movinet) * [TensorFlow Ranking Keras pipeline for distributed training](https://tensorflow.google.cn/ranking/tutorials/ranking_dnn_distributed) |

This is the reduction operation for the elementwise [`tf.math.minimum`](https://tensorflow.google.cn/api_docs/python/tf/math/minimum) op.

Reduces `input_tensor` along the dimensions given in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
of the entries in `axis`, which must be unique. If `keepdims` is true, the
reduced dimensions are retained with length 1.

If `axis` is None, all dimensions are reduced, and a
tensor with a single element is returned.

#### For example:

```
>>> a = tf.constant([
...   [[1, 2], [3, 4]],
...   [[1, 2], [3, 4]]
... ])
>>> tf.reduce_min(a)
<tf.Tensor: shape=(), dtype=int32, numpy=1>
```

Choosing a specific axis returns minimum element in the given axis:

```
>>> b = tf.constant([[1, 2, 3], [4, 5, 6]])
>>> tf.reduce_min(b, axis=0)
<tf.Tensor: shape=(3,), dtype=int32, numpy=array([1, 2, 3], dtype=int32)>
>>> tf.reduce_min(b, axis=1)
<tf.Tensor: shape=(2,), dtype=int32, numpy=array([1, 4], dtype=int32)>
```

Setting `keepdims` to `True` retains the dimension of `input_tensor`:

```
>>> tf.reduce_min(a, keepdims=True)
<tf.Tensor: shape=(1, 1, 1), dtype=int32, numpy=array([[[1]]], dtype=int32)>
>>> tf.math.reduce_min(a, axis=0, keepdims=True)
<tf.Tensor: shape=(1, 2, 2), dtype=int32, numpy=
array([[[1, 2],
        [3, 4]]], dtype=int32)>
```

| Args | |

|  |  |
| --- | --- |
| `input_tensor` | The tensor to reduce. Should have real numeric type. |
| `axis` | The dimensions to reduce. If `None` (the default), reduces all dimensions. Must be in the range `[-rank(input_tensor), rank(input_tensor))`. |
| `keepdims` | If true, retains reduced dimensions with length 1. |
| `name` | A name for the operation (optional). |

| Returns | |
| The reduced tensor. | |

## numpy compatibility

Equivalent to np.min