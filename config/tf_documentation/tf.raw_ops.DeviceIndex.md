# tf.raw_ops.DeviceIndex

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DeviceIndex](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DeviceIndex)

---

Return the index of device the op runs.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.DeviceIndex`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DeviceIndex)

```
tf.raw_ops.DeviceIndex(
    device_names, name=None
)
```

Given a list of device names, this operation returns the index of the device
this op runs. The length of the list is returned in two cases:
(1) Device does not exist in the given device list.
(2) It is in XLA compilation.

| Args | |

|  |  |
| --- | --- |
| `device_names` | A list of `strings`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int32`. | |