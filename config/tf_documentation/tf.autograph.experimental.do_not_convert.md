# tf.autograph.experimental.do_not_convert

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/autograph/experimental/do_not_convert](https://tensorflow.google.cn/api_docs/python/tf/autograph/experimental/do_not_convert)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/autograph/impl/api.py#L624-L648) |

Decorator that suppresses the conversion of a function.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.autograph.experimental.do_not_convert`](https://tensorflow.google.cn/api_docs/python/tf/autograph/experimental/do_not_convert)

```
tf.autograph.experimental.do_not_convert(
    func=None
)
```

| Args | |

|  |  |
| --- | --- |
| `func` | function to decorate. |

| Returns | |
| If `func` is not None, returns a `Callable` which is equivalent to `func`, but is not converted by AutoGraph. If `func` is None, returns a decorator that, when invoked with a single `func` argument, returns a `Callable` equivalent to the above case. | |