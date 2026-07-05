# tf.math.equal

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/equal](https://tensorflow.google.cn/api_docs/python/tf/math/equal)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L1784-L1818) |

Returns the truth value of (x == y) element-wise.

#### View aliases

**Main aliases**

[`tf.equal`](https://tensorflow.google.cn/api_docs/python/tf/math/equal)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.equal`](https://tensorflow.google.cn/api_docs/python/tf/math/equal), [`tf.compat.v1.math.equal`](https://tensorflow.google.cn/api_docs/python/tf/math/equal)

```
tf.math.equal(
    x, y, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Multilayer perceptrons for digit recognition with Core APIs](https://tensorflow.google.cn/guide/core/mlp_core) * [Distributed training with Core APIs and DTensor](https://tensorflow.google.cn/guide/core/distribution) * [Extension types](https://tensorflow.google.cn/guide/extension_type) * [MinDiff Data Preparation](https://tensorflow.google.cn/responsible_ai/model_remediation/min_diff/guide/min_diff_data_preparation) | * [Tutorial on Multi Armed Bandits in TF-Agents](https://tensorflow.google.cn/agents/tutorials/bandits_tutorial) * [Classify Flowers with Transfer Learning](https://tensorflow.google.cn/hub/tutorials/image_feature_vector) * [Federated Learning for Image Classification](https://tensorflow.google.cn/federated/tutorials/federated_learning_for_image_classification) * [Sending Different Data To Particular Clients With tff.federated\_select](https://tensorflow.google.cn/federated/tutorials/federated_select) * [End to end example for BigQuery TensorFlow reader](https://tensorflow.google.cn/io/tutorials/bigquery) |

Performs a [broadcast](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) with the
arguments and then an element-wise equality comparison, returning a Tensor of
boolean values.

#### For example:

```
>>> x = tf.constant([2, 4])
>>> y = tf.constant(2)
>>> tf.math.equal(x, y)
<tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True,  False])>
```

```
>>> x = tf.constant([2, 4])
>>> y = tf.constant([2, 4])
>>> tf.math.equal(x, y)
<tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True,  True])>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor). |
| `y` | A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor). |
| `name` | A name for the operation (optional). |

| Returns | |
| A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) of type bool with the same size as that of x or y. | |

| Raises | |
| [`tf.errors.InvalidArgumentError`](https://tensorflow.google.cn/api_docs/python/tf/errors/InvalidArgumentError): If shapes of arguments are incompatible | |