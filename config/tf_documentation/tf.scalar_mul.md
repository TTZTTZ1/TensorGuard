# tf.scalar_mul

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/scalar_mul](https://tensorflow.google.cn/api_docs/python/tf/scalar_mul)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L654-L660) |

Multiplies a scalar times a `Tensor` or `IndexedSlices` object.

#### View aliases

**Main aliases**

[`tf.scalar_mul`](https://tensorflow.google.cn/api_docs/python/tf/math/scalar_mul)

```
tf.math.scalar_mul(
    scalar, x, name=None
)
```

This is a special case of [`tf.math.multiply`](https://tensorflow.google.cn/api_docs/python/tf/math/multiply), where the first value must be a
`scalar`. Unlike the general form of [`tf.math.multiply`](https://tensorflow.google.cn/api_docs/python/tf/math/multiply), this is operation is
guaranteed to be efficient for [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices).

```
>>> x = tf.reshape(tf.range(30, dtype=tf.float32), [10, 3])
>>> with tf.GradientTape() as g:
...   g.watch(x)
...   y = tf.gather(x, [1, 2])  # IndexedSlices
...   z = tf.math.scalar_mul(10.0, y)
```

| Args | |

|  |  |
| --- | --- |
| `scalar` | A 0-D scalar `Tensor`. Must have known shape. |
| `x` | A `Tensor` or `IndexedSlices` to be scaled. |
| `name` | A name for the operation (optional). |

| Returns | |
| `scalar * x` of the same type (`Tensor` or `IndexedSlices`) as `x`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if scalar is not a 0-D `scalar`. |