# tf.type_spec_from_value

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/type_spec_from_value](https://tensorflow.google.cn/api_docs/python/tf/type_spec_from_value)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/type_spec.py#L958-L1004) |

Returns a [`tf.TypeSpec`](https://tensorflow.google.cn/api_docs/python/tf/TypeSpec) that represents the given `value`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.type_spec_from_value`](https://tensorflow.google.cn/api_docs/python/tf/type_spec_from_value)

```
tf.type_spec_from_value(
    value
) -> tf.TypeSpec

tf.TypeSpec
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Extension types](https://tensorflow.google.cn/guide/extension_type) |

| Examples | |
|  | |

```
>>> tf.type_spec_from_value(tf.constant([1, 2, 3]))
TensorSpec(shape=(3,), dtype=tf.int32, name=None)
>>> tf.type_spec_from_value(np.array([4.0, 5.0], np.float64))
TensorSpec(shape=(2,), dtype=tf.float64, name=None)
>>> tf.type_spec_from_value(tf.ragged.constant([[1, 2], [3, 4, 5]]))
RaggedTensorSpec(TensorShape([2, None]), tf.int32, 1, tf.int64)
```

```
>>> example_input = tf.ragged.constant([[1, 2], [3]])
>>> @tf.function(input_signature=[tf.type_spec_from_value(example_input)])
... def f(x):
...   return tf.reduce_sum(x, axis=1)
```

| Args | |

|  |  |
| --- | --- |
| `value` | A value that can be accepted or returned by TensorFlow APIs. Accepted types for `value` include [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor), any value that can be converted to [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) using [`tf.convert_to_tensor`](https://tensorflow.google.cn/api_docs/python/tf/convert_to_tensor), and any subclass of `CompositeTensor` (such as [`tf.RaggedTensor`](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensor)). |

| Returns | |
| A `TypeSpec` that is compatible with `value`. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If a TypeSpec cannot be built for `value`, because its type is not supported. |