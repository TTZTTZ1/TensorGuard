# tf.math.maximum

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/maximum](https://tensorflow.google.cn/api_docs/python/tf/math/maximum)

---

Returns the max of x and y (i.e. x > y ? x : y) element-wise.

#### View aliases

**Main aliases**

[`tf.maximum`](https://tensorflow.google.cn/api_docs/python/tf/math/maximum)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.maximum`](https://tensorflow.google.cn/api_docs/python/tf/math/maximum)

```
tf.math.maximum(
    x: Annotated[Any, tf.raw_ops.Any],
    y: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
tf.raw_ops.Any
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Extension types](https://tensorflow.google.cn/guide/extension_type) * [Introduction to graphs and tf.function](https://tensorflow.google.cn/guide/intro_to_graphs) | * [Generate music with an RNN](https://tensorflow.google.cn/tutorials/audio/music_generation) * [Instance Segmentation with Model Garden](https://tensorflow.google.cn/tfmodels/vision/instance_segmentation) * [Graph regularization for sentiment classification using synthesized graphs](https://tensorflow.google.cn/neural_structured_learning/tutorials/graph_keras_lstm_imdb) * [Substantial Undocumented Infection Facilitates the Rapid Dissemination of Novel Coronavirus (SARS-CoV2)](https://tensorflow.google.cn/probability/examples/Undocumented_Infection_and_the_Dissemination_of_SARS-CoV2) * [Human Pose Classification with MoveNet and TensorFlow Lite](https://tensorflow.google.cn/lite/tutorials/pose_classification) |

#### Example:

```
>>> x = tf.constant([0., 0., 0., 0.])
>>> y = tf.constant([-2., 0., 2., 5.])
>>> tf.math.maximum(x, y)
<tf.Tensor: shape=(4,), dtype=float32, numpy=array([0., 0., 2., 5.], dtype=float32)>
```

Note that `maximum` supports [broadcast semantics](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) for `x` and `y`.

```
>>> x = tf.constant([-5., 0., 0., 0.])
>>> y = tf.constant([-3.])
>>> tf.math.maximum(x, y)
<tf.Tensor: shape=(4,), dtype=float32, numpy=array([-3., 0., 0., 0.], dtype=float32)>
```

The reduction version of this elementwise operation is [`tf.math.reduce_max`](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_max)

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `uint32`, `int64`, `uint64`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |