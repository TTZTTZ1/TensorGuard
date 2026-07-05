# tf.raw_ops.SamplingDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SamplingDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SamplingDataset)

---

Creates a dataset that takes a Bernoulli sample of the contents of another dataset.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SamplingDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SamplingDataset)

```
tf.raw_ops.SamplingDataset(
    input_dataset, rate, seed, seed2, output_types, output_shapes, name=None
)
```

There is no transformation in the [`tf.data`](https://tensorflow.google.cn/api_docs/python/tf/data) Python API for creating this dataset.
Instead, it is created as a result of the `filter_with_random_uniform_fusion`
static optimization. Whether this optimization is performed is determined by the
`experimental_optimization.filter_with_random_uniform_fusion` option of
[`tf.data.Options`](https://tensorflow.google.cn/api_docs/python/tf/data/Options).

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `rate` | A `Tensor` of type `float32`. A scalar representing the sample rate. Each element of `input_dataset` is retained with this probability, independent of all other elements. |
| `seed` | A `Tensor` of type `int64`. A scalar representing seed of random number generator. |
| `seed2` | A `Tensor` of type `int64`. A scalar representing seed2 of random number generator. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |