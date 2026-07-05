# tf.data.experimental.OptimizationOptions

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/OptimizationOptions](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/OptimizationOptions)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/options.py#L304-L459) |

Represents options for dataset optimizations.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.OptimizationOptions`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/OptimizationOptions)

```
tf.data.experimental.OptimizationOptions()
```

You can set the optimization options of a dataset through the
`experimental_optimization` property of [`tf.data.Options`](https://tensorflow.google.cn/api_docs/python/tf/data/Options); the property is
an instance of [`tf.data.experimental.OptimizationOptions`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/OptimizationOptions).

```
options = tf.data.Options()
options.experimental_optimization.noop_elimination = True
options.experimental_optimization.apply_default_optimizations = False
dataset = dataset.with_options(options)
```

| Attributes | |

|  |  |
| --- | --- |
| `apply_default_optimizations` | Whether to apply default graph optimizations. If False, only graph optimizations that have been explicitly enabled will be applied. |
| `filter_fusion` | Whether to fuse filter transformations. If None, defaults to False. |
| `filter_parallelization` | Whether to parallelize stateless filter transformations. If None, defaults to False. |
| `inject_prefetch` | Whether to inject prefetch transformation as the last transformation when the last transformation is a synchronous transformation. If None, defaults to True. |
| `map_and_batch_fusion` | Whether to fuse map and batch transformations. If None, defaults to True. |
| `map_and_filter_fusion` | Whether to fuse map and filter transformations. If None, defaults to False. |
| `map_fusion` | Whether to fuse map transformations. If None, defaults to False. |
| `map_parallelization` | Whether to parallelize stateless map transformations. If None, defaults to True. |
| `noop_elimination` | Whether to eliminate no-op transformations. If None, defaults to True. |
| `parallel_batch` | Whether to parallelize copying of batch elements. If None, defaults to True. |
| `seq_interleave_prefetch` | Whether to replace parallel interleave using a sequential interleave that prefetches elements from its input iterators. If None, defaults to False. |
| `shuffle_and_repeat_fusion` | Whether to fuse shuffle and repeat transformations. If None, defaults to True. |

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