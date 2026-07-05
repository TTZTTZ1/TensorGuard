# tf.nn.collapse_repeated

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/collapse_repeated](https://tensorflow.google.cn/api_docs/python/tf/nn/collapse_repeated)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/ctc_ops.py#L1172-L1233) |

Merge repeated labels into single labels.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.nn.collapse_repeated`](https://tensorflow.google.cn/api_docs/python/tf/nn/collapse_repeated)

```
tf.nn.collapse_repeated(
    labels, seq_length, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `labels` | Tensor of shape [batch, max value in seq\_length] |
| `seq_length` | Tensor of shape [batch], sequence length of each batch element. |
| `name` | A name for this `Op`. Defaults to "collapse\_repeated\_labels". |

| Returns | |
| A tuple `(collapsed_labels, new_seq_length)` where | |
| `collapsed_labels` | Tensor of shape [batch, max\_seq\_length] with repeated labels collapsed and padded to max\_seq\_length, eg: `[[A, A, B, B, A], [A, B, C, D, E]] => [[A, B, A, 0, 0], [A, B, C, D, E]]` |
| `new_seq_length` | int tensor of shape [batch] with new sequence lengths. |