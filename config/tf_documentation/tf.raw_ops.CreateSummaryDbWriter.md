# tf.raw_ops.CreateSummaryDbWriter

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CreateSummaryDbWriter](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CreateSummaryDbWriter)

---

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CreateSummaryDbWriter`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CreateSummaryDbWriter)

```
tf.raw_ops.CreateSummaryDbWriter(
    writer, db_uri, experiment_name, run_name, user_name, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `writer` | A `Tensor` of type `resource`. |
| `db_uri` | A `Tensor` of type `string`. |
| `experiment_name` | A `Tensor` of type `string`. |
| `run_name` | A `Tensor` of type `string`. |
| `user_name` | A `Tensor` of type `string`. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |