# tf.data.experimental.copy_to_device

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/copy_to_device](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/copy_to_device)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/prefetching_ops.py#L65-L82) |

A transformation that copies dataset elements to the given `target_device`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.copy_to_device`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/copy_to_device)

```
tf.data.experimental.copy_to_device(
    target_device, source_device='/cpu:0'
)
```

| Args | |

|  |  |
| --- | --- |
| `target_device` | The name of a device to which elements will be copied. |
| `source_device` | The original device on which `input_dataset` will be placed. |

| Returns | |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#apply). | |