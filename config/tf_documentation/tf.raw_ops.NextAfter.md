# tf.raw_ops.NextAfter

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NextAfter](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NextAfter)

---

Returns the next representable value of `x1` in the direction of `x2`, element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.NextAfter`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NextAfter)

```
tf.raw_ops.NextAfter(
    x1, x2, name=None
)
```

This operation returns the same result as the C++ std::nextafter function.

It can also return a subnormal number.

| Args | |

|  |  |
| --- | --- |
| `x1` | A `Tensor`. Must be one of the following types: `float64`, `float32`. |
| `x2` | A `Tensor`. Must have the same type as `x1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x1`. | |

## cpp compatibility

Equivalent to C++ std::nextafter function.