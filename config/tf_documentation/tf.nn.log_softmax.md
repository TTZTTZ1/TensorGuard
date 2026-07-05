# tf.nn.log_softmax

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/log_softmax](https://tensorflow.google.cn/api_docs/python/tf/nn/log_softmax)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_ops.py#L3955-L3980) |

Computes log softmax activations.

#### View aliases

**Main aliases**

[`tf.math.log_softmax`](https://tensorflow.google.cn/api_docs/python/tf/nn/log_softmax)

```
tf.nn.log_softmax(
    logits, axis=None, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Training with Orbit](https://tensorflow.google.cn/tfmodels/orbit/index) |

For each batch `i` and class `j` we have

```
logsoftmax = logits - log(reduce_sum(exp(logits), axis))
```

| Args | |

|  |  |
| --- | --- |
| `logits` | A non-empty `Tensor`. Must be one of the following types: `half`, `float32`, `float64`. |
| `axis` | The dimension softmax would be performed on. The default is -1 which indicates the last dimension. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `logits`. Same shape as `logits`. | |

| Raises | |

|  |  |
| --- | --- |
| `InvalidArgumentError` | if `logits` is empty or `axis` is beyond the last dimension of `logits`. |