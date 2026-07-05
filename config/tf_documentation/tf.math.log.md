# tf.math.log

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/log](https://tensorflow.google.cn/api_docs/python/tf/math/log)

---

Computes natural logarithm of x element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.log`](https://tensorflow.google.cn/api_docs/python/tf/math/log)

```
tf.math.log(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Optimizers with Core APIs](https://tensorflow.google.cn/guide/core/optimizers_core) | * [Convolutional Variational Autoencoder](https://tensorflow.google.cn/tutorials/generative/cvae) * [Playing CartPole with the Actor-Critic method](https://tensorflow.google.cn/tutorials/reinforcement_learning/actor_critic) * [Learnable Distributions Zoo](https://tensorflow.google.cn/probability/examples/Learnable_Distributions_Zoo) * [Bayesian Modeling with Joint Distribution](https://tensorflow.google.cn/probability/examples/Modeling_with_JointDistribution) * [Audio Data Preparation and Augmentation](https://tensorflow.google.cn/io/tutorials/audio) |

I.e., \(y = \log\_e x\).

#### Example:

```
>>> x = tf.constant([0, 0.5, 1, 5])
>>> tf.math.log(x)
<tf.Tensor: shape=(4,), dtype=float32, numpy=array([      -inf, -0.6931472,  0.       ,  1.609438 ], dtype=float32)>
```

See: <https://en.wikipedia.org/wiki/Logarithm>

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |