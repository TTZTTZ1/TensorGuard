# tf.math.sobol_sample

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/sobol_sample](https://tensorflow.google.cn/api_docs/python/tf/math/sobol_sample)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L5512-L5534) |

Generates points from the Sobol sequence.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.math.sobol_sample`](https://tensorflow.google.cn/api_docs/python/tf/math/sobol_sample)

```
tf.math.sobol_sample(
    dim,
    num_results,
    skip=0,
    dtype=tf.dtypes.float32,
    name=None
)

tf.dtypes.float32
```

Creates a Sobol sequence with `num_results` samples. Each sample has dimension
`dim`. Skips the first `skip` samples.

| Args | |

|  |  |
| --- | --- |
| `dim` | Positive scalar `Tensor` representing each sample's dimension. |
| `num_results` | Positive scalar `Tensor` of dtype int32. The number of Sobol points to return in the output. |
| `skip` | (Optional) Positive scalar `Tensor` of dtype int32. The number of initial points of the Sobol sequence to skip. Default value is 0. |
| `dtype` | (Optional) The `tf.Dtype` of the sample. One of: [`tf.float32`](https://tensorflow.google.cn/api_docs/python/tf#float32) or [`tf.float64`](https://tensorflow.google.cn/api_docs/python/tf#float64). Defaults to [`tf.float32`](https://tensorflow.google.cn/api_docs/python/tf#float32). |
| `name` | (Optional) Python `str` name prefixed to ops created by this function. |

| Returns | |
| `Tensor` of samples from Sobol sequence with `shape` [num\_results, dim]. | |