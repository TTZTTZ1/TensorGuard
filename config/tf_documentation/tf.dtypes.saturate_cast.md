# tf.dtypes.saturate_cast

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/dtypes/saturate_cast](https://tensorflow.google.cn/api_docs/python/tf/dtypes/saturate_cast)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L1023-L1103) |

Performs a safe saturating cast of `value` to `dtype`.

#### View aliases

**Main aliases**

[`tf.saturate_cast`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/saturate_cast)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.dtypes.saturate_cast`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/saturate_cast), [`tf.compat.v1.saturate_cast`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/saturate_cast)

```
tf.dtypes.saturate_cast(
    value, dtype, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Learned data compression](https://tensorflow.google.cn/tutorials/generative/data_compression) |

This function casts the input to `dtype` without overflow. If
there is a danger that values would over or underflow in the cast, this op
applies the appropriate clamping before the cast. See [`tf.cast`](https://tensorflow.google.cn/api_docs/python/tf/cast) for more
details.

| Args | |

|  |  |
| --- | --- |
| `value` | A `Tensor`. |
| `dtype` | The desired output `DType`. |
| `name` | A name for the operation (optional). |

| Returns | |
| `value` safely cast to `dtype`. | |