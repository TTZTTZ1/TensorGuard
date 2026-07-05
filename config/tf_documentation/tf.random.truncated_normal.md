# tf.random.truncated_normal

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/random/truncated_normal](https://tensorflow.google.cn/api_docs/python/tf/random/truncated_normal)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/random_ops.py#L155-L204) |

Outputs random values from a truncated normal distribution.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.random.truncated_normal`](https://tensorflow.google.cn/api_docs/python/tf/random/truncated_normal), [`tf.compat.v1.truncated_normal`](https://tensorflow.google.cn/api_docs/python/tf/random/truncated_normal)

```
tf.random.truncated_normal(
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

| Used in the guide |
| --- |
| * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) |

The values are drawn from a normal distribution with specified mean and
standard deviation, discarding and re-drawing any samples that are more than
two standard deviations from the mean.

#### Examples:

```
>>> tf.random.truncated_normal(shape=[2])
<tf.Tensor: shape=(2,), dtype=float32, numpy=array([..., ...], dtype=float32)>
```

```
>>> tf.random.truncated_normal(shape=[2], mean=3, stddev=1, dtype=tf.float32)
<tf.Tensor: shape=(2,), dtype=float32, numpy=array([..., ...], dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `shape` | A 1-D integer Tensor or Python array. The shape of the output tensor. |
| `mean` | A 0-D Tensor or Python value of type `dtype`. The mean of the truncated normal distribution. |
| `stddev` | A 0-D Tensor or Python value of type `dtype`. The standard deviation of the normal distribution, before truncation. |
| `dtype` | The type of the output. Restricted to floating-point types: [`tf.half`](https://tensorflow.google.cn/api_docs/python/tf#half), `tf.float`, [`tf.double`](https://tensorflow.google.cn/api_docs/python/tf#double), etc. |
| `seed` | A Python integer. Used to create a random seed for the distribution. See [`tf.random.set_seed`](https://tensorflow.google.cn/api_docs/python/tf/random/set_seed) for more information. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tensor of the specified shape filled with random truncated normal values. | |