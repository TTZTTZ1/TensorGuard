# tf.clip_by_value

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/clip_by_value](https://tensorflow.google.cn/api_docs/python/tf/clip_by_value)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/clip_ops.py#L34-L125) |

Clips tensor values to a specified min and max.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.clip_by_value`](https://tensorflow.google.cn/api_docs/python/tf/clip_by_value)

```
tf.clip_by_value(
    t, clip_value_min, clip_value_max, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Matrix approximation with Core APIs](https://tensorflow.google.cn/guide/core/matrix_core) | * [Intro to Autoencoders](https://tensorflow.google.cn/tutorials/generative/autoencoder) * [DeepDream](https://tensorflow.google.cn/tutorials/generative/deepdream) * [Adversarial example using FGSM](https://tensorflow.google.cn/tutorials/generative/adversarial_fgsm) * [Neural style transfer](https://tensorflow.google.cn/tutorials/generative/style_transfer) * [Data augmentation](https://tensorflow.google.cn/tutorials/images/data_augmentation) |

Given a tensor `t`, this operation returns a tensor of the same type and
shape as `t` with its values clipped to `clip_value_min` and `clip_value_max`.
Any values less than `clip_value_min` are set to `clip_value_min`. Any values
greater than `clip_value_max` are set to `clip_value_max`.

**Note:** `clip_value_min` needs to be smaller or equal to `clip_value_max` for
correct results.

#### For example:

Basic usage passes a scalar as the min and max value.

```
>>> t = tf.constant([[-10., -1., 0.], [0., 2., 10.]])
>>> t2 = tf.clip_by_value(t, clip_value_min=-1, clip_value_max=1)
>>> t2.numpy()
array([[-1., -1.,  0.],
       [ 0.,  1.,  1.]], dtype=float32)
```

The min and max can be the same size as `t`, or broadcastable to that size.

```
>>> t = tf.constant([[-1, 0., 10.], [-1, 0, 10]])
>>> clip_min = [[2],[1]]
>>> t3 = tf.clip_by_value(t, clip_value_min=clip_min, clip_value_max=100)
>>> t3.numpy()
array([[ 2.,  2., 10.],
       [ 1.,  1., 10.]], dtype=float32)
```

Broadcasting fails, intentionally, if you would expand the dimensions of `t`

```
>>> t = tf.constant([[-1, 0., 10.], [-1, 0, 10]])
>>> clip_min = [[[2, 1]]] # Has a third axis
>>> t4 = tf.clip_by_value(t, clip_value_min=clip_min, clip_value_max=100)
Traceback (most recent call last):
... 
InvalidArgumentError: Incompatible shapes: [2,3] vs. [1,1,2]
```

It throws a `TypeError` if you try to clip an `int` to a `float` value
([`tf.cast`](https://tensorflow.google.cn/api_docs/python/tf/cast) the input to `float` first).

```
>>> t = tf.constant([[1, 2], [3, 4]], dtype=tf.int32)
>>> t5 = tf.clip_by_value(t, clip_value_min=-3.1, clip_value_max=3.1)
Traceback (most recent call last):
... 
TypeError: Cannot convert ...
```

| Args | |

|  |  |
| --- | --- |
| `t` | A `Tensor` or `IndexedSlices`. |
| `clip_value_min` | The minimum value to clip to. A scalar `Tensor` or one that is broadcastable to the shape of `t`. |
| `clip_value_max` | The maximum value to clip to. A scalar `Tensor` or one that is broadcastable to the shape of `t`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A clipped `Tensor` or `IndexedSlices`. | |

| Raises | |
| [`tf.errors.InvalidArgumentError`](https://tensorflow.google.cn/api_docs/python/tf/errors/InvalidArgumentError): If the clip tensors would trigger array broadcasting that would make the returned tensor larger than the input. | |
| `TypeError` | If dtype of the input is `int32` and dtype of the `clip_value_min` or `clip_value_max` is `float32` |