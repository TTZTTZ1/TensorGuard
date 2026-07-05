# tf.tensordot

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/tensordot](https://tensorflow.google.cn/api_docs/python/tf/tensordot)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L4967-L5146) |

Tensor contraction of a and b along specified axes and outer product.

#### View aliases

**Main aliases**

[`tf.linalg.tensordot`](https://tensorflow.google.cn/api_docs/python/tf/tensordot)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.linalg.tensordot`](https://tensorflow.google.cn/api_docs/python/tf/tensordot), [`tf.compat.v1.tensordot`](https://tensorflow.google.cn/api_docs/python/tf/tensordot)

```
tf.tensordot(
    a, b, axes, name=None
)
```

Tensordot (also known as tensor contraction) sums the product of elements
from `a` and `b` over the indices specified by `axes`.

This operation corresponds to [`numpy.tensordot(a, b, axes)`](https://tensorflow.google.cn/api_docs/python/tf/keras/ops/tensordot).

Example 1: When `a` and `b` are matrices (order 2), the case `axes=1`
is equivalent to matrix multiplication.

Example 2: When `a` and `b` are matrices (order 2), the case
`axes = [[1], [0]]` is equivalent to matrix multiplication.

Example 3: When `a` and `b` are matrices (order 2), the case `axes=0` gives
the outer product, a tensor of order 4.

Example 4: Suppose that \(a\_{ijk}\) and \(b\_{lmn}\) represent two
tensors of order 3. Then, `contract(a, b, [[0], [2]])` is the order 4 tensor
\(c\_{jklm}\) whose entry
corresponding to the indices \((j,k,l,m)\) is given by:

\( c\_{jklm} = \sum\_i a\_{ijk} b\_{lmi} \).

In general, `order(c) = order(a) + order(b) - 2*len(axes[0])`.

| Args | |

|  |  |
| --- | --- |
| `a` | `Tensor` of type `float32` or `float64`. |
| `b` | `Tensor` with the same type as `a`. |
| `axes` | Either a scalar `N`, or a list or an `int32` `Tensor` of shape [2, k]. If axes is a scalar, sum over the last N axes of a and the first N axes of b in order. If axes is a list or `Tensor` the first and second row contain the set of unique integers specifying axes along which the contraction is computed, for `a` and `b`, respectively. The number of axes for `a` and `b` must be equal. If `axes=0`, computes the outer product between `a` and `b`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` with the same type as `a`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If the shapes of `a`, `b`, and `axes` are incompatible. |
| `IndexError` | If the values in axes exceed the rank of the corresponding tensor. |