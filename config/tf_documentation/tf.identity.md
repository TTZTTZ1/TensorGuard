# tf.identity

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/identity](https://tensorflow.google.cn/api_docs/python/tf/identity)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L253-L314) |

Return a Tensor with the same shape and contents as input.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.identity`](https://tensorflow.google.cn/api_docs/python/tf/identity)

```
tf.identity(
    input, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrate LoggingTensorHook and StopAtStepHook to Keras callbacks](https://tensorflow.google.cn/guide/migrate/logging_stop_hook) | * [Substantial Undocumented Infection Facilitates the Rapid Dissemination of Novel Coronavirus (SARS-CoV2)](https://tensorflow.google.cn/probability/examples/Undocumented_Infection_and_the_Dissemination_of_SARS-CoV2) |

The return value is not the same Tensor as the original, but contains the same
values. This operation is fast when used on the same device.

#### For example:

```
>>> a = tf.constant([0.78])
>>> a_identity = tf.identity(a)
>>> a.numpy()
array([0.78], dtype=float32)
>>> a_identity.numpy()
array([0.78], dtype=float32)
```

Calling [`tf.identity`](https://tensorflow.google.cn/api_docs/python/tf/identity) on a variable will make a Tensor that represents the
value of that variable at the time it is called. This is equivalent to calling
`<variable>.read_value()`.

```
>>> a = tf.Variable(5)
>>> a_identity = tf.identity(a)
>>> a.assign_add(1)
<tf.Variable ... shape=() dtype=int32, numpy=6>
>>> a.numpy()
6
>>> a_identity.numpy()
5
```

This function can also be used to explicitly transfer tensors between devices.
For example, to transfer a tensor in GPU memory back to host memory, one can
use:

```
>>> with tf.device("/gpu:0"):
...   x_on_gpu = tf.constant(1)
>>> with tf.device("/cpu:0"):
...   x_on_cpu = tf.identity(x_on_gpu)
>>> x_on_cpu.device
'/job:localhost/replica:0/task:0/device:CPU:0'
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`, a `Variable`, a `CompositeTensor` or anything that can be converted to a tensor using [`tf.convert_to_tensor`](https://tensorflow.google.cn/api_docs/python/tf/convert_to_tensor). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` or CompositeTensor. Has the same type and contents as `input`. | |