# tf.nn.isotonic_regression

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/isotonic_regression](https://tensorflow.google.cn/api_docs/python/tf/nn/isotonic_regression)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_ops.py#L6617-L6689) |

Solves isotonic regression problems along the given axis.

```
tf.nn.isotonic_regression(
    inputs, decreasing=True, axis=-1
)
```

For each vector x, the problem solved is

\[\argmin\_{y\_1 >= y\_2 >= ... >= y\_n} \sum\_i (x\_i - y\_i)^2.\]

As the solution is component-wise constant, a second tensor is returned that
encodes the segments. The problems are solved over the given axis.

Consider the following example, where we solve a batch of two problems. The
first input is [3, 1, 2], while the second [1, 3, 4](/api_docs/python/tf/nn/as%20the%20axis%20is%201).

```
>>> x = tf.constant([[3, 1, 2], [1, 3, 4]], dtype=tf.float32)
>>> y, segments = tf.nn.isotonic_regression(x, axis=1)
>>> y  # The solution.
<tf.Tensor: shape=(2, 3), dtype=float32, numpy=
array([[3.       , 1.5      , 1.5      ],
       [2.6666667, 2.6666667, 2.6666667]], dtype=float32)>
```

Note that the first solution has two blocks [2] and [1.5, 1.5]. The second
solution is constant, and thus has a single segment. These segments are
exactly what the second returned tensor encodes:

```
>>> segments
<tf.Tensor: shape=(2, 3), dtype=int32, numpy=
array([[0, 1, 1],
       [0, 0, 0]], dtype=int32)>
```

| Args | |

|  |  |
| --- | --- |
| `inputs` | A tensor holding the inputs. |
| `decreasing` | If set to False, the inequalities in the optimizing constrained are flipped. |
| `axis` | The axis along which the problems should be solved. |

| Returns | |

|  |  |
| --- | --- |
| `output` | The solutions, same shape as type as the input. |
| `segments` | An int32 tensor, same shape as the input indicating the segments that have the same value. Specifically, those positions that have the same value correspond to the same segment. These values start at zero, and are monotonously increasing for each solution. |