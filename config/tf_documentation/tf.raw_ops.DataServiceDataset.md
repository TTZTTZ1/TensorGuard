# tf.raw_ops.DataServiceDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DataServiceDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DataServiceDataset)

---

Creates a dataset that reads data from the tf.data service.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.DataServiceDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DataServiceDataset)

```
tf.raw_ops.DataServiceDataset(
    dataset_id,
    processing_mode,
    address,
    protocol,
    job_name,
    max_outstanding_requests,
    iteration_counter,
    output_types,
    output_shapes,
    task_refresh_interval_hint_ms=-1,
    data_transfer_protocol='',
    target_workers='AUTO',
    cross_trainer_cache_options='',
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `dataset_id` | A `Tensor` of type `int64`. |
| `processing_mode` | A `Tensor` of type `string`. |
| `address` | A `Tensor` of type `string`. |
| `protocol` | A `Tensor` of type `string`. |
| `job_name` | A `Tensor` of type `string`. |
| `max_outstanding_requests` | A `Tensor` of type `int64`. |
| `iteration_counter` | A `Tensor` of type `resource`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `task_refresh_interval_hint_ms` | An optional `int`. Defaults to `-1`. |
| `data_transfer_protocol` | An optional `string`. Defaults to `""`. |
| `target_workers` | An optional `string`. Defaults to `"AUTO"`. |
| `cross_trainer_cache_options` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |