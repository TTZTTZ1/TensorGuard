# tf.data.Options

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/Options](https://tensorflow.google.cn/api_docs/python/tf/data/Options)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/options.py#L507-L741) |

Represents options for [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.Options`](https://tensorflow.google.cn/api_docs/python/tf/data/Options)

```
tf.data.Options()
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Distributed Input](https://tensorflow.google.cn/tutorials/distribute/input) * [Multi-worker training with Keras](https://tensorflow.google.cn/tutorials/distribute/multi_worker_with_keras) |

A [`tf.data.Options`](https://tensorflow.google.cn/api_docs/python/tf/data/Options) object can be, for instance, used to control which static
optimizations to apply to the input pipeline graph or whether to use
performance modeling to dynamically tune the parallelism of operations such as
[`tf.data.Dataset.map`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#map) or [`tf.data.Dataset.interleave`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#interleave).

The options are set for the entire dataset and are carried over to datasets
created through tf.data transformations.

The options can be set by constructing an `Options` object and using the
[`tf.data.Dataset.with_options(options)`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#with_options) transformation, which returns a
dataset with the options set.

```
>>> dataset = tf.data.Dataset.range(42)
>>> options = tf.data.Options()
>>> options.deterministic = False
>>> dataset = dataset.with_options(options)
>>> print(dataset.options().deterministic)
False
```

**Note:** A known limitation of the [`tf.data.Options`](https://tensorflow.google.cn/api_docs/python/tf/data/Options) implementation is that the
options are not preserved across tf.function boundaries. In particular, to
set options for a dataset that is iterated within a tf.function, the options
need to be set within the same tf.function.

| Attributes | |

|  |  |
| --- | --- |
| `autotune` | The autotuning options associated with the dataset. See [`tf.data.experimental.AutotuneOptions`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/AutotuneOptions) for more details. |
| `dataset_name` | A name for the dataset, to help in debugging. |
| `deterministic` | Whether the outputs need to be produced in deterministic order. If None, defaults to True. |
| `experimental_deterministic` | DEPRECATED. Use `deterministic` instead. |
| `experimental_distribute` | The distribution strategy options associated with the dataset. See [`tf.data.experimental.DistributeOptions`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/DistributeOptions) for more details. |
| `experimental_external_state_policy` | This option can be used to override the default policy for how to handle external state when serializing a dataset or checkpointing its iterator. There are three settings available - IGNORE: External state is ignored without a warning; WARN: External state is ignored and a warning is logged; FAIL: External state results in an error. |
| `experimental_optimization` | The optimization options associated with the dataset. See [`tf.data.experimental.OptimizationOptions`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/OptimizationOptions) for more details. |
| `experimental_slack` | Whether to introduce 'slack' in the last `prefetch` of the input pipeline, if it exists. This may reduce CPU contention with accelerator host-side activity at the start of a step. The slack frequency is determined by the number of devices attached to this input pipeline. If None, defaults to False. |
| `experimental_symbolic_checkpoint` | Whether to checkpoint internal input pipeline state maintaining cursors into data sources that identify last element(s) produced as output to the tf.data consumer. This is alternative to the default 'explicit' checkpointing which stores the internal input pipeline state in the checkpoint. Note that symbolic checkpointing is not supported for transformations that can reorder elements. |
| `experimental_threading` | DEPRECATED. Use `threading` instead. |
| `experimental_warm_start` | Whether to start background threads of asynchronous transformations upon iterator creation, as opposed to during the first call to `next()`. Defaults to `False`. This improves the latency of the initial 'next()' calls at the expense of requiring more memory to hold prefetched elements between the time of iterator construction and usage. |
| `framework_type` | The list of frameworks that are used to generate this pipeline, used for telemetry. |
| `threading` | The threading options associated with the dataset. See [`tf.data.ThreadingOptions`](https://tensorflow.google.cn/api_docs/python/tf/data/ThreadingOptions) for more details. |

## Methods

### `merge`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/ops/options.py#L727-L741)

```
merge(
    options
)
```

Merges itself with the given [`tf.data.Options`](https://tensorflow.google.cn/api_docs/python/tf/data/Options).

If this object and the `options` to merge set an option differently, a
warning is generated and this object's value is updated with the `options`
object's value.

| Args | |

|  |  |
| --- | --- |
| `options` | The [`tf.data.Options`](https://tensorflow.google.cn/api_docs/python/tf/data/Options) to merge with. |

| Returns | |
| New [`tf.data.Options`](https://tensorflow.google.cn/api_docs/python/tf/data/Options) object which is the result of merging self with the input [`tf.data.Options`](https://tensorflow.google.cn/api_docs/python/tf/data/Options). | |

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