# tf.math.exp

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/exp](https://tensorflow.google.cn/api_docs/python/tf/math/exp)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L5459-L5506) |

Computes exponential of x element-wise. \(y = e^x\).

#### View aliases

**Main aliases**

[`tf.exp`](https://tensorflow.google.cn/api_docs/python/tf/math/exp)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.exp`](https://tensorflow.google.cn/api_docs/python/tf/math/exp)

```
tf.math.exp(
    x, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Understanding masking & padding](https://tensorflow.google.cn/guide/keras/understanding_masking_and_padding) | * [Scalable model compression](https://tensorflow.google.cn/tutorials/optimization/compression) * [Convolutional Variational Autoencoder](https://tensorflow.google.cn/tutorials/generative/cvae) * [Learned data compression](https://tensorflow.google.cn/tutorials/generative/data_compression) * [Multiple changepoint detection and Bayesian model selection](https://tensorflow.google.cn/probability/examples/Multiple_changepoint_detection_and_Bayesian_model_selection) * [Modeling COVID-19 spread in Europe and the effect of interventions](https://tensorflow.google.cn/probability/examples/Estimating_COVID_19_in_11_European_countries) |

This function computes the exponential of the input tensor element-wise.
i.e. [`math.exp(x)`](https://tensorflow.google.cn/api_docs/python/tf/math/exp) or \(e^x\), where `x` is the input tensor.
\(e\) denotes Euler's number and is approximately equal to 2.718281.
Output is positive for any real input.

```
>>> x = tf.constant(2.0)
>>> tf.math.exp(x)
<tf.Tensor: shape=(), dtype=float32, numpy=7.389056>
```

```
>>> x = tf.constant([2.0, 8.0])
>>> tf.math.exp(x)
<tf.Tensor: shape=(2,), dtype=float32,
numpy=array([   7.389056, 2980.958   ], dtype=float32)>
```

For complex numbers, the exponential value is calculated as

\[
e^{x+iy} = {e^x} {e^{iy} } = {e^x} ({\cos (y) + i \sin (y)})
\]

For `1+1j` the value would be computed as:

\[
e^1 (\cos (1) + i \sin (1)) = 2.7182817 \times (0.5403023+0.84147096j)
\]

```
>>> x = tf.constant(1 + 1j)
>>> tf.math.exp(x)
<tf.Tensor: shape=(), dtype=complex128,
numpy=(1.4686939399158851+2.2873552871788423j)>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor). Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor). Has the same type as `x`. | |

## numpy compatibility

Equivalent to np.exp