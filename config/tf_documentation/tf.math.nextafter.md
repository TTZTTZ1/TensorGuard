# tf.math.nextafter

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/nextafter](https://tensorflow.google.cn/api_docs/python/tf/math/nextafter)

---

Returns the next representable value of `x1` in the direction of `x2`, element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.math.nextafter`](https://tensorflow.google.cn/api_docs/python/tf/math/nextafter)

```
tf.math.nextafter(
    x1: Annotated[Any, tf.raw_ops.Any],
    x2: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
tf.raw_ops.Any
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