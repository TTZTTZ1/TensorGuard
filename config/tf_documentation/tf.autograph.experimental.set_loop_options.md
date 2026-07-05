# tf.autograph.experimental.set_loop_options

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/autograph/experimental/set_loop_options](https://tensorflow.google.cn/api_docs/python/tf/autograph/experimental/set_loop_options)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/autograph/lang/directives.py#L45-L94) |

Specifies additional arguments to be passed to the enclosing while\_loop.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.autograph.experimental.set_loop_options`](https://tensorflow.google.cn/api_docs/python/tf/autograph/experimental/set_loop_options)

```
tf.autograph.experimental.set_loop_options(
    parallel_iterations=UNSPECIFIED,
    swap_memory=UNSPECIFIED,
    maximum_iterations=UNSPECIFIED,
    shape_invariants=UNSPECIFIED
)
```

The parameters apply to and only to the immediately enclosing loop. It only
has effect if the loop is staged as a TF while\_loop; otherwise the parameters
have no effect.

| Usage | |
|  | |

```
>>> @tf.function(autograph=True)
... def f():
...   n = 0
...   for i in tf.range(10):
...     tf.autograph.experimental.set_loop_options(maximum_iterations=3)
...     n += 1
...   return n
```

```
>>> @tf.function(autograph=True)
... def f():
...   v = tf.constant((0,))
...   for i in tf.range(3):
...     tf.autograph.experimental.set_loop_options(
...         shape_invariants=[(v, tf.TensorShape([None]))]
...     )
...     v = tf.concat((v, [i]), 0)
...   return v
```

Also see tf.while\_loop.

| Args | |

|  |  |
| --- | --- |
| `parallel_iterations` | The maximum number of iterations allowed to run in parallel at any given time. Note that this does not guarantee parallel execution. |
| `swap_memory` | Whether to store intermediate values needed for gradients on the CPU instead of GPU. |
| `maximum_iterations` | Allows limiting the total number of iterations executed by the loop. |
| `shape_invariants` | Allows controlling the argument with the same name passed to tf.while\_loop. Unlike tf.while\_loop, this is a list of `(tensor, shape)` pairs. |