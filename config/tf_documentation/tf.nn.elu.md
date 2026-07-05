# tf.nn.elu

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/elu](https://tensorflow.google.cn/api_docs/python/tf/nn/elu)

---

Computes the exponential linear function.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.nn.elu`](https://tensorflow.google.cn/api_docs/python/tf/nn/elu)

```
tf.nn.elu(
    features: Annotated[Any, TV_Elu_T], name=None
) -> Annotated[Any, TV_Elu_T]
```

The ELU function is defined as:

* \( e ^ x - 1 \) if \( x < 0 \)
* \( x \) if \( x >= 0 \)

#### Examples:

```
>>> tf.nn.elu(1.0)
<tf.Tensor: shape=(), dtype=float32, numpy=1.0>
>>> tf.nn.elu(0.0)
<tf.Tensor: shape=(), dtype=float32, numpy=0.0>
>>> tf.nn.elu(-1000.0)
<tf.Tensor: shape=(), dtype=float32, numpy=-1.0>
```

See [Fast and Accurate Deep Network Learning by Exponential Linear Units (ELUs)](http://arxiv.org/abs/1511.07289)

| Args | |

|  |  |
| --- | --- |
| `features` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `features`. | |