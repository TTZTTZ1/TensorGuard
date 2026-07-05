# tf.random.uniform

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/random/uniform](https://tensorflow.google.cn/api_docs/python/tf/random/uniform)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/random_ops.py#L211-L320) |

Outputs random values from a uniform distribution.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.random.uniform`](https://tensorflow.google.cn/api_docs/python/tf/random/uniform), [`tf.compat.v1.random_uniform`](https://tensorflow.google.cn/api_docs/python/tf/random/uniform)

```
tf.random.uniform(
    shape,
    minval=0,
    maxval=None,
    dtype=tf.dtypes.float32,
    seed=None,
    name=None
)

tf.dtypes.float32
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Validating correctness & numerical equivalence](https://tensorflow.google.cn/guide/migrate/validate_correctness) * [tf.data: Build TensorFlow input pipelines](https://tensorflow.google.cn/guide/data) * [Introduction to graphs and tf.function](https://tensorflow.google.cn/guide/intro_to_graphs) * [Logistic regression for binary classification with Core APIs](https://tensorflow.google.cn/guide/core/logistic_regression_core) * [Quickstart for the TensorFlow Core APIs](https://tensorflow.google.cn/guide/core/quickstart_core) | * [Customization basics: tensors and operations](https://tensorflow.google.cn/tutorials/customization/basics) * [Parameter server training with ParameterServerStrategy](https://tensorflow.google.cn/tutorials/distribute/parameter_server_training) * [Learned data compression](https://tensorflow.google.cn/tutorials/generative/data_compression) * [DeepDream](https://tensorflow.google.cn/tutorials/generative/deepdream) * [pix2pix: Image-to-image translation with a conditional GAN](https://tensorflow.google.cn/tutorials/generative/pix2pix) |

The generated values follow a uniform distribution in the range
`[minval, maxval)`. The lower bound `minval` is included in the range, while
the upper bound `maxval` is excluded.

For floats, the default range is `[0, 1)`. For ints, at least `maxval` must
be specified explicitly.

In the integer case, the random integers are slightly biased unless
`maxval - minval` is an exact power of two. The bias is small for values of
`maxval - minval` significantly smaller than the range of the output (either
`2**32` or `2**64`).

#### Examples:

```
>>> tf.random.uniform(shape=[2])
<tf.Tensor: shape=(2,), dtype=float32, numpy=array([..., ...], dtype=float32)>
>>> tf.random.uniform(shape=[], minval=-1., maxval=0.)
<tf.Tensor: shape=(), dtype=float32, numpy=-...>
>>> tf.random.uniform(shape=[], minval=5, maxval=10, dtype=tf.int64)
<tf.Tensor: shape=(), dtype=int64, numpy=...>
```

The `seed` argument produces a deterministic sequence of tensors across
multiple calls. To repeat that sequence, use [`tf.random.set_seed`](https://tensorflow.google.cn/api_docs/python/tf/random/set_seed):

```
>>> tf.random.set_seed(5)
>>> tf.random.uniform(shape=[], maxval=3, dtype=tf.int32, seed=10)
<tf.Tensor: shape=(), dtype=int32, numpy=2>
>>> tf.random.uniform(shape=[], maxval=3, dtype=tf.int32, seed=10)
<tf.Tensor: shape=(), dtype=int32, numpy=0>
>>> tf.random.set_seed(5)
>>> tf.random.uniform(shape=[], maxval=3, dtype=tf.int32, seed=10)
<tf.Tensor: shape=(), dtype=int32, numpy=2>
>>> tf.random.uniform(shape=[], maxval=3, dtype=tf.int32, seed=10)
<tf.Tensor: shape=(), dtype=int32, numpy=0>
```

Without [`tf.random.set_seed`](https://tensorflow.google.cn/api_docs/python/tf/random/set_seed) but with a `seed` argument is specified, small
changes to function graphs or previously executed operations will change the
returned value. See [`tf.random.set_seed`](https://tensorflow.google.cn/api_docs/python/tf/random/set_seed) for details.

| Args | |

|  |  |
| --- | --- |
| `shape` | A 1-D integer Tensor or Python array. The shape of the output tensor. |
| `minval` | A Tensor or Python value of type `dtype`, broadcastable with `shape` (for integer types, broadcasting is not supported, so it needs to be a scalar). The lower bound on the range of random values to generate (inclusive). Defaults to 0. |
| `maxval` | A Tensor or Python value of type `dtype`, broadcastable with `shape` (for integer types, broadcasting is not supported, so it needs to be a scalar). The upper bound on the range of random values to generate (exclusive). Defaults to 1 if `dtype` is floating point. |
| `dtype` | The type of the output: `float16`, `bfloat16`, `float32`, `float64`, `int32`, or `int64`. Defaults to `float32`. |
| `seed` | A Python integer. Used in combination with [`tf.random.set_seed`](https://tensorflow.google.cn/api_docs/python/tf/random/set_seed) to create a reproducible sequence of tensors across multiple calls. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tensor of the specified shape filled with random uniform values. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `dtype` is integral and `maxval` is not specified. |