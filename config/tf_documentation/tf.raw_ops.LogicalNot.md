# tf.raw_ops.LogicalNot

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LogicalNot](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LogicalNot)

---

Returns the truth value of `NOT x` element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.LogicalNot`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/LogicalNot)

```
tf.raw_ops.LogicalNot(
    x, name=None
)
```

#### Example:

```
>>> tf.math.logical_not(tf.constant([True, False]))
<tf.Tensor: shape=(2,), dtype=bool, numpy=array([False,  True])>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor` of type `bool`. A `Tensor` of type `bool`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |