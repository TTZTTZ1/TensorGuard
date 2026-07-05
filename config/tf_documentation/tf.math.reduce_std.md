# tf.math.reduce_std

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/reduce_std](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_std)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L2613-L2661) |

Computes the standard deviation of elements across dimensions of a tensor.

```
tf.math.reduce_std(
    input_tensor, axis=None, keepdims=False, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Logistic regression for binary classification with Core APIs](https://tensorflow.google.cn/guide/core/logistic_regression_core) * [Quickstart for the TensorFlow Core APIs](https://tensorflow.google.cn/guide/core/quickstart_core) | * [DeepDream](https://tensorflow.google.cn/tutorials/generative/deepdream) * [Playing CartPole with the Actor-Critic method](https://tensorflow.google.cn/tutorials/reinforcement_learning/actor_critic) * [Modeling COVID-19 spread in Europe and the effect of interventions](https://tensorflow.google.cn/probability/examples/Estimating_COVID_19_in_11_European_countries) * [Barren plateaus](https://tensorflow.google.cn/quantum/tutorials/barren_plateaus) * [Quantum data](https://tensorflow.google.cn/quantum/tutorials/quantum_data) |

Reduces `input_tensor` along the dimensions given in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
of the entries in `axis`, which must be unique. If `keepdims` is true, the
reduced dimensions are retained with length 1.

If `axis` is None, all dimensions are reduced, and a
tensor with a single element is returned.

#### For example:

```
>>> x = tf.constant([[1., 2.], [3., 4.]])
>>> tf.math.reduce_std(x)
<tf.Tensor: shape=(), dtype=float32, numpy=1.118034>
>>> tf.math.reduce_std(x, 0)
<tf.Tensor: shape=(2,), dtype=float32, numpy=array([1., 1.], dtype=float32)>
>>> tf.math.reduce_std(x, 1)
<tf.Tensor: shape=(2,), dtype=float32, numpy=array([0.5, 0.5], dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `input_tensor` | The tensor to reduce. Should have real or complex type. |
| `axis` | The dimensions to reduce. If `None` (the default), reduces all dimensions. Must be in the range `[-rank(input_tensor), rank(input_tensor))`. |
| `keepdims` | If true, retains reduced dimensions with length 1. |
| `name` | A name scope for the associated operations (optional). |

| Returns | |
| The reduced tensor, of the same dtype as the input\_tensor. Note, for `complex64` or `complex128` input, the returned `Tensor` will be of type `float32` or `float64`, respectively. | |

## numpy compatibility

Equivalent to np.std

Please note `np.std` has a `dtype` parameter that could be used to specify the
output type. By default this is `dtype=float64`. On the other hand,
[`tf.math.reduce_std`](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_std) has aggressive type inference from `input_tensor`.