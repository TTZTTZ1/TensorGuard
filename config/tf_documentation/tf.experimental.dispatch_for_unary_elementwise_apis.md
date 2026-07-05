# tf.experimental.dispatch_for_unary_elementwise_apis

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/dispatch_for_unary_elementwise_apis](https://tensorflow.google.cn/api_docs/python/tf/experimental/dispatch_for_unary_elementwise_apis)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/util/dispatch.py#L811-L875) |

Decorator to override default implementation for unary elementwise APIs.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.experimental.dispatch_for_unary_elementwise_apis`](https://tensorflow.google.cn/api_docs/python/tf/experimental/dispatch_for_unary_elementwise_apis)

```
tf.experimental.dispatch_for_unary_elementwise_apis(
    x_type
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Extension types](https://tensorflow.google.cn/guide/extension_type) |

The decorated function (known as the "elementwise api handler") overrides
the default implementation for any unary elementwise API whenever the value
for the first argument (typically named `x`) matches the type annotation
`x_type`. The elementwise api handler is called with two arguments:

`elementwise_api_handler(api_func, x)`

Where `api_func` is a function that takes a single parameter and performs the
elementwise operation (e.g., [`tf.abs`](https://tensorflow.google.cn/api_docs/python/tf/math/abs)), and `x` is the first argument to the
elementwise api.

The following example shows how this decorator can be used to update all
unary elementwise operations to handle a `MaskedTensor` type:

```
>>> class MaskedTensor(tf.experimental.ExtensionType):
...   values: tf.Tensor
...   mask: tf.Tensor
>>> @dispatch_for_unary_elementwise_apis(MaskedTensor)
... def unary_elementwise_api_handler(api_func, x):
...   return MaskedTensor(api_func(x.values), x.mask)
>>> mt = MaskedTensor([1, -2, -3], [True, False, True])
>>> abs_mt = tf.abs(mt)
>>> print(f"values={abs_mt.values.numpy()}, mask={abs_mt.mask.numpy()}")
values=[1 2 3], mask=[ True False True]
```

For unary elementwise operations that take extra arguments beyond `x`, those
arguments are *not* passed to the elementwise api handler, but are
automatically added when `api_func` is called. E.g., in the following
example, the `dtype` parameter is not passed to
`unary_elementwise_api_handler`, but is added by `api_func`.

```
>>> ones_mt = tf.ones_like(mt, dtype=tf.float32)
>>> print(f"values={ones_mt.values.numpy()}, mask={ones_mt.mask.numpy()}")
values=[1.0 1.0 1.0], mask=[ True False True]
```

| Args | |

|  |  |
| --- | --- |
| `x_type` | A type annotation indicating when the api handler should be called. See `dispatch_for_api` for a list of supported annotation types. |

| Returns | |
| A decorator. | |

#### Registered APIs

The unary elementwise APIs are:

<>