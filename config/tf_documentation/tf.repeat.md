# tf.repeat

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/repeat](https://tensorflow.google.cn/api_docs/python/tf/repeat)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L6592-L6643) |

Repeat elements of `input`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.repeat`](https://tensorflow.google.cn/api_docs/python/tf/repeat)

```
tf.repeat(
    input, repeats, axis=None, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Transfer learning with YAMNet for environmental sound classification](https://tensorflow.google.cn/tutorials/audio/transfer_learning_audio) * [Parametrized Quantum Circuits for Reinforcement Learning](https://tensorflow.google.cn/quantum/tutorials/quantum_reinforcement_learning) * [Recommend movies for users with TensorFlow Ranking](https://tensorflow.google.cn/ranking/tutorials/quickstart) * [Listwise ranking](https://tensorflow.google.cn/recommenders/examples/listwise_ranking) |

See also [`tf.concat`](https://tensorflow.google.cn/api_docs/python/tf/concat), [`tf.stack`](https://tensorflow.google.cn/api_docs/python/tf/stack), [`tf.tile`](https://tensorflow.google.cn/api_docs/python/tf/tile).

| Args | |

|  |  |
| --- | --- |
| `input` | An `N`-dimensional Tensor. |
| `repeats` | An 1-D `int` Tensor. The number of repetitions for each element. repeats is broadcasted to fit the shape of the given axis. `len(repeats)` must equal `input.shape[axis]` if axis is not None. |
| `axis` | An int. The axis along which to repeat values. By default, (axis=None), use the flattened input array, and return a flat output array. |
| `name` | A name for the operation. |

| Returns | |
| A Tensor which has the same shape as `input`, except along the given axis. If axis is None then the output array is flattened to match the flattened input array. | |

#### Example usage:

```
>>> repeat(['a', 'b', 'c'], repeats=[3, 0, 2], axis=0)
<tf.Tensor: shape=(5,), dtype=string,
numpy=array([b'a', b'a', b'a', b'c', b'c'], dtype=object)>
```

```
>>> repeat([[1, 2], [3, 4]], repeats=[2, 3], axis=0)
<tf.Tensor: shape=(5, 2), dtype=int32, numpy=
array([[1, 2],
       [1, 2],
       [3, 4],
       [3, 4],
       [3, 4]], dtype=int32)>
```

```
>>> repeat([[1, 2], [3, 4]], repeats=[2, 3], axis=1)
<tf.Tensor: shape=(2, 5), dtype=int32, numpy=
array([[1, 1, 2, 2, 2],
       [3, 3, 4, 4, 4]], dtype=int32)>
```

```
>>> repeat(3, repeats=4)
<tf.Tensor: shape=(4,), dtype=int32, numpy=array([3, 3, 3, 3], dtype=int32)>
```

```
>>> repeat([[1,2], [3,4]], repeats=2)
<tf.Tensor: shape=(8,), dtype=int32,
numpy=array([1, 1, 2, 2, 3, 3, 4, 4], dtype=int32)>
```