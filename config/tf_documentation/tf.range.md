# tf.range

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/range](https://tensorflow.google.cn/api_docs/python/tf/range)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L1940-L2021) |

Creates a sequence of numbers.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.range`](https://tensorflow.google.cn/api_docs/python/tf/range)

```
tf.range(limit, delta=1, dtype=None, name='range')
tf.range(start, limit, delta=1, dtype=None, name='range')
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [DTensor concepts](https://tensorflow.google.cn/guide/dtensor_overview) * [Better performance with tf.function](https://tensorflow.google.cn/guide/function) * [Training checkpoints](https://tensorflow.google.cn/guide/checkpoint) * [Estimators](https://tensorflow.google.cn/guide/estimator) * [Optimizers with Core APIs](https://tensorflow.google.cn/guide/core/optimizers_core) | * [Integrated gradients](https://tensorflow.google.cn/tutorials/interpretability/integrated_gradients) * [DeepDream](https://tensorflow.google.cn/tutorials/generative/deepdream) * [Save and load a model using a distribution strategy](https://tensorflow.google.cn/tutorials/distribute/save_and_load) * [Playing CartPole with the Actor-Critic method](https://tensorflow.google.cn/tutorials/reinforcement_learning/actor_critic) * [Distributed Input](https://tensorflow.google.cn/tutorials/distribute/input) |

Creates a sequence of numbers that begins at `start` and extends by
increments of `delta` up to but not including `limit`.

The dtype of the resulting tensor is inferred from the inputs unless
it is provided explicitly.

Like the Python builtin `range`, `start` defaults to 0, so that
`range(n) = range(0, n)`.

#### For example:

```
>>> start = 3
>>> limit = 18
>>> delta = 3
>>> tf.range(start, limit, delta)
<tf.Tensor: shape=(5,), dtype=int32,
numpy=array([ 3,  6,  9, 12, 15], dtype=int32)>
```

```
>>> start = 3
>>> limit = 1
>>> delta = -0.5
>>> tf.range(start, limit, delta)
<tf.Tensor: shape=(4,), dtype=float32,
numpy=array([3. , 2.5, 2. , 1.5], dtype=float32)>
```

```
>>> limit = 5
>>> tf.range(limit)
<tf.Tensor: shape=(5,), dtype=int32,
numpy=array([0, 1, 2, 3, 4], dtype=int32)>
```

| Args | |

|  |  |
| --- | --- |
| `start` | A 0-D `Tensor` (scalar). Acts as first entry in the range if `limit` is not None; otherwise, acts as range limit and first entry defaults to 0. |
| `limit` | A 0-D `Tensor` (scalar). Upper limit of sequence, exclusive. If None, defaults to the value of `start` while the first entry of the range defaults to 0. |
| `delta` | A 0-D `Tensor` (scalar). Number that increments `start`. Defaults to 1. |
| `dtype` | The type of the elements of the resulting tensor. |
| `name` | A name for the operation. Defaults to "range". |

| Returns | |
| An 1-D `Tensor` of type `dtype`. | |

## numpy compatibility

Equivalent to np.arange