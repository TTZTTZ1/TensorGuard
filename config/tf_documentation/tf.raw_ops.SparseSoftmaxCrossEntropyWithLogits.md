# tf.raw_ops.SparseSoftmaxCrossEntropyWithLogits

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSoftmaxCrossEntropyWithLogits](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSoftmaxCrossEntropyWithLogits)

---

Computes softmax cross entropy cost and gradients to backpropagate.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseSoftmaxCrossEntropyWithLogits`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseSoftmaxCrossEntropyWithLogits)

```
tf.raw_ops.SparseSoftmaxCrossEntropyWithLogits(
    features, labels, name=None
)
```

Unlike `SoftmaxCrossEntropyWithLogits`, this operation does not accept
a matrix of label probabilities, but rather a single label per row
of features. This label is considered to have probability 1.0 for the
given row.

Inputs are the logits, not probabilities.

| Args | |

|  |  |
| --- | --- |
| `features` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. batch\_size x num\_classes matrix |
| `labels` | A `Tensor`. Must be one of the following types: `int32`, `int64`. batch\_size vector with values in [0, num\_classes). This is the label for the given minibatch entry. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (loss, backprop). | |
| `loss` | A `Tensor`. Has the same type as `features`. |
| `backprop` | A `Tensor`. Has the same type as `features`. |