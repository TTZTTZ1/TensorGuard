# tf.timestamp

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/timestamp](https://tensorflow.google.cn/api_docs/python/tf/timestamp)

---

Provides the time since epoch in seconds.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.timestamp`](https://tensorflow.google.cn/api_docs/python/tf/timestamp)

```
tf.timestamp(
    name=None
) -> Annotated[Any, _atypes.Float64]
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Random noise generation in TFF](https://tensorflow.google.cn/federated/tutorials/random_noise_generation) |

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