# tf.raw_ops.Recv

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Recv](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Recv)

---

Receives the named tensor from send\_device on recv\_device.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Recv`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Recv)

```
tf.raw_ops.Recv(
    tensor_type,
    tensor_name,
    send_device,
    send_device_incarnation,
    recv_device,
    client_terminated=False,
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `tensor_type` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). |
| `tensor_name` | A `string`. The name of the tensor to receive. |
| `send_device` | A `string`. The name of the device sending the tensor. |
| `send_device_incarnation` | An `int`. The current incarnation of send\_device. |
| `recv_device` | A `string`. The name of the device receiving the tensor. |
| `client_terminated` | An optional `bool`. Defaults to `False`. If set to true, this indicates that the node was added to the graph as a result of a client-side feed or fetch of Tensor data, in which case the corresponding send or recv is expected to be managed locally by the caller. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `tensor_type`. | |