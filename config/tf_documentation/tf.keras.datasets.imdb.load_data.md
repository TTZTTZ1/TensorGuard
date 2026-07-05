# tf.keras.datasets.imdb.load_data

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/datasets/imdb/load_data](https://tensorflow.google.cn/api_docs/python/tf/keras/datasets/imdb/load_data)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/datasets/imdb.py#L12-L140) |

Loads the [IMDB dataset](https://ai.stanford.edu/%7Eamaas/data/sentiment/).

```
tf.keras.datasets.imdb.load_data(
    path='imdb.npz',
    num_words=None,
    skip_top=0,
    maxlen=None,
    seed=113,
    start_char=1,
    oov_char=2,
    index_from=3,
    **kwargs
)
```

This is a dataset of 25,000 movies reviews from IMDB, labeled by sentiment
(positive/negative). Reviews have been preprocessed, and each review is
encoded as a list of word indexes (integers).
For convenience, words are indexed by overall frequency in the dataset,
so that for instance the integer "3" encodes the 3rd most frequent word in
the data. This allows for quick filtering operations such as:
"only consider the top 10,000 most
common words, but eliminate the top 20 most common words".

As a convention, "0" does not stand for a specific word, but instead is used
to encode the pad token.

| Args | |

|  |  |
| --- | --- |
| `path` | where to cache the data (relative to `~/.keras/dataset`). |
| `num_words` | integer or None. Words are ranked by how often they occur (in the training set) and only the `num_words` most frequent words are kept. Any less frequent word will appear as `oov_char` value in the sequence data. If None, all words are kept. Defaults to `None`. |
| `skip_top` | skip the top N most frequently occurring words (which may not be informative). These words will appear as `oov_char` value in the dataset. When 0, no words are skipped. Defaults to `0`. |
| `maxlen` | int or None. Maximum sequence length. Any longer sequence will be truncated. None, means no truncation. Defaults to `None`. |
| `seed` | int. Seed for reproducible data shuffling. |
| `start_char` | int. The start of a sequence will be marked with this character. 0 is usually the padding character. Defaults to `1`. |
| `oov_char` | int. The out-of-vocabulary character. Words that were cut out because of the `num_words` or `skip_top` limits will be replaced with this character. |
| `index_from` | int. Index actual words with this index and higher. |

| Returns | |
| Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`. | |

**`x_train`, `x_test`**: lists of sequences, which are lists of indexes
(integers). If the num\_words argument was specific, the maximum
possible index value is `num_words - 1`. If the `maxlen` argument was
specified, the largest possible sequence length is `maxlen`.

**`y_train`, `y_test`**: lists of integer labels (1 or 0).

**Note:** The 'out of vocabulary' character is only used for
words that were present in the training set but are not included
because they're not making the `num_words` cut here.
Words that were not seen in the training set but are in the test set
have simply been skipped.