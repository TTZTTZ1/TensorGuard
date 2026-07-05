# tf.math.imag

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/imag](https://tensorflow.google.cn/api_docs/python/tf/math/imag)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L829-L860) |

Returns the imaginary part of a complex (or real) tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.imag`](https://tensorflow.google.cn/api_docs/python/tf/math/imag)

```
tf.math.imag(
    input, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Scalable model compression](https://tensorflow.google.cn/tutorials/optimization/compression) |

Given a tensor `input`, this operation returns a tensor of type `float` that
is the imaginary part of each element in `input` considered as a complex
number. If `input` is real, a tensor of all zeros is returned.

#### For example:

```
x = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j])
tf.math.imag(x)  # [4.75, 5.75]
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `float`, `double`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `float32` or `float64`. | |