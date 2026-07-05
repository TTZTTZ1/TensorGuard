# tf.nn.selu

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/selu](https://tensorflow.google.cn/api_docs/python/tf/nn/selu)

---

Computes scaled exponential linear: `scale * alpha * (exp(features) - 1)`

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.nn.selu`](https://tensorflow.google.cn/api_docs/python/tf/nn/selu)

```
tf.nn.selu(
    features: Annotated[Any, TV_Selu_T], name=None
) -> Annotated[Any, TV_Selu_T]
```

if < 0, `scale * features` otherwise.

To be used together with
`initializer = tf.variance_scaling_initializer(factor=1.0, mode='FAN_IN')`.
For correct dropout, use `tf.contrib.nn.alpha_dropout`.

See [Self-Normalizing Neural Networks](https://arxiv.org/abs/1706.02515)

| Args | |

|  |  |
| --- | --- |
| `features` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `features`. | |