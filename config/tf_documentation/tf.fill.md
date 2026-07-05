# tf.fill

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/fill](https://tensorflow.google.cn/api_docs/python/tf/fill)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L204-L250) |

Creates a tensor filled with a scalar value.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.fill`](https://tensorflow.google.cn/api_docs/python/tf/fill)

```
tf.fill(
    dims, value, name=None, layout=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) * [tf.data: Build TensorFlow input pipelines](https://tensorflow.google.cn/guide/data) * [Subword tokenizers](https://tensorflow.google.cn/text/guide/subwords_tokenizer) * [Unicode strings](https://tensorflow.google.cn/text/guide/unicode) | * [Scalable model compression](https://tensorflow.google.cn/tutorials/optimization/compression) * [Multiple changepoint detection and Bayesian model selection](https://tensorflow.google.cn/probability/examples/Multiple_changepoint_detection_and_Bayesian_model_selection) * [Graph-based Neural Structured Learning in TFX](https://tensorflow.google.cn/tfx/tutorials/tfx/neural_structured_learning) * [Graph regularization for sentiment classification using synthesized graphs](https://tensorflow.google.cn/neural_structured_learning/tutorials/graph_keras_lstm_imdb) * [Bayesian Gaussian Mixture Model and Hamiltonian MCMC](https://tensorflow.google.cn/probability/examples/Bayesian_Gaussian_Mixture_Model) |

See also [`tf.ones`](https://tensorflow.google.cn/api_docs/python/tf/ones), [`tf.zeros`](https://tensorflow.google.cn/api_docs/python/tf/zeros), [`tf.one_hot`](https://tensorflow.google.cn/api_docs/python/tf/one_hot), [`tf.eye`](https://tensorflow.google.cn/api_docs/python/tf/eye).

This operation creates a tensor of shape `dims` and fills it with `value`.

#### For example:

```
>>> tf.fill([2, 3], 9)
<tf.Tensor: shape=(2, 3), dtype=int32, numpy=
array([[9, 9, 9],
       [9, 9, 9]], dtype=int32)>
```

[`tf.fill`](https://tensorflow.google.cn/api_docs/python/tf/fill) evaluates at graph runtime and supports dynamic shapes based on
other runtime `tf.Tensors`, unlike [`tf.constant(value, shape=dims)`](https://tensorflow.google.cn/api_docs/python/tf/constant), which
embeds the value as a `Const` node.

| Args | |

|  |  |
| --- | --- |
| `dims` | A 1-D sequence of non-negative numbers. Represents the shape of the output [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor). Entries should be of type: `int32`, `int64`. |
| `value` | A value to fill the returned [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor). |
| `name` | Optional string. The name of the output [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor). |
| `layout` | Optional, [`tf.experimental.dtensor.Layout`](https://tensorflow.google.cn/api_docs/python/tf/experimental/dtensor/Layout). If provided, the result is a [DTensor](https://tensorflow.google.cn/guide/dtensor_overview) with the provided layout. |

| Returns | |
| A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) with shape `dims` and the same dtype as `value`. | |

| Raises | |

|  |  |
| --- | --- |
| `InvalidArgumentError` | `dims` contains negative entries. |
| `NotFoundError` | `dims` contains non-integer entries. |

## numpy compatibility

Similar to `np.full`. In `numpy`, more parameters are supported. Passing a
number argument as the shape (`np.full(5, value)`) is valid in `numpy` for
specifying a 1-D shaped result, while TensorFlow does not support this syntax.