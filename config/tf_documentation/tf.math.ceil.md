# tf.math.ceil

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/ceil](https://tensorflow.google.cn/api_docs/python/tf/math/ceil)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L5392-L5417) |

Return the ceiling of the input, element-wise.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.ceil`](https://tensorflow.google.cn/api_docs/python/tf/math/ceil)

```
tf.math.ceil(
    x, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Scalable model compression](https://tensorflow.google.cn/tutorials/optimization/compression) * [Preprocessing data with TensorFlow Transform](https://tensorflow.google.cn/tfx/tutorials/transform/census) |

#### For example:

```
>>> tf.math.ceil([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
<tf.Tensor: shape=(7,), dtype=float32,
numpy=array([-1., -1., -0.,  1.,  2.,  2.,  2.], dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor). Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. `int32` |
| `name` | A name for the operation (optional). |

| Returns | |
| A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor). Has the same type as `x`. | |

## numpy compatibility

Equivalent to np.ceil