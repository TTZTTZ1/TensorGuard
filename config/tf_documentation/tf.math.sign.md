# tf.math.sign

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/sign](https://tensorflow.google.cn/api_docs/python/tf/math/sign)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L741-L785) |

Returns an element-wise indication of the sign of a number.

#### View aliases

**Main aliases**

[`tf.sign`](https://tensorflow.google.cn/api_docs/python/tf/math/sign)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.sign`](https://tensorflow.google.cn/api_docs/python/tf/math/sign)

```
tf.math.sign(
    x, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Adversarial example using FGSM](https://tensorflow.google.cn/tutorials/generative/adversarial_fgsm) * [Tutorial on Multi Armed Bandits in TF-Agents](https://tensorflow.google.cn/agents/tutorials/bandits_tutorial) |

`y = sign(x) = -1 if x < 0; 0 if x == 0; 1 if x > 0`.

For complex numbers, `y = sign(x) = x / |x| if x != 0, otherwise y = 0`.

#### Example usage:

```
>>> # real number
>>> tf.math.sign([0., 2., -3.])
<tf.Tensor: shape=(3,), dtype=float32,
numpy=array([ 0.,  1., -1.], dtype=float32)>
```

```
>>> # complex number
>>> tf.math.sign([1 + 1j, 0 + 0j])
<tf.Tensor: shape=(2,), dtype=complex128,
numpy=array([0.70710678+0.70710678j, 0.        +0.j        ])>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A Tensor. Must be one of the following types: bfloat16, half, float32, float64, int32, int64, complex64, complex128. |
| `name` | A name for the operation (optional). |

| Returns | |
| A Tensor. Has the same type as x. | |

If x is a SparseTensor, returns SparseTensor(x.indices,
tf.math.sign(x.values, ...), x.dense\_shape).

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.sign(x.values, ...), x.dense_shape)`