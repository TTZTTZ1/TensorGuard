# tf.math.lbeta

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/lbeta](https://tensorflow.google.cn/api_docs/python/tf/math/lbeta)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/special_math_ops.py#L45-L98) |

Computes \(ln(|Beta(x)|)\), reducing along the last dimension.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.lbeta`](https://tensorflow.google.cn/api_docs/python/tf/math/lbeta), [`tf.compat.v1.math.lbeta`](https://tensorflow.google.cn/api_docs/python/tf/math/lbeta)

```
tf.math.lbeta(
    x, name=None
)
```

Given one-dimensional \(z = [z\_1,...,z\_K]\), we define

\[Beta(z) = \frac{\prod\_j \Gamma(z\_j)}{\Gamma(\sum\_j z\_j)},\]

where \(\Gamma\) is the gamma function.

And for \(n + 1\) dimensional \(x\) with shape \([N\_1, ..., N\_n, K]\), we define

\[lbeta(x)[i\_1, ..., i\_n] = \log{|Beta(x[i\_1, ..., i\_n, :])|}.\]

In other words, the last dimension is treated as the \(z\) vector.

Note that if \(z = [u, v]\), then

\[Beta(z) = \frac{\Gamma(u)\Gamma(v)}{\Gamma(u + v)}
= \int\_0^1 t^{u-1} (1 - t)^{v-1} \mathrm{d}t,\]

which defines the traditional bivariate beta function.

If the last dimension is empty, we follow the convention that the sum over
the empty set is zero, and the product is one.

| Args | |

|  |  |
| --- | --- |
| `x` | A rank `n + 1` `Tensor`, `n >= 0` with type `float`, or `double`. |
| `name` | A name for the operation (optional). |

| Returns | |
| The logarithm of \(|Beta(x)|\) reducing along the last dimension. | |