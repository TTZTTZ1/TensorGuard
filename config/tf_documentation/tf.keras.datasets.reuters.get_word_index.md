# tf.keras.datasets.reuters.get_word_index

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/datasets/reuters/get_word_index](https://tensorflow.google.cn/api_docs/python/tf/keras/datasets/reuters/get_word_index)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/datasets/reuters.py#L135-L162) |

Retrieves a dict mapping words to their index in the Reuters dataset.

```
tf.keras.datasets.reuters.get_word_index(
    path='reuters_word_index.json'
)
```

Actual word indices starts from 3, with 3 indices reserved for:
0 (padding), 1 (start), 2 (oov).

E.g. word index of 'the' is 1, but the in the actual training data, the
index of 'the' will be 1 + 3 = 4. Vice versa, to translate word indices in
training data back to words using this mapping, indices need to subtract 3.

| Args | |

|  |  |
| --- | --- |
| `path` | where to cache the data (relative to `~/.keras/dataset`). |

| Returns | |
| The word index dictionary. Keys are word strings, values are their index. | |