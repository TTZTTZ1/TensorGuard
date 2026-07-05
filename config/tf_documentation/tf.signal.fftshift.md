# tf.signal.fftshift

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/signal/fftshift](https://tensorflow.google.cn/api_docs/python/tf/signal/fftshift)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/signal/fft_ops.py#L603-L645) |

Shift the zero-frequency component to the center of the spectrum.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.signal.fftshift`](https://tensorflow.google.cn/api_docs/python/tf/signal/fftshift)

```
tf.signal.fftshift(
    x, axes=None, name=None
)
```

This function swaps half-spaces for all axes listed (defaults to all).
Note that `y[0]` is the Nyquist component only if `len(x)` is even.

#### For example:

```
x = tf.signal.fftshift([ 0.,  1.,  2.,  3.,  4., -5., -4., -3., -2., -1.])
x.numpy() # array([-5., -4., -3., -2., -1.,  0.,  1.,  2.,  3.,  4.])
```

| Args | |

|  |  |
| --- | --- |
| `x` | `Tensor`, input tensor. |
| `axes` | `int` or shape `tuple`, optional Axes over which to shift. Default is None, which shifts all axes. |
| `name` | An optional name for the operation. |

| Returns | |
| A `Tensor`, The shifted tensor. | |

## numpy compatibility

Equivalent to numpy.fft.fftshift.
<https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fftshift.html>