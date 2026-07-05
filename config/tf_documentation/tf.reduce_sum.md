# tf.reduce_sum

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/reduce_sum](https://tensorflow.google.cn/api_docs/python/tf/reduce_sum)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L2146-L2210) |

Computes the sum of elements across dimensions of a tensor.

#### View aliases

**Main aliases**

[`tf.reduce_sum`](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_sum)

```
tf.math.reduce_sum(
    input_tensor, axis=None, keepdims=False, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Advanced automatic differentiation](https://tensorflow.google.cn/guide/advanced_autodiff) * [Better performance with tf.function](https://tensorflow.google.cn/guide/function) * [TensorFlow basics](https://tensorflow.google.cn/guide/basics) * [Matrix approximation with Core APIs](https://tensorflow.google.cn/guide/core/matrix_core) * [Extension types](https://tensorflow.google.cn/guide/extension_type) | * [Using DTensors with Keras](https://tensorflow.google.cn/tutorials/distribute/dtensor_keras_tutorial) * [Distributed training with DTensors](https://tensorflow.google.cn/tutorials/distribute/dtensor_ml_tutorial) * [Convolutional Variational Autoencoder](https://tensorflow.google.cn/tutorials/generative/cvae) * [Neural style transfer](https://tensorflow.google.cn/tutorials/generative/style_transfer) * [Playing CartPole with the Actor-Critic method](https://tensorflow.google.cn/tutorials/reinforcement_learning/actor_critic) |

This is the reduction operation for the elementwise [`tf.math.add`](https://tensorflow.google.cn/api_docs/python/tf/math/add) op.

Reduces `input_tensor` along the dimensions given in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
of the entries in `axis`, which must be unique. If `keepdims` is true, the
reduced dimensions are retained with length 1.

If `axis` is None, all dimensions are reduced, and a
tensor with a single element is returned.

| For example | |
|  | |

```
>>> # x has a shape of (2, 3) (two rows and three columns):
>>> x = tf.constant([[1, 1, 1], [1, 1, 1]])
>>> x.numpy()
array([[1, 1, 1],
       [1, 1, 1]], dtype=int32)
>>> # sum all the elements
>>> # 1 + 1 + 1 + 1 + 1+ 1 = 6
>>> tf.reduce_sum(x).numpy()
6
>>> # reduce along the first dimension
>>> # the result is [1, 1, 1] + [1, 1, 1] = [2, 2, 2]
>>> tf.reduce_sum(x, 0).numpy()
array([2, 2, 2], dtype=int32)
>>> # reduce along the second dimension
>>> # the result is [1, 1] + [1, 1] + [1, 1] = [3, 3]
>>> tf.reduce_sum(x, 1).numpy()
array([3, 3], dtype=int32)
>>> # keep the original dimensions
>>> tf.reduce_sum(x, 1, keepdims=True).numpy()
array([[3],
       [3]], dtype=int32)
>>> # reduce along both dimensions
>>> # the result is 1 + 1 + 1 + 1 + 1 + 1 = 6
>>> # or, equivalently, reduce along rows, then reduce the resultant array
>>> # [1, 1, 1] + [1, 1, 1] = [2, 2, 2]
>>> # 2 + 2 + 2 = 6
>>> tf.reduce_sum(x, [0, 1]).numpy()
6
```

| Args | |

|  |  |
| --- | --- |
| `input_tensor` | The tensor to reduce. Should have numeric type. |
| `axis` | The dimensions to reduce. If `None` (the default), reduces all dimensions. Must be in the range `[-rank(input_tensor), rank(input_tensor)]`. |
| `keepdims` | If true, retains reduced dimensions with length 1. |
| `name` | A name for the operation (optional). |

| Returns | |
| The reduced tensor, of the same dtype as the input\_tensor. | |

## numpy compatibility

Equivalent to np.sum apart the fact that numpy upcast uint8 and int32 to
int64 while tensorflow returns the same dtype as the input.