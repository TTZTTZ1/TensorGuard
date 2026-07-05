# tf.train.FloatList

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/train/FloatList](https://tensorflow.google.cn/api_docs/python/tf/train/FloatList)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/core/example/feature.proto) |

Used in [`tf.train.Example`](https://tensorflow.google.cn/api_docs/python/tf/train/Example) protos. Holds a list of floats.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.train.FloatList`](https://tensorflow.google.cn/api_docs/python/tf/train/FloatList)

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [TFRecord and tf.train.Example](https://tensorflow.google.cn/tutorials/load_data/tfrecord) * [Graph-based Neural Structured Learning in TFX](https://tensorflow.google.cn/tfx/tutorials/tfx/neural_structured_learning) * [Feature Engineering using TFX Pipeline and TensorFlow Transform](https://tensorflow.google.cn/tfx/tutorials/tfx/penguin_tft) * [Graph regularization for sentiment classification using synthesized graphs](https://tensorflow.google.cn/neural_structured_learning/tutorials/graph_keras_lstm_imdb) * [Preprocessing data with TensorFlow Transform](https://tensorflow.google.cn/tfx/tutorials/transform/census) |

An `Example` proto is a representation of the following python type:

```
Dict[str,
     Union[List[bytes],
           List[int64],
           List[float]]]
```

This proto implements the `List[float]` portion.

```
>>> from google.protobuf import text_format
>>> example = text_format.Parse('''
...   features {
...     feature {key: "my_feature"
...              value {float_list {value: [1., 2., 3., 4. ]} } }
...   }''',
...   tf.train.Example())
>>> 
>>> example.features.feature['my_feature'].float_list.value
[1.0, 2.0, 3.0, 4.0]
```

Use [`tf.io.parse_example`](https://tensorflow.google.cn/api_docs/python/tf/io/parse_example) to extract tensors from a serialized `Example` proto:

```
>>> tf.io.parse_example(
...     example.SerializeToString(),
...     features = {'my_feature': tf.io.RaggedFeature(dtype=tf.float32)})
{'my_feature': <tf.Tensor: shape=(4,), dtype=float32,
                           numpy=array([1., 2., 3., 4.], dtype=float32)>}
```

See the [`tf.train.Example`](https://tensorflow.google.cn/tutorials/load_data/tfrecord#tftrainexample)
guide for usage details.

| Attributes | |

|  |  |
| --- | --- |
| `value` | `repeated float value` |