# tf.nn.ctc_unique_labels

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/ctc_unique_labels](https://tensorflow.google.cn/api_docs/python/tf/nn/ctc_unique_labels)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/ctc_ops.py#L1270-L1303) |

Get unique labels and indices for batched labels for [`tf.nn.ctc_loss`](https://tensorflow.google.cn/api_docs/python/tf/nn/ctc_loss).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.nn.ctc_unique_labels`](https://tensorflow.google.cn/api_docs/python/tf/nn/ctc_unique_labels)

```
tf.nn.ctc_unique_labels(
    labels, name=None
)
```

For use with [`tf.nn.ctc_loss`](https://tensorflow.google.cn/api_docs/python/tf/nn/ctc_loss) optional argument `unique`: This op can be
used to preprocess labels in input pipeline to for better speed/memory use
computing the ctc loss on TPU.

| Example | |
| ctc\_unique\_labels([[3, 4, 4, 3]]) -> unique labels padded with 0: [[3, 4, 0, 0]] indices of original labels in unique: [0, 1, 1, 0] | |

| Args | |

|  |  |
| --- | --- |
| `labels` | tensor of shape [batch\_size, max\_label\_length] padded with 0. |
| `name` | A name for this `Op`. Defaults to "ctc\_unique\_labels". |

| Returns | |
| tuple of | |

* unique labels, tensor of shape `[batch_size, max_label_length]`
* indices into unique labels, shape `[batch_size, max_label_length]`