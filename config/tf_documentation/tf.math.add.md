# tf.math.add

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/add](https://tensorflow.google.cn/api_docs/python/tf/math/add)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L3835-L3913) |

Returns x + y element-wise.

#### View aliases

**Main aliases**

[`tf.add`](https://tensorflow.google.cn/api_docs/python/tf/math/add)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.add`](https://tensorflow.google.cn/api_docs/python/tf/math/add)

```
tf.math.add(
    x, y, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [TF-NumPy Type Promotion](https://tensorflow.google.cn/guide/tf_numpy_type_promotion) * [Distributed training with Core APIs and DTensor](https://tensorflow.google.cn/guide/core/distribution) * [Logistic regression for binary classification with Core APIs](https://tensorflow.google.cn/guide/core/logistic_regression_core) * [Multilayer perceptrons for digit recognition with Core APIs](https://tensorflow.google.cn/guide/core/mlp_core) * [Quickstart for the TensorFlow Core APIs](https://tensorflow.google.cn/guide/core/quickstart_core) | * [Customization basics: tensors and operations](https://tensorflow.google.cn/tutorials/customization/basics) * [Introduction to Fairness Indicators](https://tensorflow.google.cn/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_Example_Colab) * [Building Your Own Federated Learning Algorithm](https://tensorflow.google.cn/federated/tutorials/building_your_own_federated_learning_algorithm) * [Custom Federated Algorithms, Part 1: Introduction to the Federated Core](https://tensorflow.google.cn/federated/tutorials/custom_federated_algorithms_1) * [Client-efficient large-model federated learning via `federated\_select` and sparse aggregation](https://tensorflow.google.cn/federated/tutorials/sparse_federated_learning) |

Example usages below.

Add a scalar and a list:

```
>>> x = [1, 2, 3, 4, 5]
>>> y = 1
>>> tf.add(x, y)
<tf.Tensor: shape=(5,), dtype=int32, numpy=array([2, 3, 4, 5, 6],
dtype=int32)>
```

Note that binary `+` operator can be used instead:

```
>>> x = tf.convert_to_tensor([1, 2, 3, 4, 5])
>>> y = tf.convert_to_tensor(1)
>>> x + y
<tf.Tensor: shape=(5,), dtype=int32, numpy=array([2, 3, 4, 5, 6],
dtype=int32)>
```

Add a tensor and a list of same shape:

```
>>> x = [1, 2, 3, 4, 5]
>>> y = tf.constant([1, 2, 3, 4, 5])
>>> tf.add(x, y)
<tf.Tensor: shape=(5,), dtype=int32,
numpy=array([ 2,  4,  6,  8, 10], dtype=int32)>
```

**Warning:** If one of the inputs (`x` or `y`) is a tensor and the other is a
non-tensor, the non-tensor input will adopt (or get casted to) the data type
of the tensor input. This can potentially cause unwanted overflow or underflow
conversion.

For example,

```
>>> x = tf.constant([1, 2], dtype=tf.int8)
>>> y = [2**7 + 1, 2**7 + 2]
>>> tf.add(x, y)
<tf.Tensor: shape=(2,), dtype=int8, numpy=array([-126, -124], dtype=int8)>
```

When adding two input values of different shapes, `Add` follows NumPy
broadcasting rules. The two input array shapes are compared element-wise.
Starting with the trailing dimensions, the two dimensions either have to be
equal or one of them needs to be `1`.

For example,

```
>>> x = np.ones(6).reshape(1, 2, 1, 3)
>>> y = np.ones(6).reshape(2, 1, 3, 1)
>>> tf.add(x, y).shape.as_list()
[2, 2, 3, 3]
```

Another example with two arrays of different dimension.

```
>>> x = np.ones([1, 2, 1, 4])
>>> y = np.ones([3, 4])
>>> tf.add(x, y).shape.as_list()
[1, 2, 3, 4]
```

The reduction version of this elementwise operation is [`tf.math.reduce_sum`](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_sum)

| Args | |

|  |  |
| --- | --- |
| `x` | A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor). Must be one of the following types: bfloat16, half, float16, float32, float64, uint8, uint16, uint32, uint64, int8, int16, int32, int64, complex64, complex128, string. |
| `y` | A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor). Must have the same type as x. |
| `name` | A name for the operation (optional) |