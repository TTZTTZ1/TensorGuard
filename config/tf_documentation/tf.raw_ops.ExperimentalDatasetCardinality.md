# tf.raw_ops.ExperimentalDatasetCardinality

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ExperimentalDatasetCardinality](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ExperimentalDatasetCardinality)

---

Returns the cardinality of `input_dataset`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ExperimentalDatasetCardinality`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ExperimentalDatasetCardinality)

```
tf.raw_ops.ExperimentalDatasetCardinality(
    input_dataset, name=None
)
```

Returns the cardinality of `input_dataset`.

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. A variant tensor representing the dataset to return cardinality for. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int64`. | |