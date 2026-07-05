# tf.raw_ops.TileGrad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TileGrad](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TileGrad)

---

Returns the gradient of `Tile`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TileGrad`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TileGrad)

```
tf.raw_ops.TileGrad(
    input, multiples, name=None
)
```

Since `Tile` takes an input and repeats the input `multiples` times
along each dimension, `TileGrad` takes in `multiples` and aggregates
each repeated tile of `input` into `output`.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. |
| `multiples` | A `Tensor` of type `int32`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |