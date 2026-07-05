# tf.raw_ops.CacheDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CacheDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CacheDataset)

---

Creates a dataset that caches elements from `input_dataset`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CacheDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CacheDataset)

```
tf.raw_ops.CacheDataset(
    input_dataset,
    filename,
    output_types,
    output_shapes,
    metadata='',
    name=None
)
```

A CacheDataset will iterate over the input\_dataset, and store tensors. If the
cache already exists, the cache will be used. If the cache is inappropriate
(e.g. cannot be opened, contains tensors of the wrong shape / size), an error
will the returned when used.

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `filename` | A `Tensor` of type `string`. A path on the filesystem where we should cache the dataset. Note: this will be a directory. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |