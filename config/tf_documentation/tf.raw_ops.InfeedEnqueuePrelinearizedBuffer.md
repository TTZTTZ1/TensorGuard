# tf.raw_ops.InfeedEnqueuePrelinearizedBuffer

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/InfeedEnqueuePrelinearizedBuffer](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/InfeedEnqueuePrelinearizedBuffer)

---

An op which enqueues prelinearized buffer into TPU infeed.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.InfeedEnqueuePrelinearizedBuffer`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/InfeedEnqueuePrelinearizedBuffer)

```
tf.raw_ops.InfeedEnqueuePrelinearizedBuffer(
    input, device_ordinal=-1, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` of type `variant`. A variant tensor representing linearized output. |
| `device_ordinal` | An optional `int`. Defaults to `-1`. The TPU device to use. This should be -1 when the Op is running on a TPU device and = 0 when the Op is running on the CPU device. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |