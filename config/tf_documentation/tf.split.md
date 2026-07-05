# tf.split

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/split](https://tensorflow.google.cn/api_docs/python/tf/split)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L1710-L1789) |

Splits a tensor `value` into a list of sub tensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.split`](https://tensorflow.google.cn/api_docs/python/tf/split)

```
tf.split(
    value, num_or_size_splits, axis=0, num=None, name='split'
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Distributed training with Core APIs and DTensor](https://tensorflow.google.cn/guide/core/distribution) * [Understanding masking & padding](https://tensorflow.google.cn/guide/keras/understanding_masking_and_padding) | * [Using DTensors with Keras](https://tensorflow.google.cn/tutorials/distribute/dtensor_keras_tutorial) * [Distributed training with DTensors](https://tensorflow.google.cn/tutorials/distribute/dtensor_ml_tutorial) * [Convolutional Variational Autoencoder](https://tensorflow.google.cn/tutorials/generative/cvae) * [MoViNet for streaming action recognition](https://tensorflow.google.cn/hub/tutorials/movinet) * [Bayesian Modeling with Joint Distribution](https://tensorflow.google.cn/probability/examples/Modeling_with_JointDistribution) |

See also [`tf.unstack`](https://tensorflow.google.cn/api_docs/python/tf/unstack).

If `num_or_size_splits` is an `int`, then it splits `value` along the
dimension `axis` into `num_or_size_splits` smaller tensors. This requires that
`value.shape[axis]` is divisible by `num_or_size_splits`.

If `num_or_size_splits` is a 1-D Tensor (or list), then `value` is split into
`len(num_or_size_splits)` elements. The shape of the `i`-th
element has the same size as the `value` except along dimension `axis` where
the size is `num_or_size_splits[i]`.

#### For example:

```
>>> x = tf.Variable(tf.random.uniform([5, 30], -1, 1))
>>> 
>>> # Split `x` into 3 tensors along dimension 1
>>> s0, s1, s2 = tf.split(x, num_or_size_splits=3, axis=1)
>>> tf.shape(s0).numpy()
array([ 5, 10], dtype=int32)
>>> 
>>> # Split `x` into 3 tensors with sizes [4, 15, 11] along dimension 1
>>> split0, split1, split2 = tf.split(x, [4, 15, 11], 1)
>>> tf.shape(split0).numpy()
array([5, 4], dtype=int32)
>>> tf.shape(split1).numpy()
array([ 5, 15], dtype=int32)
>>> tf.shape(split2).numpy()
array([ 5, 11], dtype=int32)
```

| Args | |

|  |  |
| --- | --- |
| `value` | The `Tensor` to split. |
| `num_or_size_splits` | Either an `int` indicating the number of splits along `axis` or a 1-D integer `Tensor` or Python list containing the sizes of each output tensor along `axis`. If an `int`, then it must evenly divide `value.shape[axis]`; otherwise the sum of sizes along the split axis must match that of the `value`. |
| `axis` | An `int` or scalar `int32` `Tensor`. The dimension along which to split. Must be in the range `[-rank(value), rank(value))`. Defaults to 0. |
| `num` | Optional, an `int`, used to specify the number of outputs when it cannot be inferred from the shape of `size_splits`. |
| `name` | A name for the operation (optional). |

| Returns | |
| if `num_or_size_splits` is an `int` returns a list of `num_or_size_splits` `Tensor` objects; if `num_or_size_splits` is a 1-D list or 1-D `Tensor` returns `num_or_size_splits.get_shape[0]` `Tensor` objects resulting from splitting `value`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `num` is unspecified and cannot be inferred. |
| `ValueError` | If `num_or_size_splits` is a scalar `Tensor`. |