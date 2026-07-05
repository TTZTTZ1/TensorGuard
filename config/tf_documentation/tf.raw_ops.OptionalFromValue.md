# tf.raw_ops.OptionalFromValue

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OptionalFromValue](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OptionalFromValue)

---

Constructs an Optional variant from a tuple of tensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.OptionalFromValue`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OptionalFromValue)

```
tf.raw_ops.OptionalFromValue(
    components, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `components` | A list of `Tensor` objects. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |