# tf.raw_ops.CTCGreedyDecoder

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CTCGreedyDecoder](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CTCGreedyDecoder)

---

Performs greedy decoding on the logits given in inputs.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CTCGreedyDecoder`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CTCGreedyDecoder)

```
tf.raw_ops.CTCGreedyDecoder(
    inputs, sequence_length, merge_repeated=False, blank_index=-1, name=None
)
```

A note about the attribute merge\_repeated: if enabled, when
consecutive logits' maximum indices are the same, only the first of
these is emitted. Labeling the blank '\*', the sequence "A B B \* B B"
becomes "A B B" if merge\_repeated = True and "A B B B B" if
merge\_repeated = False.

Regardless of the value of merge\_repeated, if the maximum index of a given
time and batch corresponds to the blank, index `(num_classes - 1)`, no new
element is emitted.

| Args | |

|  |  |
| --- | --- |
| `inputs` | A `Tensor`. Must be one of the following types: `float32`, `float64`. 3-D, shape: `(max_time x batch_size x num_classes)`, the logits. |
| `sequence_length` | A `Tensor` of type `int32`. A vector containing sequence lengths, size `(batch_size)`. |
| `merge_repeated` | An optional `bool`. Defaults to `False`. If True, merge repeated classes in output. |
| `blank_index` | An optional `int`. Defaults to `-1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (decoded\_indices, decoded\_values, decoded\_shape, log\_probability). | |
| `decoded_indices` | A `Tensor` of type `int64`. |
| `decoded_values` | A `Tensor` of type `int64`. |
| `decoded_shape` | A `Tensor` of type `int64`. |
| `log_probability` | A `Tensor`. Has the same type as `inputs`. |