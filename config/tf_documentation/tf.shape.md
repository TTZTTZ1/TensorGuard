# tf.shape

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/shape](https://tensorflow.google.cn/api_docs/python/tf/shape)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L596-L654) |

Returns a tensor containing the shape of the input tensor.

```
tf.shape(
    input, out_type=None, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Effective Tensorflow 2](https://tensorflow.google.cn/guide/effective_tf2) * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) * [Introduction to Tensors](https://tensorflow.google.cn/guide/tensor) * [Customizing what happens in `fit()` with TensorFlow](https://tensorflow.google.cn/guide/keras/custom_train_step_in_tensorflow) * [Customizing what happens in `fit()`](https://tensorflow.google.cn/guide/keras/customizing_what_happens_in_fit) | * [DeepDream](https://tensorflow.google.cn/tutorials/generative/deepdream) * [Neural style transfer](https://tensorflow.google.cn/tutorials/generative/style_transfer) * [Transfer learning with YAMNet for environmental sound classification](https://tensorflow.google.cn/tutorials/audio/transfer_learning_audio) * [pix2pix: Image-to-image translation with a conditional GAN](https://tensorflow.google.cn/tutorials/generative/pix2pix) * [Playing CartPole with the Actor-Critic method](https://tensorflow.google.cn/tutorials/reinforcement_learning/actor_critic) |

See also [`tf.size`](https://tensorflow.google.cn/api_docs/python/tf/size), [`tf.rank`](https://tensorflow.google.cn/api_docs/python/tf/rank).

[`tf.shape`](https://tensorflow.google.cn/api_docs/python/tf/shape) returns a 1-D integer tensor representing the shape of `input`.
For a scalar input, the tensor returned has a shape of (0,) and its value is
the empty vector (i.e. []).

#### For example:

```
>>> tf.shape(1.)
<tf.Tensor: shape=(0,), dtype=int32, numpy=array([], dtype=int32)>
```

```
>>> t = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
>>> tf.shape(t)
<tf.Tensor: shape=(3,), dtype=int32, numpy=array([2, 2, 3], dtype=int32)>
```

**Note:** When using symbolic tensors, such as when using the Keras API,
tf.shape() will return the shape of the symbolic tensor.

```
>>> a = tf.keras.layers.Input((None, 10))
>>> tf.shape(a)
<... shape=(3,) dtype=int32...>
```

In these cases, using [`tf.Tensor.shape`](https://tensorflow.google.cn/api_docs/python/tf/Tensor#shape) will return more informative results.

```
>>> a.shape
TensorShape([None, None, 10])
```

(The first `None` represents the as yet unknown batch size.)

[`tf.shape`](https://tensorflow.google.cn/api_docs/python/tf/shape) and [`Tensor.shape`](https://tensorflow.google.cn/api_docs/python/tf/Tensor#shape) should be identical in eager mode. Within
[`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) or within a [`compat.v1`](https://tensorflow.google.cn/api_docs/python/tf/compat/v1) context, not all dimensions may be
known until execution time. Hence, when defining custom layers and models
for graph mode, prefer the dynamic [`tf.shape(x)`](https://tensorflow.google.cn/api_docs/python/tf/shape) over the static `x.shape`.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` or `SparseTensor`. |
| `out_type` | (Optional) The specified output type of the operation (`int32` or `int64`). Defaults to [`tf.int32`](https://tensorflow.google.cn/api_docs/python/tf#int32). (Note: there is an experimental flag, `tf_shape_default_int64` that changes the default to [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64). This is an unsupported, experimental setting that causes known breakages.) |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `out_type`. | |