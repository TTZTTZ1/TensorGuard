# tf.random.normal

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/random/normal](https://tensorflow.google.cn/api_docs/python/tf/random/normal)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/random_ops.py#L39-L95) |

Outputs random values from a normal distribution.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.random.normal`](https://tensorflow.google.cn/api_docs/python/tf/random/normal), [`tf.compat.v1.random_normal`](https://tensorflow.google.cn/api_docs/python/tf/random/normal)

```
tf.random.normal(
    shape,
    mean=0.0,
    stddev=1.0,
    dtype=tf.dtypes.float32,
    seed=None,
    name=None
)

tf.dtypes.float32
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Use TF1.x models in TF2 workflows](https://tensorflow.google.cn/guide/migrate/model_mapping) * [Advanced automatic differentiation](https://tensorflow.google.cn/guide/advanced_autodiff) * [Introduction to modules, layers, and models](https://tensorflow.google.cn/guide/intro_to_modules) * [Introduction to gradients and automatic differentiation](https://tensorflow.google.cn/guide/autodiff) * [Basic training loops](https://tensorflow.google.cn/guide/basic_training_loops) | * [Convolutional Variational Autoencoder](https://tensorflow.google.cn/tutorials/generative/cvae) * [Deep Convolutional Generative Adversarial Network](https://tensorflow.google.cn/tutorials/generative/dcgan) * [Intro to Autoencoders](https://tensorflow.google.cn/tutorials/generative/autoencoder) * [Uncertainty-aware Deep Learning with SNGP](https://tensorflow.google.cn/tutorials/understanding/sngp) * [Transfer learning for video classification with MoViNet](https://tensorflow.google.cn/tutorials/video/transfer_learning_with_movinet) |

Example that generates a new set of random values every time:

```
>>> tf.random.set_seed(5);
>>> tf.random.normal([4], 0, 1, tf.float32)
<tf.Tensor: shape=(4,), dtype=float32, numpy=..., dtype=float32)>
```

Example that outputs a reproducible result:

```
>>> tf.random.set_seed(5);
>>> tf.random.normal([2,2], 0, 1, tf.float32, seed=1)
<tf.Tensor: shape=(2, 2), dtype=float32, numpy=
array([[-1.3768897 , -0.01258316],
      [-0.169515   ,  1.0824056 ]], dtype=float32)>
```

In this case, we are setting both the global and operation-level seed to
ensure this result is reproducible. See [`tf.random.set_seed`](https://tensorflow.google.cn/api_docs/python/tf/random/set_seed) for more
information.

| Args | |

|  |  |
| --- | --- |
| `shape` | A 1-D integer Tensor or Python array. The shape of the output tensor. |
| `mean` | A Tensor or Python value of type `dtype`, broadcastable with `stddev`. The mean of the normal distribution. |
| `stddev` | A Tensor or Python value of type `dtype`, broadcastable with `mean`. The standard deviation of the normal distribution. |
| `dtype` | The float type of the output: `float16`, `bfloat16`, `float32`, `float64`. Defaults to `float32`. |
| `seed` | A Python integer. Used to create a random seed for the distribution. See [`tf.random.set_seed`](https://tensorflow.google.cn/api_docs/python/tf/random/set_seed) for behavior. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tensor of the specified shape filled with random normal values. | |