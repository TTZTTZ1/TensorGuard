# tf.raw_ops.DatasetCardinality

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DatasetCardinality](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DatasetCardinality)

---

Returns the cardinality of `input_dataset`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.DatasetCardinality`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DatasetCardinality)

```
tf.raw_ops.DatasetCardinality(
    input_dataset, cardinality_options='', name=None
)
```

Returns the cardinality of `input_dataset`.

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. A variant tensor representing the dataset to return cardinality for. |
| `cardinality_options` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int64`. | |