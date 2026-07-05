# tf.raw_ops.CTCBeamSearchDecoder

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CTCBeamSearchDecoder](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CTCBeamSearchDecoder)

---

Performs beam search decoding on the logits given in input.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CTCBeamSearchDecoder`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CTCBeamSearchDecoder)

```
tf.raw_ops.CTCBeamSearchDecoder(
    inputs,
    sequence_length,
    beam_width,
    top_paths,
    merge_repeated=True,
    name=None
)
```

A note about the attribute merge\_repeated: For the beam search decoder,
this means that if consecutive entries in a beam are the same, only
the first of these is emitted. That is, when the top path is "A B B B B",
"A B" is returned if merge\_repeated = True but "A B B B B" is
returned if merge\_repeated = False.

| Args | |

|  |  |
| --- | --- |
| `inputs` | A `Tensor`. Must be one of the following types: `float32`, `float64`. 3-D, shape: `(max_time x batch_size x num_classes)`, the logits. |
| `sequence_length` | A `Tensor` of type `int32`. A vector containing sequence lengths, size `(batch)`. |
| `beam_width` | An `int` that is `>= 1`. A scalar >= 0 (beam search beam width). |
| `top_paths` | An `int` that is `>= 1`. A scalar >= 0, <= beam\_width (controls output size). |
| `merge_repeated` | An optional `bool`. Defaults to `True`. If true, merge repeated classes in output. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (decoded\_indices, decoded\_values, decoded\_shape, log\_probability). | |
| `decoded_indices` | A list of `top_paths` `Tensor` objects with type `int64`. |
| `decoded_values` | A list of `top_paths` `Tensor` objects with type `int64`. |
| `decoded_shape` | A list of `top_paths` `Tensor` objects with type `int64`. |
| `log_probability` | A `Tensor`. Has the same type as `inputs`. |