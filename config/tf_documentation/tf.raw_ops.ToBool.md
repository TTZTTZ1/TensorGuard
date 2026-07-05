# tf.raw_ops.ToBool

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ToBool](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ToBool)

---

Converts a tensor to a scalar predicate.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ToBool`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ToBool)

```
tf.raw_ops.ToBool(
    input, name=None
)
```

Converts a tensor to a scalar predicate with the following rules:

* For 0D tensors, truthiness is determined by comparing against a "zero"
  value. For numerical types it is the obvious zero. For strings it is the
  empty string.
* For >0D tensors, truthiness is determined by looking at the number of
  elements. If has zero elements, then the result is false. Otherwise the
  result is true.

This matches the behavior of If and While for determining if a tensor counts
as true/false for a branch condition.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |