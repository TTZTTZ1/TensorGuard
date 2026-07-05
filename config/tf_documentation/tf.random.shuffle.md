# tf.random.shuffle

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/random/shuffle](https://tensorflow.google.cn/api_docs/python/tf/random/shuffle)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/random_ops.py#L326-L356) |

Randomly shuffles a tensor along its first dimension.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.random.shuffle`](https://tensorflow.google.cn/api_docs/python/tf/random/shuffle), [`tf.compat.v1.random_shuffle`](https://tensorflow.google.cn/api_docs/python/tf/random/shuffle)

```
tf.random.shuffle(
    value, seed=None, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Quickstart for the TensorFlow Core APIs](https://tensorflow.google.cn/guide/core/quickstart_core) | * [Generalized Linear Models](https://tensorflow.google.cn/probability/examples/Generalized_Linear_Models) |

The tensor is shuffled along dimension 0, such that each `value[j]` is mapped
to one and only one `output[i]`. For example, a mapping that might occur for a
3x2 tensor is:

```
[[1, 2],       [[5, 6],
 [3, 4],  ==>   [1, 2],
 [5, 6]]        [3, 4]]
```

| Args | |

|  |  |
| --- | --- |
| `value` | A Tensor to be shuffled. |
| `seed` | A Python integer. Used to create a random seed for the distribution. See [`tf.random.set_seed`](https://tensorflow.google.cn/api_docs/python/tf/random/set_seed) for behavior. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tensor of same shape and type as `value`, shuffled along its first dimension. | |