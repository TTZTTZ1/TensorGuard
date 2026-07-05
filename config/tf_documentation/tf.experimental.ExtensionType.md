# tf.experimental.ExtensionType

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/ExtensionType](https://tensorflow.google.cn/api_docs/python/tf/experimental/ExtensionType)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/extension_type.py#L99-L329) |

Base class for TensorFlow `ExtensionType` classes.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.experimental.ExtensionType`](https://tensorflow.google.cn/api_docs/python/tf/experimental/ExtensionType)

```
tf.experimental.ExtensionType(
    *args, **kwargs
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Extension types](https://tensorflow.google.cn/guide/extension_type) |

Tensorflow `ExtensionType` classes are specialized Python classes that can be
used transparently with TensorFlow -- e.g., they can be used with ops
such as [`tf.cond`](https://tensorflow.google.cn/api_docs/python/tf/cond) or [`tf.while_loop`](https://tensorflow.google.cn/api_docs/python/tf/while_loop) and used as inputs or outputs for
[`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) and Keras layers.

New `ExtensionType` classes are defined by creating a subclass of
`tf.ExtensionType` that
contains type annotations for all instance variables. The following type
annotations are supported:

| Type | Example |
| --- | --- |
| Python integers | `i: int` |
| Python floats | `f: float` |
| Python strings | `s: str` |
| Python booleans | `b: bool` |
| Python None | `n: None` |
| Python tuple | `params: tuple[int, float, int, int]` |
| Python tuple w/ Ellipsis | `lengths: tuple[int, ...]` |
| Tensors | `t: tf.Tensor` |
| Composite Tensors | `rt: tf.RaggedTensor` |
| Extension Types | `m: MyMaskedTensor` |
| Tensor shapes | `shape: tf.TensorShape` |
| Tensor dtypes | `dtype: tf.DType` |
| Type unions | `length: typing.Union[int, float]` |
| Tuples | `params: typing.Tuple[int, float, int, int]` |
| Tuples w/ Ellipsis | `lengths: typing.Tuple[int, ...]` |
| Mappings | `tags: typing.Mapping[str, str]` |

Fields annotated with `typing.Mapping` will be stored using an immutable
mapping type.

ExtensionType values are immutable -- i.e., once constructed, you can not
modify or delete any of their instance members.

### Examples

```
>>> class MaskedTensor(ExtensionType):
...   values: tf.Tensor
...   mask: tf.Tensor
```

```
>>> class Toy(ExtensionType):
...   name: str
...   price: tensor.Tensor
...   features: typing.Mapping[str, tf.Tensor]
```

```
>>> class ToyStore(ExtensionType):
...   name: str
...   toys: typing.Tuple[Toy, ...]
```

## Methods

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/extension_type.py#L276-L305)

```
__eq__(
    other
)
```

Return self==value.

### `__ne__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/extension_type.py#L307-L312)

```
__ne__(
    other
)
```

Return self!=value.