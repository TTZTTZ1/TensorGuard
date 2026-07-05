# tf.keras.preprocessing.text.Tokenizer

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/text/Tokenizer](https://tensorflow.google.cn/api_docs/python/tf/keras/preprocessing/text/Tokenizer)

---

[View source on GitHub](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/text.py#L81-L312) |

DEPRECATED.

```
tf.keras.preprocessing.text.Tokenizer(
    num_words=None,
    filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
    lower=True,
    split=' ',
    char_level=False,
    oov_token=None,
    analyzer=None,
    **kwargs
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Wiki Talk Comments Toxicity Prediction](https://tensorflow.google.cn/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_TFCO_Wiki_Case_Study) |

## Methods

### `fit_on_sequences`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/text.py#L169-L174)

```
fit_on_sequences(
    sequences
)
```

### `fit_on_texts`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/text.py#L121-L167)

```
fit_on_texts(
    texts
)
```

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/text.py#L284-L304)

```
get_config()
```

### `sequences_to_matrix`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/text.py#L238-L282)

```
sequences_to_matrix(
    sequences, mode='binary'
)
```

### `sequences_to_texts`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/text.py#L213-L214)

```
sequences_to_texts(
    sequences
)
```

### `sequences_to_texts_generator`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/text.py#L216-L232)

```
sequences_to_texts_generator(
    sequences
)
```

### `texts_to_matrix`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/text.py#L234-L236)

```
texts_to_matrix(
    texts, mode='binary'
)
```

### `texts_to_sequences`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/text.py#L176-L177)

```
texts_to_sequences(
    texts
)
```

### `texts_to_sequences_generator`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/text.py#L179-L211)

```
texts_to_sequences_generator(
    texts
)
```

### `to_json`

[View source](https://github.com/keras-team/keras/tree/v3.3.3/keras/src/legacy/preprocessing/text.py#L306-L312)

```
to_json(
    **kwargs
)
```