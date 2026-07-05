# tf.data.experimental.DistributeOptions

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/DistributeOptions](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/DistributeOptions)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/options.py#L262-L301) |

Represents options for distributed data processing.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.DistributeOptions`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/DistributeOptions)

```
tf.data.experimental.DistributeOptions()
```

You can set the distribution options of a dataset through the
`experimental_distribute` property of [`tf.data.Options`](https://tensorflow.google.cn/api_docs/python/tf/data/Options); the property is
an instance of [`tf.data.experimental.DistributeOptions`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/DistributeOptions).

```
options = tf.data.Options()
options.experimental_distribute.auto_shard_policy = tf.data.experimental.AutoShardPolicy.OFF
dataset = dataset.with_options(options)
```

| Attributes | |

|  |  |
| --- | --- |
| `auto_shard_policy` | The type of sharding to use. See [`tf.data.experimental.AutoShardPolicy`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/AutoShardPolicy) for additional information. |
| `num_devices` | The number of devices attached to this input pipeline. This will be automatically set by `MultiDeviceIterator`. |

## Methods

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/util/options.py#L38-L44)

```
__eq__(
    other
)
```

Return self==value.

### `__ne__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/util/options.py#L46-L50)

```
__ne__(
    other
)
```

Return self!=value.