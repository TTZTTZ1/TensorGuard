# tf.random.stateless_normal

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/random/stateless_normal](https://tensorflow.google.cn/api_docs/python/tf/random/stateless_normal)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/stateless_random_ops.py#L644-L692) |

Outputs deterministic pseudorandom values from a normal distribution.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.random.stateless_normal`](https://tensorflow.google.cn/api_docs/python/tf/random/stateless_normal)

```
tf.random.stateless_normal(
    shape,
    seed,
    mean=0.0,
    stddev=1.0,
    dtype=tf.dtypes.float32,
    name=None,
    alg='auto_select'
)

tf.dtypes.float32
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Random number generation](https://tensorflow.google.cn/guide/random_numbers) | * [Random noise generation in TFF](https://tensorflow.google.cn/federated/tutorials/random_noise_generation) * [Multiple changepoint detection and Bayesian model selection](https://tensorflow.google.cn/probability/examples/Multiple_changepoint_detection_and_Bayesian_model_selection) * [TFP Release Notes notebook (0.11.0)](https://tensorflow.google.cn/probability/examples/TFP_Release_Notebook_0_11_0) * [Substantial Undocumented Infection Facilitates the Rapid Dissemination of Novel Coronavirus (SARS-CoV2)](https://tensorflow.google.cn/probability/examples/Undocumented_Infection_and_the_Dissemination_of_SARS-CoV2) |

This is a stateless version of [`tf.random.normal`](https://tensorflow.google.cn/api_docs/python/tf/random/normal): if run twice with the
same seeds and shapes, it will produce the same pseudorandom numbers. The
output is consistent across multiple runs on the same hardware (and between
CPU and GPU), but may change between versions of TensorFlow or on non-CPU/GPU
hardware.

| Args | |

|  |  |
| --- | --- |
| `shape` | A 1-D integer Tensor or Python array. The shape of the output tensor. |
| `seed` | A shape [2] Tensor, the seed to the random number generator. Must have dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.) |
| `mean` | A 0-D Tensor or Python value of type `dtype`. The mean of the normal distribution. |
| `stddev` | A 0-D Tensor or Python value of type `dtype`. The standard deviation of the normal distribution. |
| `dtype` | The float type of the output: `float16`, `bfloat16`, `float32`, `float64`. Defaults to `float32`. |
| `name` | A name for the operation (optional). |
| `alg` | The RNG algorithm used to generate the random numbers. See [`tf.random.stateless_uniform`](https://tensorflow.google.cn/api_docs/python/tf/random/stateless_uniform) for a detailed explanation. |

| Returns | |
| A tensor of the specified shape filled with random normal values. | |