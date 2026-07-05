# tf.cos

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/cos](https://tensorflow.google.cn/api_docs/python/tf/cos)

---

Computes cos of x element-wise.

#### View aliases

**Main aliases**

[`tf.cos`](https://tensorflow.google.cn/api_docs/python/tf/math/cos)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.cos`](https://tensorflow.google.cn/api_docs/python/tf/math/cos)

```
tf.math.cos(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [TFP Release Notes notebook (0.12.1)](https://tensorflow.google.cn/probability/examples/TFP_Release_Notebook_0_12_1) |

Given an input tensor, this function computes cosine of every
element in the tensor. Input range is `(-inf, inf)` and
output range is `[-1,1]`. If input lies outside the boundary, `nan`
is returned.

```
  x = tf.constant([-float("inf"), -9, -0.5, 1, 1.2, 200, 10000, float("inf")])
  tf.math.cos(x) ==> [nan -0.91113025 0.87758255 0.5403023 0.36235774 0.48718765 -0.95215535 nan]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |