# tf.raw_ops.NotEqual

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NotEqual](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NotEqual)

---

Returns the truth value of (x != y) element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.NotEqual`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/NotEqual)

```
tf.raw_ops.NotEqual(
    x, y, incompatible_shape_error=True, name=None
)
```

**Note:** `NotEqual` supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `incompatible_shape_error` | An optional `bool`. Defaults to `True`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |