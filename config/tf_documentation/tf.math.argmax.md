# tf.math.argmax

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/argmax](https://tensorflow.google.cn/api_docs/python/tf/math/argmax)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L262-L296) |

Returns the index with the largest value across axes of a tensor.

#### View aliases

**Main aliases**

[`tf.argmax`](https://tensorflow.google.cn/api_docs/python/tf/math/argmax)

```
tf.math.argmax(
    input,
    axis=None,
    output_type=tf.dtypes.int64,
    name=None
)

tf.dtypes.int64
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Multilayer perceptrons for digit recognition with Core APIs](https://tensorflow.google.cn/guide/core/mlp_core) * [Migrate metrics and optimizers](https://tensorflow.google.cn/guide/migrate/metrics_optimizers) * [Distributed training with Core APIs and DTensor](https://tensorflow.google.cn/guide/core/distribution) * [Introduction to Tensors](https://tensorflow.google.cn/guide/tensor) * [Introduction to Variables](https://tensorflow.google.cn/guide/variable) | * [Transfer learning with YAMNet for environmental sound classification](https://tensorflow.google.cn/tutorials/audio/transfer_learning_audio) * [Transfer learning with TensorFlow Hub](https://tensorflow.google.cn/tutorials/images/transfer_learning_with_hub) * [Custom training: walkthrough](https://tensorflow.google.cn/tutorials/customization/custom_training_walkthrough) * [Simple audio recognition: Recognizing keywords](https://tensorflow.google.cn/tutorials/audio/simple_audio) * [Distributed training with DTensors](https://tensorflow.google.cn/tutorials/distribute/dtensor_ml_tutorial) |

In case of identity returns the smallest index.

#### For example:

```
>>> A = tf.constant([2, 20, 30, 3, 6])
>>> tf.math.argmax(A)  # A[2] is maximum in tensor A
<tf.Tensor: shape=(), dtype=int64, numpy=2>
>>> B = tf.constant([[2, 20, 30, 3, 6], [3, 11, 16, 1, 8],
...                  [14, 45, 23, 5, 27]])
>>> tf.math.argmax(B, 0)
<tf.Tensor: shape=(5,), dtype=int64, numpy=array([2, 2, 0, 2, 2])>
>>> tf.math.argmax(B, 1)
<tf.Tensor: shape=(3,), dtype=int64, numpy=array([2, 2, 1])>
>>> C = tf.constant([0, 0, 0, 0])
>>> tf.math.argmax(C) # Returns smallest index in case of ties
<tf.Tensor: shape=(), dtype=int64, numpy=0>
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. |
| `axis` | An integer, the axis to reduce across. Default to 0. |
| `output_type` | An optional output dtype ([`tf.int32`](https://tensorflow.google.cn/api_docs/python/tf#int32) or [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64)). Defaults to [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64). |
| `name` | An optional name for the operation. |

| Returns | |
| A `Tensor` of type `output_type`. | |