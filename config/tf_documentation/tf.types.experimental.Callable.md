# tf.types.experimental.Callable

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/types/experimental/Callable](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/Callable)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/types/core.py#L111-L139) |

Base class for TF callables like those created by tf.function.

**Note:** Callables are conceptually very similar to [`tf.Operation`](https://tensorflow.google.cn/api_docs/python/tf/Operation): a
[`tf.Operation`](https://tensorflow.google.cn/api_docs/python/tf/Operation) is a kind of callable.

| Attributes | |

|  |  |
| --- | --- |
| `function_type` | Returns a FunctionType describing this callable. |

## Methods

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/types/core.py#L124-L139)

```
__call__(
    *args, **kwargs
)
```

Executes this callable.

This behaves like a regular op - in eager mode, it immediately starts
execution, returning results. In graph mode, it creates ops which return
symbolic TensorFlow values (like [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor), [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset),
etc.). For example, [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) callables typically generate a
[`tf.raw_ops.PartitionedCall`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/PartitionedCall) op, but not always - the
exact operations being generated are an internal implementation detail.

| Args | |

|  |  |
| --- | --- |
| `*args` | positional argument for this call |
| `**kwargs` | keyword arguments for this call |

| Returns | |
| The execution results. | |