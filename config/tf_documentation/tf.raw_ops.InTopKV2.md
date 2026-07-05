# tf.raw_ops.InTopKV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/InTopKV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/InTopKV2)

---

Says whether the targets are in the top `K` predictions.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.InTopKV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/InTopKV2)

```
tf.raw_ops.InTopKV2(
    predictions, targets, k, name=None
)
```

This outputs a `batch_size` bool array, an entry `out[i]` is `true` if the
prediction for the target class is among the top `k` predictions among
all predictions for example `i`. Note that the behavior of `InTopK` differs
from the `TopK` op in its handling of ties; if multiple classes have the
same prediction value and straddle the top-`k` boundary, all of those
classes are considered to be in the top `k`.

More formally, let

\(predictions\_i\) be the predictions for all classes for example `i`,
\(targets\_i\) be the target class for example `i`,
\(out\_i\) be the output for example `i`,

\[out\_i = predictions\_{i, targets\_i} \in TopKIncludingTies(predictions\_i)\]

| Args | |

|  |  |
| --- | --- |
| `predictions` | A `Tensor` of type `float32`. A `batch_size` x `classes` tensor. |
| `targets` | A `Tensor`. Must be one of the following types: `int32`, `int64`. A `batch_size` vector of class ids. |
| `k` | A `Tensor`. Must have the same type as `targets`. Number of top elements to look at for computing precision. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |