# tf.data.experimental.prefetch_to_device

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/prefetch_to_device](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/prefetch_to_device)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/prefetching_ops.py#L33-L62) |

A transformation that prefetches dataset values to the given `device`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.prefetch_to_device`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/prefetch_to_device)

```
tf.data.experimental.prefetch_to_device(
    device, buffer_size=None
)
```

**Note:** Although the transformation creates a [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset), the
transformation must be the final `Dataset` in the input pipeline.

For example,

```
>>> dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])
>>> dataset = dataset.apply(tf.data.experimental.prefetch_to_device("/cpu:0"))
>>> for element in dataset:
...   print(f'Tensor {element} is on device {element.device}')
Tensor 1 is on device /job:localhost/replica:0/task:0/device:CPU:0
Tensor 2 is on device /job:localhost/replica:0/task:0/device:CPU:0
Tensor 3 is on device /job:localhost/replica:0/task:0/device:CPU:0
```

| Args | |

|  |  |
| --- | --- |
| `device` | A string. The name of a device to which elements will be prefetched. |
| `buffer_size` | (Optional.) The number of elements to buffer on `device`. Defaults to an automatically chosen value. |

| Returns | |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#apply). | |