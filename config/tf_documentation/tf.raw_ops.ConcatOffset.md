# tf.raw_ops.ConcatOffset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ConcatOffset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ConcatOffset)

---

Computes offsets of concat inputs within its output.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ConcatOffset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ConcatOffset)

```
tf.raw_ops.ConcatOffset(
    concat_dim, shape, name=None
)
```

#### For example:

```
>>> x = [2, 2, 7]
>>> y = [2, 3, 7]
>>> z = [2, 9, 7]
>>> offsets = concat_offset(1, [x, y, z])
>>> [list(off.numpy()) for off in offsets]
[[0, 0, 0], [0, 2, 0], [0, 5, 0]]
```

This is typically used by gradient computations for a concat operation.

| Args | |

|  |  |
| --- | --- |
| `concat_dim` | A `Tensor` of type `int32`. The dimension along which to concatenate. |
| `shape` | A list of at least 2 `Tensor` objects with the same type in: `int32`, `int64`. The `N` int32 or int64 vectors representing shape of tensors being concatenated. |
| `name` | A name for the operation (optional). |

| Returns | |
| A list with the same length as `shape` of `Tensor` objects with the same type as `shape`. | |