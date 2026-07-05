# tf.raw_ops.Timestamp

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Timestamp](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Timestamp)

---

Provides the time since epoch in seconds.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Timestamp`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Timestamp)

```
tf.raw_ops.Timestamp(
    name=None
)
```

Returns the timestamp as a `float64` for seconds since the Unix epoch.

#### Common usages include:

* Logging
* Providing a random number seed
* Debugging graph execution
* Generating timing information, mainly through comparison of timestamps

**Note:** In graph mode, the timestamp is computed when the op is executed,
not when it is added to the graph. In eager mode, the timestamp is computed
when the op is eagerly executed.

| Args | |

|  |  |
| --- | --- |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `float64`. | |