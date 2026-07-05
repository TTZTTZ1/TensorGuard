# tf.linalg.l2_normalize

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linalg/l2_normalize](https://tensorflow.google.cn/api_docs/python/tf/linalg/l2_normalize)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_impl.py#L540-L596) |

Normalizes along dimension `axis` using an L2 norm. (deprecated arguments)

#### View aliases

**Main aliases**

[`tf.linalg.l2_normalize`](https://tensorflow.google.cn/api_docs/python/tf/math/l2_normalize), [`tf.nn.l2_normalize`](https://tensorflow.google.cn/api_docs/python/tf/math/l2_normalize)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.linalg.l2_normalize`](https://tensorflow.google.cn/api_docs/python/tf/math/l2_normalize), [`tf.compat.v1.math.l2_normalize`](https://tensorflow.google.cn/api_docs/python/tf/math/l2_normalize), [`tf.compat.v1.nn.l2_normalize`](https://tensorflow.google.cn/api_docs/python/tf/math/l2_normalize)

```
tf.math.l2_normalize(
    x, axis=None, epsilon=1e-12, name=None, dim=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Universal Sentence Encoder](https://tensorflow.google.cn/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder) * [Universal Sentence Encoder-Lite demo](https://tensorflow.google.cn/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder_lite) * [TFP Release Notes notebook (0.11.0)](https://tensorflow.google.cn/probability/examples/TFP_Release_Notebook_0_11_0) * [TFP Release Notes notebook (0.12.1)](https://tensorflow.google.cn/probability/examples/TFP_Release_Notebook_0_12_1) |

**Deprecated:** SOME ARGUMENTS ARE DEPRECATED: `(dim)`. They will be removed in a future version.
Instructions for updating:
dim is deprecated, use axis instead

For a 1-D tensor with `axis = 0`, computes

```
output = x / sqrt(max(sum(x**2), epsilon))
```

For `x` with more dimensions, independently normalizes each 1-D slice along
dimension `axis`.

1-D tensor example:

```
>>> x = tf.constant([3.0, 4.0])
>>> tf.math.l2_normalize(x).numpy()
array([0.6, 0.8], dtype=float32)
```

2-D tensor example:

```
>>> x = tf.constant([[3.0], [4.0]])
>>> tf.math.l2_normalize(x, 0).numpy()
array([[0.6],
     [0.8]], dtype=float32)
```

```
>>> x = tf.constant([[3.0], [4.0]])
>>> tf.math.l2_normalize(x, 1).numpy()
array([[1.],
     [1.]], dtype=float32)
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. |
| `axis` | Dimension along which to normalize. A scalar or a vector of integers. |
| `epsilon` | A lower bound value for the norm. Will use `sqrt(epsilon)` as the divisor if `norm < sqrt(epsilon)`. |
| `name` | A name for this operation (optional). |
| `dim` | Deprecated, do not use. |

| Returns | |
| A `Tensor` with the same shape as `x`. | |