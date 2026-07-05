# tf.signal.ifftshift

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/signal/ifftshift](https://tensorflow.google.cn/api_docs/python/tf/signal/ifftshift)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/signal/fft_ops.py#L648-L690) |

The inverse of fftshift.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.signal.ifftshift`](https://tensorflow.google.cn/api_docs/python/tf/signal/ifftshift)

```
tf.signal.ifftshift(
    x, axes=None, name=None
)
```

Although identical for even-length x,
the functions differ by one sample for odd-length x.

#### For example:

```
x = tf.signal.ifftshift([[ 0.,  1.,  2.],[ 3.,  4., -4.],[-3., -2., -1.]])
x.numpy() # array([[ 4., -4.,  3.],[-2., -1., -3.],[ 1.,  2.,  0.]])
```

| Args | |

|  |  |
| --- | --- |
| `x` | `Tensor`, input tensor. |
| `axes` | `int` or shape `tuple` Axes over which to calculate. Defaults to None, which shifts all axes. |
| `name` | An optional name for the operation. |

| Returns | |
| A `Tensor`, The shifted tensor. | |

## numpy compatibility

Equivalent to numpy.fft.ifftshift.
<https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.ifftshift.html>