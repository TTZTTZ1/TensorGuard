# tf.experimental.dlpack.to_dlpack

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/dlpack/to_dlpack](https://tensorflow.google.cn/api_docs/python/tf/experimental/dlpack/to_dlpack)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/dlpack/dlpack.py#L22-L41) |

Returns the dlpack capsule representing the tensor.

```
tf.experimental.dlpack.to_dlpack(
    tf_tensor
)
```

This operation ensures the underlying data memory is ready when returns.

```
  a = tf.tensor([1, 10])
  dlcapsule = tf.experimental.dlpack.to_dlpack(a)
  # dlcapsule represents the dlpack data structure
```

| Args | |

|  |  |
| --- | --- |
| `tf_tensor` | Tensorflow eager tensor, to be converted to dlpack capsule. |

| Returns | |
| A PyCapsule named as dltensor, which shares the underlying memory to other framework. This PyCapsule can be consumed only once. | |