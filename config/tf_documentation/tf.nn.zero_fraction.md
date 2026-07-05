# tf.nn.zero_fraction

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/zero_fraction](https://tensorflow.google.cn/api_docs/python/tf/nn/zero_fraction)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_impl.py#L620-L659) |

Returns the fraction of zeros in `value`.

#### View aliases

**Main aliases**

[`tf.nn.zero_fraction`](https://tensorflow.google.cn/api_docs/python/tf/math/zero_fraction)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.math.zero_fraction`](https://tensorflow.google.cn/api_docs/python/tf/math/zero_fraction), [`tf.compat.v1.nn.zero_fraction`](https://tensorflow.google.cn/api_docs/python/tf/math/zero_fraction)

```
tf.math.zero_fraction(
    value, name=None
)
```

If `value` is empty, the result is `nan`.

This is useful in summaries to measure and report sparsity. For example,

```
    z = tf.nn.relu(...)
    summ = tf.compat.v1.summary.scalar('sparsity', tf.nn.zero_fraction(z))
```

| Args | |

|  |  |
| --- | --- |
| `value` | A tensor of numeric type. |
| `name` | A name for the operation (optional). |

| Returns | |
| The fraction of zeros in `value`, with type `float32`. | |