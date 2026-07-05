# tf.data.experimental.AutotuneOptions

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/AutotuneOptions](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/AutotuneOptions)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/options.py#L193-L259) |

Represents options for autotuning dataset performance.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.AutotuneOptions`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/AutotuneOptions)

```
tf.data.experimental.AutotuneOptions()
```

```
options = tf.data.Options()
options.autotune.enabled = False
dataset = dataset.with_options(options)
```

| Attributes | |

|  |  |
| --- | --- |
| `autotune_algorithm` | When autotuning is enabled (through `autotune`), determines the algorithm to use. |
| `cpu_budget` | When autotuning is enabled (through `autotune`), determines the CPU budget to use. Values greater than the number of schedulable CPU cores are allowed but may result in CPU contention. If None, defaults to the number of schedulable CPU cores. |
| `enabled` | Whether to automatically tune performance knobs. If None, defaults to True. |
| `ram_budget` | When autotuning is enabled (through `autotune`), determines the RAM budget to use. Values greater than the available RAM in bytes may result in OOM. If None, defaults to half of the available RAM in bytes. |

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