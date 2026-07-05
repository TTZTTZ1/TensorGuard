# tf.square

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/square](https://tensorflow.google.cn/api_docs/python/tf/square)

---

Computes square of x element-wise.

#### View aliases

**Main aliases**

[`tf.square`](https://tensorflow.google.cn/api_docs/python/tf/math/square)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.square`](https://tensorflow.google.cn/api_docs/python/tf/math/square)

```
tf.math.square(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Better performance with tf.function](https://tensorflow.google.cn/guide/function) * [Basic training loops](https://tensorflow.google.cn/guide/basic_training_loops) * [TensorFlow basics](https://tensorflow.google.cn/guide/basics) * [Distributed training with Core APIs and DTensor](https://tensorflow.google.cn/guide/core/distribution) * [Multilayer perceptrons for digit recognition with Core APIs](https://tensorflow.google.cn/guide/core/mlp_core) | * [Customization basics: tensors and operations](https://tensorflow.google.cn/tutorials/customization/basics) |

I.e., \(y = x \* x = x^2\).

```
>>> tf.math.square([-2., 0., 3.])
<tf.Tensor: shape=(3,), dtype=float32, numpy=array([4., 0., 9.], dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.square(x.values, ...), x.dense_shape)`