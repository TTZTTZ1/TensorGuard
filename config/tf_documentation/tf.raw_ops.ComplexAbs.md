# tf.raw_ops.ComplexAbs

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ComplexAbs](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ComplexAbs)

---

Computes the complex absolute value of a tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ComplexAbs`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ComplexAbs)

```
tf.raw_ops.ComplexAbs(
    x,
    Tout=tf.dtypes.float32,
    name=None
)

tf.dtypes.float32
```

Given a tensor `x` of complex numbers, this operation returns a tensor of type
`float` or `double` that is the absolute value of each element in `x`. All
elements in `x` must be complex numbers of the form \(a + bj\). The absolute
value is computed as \( \sqrt{a^2 + b^2}\).

#### For example:

```
>>> x = tf.complex(3.0, 4.0)
>>> print((tf.raw_ops.ComplexAbs(x=x, Tout=tf.dtypes.float32, name=None)).numpy())
5.0
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `complex64`, `complex128`. |
| `Tout` | An optional [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType) from: `tf.float32, tf.float64`. Defaults to [`tf.float32`](https://tensorflow.google.cn/api_docs/python/tf#float32). |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `Tout`. | |