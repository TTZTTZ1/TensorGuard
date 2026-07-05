# tf.data.experimental.assert_cardinality

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/assert_cardinality](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/assert_cardinality)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/cardinality.py#L67-L96) |

Asserts the cardinality of the input dataset.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.assert_cardinality`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/assert_cardinality)

```
tf.data.experimental.assert_cardinality(
    expected_cardinality
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Fine tuning models for plant disease detection](https://tensorflow.google.cn/hub/tutorials/cropnet_on_device) |

**Note:** The following assumes that "examples.tfrecord" contains 42 records.

```
>>> dataset = tf.data.TFRecordDataset("examples.tfrecord")
>>> cardinality = tf.data.experimental.cardinality(dataset)
>>> print((cardinality == tf.data.experimental.UNKNOWN_CARDINALITY).numpy())
True
>>> dataset = dataset.apply(tf.data.experimental.assert_cardinality(42))
>>> print(tf.data.experimental.cardinality(dataset).numpy())
42
```

| Args | |

|  |  |
| --- | --- |
| `expected_cardinality` | The expected cardinality of the input dataset. |

| Returns | |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#apply). | |

| Raises | |

|  |  |
| --- | --- |
| `FailedPreconditionError` | The assertion is checked at runtime (when iterating the dataset) and an error is raised if the actual and expected cardinality differ. |