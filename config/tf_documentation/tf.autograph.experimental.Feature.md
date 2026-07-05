# tf.autograph.experimental.Feature

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/autograph/experimental/Feature](https://tensorflow.google.cn/api_docs/python/tf/autograph/experimental/Feature)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/autograph/core/converter.py#L78-L127) |

This enumeration represents optional conversion options.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.autograph.experimental.Feature`](https://tensorflow.google.cn/api_docs/python/tf/autograph/experimental/Feature)

These conversion options are experimental. They are subject to change without
notice and offer no guarantees.

*Example Usage*

```
optionals= tf.autograph.experimental.Feature.EQUALITY_OPERATORS
@tf.function(experimental_autograph_options=optionals)
def f(i):
  if i == 0:  # EQUALITY_OPERATORS allows the use of == here.
    tf.print('i is zero')
```

| Attributes | |

|  |  |
| --- | --- |
| `ALL` | Enable all features. |
| `AUTO_CONTROL_DEPS` | Insert of control dependencies in the generated code. |
| `ASSERT_STATEMENTS` | Convert Tensor-dependent assert statements to tf.Assert. |
| `BUILTIN_FUNCTIONS` | Convert builtin functions applied to Tensors to their TF counterparts. |
| `EQUALITY_OPERATORS` | Whether to convert the equality operator ('==') to tf.math.equal. |
| `LISTS` | Convert list idioms, like initializers, slices, append, etc. |
| `NAME_SCOPES` | Insert name scopes that name ops according to context, like the function they were defined in. |

| Class Variables | |

|  |  |
| --- | --- |
| ALL | `<Feature.ALL: 'ALL'>` |
| ASSERT\_STATEMENTS | `<Feature.ASSERT_STATEMENTS: 'ASSERT_STATEMENTS'>` |
| AUTO\_CONTROL\_DEPS | `<Feature.AUTO_CONTROL_DEPS: 'AUTO_CONTROL_DEPS'>` |
| BUILTIN\_FUNCTIONS | `<Feature.BUILTIN_FUNCTIONS: 'BUILTIN_FUNCTIONS'>` |
| EQUALITY\_OPERATORS | `<Feature.EQUALITY_OPERATORS: 'EQUALITY_OPERATORS'>` |
| LISTS | `<Feature.LISTS: 'LISTS'>` |
| NAME\_SCOPES | `<Feature.NAME_SCOPES: 'NAME_SCOPES'>` |