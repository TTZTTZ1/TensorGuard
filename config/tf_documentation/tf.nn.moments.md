# tf.nn.moments

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/moments](https://tensorflow.google.cn/api_docs/python/tf/nn/moments)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_impl.py#L1281-L1315) |

Calculates the mean and variance of `x`.

```
tf.nn.moments(
    x, axes, shift=None, keepdims=False, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Distributed training with DTensors](https://tensorflow.google.cn/tutorials/distribute/dtensor_ml_tutorial) |

The mean and variance are calculated by aggregating the contents of `x`
across `axes`. If `x` is 1-D and `axes = [0]` this is just the mean
and variance of a vector.

**Note:** shift is currently not used; the true mean is computed and used.

When using these moments for batch normalization (see
[`tf.nn.batch_normalization`](https://tensorflow.google.cn/api_docs/python/tf/nn/batch_normalization)):

* for so-called "global normalization", used with convolutional filters with
  shape `[batch, height, width, depth]`, pass `axes=[0, 1, 2]`.
* for simple batch normalization pass `axes=[0]` (batch only).

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. |
| `axes` | Array of ints. Axes along which to compute mean and variance. |
| `shift` | Not used in the current implementation. |
| `keepdims` | produce moments with the same dimensionality as the input. |
| `name` | Name used to scope the operations that compute the moments. |

| Returns | |
| Two `Tensor` objects: `mean` and `variance`. | |