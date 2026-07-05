# tf.squeeze

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/squeeze](https://tensorflow.google.cn/api_docs/python/tf/squeeze)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L4254-L4327) |

Removes dimensions of size 1 from the shape of a tensor.

```
tf.squeeze(
    input, axis=None, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Logistic regression for binary classification with Core APIs](https://tensorflow.google.cn/guide/core/logistic_regression_core) * [Multilayer perceptrons for digit recognition with Core APIs](https://tensorflow.google.cn/guide/core/mlp_core) * [Quickstart for the TensorFlow Core APIs](https://tensorflow.google.cn/guide/core/quickstart_core) * [Unicode strings](https://tensorflow.google.cn/text/guide/unicode) | * [Learned data compression](https://tensorflow.google.cn/tutorials/generative/data_compression) * [Generate music with an RNN](https://tensorflow.google.cn/tutorials/audio/music_generation) * [Simple audio recognition: Recognizing keywords](https://tensorflow.google.cn/tutorials/audio/simple_audio) * [Intro to Autoencoders](https://tensorflow.google.cn/tutorials/generative/autoencoder) * [Transfer learning with YAMNet for environmental sound classification](https://tensorflow.google.cn/tutorials/audio/transfer_learning_audio) |

Given a tensor `input`, this operation returns a tensor of the same type with
all dimensions of size 1 removed. If you don't want to remove all size 1
dimensions, you can remove specific size 1 dimensions by specifying
`axis`.

#### For example:

```
# 't' is a tensor of shape [1, 2, 1, 3, 1, 1]
tf.shape(tf.squeeze(t))  # [2, 3]
```

Or, to remove specific size 1 dimensions:

```
# 't' is a tensor of shape [1, 2, 1, 3, 1, 1]
tf.shape(tf.squeeze(t, [2, 4]))  # [1, 2, 3, 1]
```

Unlike the older op [`tf.compat.v1.squeeze`](https://tensorflow.google.cn/api_docs/python/tf/compat/v1/squeeze), this op does not accept a
deprecated `squeeze_dims` argument.

**Note:** if `input` is a [`tf.RaggedTensor`](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensor), then this operation takes `O(N)`
time, where `N` is the number of elements in the squeezed dimensions.**Note:** If squeeze is performed on dimensions of unknown sizes, then the
returned Tensor will be of unknown shape. A common situation is when the
first (batch) dimension is of size `None`, [`tf.squeeze`](https://tensorflow.google.cn/api_docs/python/tf/squeeze) returns
`<unknown>` shape which may be a surprise. Specify the `axis=` argument
to get the expected result, as illustrated in the following example:

```
@tf.function
def func(x):
  print('x.shape:', x.shape)
  known_axes = [i for i, size in enumerate(x.shape) if size == 1]
  y = tf.squeeze(x, axis=known_axes)
  print('shape of tf.squeeze(x, axis=known_axes):', y.shape)
  y = tf.squeeze(x)
  print('shape of tf.squeeze(x):', y.shape)
  return 0

_ = func.get_concrete_function(tf.TensorSpec([None, 1, 2], dtype=tf.int32))
# Output is.
# x.shape: (None, 1, 2)
# shape of tf.squeeze(x, axis=known_axes): (None, 2)
# shape of tf.squeeze(x): <unknown>
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. The `input` to squeeze. |
| `axis` | An optional list of `ints`. Defaults to `[]`. If specified, only squeezes the dimensions listed. The dimension index starts at 0. It is an error to squeeze a dimension that is not 1. Must be in the range `[-rank(input), rank(input))`. Must be specified if `input` is a `RaggedTensor`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. Contains the same data as `input`, but has one or more dimensions of size 1 removed. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | The input cannot be converted to a tensor, or the specified axis cannot be squeezed. |