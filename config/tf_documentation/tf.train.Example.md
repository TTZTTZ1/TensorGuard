# tf.train.Example

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/train/Example](https://tensorflow.google.cn/api_docs/python/tf/train/Example)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/core/example/example.proto) |

An `Example` is a standard proto storing data for training and inference.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.train.Example`](https://tensorflow.google.cn/api_docs/python/tf/train/Example)

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [tf.data: Build TensorFlow input pipelines](https://tensorflow.google.cn/guide/data) * [Estimators](https://tensorflow.google.cn/guide/estimator) * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) | * [TFRecord and tf.train.Example](https://tensorflow.google.cn/tutorials/load_data/tfrecord) * [Graph-based Neural Structured Learning in TFX](https://tensorflow.google.cn/tfx/tutorials/tfx/neural_structured_learning) * [TensorFlow Ranking Keras pipeline for distributed training](https://tensorflow.google.cn/ranking/tutorials/ranking_dnn_distributed) * [FaceSSD Fairness Indicators Example Colab](https://tensorflow.google.cn/responsible_ai/fairness_indicators/tutorials/Facessd_Fairness_Indicators_Example_Colab) * [Graph regularization for sentiment classification using synthesized graphs](https://tensorflow.google.cn/neural_structured_learning/tutorials/graph_keras_lstm_imdb) |

An `Example` proto is a representation of the following python type:

```
Dict[str,
     Union[List[bytes],
           List[int64],
           List[float]]]
```

It contains a key-value store [`Example.features`](https://tensorflow.google.cn/api_docs/python/tf/train/Example#features) where each key (string) maps
to a [`tf.train.Feature`](https://tensorflow.google.cn/api_docs/python/tf/train/Feature) message which contains a fixed-type list. This flexible
and compact format allows the storage of large amounts of typed data, but
requires that the data shape and use be determined by the configuration files
and parsers that are used to read and write this format (refer to
[`tf.io.parse_example`](https://tensorflow.google.cn/api_docs/python/tf/io/parse_example) for details).

```
>>> from google.protobuf import text_format
>>> example = text_format.Parse('''
...   features {
...     feature {key: "my_feature"
...              value {int64_list {value: [1, 2, 3, 4]} } }
...   }''',
...   tf.train.Example())
```

Use [`tf.io.parse_example`](https://tensorflow.google.cn/api_docs/python/tf/io/parse_example) to extract tensors from a serialized `Example` proto:

```
>>> tf.io.parse_example(
...     example.SerializeToString(),
...     features = {'my_feature': tf.io.RaggedFeature(dtype=tf.int64)})
{'my_feature': <tf.Tensor: shape=(4,), dtype=float32,
                           numpy=array([1, 2, 3, 4], dtype=int64)>}
```

While the list of keys, and the contents of each key *could* be different for
every `Example`, TensorFlow expects a fixed list of keys, each with a fixed
`tf.dtype`. A conformant `Example` dataset obeys the following conventions:

* If a Feature `K` exists in one example with data type `T`, it must be of
  type `T` in all other examples when present. It may be omitted.
* The number of instances of Feature `K` list data may vary across examples,
  depending on the requirements of the model.
* If a Feature `K` doesn't exist in an example, a `K`-specific default will be
  used, if configured.
* If a Feature `K` exists in an example but contains no items, the intent
  is considered to be an empty tensor and no default will be used.

| Attributes | |

|  |  |
| --- | --- |
| `features` | `Features features` |