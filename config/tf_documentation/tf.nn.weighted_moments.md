# tf.nn.weighted_moments

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/weighted_moments](https://tensorflow.google.cn/api_docs/python/tf/nn/weighted_moments)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_impl.py#L1395-L1417) |

Returns the frequency-weighted mean and variance of `x`.

```
tf.nn.weighted_moments(
    x, axes, frequency_weights, keepdims=False, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `x` | A tensor. |
| `axes` | 1-d tensor of int32 values; these are the axes along which to compute mean and variance. |
| `frequency_weights` | A tensor of positive weights which can be broadcast with x. |
| `keepdims` | Produce moments with the same dimensionality as the input. |
| `name` | Name used to scope the operation. |

| Returns | |
| Two tensors: `weighted_mean` and `weighted_variance`. | |