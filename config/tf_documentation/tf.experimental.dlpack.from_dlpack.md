# tf.experimental.dlpack.from_dlpack

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/dlpack/from_dlpack](https://tensorflow.google.cn/api_docs/python/tf/experimental/dlpack/from_dlpack)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/dlpack/dlpack.py#L44-L63) |

Returns the Tensorflow eager tensor.

```
tf.experimental.dlpack.from_dlpack(
    dlcapsule
)
```

The returned tensor uses the memory shared by dlpack capsules from other
framework.

```
  a = tf.experimental.dlpack.from_dlpack(dlcapsule)
  # `a` uses the memory shared by dlpack
```

| Args | |

|  |  |
| --- | --- |
| `dlcapsule` | A PyCapsule named as dltensor |

| Returns | |
| A Tensorflow eager tensor | |