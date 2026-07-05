# tf.raw_ops.Switch

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Switch](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Switch)

---

Forwards `data` to the output port determined by `pred`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Switch`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Switch)

```
tf.raw_ops.Switch(
    data, pred, name=None
)
```

If `pred` is true, the `data` input is forwarded to `output_true`. Otherwise,
the data goes to `output_false`.

See also `RefSwitch` and `Merge`.

| Args | |

|  |  |
| --- | --- |
| `data` | A `Tensor`. The tensor to be forwarded to the appropriate output. |
| `pred` | A `Tensor` of type `bool`. A scalar that specifies which output port will receive data. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (output\_false, output\_true). | |
| `output_false` | A `Tensor`. Has the same type as `data`. |
| `output_true` | A `Tensor`. Has the same type as `data`. |