# tf.raw_ops.ShuffleDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShuffleDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShuffleDataset)

---

Creates a dataset that shuffles elements from `input_dataset` pseudorandomly.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ShuffleDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ShuffleDataset)

```
tf.raw_ops.ShuffleDataset(
    input_dataset,
    buffer_size,
    seed,
    seed2,
    output_types,
    output_shapes,
    reshuffle_each_iteration=True,
    metadata='',
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `buffer_size` | A `Tensor` of type `int64`. The number of output elements to buffer in an iterator over this dataset. Compare with the `min_after_dequeue` attr when creating a `RandomShuffleQueue`. |
| `seed` | A `Tensor` of type `int64`. A scalar seed for the random number generator. If either `seed` or `seed2` is set to be non-zero, the random number generator is seeded by the given seed. Otherwise, a random seed is used. |
| `seed2` | A `Tensor` of type `int64`. A second scalar seed to avoid seed collision. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `reshuffle_each_iteration` | An optional `bool`. Defaults to `True`. If true, each iterator over this dataset will be given a different pseudorandomly generated seed, based on a sequence seeded by the `seed` and `seed2` inputs. If false, each iterator will be given the same seed, and repeated iteration over this dataset will yield the exact same sequence of results. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |