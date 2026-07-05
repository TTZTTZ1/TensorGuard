# tf.math.softsign

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/softsign](https://tensorflow.google.cn/api_docs/python/tf/math/softsign)

---

Computes softsign: `features / (abs(features) + 1)`.

#### View aliases

**Main aliases**

[`tf.math.softsign`](https://tensorflow.google.cn/api_docs/python/tf/nn/softsign)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.math.softsign`](https://tensorflow.google.cn/api_docs/python/tf/nn/softsign), [`tf.compat.v1.nn.softsign`](https://tensorflow.google.cn/api_docs/python/tf/nn/softsign)

```
tf.nn.softsign(
    features: Annotated[Any, TV_Softsign_T], name=None
) -> Annotated[Any, TV_Softsign_T]
```

| Args | |

|  |  |
| --- | --- |
| `features` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `features`. | |