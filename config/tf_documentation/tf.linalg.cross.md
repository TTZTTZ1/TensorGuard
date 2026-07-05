# tf.linalg.cross

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linalg/cross](https://tensorflow.google.cn/api_docs/python/tf/linalg/cross)

---

Compute the pairwise cross product.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.cross`](https://tensorflow.google.cn/api_docs/python/tf/linalg/cross), [`tf.compat.v1.linalg.cross`](https://tensorflow.google.cn/api_docs/python/tf/linalg/cross)

```
tf.linalg.cross(
    a: Annotated[Any, tf.raw_ops.Any],
    b: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
tf.raw_ops.Any
```

`a` and `b` must be the same shape; they can either be simple 3-element vectors,
or any shape where the innermost dimension is 3. In the latter case, each pair
of corresponding 3-element vectors is cross-multiplied independently.

| Args | |

|  |  |
| --- | --- |
| `a` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`. A tensor containing 3-element vectors. |
| `b` | A `Tensor`. Must have the same type as `a`. Another tensor, of same type and shape as `a`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `a`. | |