# tf.math.tanh

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/tanh](https://tensorflow.google.cn/api_docs/python/tf/math/tanh)

---

Computes hyperbolic tangent of `x` element-wise.

#### View aliases

**Main aliases**

[`tf.nn.tanh`](https://tensorflow.google.cn/api_docs/python/tf/math/tanh), [`tf.tanh`](https://tensorflow.google.cn/api_docs/python/tf/math/tanh)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.tanh`](https://tensorflow.google.cn/api_docs/python/tf/math/tanh)

```
tf.math.tanh(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Better performance with tf.function](https://tensorflow.google.cn/guide/function) |

Given an input tensor, this function computes hyperbolic tangent of every
element in the tensor. Input range is `[-inf, inf]` and
output range is `[-1,1]`.

```
>>> x = tf.constant([-float("inf"), -5, -0.5, 1, 1.2, 2, 3, float("inf")])
>>> tf.math.tanh(x)
  <tf.Tensor: shape=(8,), dtype=float32, numpy=
  array([-1.0, -0.99990916, -0.46211717,  0.7615942 ,  0.8336547 ,
          0.9640276 ,  0.9950547 ,  1.0], dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.tanh(x.values, ...), x.dense_shape)`