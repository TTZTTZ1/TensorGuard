# tf.nn.crelu

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/crelu](https://tensorflow.google.cn/api_docs/python/tf/nn/crelu)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_ops.py#L3623-L3626) |

Computes Concatenated ReLU.

```
tf.nn.crelu(
    features, axis=-1, name=None
)
```

Concatenates a ReLU which selects only the positive part of the activation
with a ReLU which selects only the *negative* part of the activation.
Note that as a result this non-linearity doubles the depth of the activations.
Source: [Understanding and Improving Convolutional Neural Networks via
Concatenated Rectified Linear Units. W. Shang, et
al.](https://arxiv.org/abs/1603.05201)

| Args | |

|  |  |
| --- | --- |
| `features` | A `Tensor` with type `float`, `double`, `int32`, `int64`, `uint8`, `int16`, or `int8`. |
| `name` | A name for the operation (optional). |
| `axis` | The axis that the output values are concatenated along. Default is -1. |

| Returns | |
| A `Tensor` with the same type as `features`. | |

| References | |
| Understanding and Improving Convolutional Neural Networks via Concatenated Rectified Linear Units: [Shang et al., 2016](http://proceedings.mlr.press/v48/shang16) ([pdf](http://proceedings.mlr.press/v48/shang16.pdf)) | |