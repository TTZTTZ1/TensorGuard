# tf.data.experimental.scan

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/scan](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/scan)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/scan_ops.py#L20-L45) |

A transformation that scans a function across an input dataset. (deprecated)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.scan`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/scan)

```
tf.data.experimental.scan(
    initial_state, scan_func
)
```

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `tf.data.Dataset.scan(...) instead

This transformation is a stateful relative of [`tf.data.Dataset.map`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#map).
In addition to mapping `scan_func` across the elements of the input dataset,
`scan()` accumulates one or more state tensors, whose initial values are
`initial_state`.

| Args | |

|  |  |
| --- | --- |
| `initial_state` | A nested structure of tensors, representing the initial state of the accumulator. |
| `scan_func` | A function that maps `(old_state, input_element)` to `(new_state, output_element)`. It must take two arguments and return a pair of nested structures of tensors. The `new_state` must match the structure of `initial_state`. |

| Returns | |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#apply). | |