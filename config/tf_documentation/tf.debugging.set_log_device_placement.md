# tf.debugging.set_log_device_placement

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/debugging/set_log_device_placement](https://tensorflow.google.cn/api_docs/python/tf/debugging/set_log_device_placement)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/eager/context.py#L2567-L2599) |

Turns logging for device placement decisions on or off.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.debugging.set_log_device_placement`](https://tensorflow.google.cn/api_docs/python/tf/debugging/set_log_device_placement)

```
tf.debugging.set_log_device_placement(
    enabled
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Use a GPU](https://tensorflow.google.cn/guide/gpu) |

Operations execute on a particular device, producing and consuming tensors on
that device. This may change the performance of the operation or require
TensorFlow to copy data to or from an accelerator, so knowing where operations
execute is useful for debugging performance issues.

For more advanced profiling, use the [TensorFlow
profiler](https://tensorflow.google.cn/guide/profiler).

Device placement for operations is typically controlled by a [`tf.device`](https://tensorflow.google.cn/api_docs/python/tf/device)
scope, but there are exceptions, for example operations on a [`tf.Variable`](https://tensorflow.google.cn/api_docs/python/tf/Variable)
which follow the initial placement of the variable. Turning off soft device
placement (with [`tf.config.set_soft_device_placement`](https://tensorflow.google.cn/api_docs/python/tf/config/set_soft_device_placement)) provides more explicit
control.

```
>>> tf.debugging.set_log_device_placement(True)
>>> tf.ones([])
>>> # [...] op Fill in device /job:localhost/replica:0/task:0/device:GPU:0
>>> with tf.device("CPU"):
...  tf.ones([])
>>> # [...] op Fill in device /job:localhost/replica:0/task:0/device:CPU:0
>>> tf.debugging.set_log_device_placement(False)
```

Turning on [`tf.debugging.set_log_device_placement`](https://tensorflow.google.cn/api_docs/python/tf/debugging/set_log_device_placement) also logs the placement of
ops inside [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) when the function is called.

| Args | |

|  |  |
| --- | --- |
| `enabled` | Whether to enabled device placement logging. |