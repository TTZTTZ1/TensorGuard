# tf.random.experimental.create_rng_state

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/random/experimental/create_rng_state](https://tensorflow.google.cn/api_docs/python/tf/random/experimental/create_rng_state)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/stateful_random_ops.py#L174-L195) |

Creates a RNG state from an integer or a vector.

#### View aliases

**Main aliases**

[`tf.random.experimental.create_rng_state`](https://tensorflow.google.cn/api_docs/python/tf/random/create_rng_state)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.random.create_rng_state`](https://tensorflow.google.cn/api_docs/python/tf/random/create_rng_state), [`tf.compat.v1.random.experimental.create_rng_state`](https://tensorflow.google.cn/api_docs/python/tf/random/create_rng_state)

```
tf.random.create_rng_state(
    seed, alg
)
```

#### Example:

```
>>> tf.random.create_rng_state(
...     1234, "philox")
<tf.Tensor: shape=(3,), dtype=int64, numpy=array([1234,    0,    0])>
>>> tf.random.create_rng_state(
...     [12, 34], "threefry")
<tf.Tensor: shape=(2,), dtype=int64, numpy=array([12, 34])>
```

| Args | |

|  |  |
| --- | --- |
| `seed` | an integer or 1-D numpy array. |
| `alg` | the RNG algorithm. Can be a string, an `Algorithm` or an integer. |

| Returns | |
| a 1-D numpy array whose size depends on the algorithm. | |