# tf.make_ndarray

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/make_ndarray](https://tensorflow.google.cn/api_docs/python/tf/make_ndarray)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_util.py#L633-L733) |

Create a numpy ndarray from a tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.make_ndarray`](https://tensorflow.google.cn/api_docs/python/tf/make_ndarray)

```
tf.make_ndarray(
    tensor
)
```

Create a numpy ndarray with the same shape and data as the tensor.

#### For example:

```
# Tensor a has shape (2,3)
a = tf.constant([[1,2,3],[4,5,6]])
proto_tensor = tf.make_tensor_proto(a)  # convert `tensor a` to a proto tensor
tf.make_ndarray(proto_tensor) # output: array([[1, 2, 3],
#                                              [4, 5, 6]], dtype=int32)
# output has shape (2,3)
```

| Args | |

|  |  |
| --- | --- |
| `tensor` | A TensorProto. |

| Returns | |
| A numpy array with the tensor contents. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | if tensor has unsupported type. |