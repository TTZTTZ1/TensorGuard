# tf.multiply

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/multiply](https://tensorflow.google.cn/api_docs/python/tf/multiply)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L475-L524) |

Returns an element-wise x \* y.

#### View aliases

**Main aliases**

[`tf.multiply`](https://tensorflow.google.cn/api_docs/python/tf/math/multiply)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.multiply`](https://tensorflow.google.cn/api_docs/python/tf/math/multiply)

```
tf.math.multiply(
    x, y, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Introduction to Tensors](https://tensorflow.google.cn/guide/tensor) * [Migrate the SavedModel workflow](https://tensorflow.google.cn/guide/migrate/saved_model) * [Training & evaluation with the built-in methods](https://tensorflow.google.cn/guide/keras/training_with_built_in_methods) | * [Customization basics: tensors and operations](https://tensorflow.google.cn/tutorials/customization/basics) * [Parametrized Quantum Circuits for Reinforcement Learning](https://tensorflow.google.cn/quantum/tutorials/quantum_reinforcement_learning) * [Universal Sentence Encoder](https://tensorflow.google.cn/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder) * [Universal Sentence Encoder-Lite demo](https://tensorflow.google.cn/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder_lite) * [TFX Estimator Component Tutorial](https://tensorflow.google.cn/tfx/tutorials/tfx/components) |

#### For example:

```
>>> x = tf.constant(([1, 2, 3, 4]))
>>> tf.math.multiply(x, x)
<tf.Tensor: shape=(4,), dtype=..., numpy=array([ 1,  4,  9, 16], dtype=int32)>
```

Since [`tf.math.multiply`](https://tensorflow.google.cn/api_docs/python/tf/math/multiply) will convert its arguments to `Tensor`s, you can also
pass in non-`Tensor` arguments:

```
>>> tf.math.multiply(7,6)
<tf.Tensor: shape=(), dtype=int32, numpy=42>
```

If `x.shape` is not the same as `y.shape`, they will be broadcast to a
compatible shape. (More about broadcasting
[here](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).)

#### For example:

```
>>> x = tf.ones([1, 2]);
>>> y = tf.ones([2, 1]);
>>> x * y  # Taking advantage of operator overriding
<tf.Tensor: shape=(2, 2), dtype=float32, numpy=
array([[1., 1.],
     [1., 1.]], dtype=float32)>
```

The reduction version of this elementwise operation is [`tf.math.reduce_prod`](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_prod)

| Args | |

|  |  |
| --- | --- |
| `x` | A Tensor. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`. |
| `y` | A `Tensor`. Must have the same type as `x`. |
| `name` | A name for the operation (optional). |

| Returns | |

A `Tensor`. Has the same type as `x`.

| Raises | |
|  | |

* InvalidArgumentError: When `x` and `y` have incompatible shapes or types.