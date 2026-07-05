# tf.histogram_fixed_width_bins

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/histogram_fixed_width_bins](https://tensorflow.google.cn/api_docs/python/tf/histogram_fixed_width_bins)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/histogram_ops.py#L31-L100) |

Bins the given values for use in a histogram.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.histogram_fixed_width_bins`](https://tensorflow.google.cn/api_docs/python/tf/histogram_fixed_width_bins)

```
tf.histogram_fixed_width_bins(
    values,
    value_range,
    nbins=100,
    dtype=tf.dtypes.int32,
    name=None
)

tf.dtypes.int32
```

Given the tensor `values`, this operation returns a rank 1 `Tensor`
representing the indices of a histogram into which each element
of `values` would be binned. The bins are equal width and
determined by the arguments `value_range` and `nbins`.

| Args | |

|  |  |
| --- | --- |
| `values` | Numeric `Tensor`. |
| `value_range` | Shape [2] `Tensor` of same `dtype` as `values`. values <= value\_range[0] will be mapped to hist[0], values >= value\_range[1] will be mapped to hist[-1]. |
| `nbins` | Scalar `int32 Tensor`. Number of histogram bins. |
| `dtype` | dtype for returned histogram. |
| `name` | A name for this operation (defaults to 'histogram\_fixed\_width'). |

| Returns | |
| A `Tensor` holding the indices of the binned values whose shape matches `values`. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If any unsupported dtype is provided. |
| [`tf.errors.InvalidArgumentError`](https://tensorflow.google.cn/api_docs/python/tf/errors/InvalidArgumentError) | If value\_range does not satisfy value\_range[0] < value\_range[1]. |

#### Examples:

```
>>> # Bins will be:  (-inf, 1), [1, 2), [2, 3), [3, 4), [4, inf)
... 
>>> nbins = 5
>>> value_range = [0.0, 5.0]
>>> new_values = [-1.0, 0.0, 1.5, 2.0, 5.0, 15]
>>> indices = tf.histogram_fixed_width_bins(new_values, value_range, nbins=5)
>>> indices.numpy()
array([0, 0, 1, 2, 4, 4], dtype=int32)
```