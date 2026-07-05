# tf.AggregationMethod

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/AggregationMethod](https://tensorflow.google.cn/api_docs/python/tf/AggregationMethod)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/gradients_util.py#L943-L987) |

A class listing aggregation methods used to combine gradients.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.AggregationMethod`](https://tensorflow.google.cn/api_docs/python/tf/AggregationMethod)

Computing partial derivatives can require aggregating gradient
contributions. This class lists the various methods that can
be used to combine gradients in the graph.

The following aggregation methods are part of the stable API for
aggregating gradients:

* `ADD_N`: All of the gradient terms are summed as part of one
  operation using the "AddN" op (see [`tf.add_n`](https://tensorflow.google.cn/api_docs/python/tf/math/add_n)). This
  method has the property that all gradients must be ready and
  buffered separately in memory before any aggregation is performed.
* `DEFAULT`: The system-chosen default aggregation method.

The following aggregation methods are experimental and may not
be supported in future releases:

* `EXPERIMENTAL_TREE`: Gradient terms are summed in pairs using
  the "AddN" op. This method of summing gradients may reduce
  performance, but it can improve memory utilization because the
  gradients can be released earlier.
* `EXPERIMENTAL_ACCUMULATE_N`: Same as `EXPERIMENTAL_TREE`.

Example usage when computing gradient:

```
>>> @tf.function
... def example():
...   x = tf.constant(1.0)
...   y = x * 2.0
...   z = y + y + y + y
...   return tf.gradients(z, [x, y],
...     aggregation_method=tf.AggregationMethod.EXPERIMENTAL_ACCUMULATE_N)
>>> example()
[<tf.Tensor: shape=(), dtype=float32, numpy=8.0>,
 <tf.Tensor: shape=(), dtype=float32, numpy=4.0>]
```

| Class Variables | |

|  |  |
| --- | --- |
| ADD\_N | `0` |
| DEFAULT | `0` |
| EXPERIMENTAL\_ACCUMULATE\_N | `2` |
| EXPERIMENTAL\_TREE | `1` |