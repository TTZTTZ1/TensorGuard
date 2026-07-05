# tf.raw_ops.Complex

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Complex](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Complex)

---

Converts two real numbers to a complex number.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Complex`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Complex)

```
tf.raw_ops.Complex(
    real,
    imag,
    Tout=tf.dtypes.complex64,
    name=None
)

tf.dtypes.complex64
```

Given a tensor `real` representing the real part of a complex number, and a
tensor `imag` representing the imaginary part of a complex number, this
operation returns complex numbers elementwise of the form \(a + bj\), where
*a* represents the `real` part and *b* represents the `imag` part.

The input tensors `real` and `imag` must have the same shape.

#### For example:

```
# tensor 'real' is [2.25, 3.25]
# tensor `imag` is [4.75, 5.75]
tf.complex(real, imag) ==> [[2.25 + 4.75j], [3.25 + 5.75j]]
```

| Args | |

|  |  |
| --- | --- |
| `real` | A `Tensor`. Must be one of the following types: `float32`, `float64`. |
| `imag` | A `Tensor`. Must have the same type as `real`. |
| `Tout` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.complex64, tf.complex128`. Defaults to [`tf.complex64`](https://tensorflow.google.cn/api_docs/python/tf#complex64). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `Tout`. | |