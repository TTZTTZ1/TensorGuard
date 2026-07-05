# tf.data.experimental.to_variant

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/to_variant](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/to_variant)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/dataset_ops.py#L4519-L4529) |

Returns a variant representing the given dataset.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.to_variant`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/to_variant)

```
tf.data.experimental.to_variant(
    dataset: tf.data.Dataset
)

tf.data.Dataset
```

| Args | |

|  |  |
| --- | --- |
| `dataset` | A [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset). |

| Returns | |
| A scalar [`tf.variant`](https://tensorflow.google.cn/api_docs/python/tf#variant) tensor representing the given dataset. | |