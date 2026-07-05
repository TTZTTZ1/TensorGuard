# tf.train.Features

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/train/Features](https://tensorflow.google.cn/api_docs/python/tf/train/Features)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/core/example/feature.proto) |

Used in [`tf.train.Example`](https://tensorflow.google.cn/api_docs/python/tf/train/Example) protos. Contains the mapping from keys to `Feature`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.train.Features`](https://tensorflow.google.cn/api_docs/python/tf/train/Features)

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [TFRecord and tf.train.Example](https://tensorflow.google.cn/tutorials/load_data/tfrecord) * [Graph regularization for sentiment classification using synthesized graphs](https://tensorflow.google.cn/neural_structured_learning/tutorials/graph_keras_lstm_imdb) * [Graph-based Neural Structured Learning in TFX](https://tensorflow.google.cn/tfx/tutorials/tfx/neural_structured_learning) * [Instance Segmentation with Model Garden](https://tensorflow.google.cn/tfmodels/vision/instance_segmentation) * [Semantic Segmentation with Model Garden](https://tensorflow.google.cn/tfmodels/vision/semantic_segmentation) |

An `Example` proto is a representation of the following python type:

```
Dict[str,
     Union[List[bytes],
           List[int64],
           List[float]]]
```

This proto implements the `Dict`.

```
>>> int_feature = tf.train.Feature(
...     int64_list=tf.train.Int64List(value=[1, 2, 3, 4]))
>>> float_feature = tf.train.Feature(
...     float_list=tf.train.FloatList(value=[1., 2., 3., 4.]))
>>> bytes_feature = tf.train.Feature(
...     bytes_list=tf.train.BytesList(value=[b"abc", b"1234"]))
>>> 
>>> example = tf.train.Example(
...     features=tf.train.Features(feature={
...         'my_ints': int_feature,
...         'my_floats': float_feature,
...         'my_bytes': bytes_feature,
...     }))
```

Use [`tf.io.parse_example`](https://tensorflow.google.cn/api_docs/python/tf/io/parse_example) to extract tensors from a serialized `Example` proto:

```
>>> tf.io.parse_example(
...     example.SerializeToString(),
...     features = {
...         'my_ints': tf.io.RaggedFeature(dtype=tf.int64),
...         'my_floats': tf.io.RaggedFeature(dtype=tf.float32),
...         'my_bytes': tf.io.RaggedFeature(dtype=tf.string)})
{'my_bytes': <tf.Tensor: shape=(2,), dtype=string,
                         numpy=array([b'abc', b'1234'], dtype=object)>,
 'my_floats': <tf.Tensor: shape=(4,), dtype=float32,
                          numpy=array([1., 2., 3., 4.], dtype=float32)>,
 'my_ints': <tf.Tensor: shape=(4,), dtype=int64,
                        numpy=array([1, 2, 3, 4])>}
```

| Attributes | |

|  |  |
| --- | --- |
| `feature` | `repeated FeatureEntry feature` |

## Child Classes

[`class FeatureEntry`](https://tensorflow.google.cn/api_docs/python/tf/train/Features/FeatureEntry)