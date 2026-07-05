# tf.raw_ops.SoftmaxCrossEntropyWithLogits

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SoftmaxCrossEntropyWithLogits](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SoftmaxCrossEntropyWithLogits)

---

Computes softmax cross entropy cost and gradients to backpropagate.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SoftmaxCrossEntropyWithLogits`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SoftmaxCrossEntropyWithLogits)

```
tf.raw_ops.SoftmaxCrossEntropyWithLogits(
    features, labels, name=None
)
```

Inputs are the logits, not probabilities.

| Args | |

|  |  |
| --- | --- |
| `features` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. batch\_size x num\_classes matrix |
| `labels` | A `Tensor`. Must have the same type as `features`. batch\_size x num\_classes matrix The caller must ensure that each batch of labels represents a valid probability distribution. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (loss, backprop). | |
| `loss` | A `Tensor`. Has the same type as `features`. |
| `backprop` | A `Tensor`. Has the same type as `features`. |