# tf.raw_ops.FakeParam

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FakeParam](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FakeParam)

---

This op is used as a placeholder in If branch functions.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.FakeParam`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/FakeParam)

```
tf.raw_ops.FakeParam(
    dtype, shape, name=None
)
```

It doesn't provide a
valid output when run, so must either be removed (e.g. replaced with a
function input) or guaranteed not to be used (e.g. if mirroring an
intermediate output needed for the gradient computation of the other branch).

| Args | |

|  |  |
| --- | --- |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). The type of the output. |
| `shape` | A [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. The purported shape of the output. This is only used for shape inference; the output will not necessarily have this shape. Can be a partial shape. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |