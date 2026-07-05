# tf.experimental.unregister_dispatch_for

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/unregister_dispatch_for](https://tensorflow.google.cn/api_docs/python/tf/experimental/unregister_dispatch_for)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/util/dispatch.py#L553-L609) |

Unregisters a function that was registered with `@dispatch_for_*`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.experimental.unregister_dispatch_for`](https://tensorflow.google.cn/api_docs/python/tf/experimental/unregister_dispatch_for)

```
tf.experimental.unregister_dispatch_for(
    dispatch_target
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Extension types](https://tensorflow.google.cn/guide/extension_type) |

This is primarily intended for testing purposes.

#### Example:

```
>>> # Define a type and register a dispatcher to override `tf.abs`:
>>> class MyTensor(tf.experimental.ExtensionType):
...   value: tf.Tensor
>>> @tf.experimental.dispatch_for_api(tf.abs)
... def my_abs(x: MyTensor):
...   return MyTensor(tf.abs(x.value))
>>> tf.abs(MyTensor(5))
MyTensor(value=<tf.Tensor: shape=(), dtype=int32, numpy=5>)
```

```
>>> # Unregister the dispatcher, so `tf.abs` no longer calls `my_abs`.
>>> unregister_dispatch_for(my_abs)
>>> tf.abs(MyTensor(5))
Traceback (most recent call last):
... 
ValueError: Attempt to convert a value ... to a Tensor.
```

| Args | |

|  |  |
| --- | --- |
| `dispatch_target` | The function to unregister. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `dispatch_target` was not registered using `@dispatch_for`, `@dispatch_for_unary_elementwise_apis`, or `@dispatch_for_binary_elementwise_apis`. |