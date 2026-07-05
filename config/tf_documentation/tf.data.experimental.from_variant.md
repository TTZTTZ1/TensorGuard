# tf.data.experimental.from_variant

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/from_variant](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/from_variant)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/dataset_ops.py#L4504-L4516) |

Constructs a dataset from the given variant and (nested) structure.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.from_variant`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/from_variant)

```
tf.data.experimental.from_variant(
    variant, structure
)
```

| Args | |

|  |  |
| --- | --- |
| `variant` | A scalar [`tf.variant`](https://tensorflow.google.cn/api_docs/python/tf#variant) tensor representing a dataset. |
| `structure` | A (nested) structure of [`tf.TypeSpec`](https://tensorflow.google.cn/api_docs/python/tf/TypeSpec) objects representing the structure of each element in the dataset. |

| Returns | |
| A [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) instance. | |