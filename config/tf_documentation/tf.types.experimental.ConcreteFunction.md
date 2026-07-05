# tf.types.experimental.ConcreteFunction

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/types/experimental/ConcreteFunction](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/ConcreteFunction)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/types/core.py#L169-L182) |

Base class for differentiable graph functions.

Inherits From: [`Callable`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/Callable)

A `ConcreteFunction` encapsulates the original graph function definition with
support for differentiability under [`tf.GradientTape`](https://tensorflow.google.cn/api_docs/python/tf/GradientTape) contexts. In the
process, it may generate new graph functions (using the original) to
efficiently perform forwards and backwards passes.

| Attributes | |

|  |  |
| --- | --- |
| `function_type` | Returns a FunctionType describing this callable. |
| `inference_fn` | Returns the original `AtomicFunction` owned by this ConcreteFunction. |

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