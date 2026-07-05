# tf.sin

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/sin](https://tensorflow.google.cn/api_docs/python/tf/sin)

---

Computes sine of x element-wise.

#### View aliases

**Main aliases**

[`tf.sin`](https://tensorflow.google.cn/api_docs/python/tf/math/sin)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.sin`](https://tensorflow.google.cn/api_docs/python/tf/math/sin)

```
tf.math.sin(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Advanced automatic differentiation](https://tensorflow.google.cn/guide/advanced_autodiff) * [Introduction to gradients and automatic differentiation](https://tensorflow.google.cn/guide/autodiff) | * [TFP Release Notes notebook (0.12.1)](https://tensorflow.google.cn/probability/examples/TFP_Release_Notebook_0_12_1) |

Given an input tensor, this function computes sine of every
element in the tensor. Input range is `(-inf, inf)` and
output range is `[-1,1]`.

```
  x = tf.constant([-float("inf"), -9, -0.5, 1, 1.2, 200, 10, float("inf")])
  tf.math.sin(x) ==> [nan -0.4121185 -0.47942555 0.84147096 0.9320391 -0.87329733 -0.54402107 nan]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |