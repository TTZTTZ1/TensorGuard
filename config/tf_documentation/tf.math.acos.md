# tf.math.acos

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/acos](https://tensorflow.google.cn/api_docs/python/tf/math/acos)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L5562-L5590) |

Computes acos of x element-wise.

#### View aliases

**Main aliases**

[`tf.acos`](https://tensorflow.google.cn/api_docs/python/tf/math/acos)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.acos`](https://tensorflow.google.cn/api_docs/python/tf/math/acos)

```
tf.math.acos(
    x, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Universal Sentence Encoder](https://tensorflow.google.cn/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder) * [Universal Sentence Encoder-Lite demo](https://tensorflow.google.cn/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder_lite) |

Provided an input tensor, the [`tf.math.acos`](https://tensorflow.google.cn/api_docs/python/tf/math/acos) operation
returns the inverse cosine of each element of the tensor.
If `y = tf.math.cos(x)` then, `x = tf.math.acos(y)`.

Input range is `[-1, 1]` and the output has a range of `[0, pi]`.

#### For example:

```
>>> x = tf.constant([1.0, -0.5, 3.4, 0.2, 0.0, -2], dtype = tf.float32)
>>> tf.math.acos(x)
<tf.Tensor: shape=(6,), dtype=float32,
numpy= array([0. , 2.0943952, nan, 1.3694383, 1.5707964, nan],
dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as x. | |