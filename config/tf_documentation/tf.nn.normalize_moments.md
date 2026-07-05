# tf.nn.normalize_moments

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/normalize_moments](https://tensorflow.google.cn/api_docs/python/tf/nn/normalize_moments)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_impl.py#L1182-L1212) |

Calculate the mean and variance of based on the sufficient statistics.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.nn.normalize_moments`](https://tensorflow.google.cn/api_docs/python/tf/nn/normalize_moments)

```
tf.nn.normalize_moments(
    counts, mean_ss, variance_ss, shift, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `counts` | A `Tensor` containing the total count of the data (one value). |
| `mean_ss` | A `Tensor` containing the mean sufficient statistics: the (possibly shifted) sum of the elements to average over. |
| `variance_ss` | A `Tensor` containing the variance sufficient statistics: the (possibly shifted) squared sum of the data to compute the variance over. |
| `shift` | A `Tensor` containing the value by which the data is shifted for numerical stability, or `None` if no shift was performed. |
| `name` | Name used to scope the operations that compute the moments. |

| Returns | |
| Two `Tensor` objects: `mean` and `variance`. | |