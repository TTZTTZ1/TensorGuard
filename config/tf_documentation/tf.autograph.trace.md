# tf.autograph.trace

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/autograph/trace](https://tensorflow.google.cn/api_docs/python/tf/autograph/trace)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/autograph/utils/ag_logging.py#L87-L107) |

Traces argument information at compilation time.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.autograph.trace`](https://tensorflow.google.cn/api_docs/python/tf/autograph/trace)

```
tf.autograph.trace(
    *args
)
```

`trace` is useful when debugging, and it always executes during the tracing
phase, that is, when the TF graph is constructed.

*Example usage*

```
import tensorflow as tf

for i in tf.range(10):
  tf.autograph.trace(i)
# Output: <Tensor ...>
```

| Args | |

|  |  |
| --- | --- |
| `*args` | Arguments to print to `sys.stdout`. |