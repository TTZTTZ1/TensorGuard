# tf.random.experimental.stateless_fold_in

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/random/experimental/stateless_fold_in](https://tensorflow.google.cn/api_docs/python/tf/random/experimental/stateless_fold_in)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/stateless_random_ops.py#L93-L132) |

Folds in data to an RNG seed to form a new RNG seed.

#### View aliases

**Main aliases**

[`tf.random.experimental.stateless_fold_in`](https://tensorflow.google.cn/api_docs/python/tf/random/fold_in)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.random.experimental.stateless_fold_in`](https://tensorflow.google.cn/api_docs/python/tf/random/fold_in), [`tf.compat.v1.random.fold_in`](https://tensorflow.google.cn/api_docs/python/tf/random/fold_in)

```
tf.random.fold_in(
    seed, data, alg='auto_select'
)
```

For example, in a distributed-training setting, suppose we have a master seed
and a replica ID. We want to fold the replica ID into the master seed to
form a "replica seed" to be used by that replica later on, so that different
replicas will generate different random numbers but the reproducibility of the
whole system can still be controlled by the master seed:

```
>>> master_seed = [1, 2]
>>> replica_id = 3
>>> replica_seed = tf.random.experimental.stateless_fold_in(
...   master_seed, replica_id)
>>> print(replica_seed)
tf.Tensor([1105988140          3], shape=(2,), dtype=int32)
>>> tf.random.stateless_normal(shape=[3], seed=replica_seed)
<tf.Tensor: shape=(3,), dtype=float32, numpy=array([0.03197195, 0.8979765 ,
0.13253039], dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `seed` | an RNG seed (a tensor with shape [2] and dtype `int32` or `int64`). (When using XLA, only `int32` is allowed.) |
| `data` | an `int32` or `int64` scalar representing data to be folded in to the seed. |
| `alg` | The RNG algorithm used to generate the random numbers. See [`tf.random.stateless_uniform`](https://tensorflow.google.cn/api_docs/python/tf/random/stateless_uniform) for a detailed explanation. |

| Returns | |
| A new RNG seed that is a deterministic function of the inputs and is statistically safe for producing a stream of new pseudo-random values. It will have the same dtype as `data` (if `data` doesn't have an explict dtype, the dtype will be determined by [`tf.convert_to_tensor`](https://tensorflow.google.cn/api_docs/python/tf/convert_to_tensor)). | |