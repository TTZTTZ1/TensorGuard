# tf.histogram_fixed_width

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/histogram_fixed_width](https://tensorflow.google.cn/api_docs/python/tf/histogram_fixed_width)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/histogram_ops.py#L103-L149) |

Return histogram of values.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.histogram_fixed_width`](https://tensorflow.google.cn/api_docs/python/tf/histogram_fixed_width)

```
tf.histogram_fixed_width(
    values,
    value_range,
    nbins=100,
    dtype=tf.dtypes.int32,
    name=None
)

tf.dtypes.int32
```

Given the tensor `values`, this operation returns a rank 1 histogram counting
the number of entries in `values` that fell into every bin. The bins are
equal width and determined by the arguments `value_range` and `nbins`.

| Args | |

|  |  |
| --- | --- |
| `values` | Numeric `Tensor`. |
| `value_range` | Shape [2] `Tensor` of same `dtype` as `values`. values <= value\_range[0] will be mapped to hist[0], values >= value\_range[1] will be mapped to hist[-1]. |
| `nbins` | Scalar `int32 Tensor`. Number of histogram bins. |
| `dtype` | dtype for returned histogram. |
| `name` | A name for this operation (defaults to 'histogram\_fixed\_width'). |

| Returns | |
| A 1-D `Tensor` holding histogram of values. | |

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
>>> hist = tf.histogram_fixed_width(new_values, value_range, nbins=5)
>>> hist.numpy()
array([2, 1, 1, 0, 2], dtype=int32)
```