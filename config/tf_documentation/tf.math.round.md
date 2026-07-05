# tf.math.round

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/round](https://tensorflow.google.cn/api_docs/python/tf/math/round)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L908-L934) |

Rounds the values of a tensor to the nearest integer, element-wise.

#### View aliases

**Main aliases**

[`tf.round`](https://tensorflow.google.cn/api_docs/python/tf/math/round)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.round`](https://tensorflow.google.cn/api_docs/python/tf/math/round)

```
tf.math.round(
    x, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Learned data compression](https://tensorflow.google.cn/tutorials/generative/data_compression) * [Substantial Undocumented Infection Facilitates the Rapid Dissemination of Novel Coronavirus (SARS-CoV2)](https://tensorflow.google.cn/probability/examples/Undocumented_Infection_and_the_Dissemination_of_SARS-CoV2) * [Research tools](https://tensorflow.google.cn/quantum/tutorials/research_tools) * [Super resolution with TensorFlow Lite](https://tensorflow.google.cn/lite/examples/super_resolution/overview) * [Graph-based Neural Structured Learning in TFX](https://tensorflow.google.cn/tfx/tutorials/tfx/neural_structured_learning) |

Rounds half to even. Also known as bankers rounding. If you want to round
according to the current system rounding mode use tf::cint.
For example:

```
x = tf.constant([0.9, 2.5, 2.3, 1.5, -4.5])
tf.round(x)  # [ 1.0, 2.0, 2.0, 2.0, -4.0 ]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor` of type `float16`, `float32`, `float64`, `int32`, or `int64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of same shape and type as `x`. | |