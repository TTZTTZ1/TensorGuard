# tf.convert_to_tensor

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/convert_to_tensor](https://tensorflow.google.cn/api_docs/python/tf/convert_to_tensor)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_conversion.py#L96-L163) |

Converts the given `value` to a `Tensor`.

```
tf.convert_to_tensor(
    value, dtype=None, dtype_hint=None, name=None
) -> tf.Tensor

tf.Tensor
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Logistic regression for binary classification with Core APIs](https://tensorflow.google.cn/guide/core/logistic_regression_core) * [Extension types](https://tensorflow.google.cn/guide/extension_type) * [Matrix approximation with Core APIs](https://tensorflow.google.cn/guide/core/matrix_core) * [TensorFlow basics](https://tensorflow.google.cn/guide/basics) * [Distributed training with Core APIs and DTensor](https://tensorflow.google.cn/guide/core/distribution) | * [DeepDream](https://tensorflow.google.cn/tutorials/generative/deepdream) * [Custom training: walkthrough](https://tensorflow.google.cn/tutorials/customization/custom_training_walkthrough) * [Distributed training with DTensors](https://tensorflow.google.cn/tutorials/distribute/dtensor_ml_tutorial) * [Load a pandas DataFrame](https://tensorflow.google.cn/tutorials/load_data/pandas_dataframe) * [Scalable model compression](https://tensorflow.google.cn/tutorials/optimization/compression) |

This function converts Python objects of various types to `Tensor`
objects. It accepts `Tensor` objects, numpy arrays, Python lists,
and Python scalars.

#### For example:

```
>>> import numpy as np
>>> def my_func(arg):
...   arg = tf.convert_to_tensor(arg, dtype=tf.float32)
...   return arg
```

```
>>> # The following calls are equivalent.
... 
>>> value_1 = my_func(tf.constant([[1.0, 2.0], [3.0, 4.0]]))
>>> print(value_1)
tf.Tensor(
  [[1. 2.]
   [3. 4.]], shape=(2, 2), dtype=float32)
>>> value_2 = my_func([[1.0, 2.0], [3.0, 4.0]])
>>> print(value_2)
tf.Tensor(
  [[1. 2.]
   [3. 4.]], shape=(2, 2), dtype=float32)
>>> value_3 = my_func(np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32))
>>> print(value_3)
tf.Tensor(
  [[1. 2.]
   [3. 4.]], shape=(2, 2), dtype=float32)
```

This function can be useful when composing a new operation in Python
(such as `my_func` in the example above). All standard Python op
constructors apply this function to each of their Tensor-valued
inputs, which allows those ops to accept numpy arrays, Python lists,
and scalars in addition to `Tensor` objects.

**Note:** This function diverges from default Numpy behavior for `float` and
`string` types when `None` is present in a Python list or scalar. Rather
than silently converting `None` values, an error will be thrown.

| Args | |

|  |  |
| --- | --- |
| `value` | An object whose type has a registered `Tensor` conversion function. |
| `dtype` | Optional element type for the returned tensor. If missing, the type is inferred from the type of `value`. |
| `dtype_hint` | Optional element type for the returned tensor, used when dtype is None. In some cases, a caller may not have a dtype in mind when converting to a tensor, so dtype\_hint can be used as a soft preference. If the conversion to `dtype_hint` is not possible, this argument has no effect. |
| `name` | Optional name to use if a new `Tensor` is created. |

| Returns | |
| A `Tensor` based on `value`. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If no conversion function is registered for `value` to `dtype`. |
| `RuntimeError` | If a registered conversion function returns an invalid value. |
| `ValueError` | If the `value` is a tensor not of given `dtype` in graph mode. |