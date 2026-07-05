# tf.data.experimental.cardinality

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/cardinality](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/cardinality)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/cardinality.py#L33-L64) |

Returns the cardinality of `dataset`, if known.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.cardinality`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/cardinality)

```
tf.data.experimental.cardinality(
    dataset
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Transfer learning and fine-tuning](https://tensorflow.google.cn/tutorials/images/transfer_learning) * [Load and preprocess images](https://tensorflow.google.cn/tutorials/load_data/images) * [Classify text with BERT](https://tensorflow.google.cn/text/tutorials/classify_text_with_bert) |

The operation returns the cardinality of `dataset`. The operation may return
[`tf.data.experimental.INFINITE_CARDINALITY`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental#INFINITE_CARDINALITY) if `dataset` contains an infinite
number of elements or [`tf.data.experimental.UNKNOWN_CARDINALITY`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental#UNKNOWN_CARDINALITY) if the
analysis fails to determine the number of elements in `dataset` (e.g. when the
dataset source is a file).

```
>>> dataset = tf.data.Dataset.range(42)
>>> print(tf.data.experimental.cardinality(dataset).numpy())
42
>>> dataset = dataset.repeat()
>>> cardinality = tf.data.experimental.cardinality(dataset)
>>> print((cardinality == tf.data.experimental.INFINITE_CARDINALITY).numpy())
True
>>> dataset = dataset.filter(lambda x: True)
>>> cardinality = tf.data.experimental.cardinality(dataset)
>>> print((cardinality == tf.data.experimental.UNKNOWN_CARDINALITY).numpy())
True
```

| Args | |

|  |  |
| --- | --- |
| `dataset` | A [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) for which to determine cardinality. |

| Returns | |
| A scalar [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64) `Tensor` representing the cardinality of `dataset`. If the cardinality is infinite or unknown, the operation returns the named constant `INFINITE_CARDINALITY` and `UNKNOWN_CARDINALITY` respectively. | |