# tf.VariableSynchronization

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/VariableSynchronization](https://tensorflow.google.cn/api_docs/python/tf/VariableSynchronization)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L63-L87) |

Indicates when a distributed variable will be synced.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.VariableSynchronization`](https://tensorflow.google.cn/api_docs/python/tf/VariableSynchronization)

* `AUTO`: Indicates that the synchronization will be determined by the current
  `DistributionStrategy` (eg. With `MirroredStrategy` this would be
  `ON_WRITE`).
* `NONE`: Indicates that there will only be one copy of the variable, so
  there is no need to sync.
* `ON_WRITE`: Indicates that the variable will be updated across devices
  every time it is written.
* `ON_READ`: Indicates that the variable will be aggregated across devices
  when it is read (eg. when checkpointing or when evaluating an op that uses
  the variable).

  Example:

```
>>> temp_grad=[tf.Variable([0.], trainable=False,
...                      synchronization=tf.VariableSynchronization.ON_READ,
...                      aggregation=tf.VariableAggregation.MEAN
...                      )]
```

| Class Variables | |

|  |  |
| --- | --- |
| AUTO | `<VariableSynchronization.AUTO: 0>` |
| NONE | `<VariableSynchronization.NONE: 1>` |
| ON\_READ | `<VariableSynchronization.ON_READ: 3>` |
| ON\_WRITE | `<VariableSynchronization.ON_WRITE: 2>` |