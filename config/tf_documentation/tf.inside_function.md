# tf.inside_function

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/inside_function](https://tensorflow.google.cn/api_docs/python/tf/inside_function)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/ops.py#L4852-L4870) |

Indicates whether the caller code is executing inside a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function).

```
tf.inside_function() -> bool
```

| Returns | |
| Boolean, True if the caller code is executing inside a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) rather than eagerly. | |

#### Example:

```
>>> tf.inside_function()
False
>>> @tf.function
... def f():
...   print(tf.inside_function())
>>> f()
True
```