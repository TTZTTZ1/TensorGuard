# tf.executing_eagerly

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/executing_eagerly](https://tensorflow.google.cn/api_docs/python/tf/executing_eagerly)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/eager/context.py#L2330-L2388) |

Checks whether the current thread has eager execution enabled.

```
tf.executing_eagerly()
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Text classification with TensorFlow Hub: Movie reviews](https://tensorflow.google.cn/tutorials/keras/text_classification_with_hub) * [Neural machine translation with attention](https://tensorflow.google.cn/text/tutorials/nmt_with_attention) * [Fast Style Transfer for Arbitrary Styles](https://tensorflow.google.cn/hub/tutorials/tf2_arbitrary_image_stylization) * [Text Classification with Movie Reviews](https://tensorflow.google.cn/hub/tutorials/tf2_text_classification) * [Graph regularization for sentiment classification using synthesized graphs](https://tensorflow.google.cn/neural_structured_learning/tutorials/graph_keras_lstm_imdb) |

Eager execution is enabled by default and this API returns `True`
in most of cases. However, this API might return `False` in the following use
cases.

* Executing inside [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function), unless under [`tf.init_scope`](https://tensorflow.google.cn/api_docs/python/tf/init_scope) or
  [`tf.config.run_functions_eagerly(True)`](https://tensorflow.google.cn/api_docs/python/tf/config/run_functions_eagerly) is previously called.
* Executing inside a transformation function for `tf.dataset`.
* [`tf.compat.v1.disable_eager_execution()`](https://tensorflow.google.cn/api_docs/python/tf/compat/v1/disable_eager_execution) is called.

#### General case:

```
>>> print(tf.executing_eagerly())
True
```

Inside [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function):

```
>>> @tf.function
... def fn():
...   with tf.init_scope():
...     print(tf.executing_eagerly())
...   print(tf.executing_eagerly())
>>> fn()
True
False
```

Inside [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) after [`tf.config.run_functions_eagerly(True)`](https://tensorflow.google.cn/api_docs/python/tf/config/run_functions_eagerly) is called:

```
>>> tf.config.run_functions_eagerly(True)
>>> @tf.function
... def fn():
...   with tf.init_scope():
...     print(tf.executing_eagerly())
...   print(tf.executing_eagerly())
>>> fn()
True
True
>>> tf.config.run_functions_eagerly(False)
```

Inside a transformation function for `tf.dataset`:

```
>>> def data_fn(x):
...   print(tf.executing_eagerly())
...   return x
>>> dataset = tf.data.Dataset.range(100)
>>> dataset = dataset.map(data_fn)
False
```

| Returns | |
| `True` if the current thread has eager execution enabled. | |