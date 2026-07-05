# tf.raw_ops.GetOptions

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GetOptions](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GetOptions)

---

Returns the [`tf.data.Options`](https://tensorflow.google.cn/api_docs/python/tf/data/Options) attached to `input_dataset`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.GetOptions`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GetOptions)

```
tf.raw_ops.GetOptions(
    input_dataset, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. A variant tensor representing the input dataset. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |