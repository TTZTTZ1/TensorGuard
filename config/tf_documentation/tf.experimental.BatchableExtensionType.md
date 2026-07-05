# tf.experimental.BatchableExtensionType

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/BatchableExtensionType](https://tensorflow.google.cn/api_docs/python/tf/experimental/BatchableExtensionType)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/extension_type.py#L831-L857) |

An ExtensionType that can be batched and unbatched.

Inherits From: [`ExtensionType`](https://tensorflow.google.cn/api_docs/python/tf/experimental/ExtensionType)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.experimental.BatchableExtensionType`](https://tensorflow.google.cn/api_docs/python/tf/experimental/BatchableExtensionType)

```
tf.experimental.BatchableExtensionType(
    *args, **kwargs
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Extension types](https://tensorflow.google.cn/guide/extension_type) |

`BatchableExtensionType`s can be used with APIs that require batching or
unbatching, including `Keras`, [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset), and [`tf.map_fn`](https://tensorflow.google.cn/api_docs/python/tf/map_fn). E.g.:

```
>>> class Vehicle(tf.experimental.BatchableExtensionType):
...   top_speed: tf.Tensor
...   mpg: tf.Tensor
>>> batch = Vehicle([120, 150, 80], [30, 40, 12])
>>> tf.map_fn(lambda vehicle: vehicle.top_speed * vehicle.mpg, batch,
...           fn_output_signature=tf.int32).numpy()
array([3600, 6000,  960], dtype=int32)
```

An `ExtensionTypeBatchEncoder` is used by these APIs to encode `ExtensionType`
values. The default encoder assumes that values can be stacked, unstacked, or
concatenated by simply stacking, unstacking, or concatenating every nested
`Tensor`, `ExtensionType`, `CompositeTensor`, or `TensorShape` field.
Extension types where this is not the case will need to override
`__batch_encoder__` with a custom `ExtensionTypeBatchEncoder`. See
[`tf.experimental.ExtensionTypeBatchEncoder`](https://tensorflow.google.cn/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder) for more details.

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