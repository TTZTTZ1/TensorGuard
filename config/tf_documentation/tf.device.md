# tf.device

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/device](https://tensorflow.google.cn/api_docs/python/tf/device)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/ops.py#L4401-L4437) |

Specifies the device for ops created/executed in this context.

```
tf.device(
    device_name
) -> ContextManager[None]
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [NumPy API on TensorFlow](https://tensorflow.google.cn/guide/tf_numpy) * [Use a GPU](https://tensorflow.google.cn/guide/gpu) * [Introduction to Variables](https://tensorflow.google.cn/guide/variable) * [Random number generation](https://tensorflow.google.cn/guide/random_numbers) * [Use TPUs](https://tensorflow.google.cn/guide/tpu) | * [Customization basics: tensors and operations](https://tensorflow.google.cn/tutorials/customization/basics) * [Solve GLUE tasks using BERT on TPU](https://tensorflow.google.cn/text/tutorials/bert_glue) |

This function specifies the device to be used for ops created/executed in a
particular context. Nested contexts will inherit and also create/execute
their ops on the specified device. If a specific device is not required,
consider not using this function so that a device can be automatically
assigned. In general the use of this function is optional. `device_name` can
be fully specified, as in "/job:worker/task:1/device:cpu:0", or partially
specified, containing only a subset of the "/"-separated fields. Any fields
which are specified will override device annotations from outer scopes.

#### For example:

```
with tf.device('/job:foo'):
  # ops created here have devices with /job:foo
  with tf.device('/job:bar/task:0/device:gpu:2'):
    # ops created here have the fully specified device above
  with tf.device('/device:gpu:1'):
    # ops created here have the device '/job:foo/device:gpu:1'
```

| Args | |

|  |  |
| --- | --- |
| `device_name` | The device name to use in the context. |

| Returns | |
| A context manager that specifies the default device to use for newly created ops. | |

| Raises | |

|  |  |
| --- | --- |
| `RuntimeError` | If a function is passed in. |