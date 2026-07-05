# tf.io.parse_single_example

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/io/parse_single_example](https://tensorflow.google.cn/api_docs/python/tf/io/parse_single_example)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/parsing_ops.py#L405-L444) |

Parses a single `Example` proto.

```
tf.io.parse_single_example(
    serialized, features, example_names=None, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [TFRecord and tf.train.Example](https://tensorflow.google.cn/tutorials/load_data/tfrecord) * [Introduction to Fairness Indicators](https://tensorflow.google.cn/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_Example_Colab) * [Graph regularization for sentiment classification using synthesized graphs](https://tensorflow.google.cn/neural_structured_learning/tutorials/graph_keras_lstm_imdb) * [Graph regularization for document classification using natural graphs](https://tensorflow.google.cn/neural_structured_learning/tutorials/graph_keras_mlp_cora) * [Recommending movies: retrieval using a sequential model](https://tensorflow.google.cn/recommenders/examples/sequential_retrieval) |

Similar to `parse_example`, except:

For dense tensors, the returned `Tensor` is identical to the output of
`parse_example`, except there is no batch dimension, the output shape is the
same as the shape given in `dense_shape`.

For `SparseTensor`s, the first (batch) column of the indices matrix is removed
(the indices matrix is a column vector), the values vector is unchanged, and
the first (`batch_size`) entry of the shape vector is removed (it is now a
single element vector).

One might see performance advantages by batching `Example` protos with
`parse_example` instead of using this function directly.

| Args | |

|  |  |
| --- | --- |
| `serialized` | A scalar string Tensor, a single serialized Example. |
| `features` | A mapping of feature keys to `FixedLenFeature` or `VarLenFeature` values. |
| `example_names` | (Optional) A scalar string Tensor, the associated name. |
| `name` | A name for this operation (optional). |

| Returns | |
| A `dict` mapping feature keys to `Tensor` and `SparseTensor` values. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if any feature is invalid. |