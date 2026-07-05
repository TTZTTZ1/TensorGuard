# tf.data.experimental.map_and_batch

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/map_and_batch](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/map_and_batch)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/batching.py#L205-L265) |

Fused implementation of `map` and `batch`. (deprecated)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.map_and_batch`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/map_and_batch)

```
tf.data.experimental.map_and_batch(
    map_func,
    batch_size,
    num_parallel_batches=None,
    drop_remainder=False,
    num_parallel_calls=None
)
```

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use [`tf.data.Dataset.map(map_func, num_parallel_calls)`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#map) followed by [`tf.data.Dataset.batch(batch_size, drop_remainder)`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#batch). Static tf.data optimizations will take care of using the fused implementation.

Maps `map_func` across `batch_size` consecutive elements of this dataset
and then combines them into a batch. Functionally, it is equivalent to `map`
followed by `batch`. This API is temporary and deprecated since input pipeline
optimization now fuses consecutive `map` and `batch` operations automatically.

| Args | |

|  |  |
| --- | --- |
| `map_func` | A function mapping a nested structure of tensors to another nested structure of tensors. |
| `batch_size` | A [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64) scalar [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor), representing the number of consecutive elements of this dataset to combine in a single batch. |
| `num_parallel_batches` | (Optional.) A [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64) scalar [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor), representing the number of batches to create in parallel. On one hand, higher values can help mitigate the effect of stragglers. On the other hand, higher values can increase contention if CPU is scarce. |
| `drop_remainder` | (Optional.) A [`tf.bool`](https://tensorflow.google.cn/api_docs/python/tf#bool) scalar [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor), representing whether the last batch should be dropped in case its size is smaller than desired; the default behavior is not to drop the smaller batch. |
| `num_parallel_calls` | (Optional.) A [`tf.int32`](https://tensorflow.google.cn/api_docs/python/tf#int32) scalar [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor), representing the number of elements to process in parallel. If not specified, `batch_size * num_parallel_batches` elements will be processed in parallel. If the value [`tf.data.AUTOTUNE`](https://tensorflow.google.cn/api_docs/python/tf/data#AUTOTUNE) is used, then the number of parallel calls is set dynamically based on available CPU. |

| Returns | |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#apply). | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If both `num_parallel_batches` and `num_parallel_calls` are specified. |