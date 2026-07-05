# tf.math.real

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/real](https://tensorflow.google.cn/api_docs/python/tf/math/real)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L788-L826) |

Returns the real part of a complex (or real) tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.real`](https://tensorflow.google.cn/api_docs/python/tf/math/real)

```
tf.math.real(
    input, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Scalable model compression](https://tensorflow.google.cn/tutorials/optimization/compression) * [Quantum data](https://tensorflow.google.cn/quantum/tutorials/quantum_data) |

Given a tensor `input`, this operation returns a tensor of type `float` that
is the real part of each element in `input` considered as a complex number.

#### For example:

```
x = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j])
tf.math.real(x)  # [-2.25, 3.25]
```

If `input` is already real, it is returned unchanged.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must have numeric type. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `float32` or `float64`. | |