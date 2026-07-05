# tf.raw_ops.BatchMatMulV3

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BatchMatMulV3](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BatchMatMulV3)

---

Multiplies slices of two tensors in batches.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.BatchMatMulV3`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/BatchMatMulV3)

```
tf.raw_ops.BatchMatMulV3(
    x, y, Tout, adj_x=False, adj_y=False, grad_x=False, grad_y=False, name=None
)
```

Multiplies all slices of `Tensor` `x` and `y` (each slice can be
viewed as an element of a batch), and arranges the individual results
in a single output tensor of the same batch size. Each of the
individual slices can optionally be adjointed (to adjoint a matrix
means to transpose and conjugate it) before multiplication by setting
the `adj_x` or `adj_y` flag to `True`, which are by default `False`.

The input tensors `x` and `y` are 2-D or higher with shape `[..., r_x, c_x]`
and `[..., r_y, c_y]`.

The output tensor is 2-D or higher with shape `[..., r_o, c_o]`, where:

```
r_o = c_x if adj_x else r_x
c_o = r_y if adj_y else c_y
```

| It is computed as | |
| output[..., :, :] = matrix(x[..., :, :]) \* matrix(y[..., :, :]) | |

**Note:** `BatchMatMulV3` supports broadcasting in the batch dimensions. More
about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`. 2-D or higher with shape `[..., r_x, c_x]`. |
| `y` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`. 2-D or higher with shape `[..., r_y, c_y]`. |
| `Tout` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.bfloat16, tf.half, tf.float32, tf.float64, tf.int16, tf.int32, tf.int64, tf.complex64, tf.complex128`. If not spcified, Tout is the same type to input type. |
| `adj_x` | An optional `bool`. Defaults to `False`. If `True`, adjoint the slices of `x`. Defaults to `False`. |
| `adj_y` | An optional `bool`. Defaults to `False`. If `True`, adjoint the slices of `y`. Defaults to `False`. |
| `grad_x` | An optional `bool`. Defaults to `False`. |
| `grad_y` | An optional `bool`. Defaults to `False`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `Tout`. | |