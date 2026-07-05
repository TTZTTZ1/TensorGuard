# tf.data.experimental.rejection_resample

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/rejection_resample](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/rejection_resample)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/resampling.py#L20-L50) |

A transformation that resamples a dataset to achieve a target distribution. (deprecated)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.rejection_resample`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/rejection_resample)

```
tf.data.experimental.rejection_resample(
    class_func, target_dist, initial_dist=None, seed=None
)
```

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use [`tf.data.Dataset.rejection_resample(...)`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#rejection_resample).**Note:** Resampling is performed via rejection sampling; some fraction
of the input values will be dropped.

| Args | |

|  |  |
| --- | --- |
| `class_func` | A function mapping an element of the input dataset to a scalar [`tf.int32`](https://tensorflow.google.cn/api_docs/python/tf#int32) tensor. Values should be in `[0, num_classes)`. |
| `target_dist` | A floating point type tensor, shaped `[num_classes]`. |
| `initial_dist` | (Optional.) A floating point type tensor, shaped `[num_classes]`. If not provided, the true class distribution is estimated live in a streaming fashion. |
| `seed` | (Optional.) Python integer seed for the resampler. |

| Returns | |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#apply). | |