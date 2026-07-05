# tf.nn.ctc_beam_search_decoder

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/ctc_beam_search_decoder](https://tensorflow.google.cn/api_docs/python/tf/nn/ctc_beam_search_decoder)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/ctc_ops.py#L446-L495) |

Performs beam search decoding on the logits given in input.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.nn.ctc_beam_search_decoder_v2`](https://tensorflow.google.cn/api_docs/python/tf/nn/ctc_beam_search_decoder)

```
tf.nn.ctc_beam_search_decoder(
    inputs, sequence_length, beam_width=100, top_paths=1
)
```

**Note:** Although in general greedy search is a special case of beam-search
with `top_paths=1` and `beam_width=1`, `ctc_beam_search_decoder` differs
from `ctc_greedy_decoder` in the treatment of blanks when computing the
probability of a sequence:

* `ctc_beam_search_decoder` treats blanks as sequence termination
* `ctc_greedy_decoder` treats blanks as regular elements

| Args | |

|  |  |
| --- | --- |
| `inputs` | 3-D `float` `Tensor`, size `[max_time, batch_size, num_classes]`. The logits. |
| `sequence_length` | 1-D `int32` vector containing sequence lengths, having size `[batch_size]`. |
| `beam_width` | An int scalar >= 0 (beam search beam width). |
| `top_paths` | An int scalar >= 0, <= beam\_width (controls output size). |

| Returns | |
| A tuple `(decoded, log_probabilities)` where | |
| `decoded` | A list of length top\_paths, where `decoded[j]` is a `SparseTensor` containing the decoded outputs: |

`decoded[j].indices`: Indices matrix `[total_decoded_outputs[j], 2]`;
The rows store: `[batch, time]`.

`decoded[j].values`: Values vector, size `[total_decoded_outputs[j]]`.
The vector stores the decoded classes for beam `j`.

`decoded[j].dense_shape`: Shape vector, size `(2)`.
The shape values are: `[batch_size, max_decoded_length[j]]`.| `log_probability` | A `float` matrix `[batch_size, top_paths]` containing sequence log-probabilities. |