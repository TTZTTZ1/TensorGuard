# tf.data.ThreadingOptions

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/ThreadingOptions](https://tensorflow.google.cn/api_docs/python/tf/data/ThreadingOptions)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/options.py#L462-L504) |

Represents options for dataset threading.

#### View aliases

**Main aliases**

[`tf.data.experimental.ThreadingOptions`](https://tensorflow.google.cn/api_docs/python/tf/data/ThreadingOptions)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.ThreadingOptions`](https://tensorflow.google.cn/api_docs/python/tf/data/ThreadingOptions), [`tf.compat.v1.data.experimental.ThreadingOptions`](https://tensorflow.google.cn/api_docs/python/tf/data/ThreadingOptions)

```
tf.data.ThreadingOptions()
```

You can set the threading options of a dataset through the
`threading` property of [`tf.data.Options`](https://tensorflow.google.cn/api_docs/python/tf/data/Options); the property is
an instance of [`tf.data.ThreadingOptions`](https://tensorflow.google.cn/api_docs/python/tf/data/ThreadingOptions).

```
options = tf.data.Options()
options.threading.private_threadpool_size = 10
dataset = dataset.with_options(options)
```

| Attributes | |

|  |  |
| --- | --- |
| `max_intra_op_parallelism` | If set, it overrides the maximum degree of intra-op parallelism. |
| `private_threadpool_size` | If set, the dataset will use a private threadpool of the given size. The value 0 can be used to indicate that the threadpool size should be determined at runtime based on the number of available CPU cores. |

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