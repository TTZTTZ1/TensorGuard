# tf.VariableAggregation

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/VariableAggregation](https://tensorflow.google.cn/api_docs/python/tf/VariableAggregation)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/variables.py#L91-L138) |

Indicates how a distributed variable will be aggregated.

[`tf.distribute.Strategy`](https://tensorflow.google.cn/api_docs/python/tf/distribute/Strategy) distributes a model by making multiple copies
(called "replicas") acting on different elements of the input batch in a
data parallel model. When performing some variable-update operation,
for example `var.assign_add(x)`, in a model, we need to resolve how to combine
the different values for `x` computed in the different replicas.

* `NONE`: This is the default, giving an error if you use a
  variable-update operation with multiple replicas.
* `SUM`: Add the updates across replicas.
* `MEAN`: Take the arithmetic mean ("average") of the updates across replicas.
* `ONLY_FIRST_REPLICA`: This is for when every replica is performing the same
  update, but we only want to perform the update once. Used, e.g., for the
  global step counter.

#### For example:

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> with strategy.scope():
...   v = tf.Variable(5.0, aggregation=tf.VariableAggregation.MEAN)
>>> @tf.function
... def update_fn():
...   return v.assign_add(1.0)
>>> strategy.run(update_fn)
PerReplica:{
  0: <tf.Tensor: shape=(), dtype=float32, numpy=6.0>,
  1: <tf.Tensor: shape=(), dtype=float32, numpy=6.0>
}
```

| Class Variables | |

|  |  |
| --- | --- |
| MEAN | `<VariableAggregationV2.MEAN: 2>` |
| NONE | `<VariableAggregationV2.NONE: 0>` |
| ONLY\_FIRST\_REPLICA | `<VariableAggregationV2.ONLY_FIRST_REPLICA: 3>` |
| SUM | `<VariableAggregationV2.SUM: 1>` |