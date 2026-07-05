# tf.raw_ops.RandomDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RandomDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RandomDataset)

---

Creates a Dataset that returns pseudorandom numbers.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.RandomDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/RandomDataset)

```
tf.raw_ops.RandomDataset(
    seed, seed2, output_types, output_shapes, metadata='', name=None
)
```

Creates a Dataset that returns a stream of uniformly distributed
pseudorandom 64-bit signed integers.

In the TensorFlow Python API, you can instantiate this dataset via the
class [`tf.data.experimental.RandomDataset`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/RandomDataset).

Instances of this dataset are also created as a result of the
`hoist_random_uniform` static optimization. Whether this optimization is
performed is determined by the `experimental_optimization.hoist_random_uniform`
option of [`tf.data.Options`](https://tensorflow.google.cn/api_docs/python/tf/data/Options).

| Args | |

|  |  |
| --- | --- |
| `seed` | A `Tensor` of type `int64`. A scalar seed for the random number generator. If either seed or seed2 is set to be non-zero, the random number generator is seeded by the given seed. Otherwise, a random seed is used. |
| `seed2` | A `Tensor` of type `int64`. A second scalar seed to avoid seed collision. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |