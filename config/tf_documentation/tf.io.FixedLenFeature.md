# tf.io.FixedLenFeature

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/io/FixedLenFeature](https://tensorflow.google.cn/api_docs/python/tf/io/FixedLenFeature)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/parsing_config.py#L298-L315) |

Configuration for parsing a fixed-length input feature.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.FixedLenFeature`](https://tensorflow.google.cn/api_docs/python/tf/io/FixedLenFeature), [`tf.compat.v1.io.FixedLenFeature`](https://tensorflow.google.cn/api_docs/python/tf/io/FixedLenFeature)

```
tf.io.FixedLenFeature(
    shape, dtype, default_value=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [tf.data: Build TensorFlow input pipelines](https://tensorflow.google.cn/guide/data) | * [TFRecord and tf.train.Example](https://tensorflow.google.cn/tutorials/load_data/tfrecord) * [Recommending movies: retrieval using a sequential model](https://tensorflow.google.cn/recommenders/examples/sequential_retrieval) * [Graph regularization for document classification using natural graphs](https://tensorflow.google.cn/neural_structured_learning/tutorials/graph_keras_mlp_cora) * [Passage Ranking using TFR-BERT](https://tensorflow.google.cn/ranking/tutorials/tfr_bert) |

To treat sparse input as dense, provide a `default_value`; otherwise,
the parse functions will fail on any examples missing this feature.

| Fields | |

|  |  |
| --- | --- |
| `shape` | Shape of input data. |
| `dtype` | Data type of input. |
| `default_value` | Value to be used if an example is missing this feature. It must be compatible with `dtype` and of the specified `shape`. |

| Attributes | |

|  |  |
| --- | --- |
| `shape` | A `namedtuple` alias for field number 0 |
| `dtype` | A `namedtuple` alias for field number 1 |
| `default_value` | A `namedtuple` alias for field number 2 |