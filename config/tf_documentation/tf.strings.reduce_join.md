# tf.strings.reduce_join

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/strings/reduce_join](https://tensorflow.google.cn/api_docs/python/tf/strings/reduce_join)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/string_ops.py#L332-L375) |

Joins all strings into a single string, or joins along an axis.

```
tf.strings.reduce_join(
    inputs, axis=None, keepdims=False, separator='', name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Subword tokenizers](https://tensorflow.google.cn/text/guide/subwords_tokenizer) | * [TensorFlow Ranking Keras pipeline for distributed training](https://tensorflow.google.cn/ranking/tutorials/ranking_dnn_distributed) * [Image captioning with visual attention](https://tensorflow.google.cn/text/tutorials/image_captioning) * [Text generation with an RNN](https://tensorflow.google.cn/text/tutorials/text_generation) * [Neural machine translation with attention](https://tensorflow.google.cn/text/tutorials/nmt_with_attention) |

This is the reduction operation for the elementwise [`tf.strings.join`](https://tensorflow.google.cn/api_docs/python/tf/strings/join) op.

```
>>> tf.strings.reduce_join([['abc','123'],
...                         ['def','456']]).numpy()
b'abc123def456'
>>> tf.strings.reduce_join([['abc','123'],
...                         ['def','456']], axis=-1).numpy()
array([b'abc123', b'def456'], dtype=object)
>>> tf.strings.reduce_join([['abc','123'],
...                         ['def','456']],
...                        axis=-1,
...                        separator=" ").numpy()
array([b'abc 123', b'def 456'], dtype=object)
```

| Args | |

|  |  |
| --- | --- |
| `inputs` | A [`tf.string`](https://tensorflow.google.cn/api_docs/python/tf#string) tensor. |
| `axis` | Which axis to join along. The default behavior is to join all elements, producing a scalar. |
| `keepdims` | If true, retains reduced dimensions with length 1. |
| `separator` | a string added between each string being joined. |
| `name` | A name for the operation (optional). |

| Returns | |
| A [`tf.string`](https://tensorflow.google.cn/api_docs/python/tf#string) tensor. | |