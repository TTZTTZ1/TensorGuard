# tf.random.experimental.stateless_split

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/random/experimental/stateless_split](https://tensorflow.google.cn/api_docs/python/tf/random/experimental/stateless_split)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/stateless_random_ops.py#L51-L90) |

Splits an RNG seed into `num` new seeds by adding a leading axis.

#### View aliases

**Main aliases**

[`tf.random.experimental.stateless_split`](https://tensorflow.google.cn/api_docs/python/tf/random/split)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.random.experimental.stateless_split`](https://tensorflow.google.cn/api_docs/python/tf/random/split), [`tf.compat.v1.random.split`](https://tensorflow.google.cn/api_docs/python/tf/random/split)

```
tf.random.split(
    seed, num=2, alg='auto_select'
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Data augmentation](https://tensorflow.google.cn/tutorials/images/data_augmentation) |

#### Example:

```
>>> seed = [1, 2]
>>> new_seeds = tf.random.split(seed, num=3)
>>> print(new_seeds)
tf.Tensor(
[[1105988140 1738052849]
 [-335576002  370444179]
 [  10670227 -246211131]], shape=(3, 2), dtype=int32)
>>> tf.random.stateless_normal(shape=[3], seed=new_seeds[0, :])
<tf.Tensor: shape=(3,), dtype=float32, numpy=array([-0.59835213, -0.9578608 ,
0.9002807 ], dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `seed` | an RNG seed (a tensor with shape [2] and dtype `int32` or `int64`). (When using XLA, only `int32` is allowed.) |
| `num` | optional, a positive integer or scalar tensor indicating the number of seeds to produce (default 2). |
| `alg` | The RNG algorithm used to generate the random numbers. See [`tf.random.stateless_uniform`](https://tensorflow.google.cn/api_docs/python/tf/random/stateless_uniform) for a detailed explanation. |

| Returns | |
| A tensor with shape [num, 2] representing `num` new seeds. It will have the same dtype as `seed` (if `seed` doesn't have an explict dtype, the dtype will be determined by [`tf.convert_to_tensor`](https://tensorflow.google.cn/api_docs/python/tf/convert_to_tensor)). | |