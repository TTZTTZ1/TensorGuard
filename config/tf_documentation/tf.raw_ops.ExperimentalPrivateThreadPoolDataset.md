# tf.raw_ops.ExperimentalPrivateThreadPoolDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ExperimentalPrivateThreadPoolDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ExperimentalPrivateThreadPoolDataset)

---

Creates a dataset that uses a custom thread pool to compute `input_dataset`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ExperimentalPrivateThreadPoolDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ExperimentalPrivateThreadPoolDataset)

```
tf.raw_ops.ExperimentalPrivateThreadPoolDataset(
    input_dataset, num_threads, output_types, output_shapes, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `num_threads` | A `Tensor` of type `int64`. Identifies the number of threads to use for the private threadpool. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |