# tf.experimental.ExtensionTypeBatchEncoder

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder](https://tensorflow.google.cn/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/extension_type.py#L651-L801) |

Class used to encode and decode extension type values for batching.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.experimental.ExtensionTypeBatchEncoder`](https://tensorflow.google.cn/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder)

In order to be batched and unbatched by APIs such as [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset),
[`tf.keras`](https://tensorflow.google.cn/api_docs/python/tf/keras), and [`tf.map_fn`](https://tensorflow.google.cn/api_docs/python/tf/map_fn), extension type values must be encoded as a list
of [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor)s, where stacking, unstacking, or concatenating these encoded
tensors and then decoding the result must be equivalent to stacking,
unstacking, or concatenating the original values. `ExtensionTypeBatchEncoder`s
are responsible for implementing this encoding.

The default `ExtensionTypeBatchEncoder` that is used by
`BatchableExtensionType` assumes that extension type values can be stacked,
unstacked, or concatenated by simply stacking, unstacking, or concatenating
every nested `Tensor`, `ExtensionType`, `CompositeTensor`, and `TensorShape`
field.

Extension types where this is not the case will need to override
`__batch_encoder__` with a custom encoder that overrides the `batch`,
`unbatch`, `encode`, and `decode` methods. E.g.:

```
>>> class CustomBatchEncoder(ExtensionTypeBatchEncoder):
...   pass # Override batch(), unbatch(), encode(), and decode().
```

```
>>> class CustomType(BatchableExtensionType):
...   x: tf.Tensor
...   y: tf.Tensor
...   shape: tf.TensorShape
...   __batch_encoder__ = CustomBatchEncoder()
```

For example, [`tf.RaggedTensor`](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensor) and [`tf.SparseTensor`](https://tensorflow.google.cn/api_docs/python/tf/sparse/SparseTensor) both use custom batch
encodings which define ops to "box" and "unbox" individual values into
[`tf.variant`](https://tensorflow.google.cn/api_docs/python/tf#variant) tensors.

## Methods

### `batch`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/extension_type.py#L686-L713)

```
batch(
    spec, batch_size
)
```

Returns the TypeSpec representing a batch of values described by `spec`.

The default definition returns a `TypeSpec` that is equal to `spec`, except
that an outer axis with size `batch_size` is added to every nested
`TypeSpec` and `TensorShape` field. Subclasses may override this default
definition, when necessary.

| Args | |

|  |  |
| --- | --- |
| `spec` | The `TypeSpec` for an individual value. |
| `batch_size` | An `int` indicating the number of values that are batched together, or `None` if the batch size is not known. |

| Returns | |
| A `TypeSpec` for a batch of values. | |

### `decode`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/extension_type.py#L767-L785)

```
decode(
    spec, encoded_value
)
```

Decodes `value` from a batchable tensor encoding.

See `encode` for a description of the default encoding. Subclasses may
override this default definition, when necessary.

| Args | |

|  |  |
| --- | --- |
| `spec` | The TypeSpec for the result value. If encoded values with spec `s` were batched, then `spec` should be `s.batch(batch_size)`; or if encoded values with spec `s` were unbatched, then `spec` should be `s.unbatch()`. |
| `encoded_value` | A nest of values returned by `encode`; or a nest of values that was formed by stacking, unstacking, or concatenating the corresponding elements of values returned by `encode`. |

| Returns | |
| A value compatible with `type_spec`. | |

### `encode`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/extension_type.py#L742-L765)

```
encode(
    spec, value, minimum_rank=0
)
```

Encodes `value` as a nest of batchable Tensors or CompositeTensors.

The default definition returns a flat tuple of all the `Tensor`s,
`CompositeTensor`s, and `ExtensionType`s from a depth-first traversal of
`value`'s fields. Subclasses may override this default definition, when
necessary.

| Args | |

|  |  |
| --- | --- |
| `spec` | The TypeSpec of the value to encode. |
| `value` | A value compatible with `spec`. |
| `minimum_rank` | The minimum rank for the returned Tensors, CompositeTensors, and ExtensionType values. This can be used to ensure that the encoded values can be unbatched this number of times. If `minimum_rank>0`, then `t.shape[:minimum_rank]` must be compatible for all values `t` returned by `encode`. |

| Returns | |
| A nest (as defined by [`tf.nest`](https://tensorflow.google.cn/api_docs/python/tf/nest)) of [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor)s, batchable `tf.CompositeTensor`s, or `tf.ExtensionType`s. Stacking, unstacking, or concatenating these encoded values and then decoding the result must be equivalent to stacking, unstacking, or concatenating the original values. | |

### `encoding_specs`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/extension_type.py#L787-L801)

```
encoding_specs(
    spec
)
```

Returns a list of `TensorSpec`(s) describing the encoding for `spec`.

See `encode` for a description of the default encoding. Subclasses may
override this default definition, when necessary.

| Args | |

|  |  |
| --- | --- |
| `spec` | The TypeSpec whose encoding should be described. |

| Returns | |
| A nest (as defined by `tf.nest) of`tf.TypeSpec`, describing the values that are returned by`self.encode(spec, ...)`. All TypeSpecs in this nest must be batchable. | |

### `unbatch`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/extension_type.py#L715-L740)

```
unbatch(
    spec
)
```

Returns the TypeSpec for a single unbatched element in `spec`.

The default definition returns a `TypeSpec` that is equal to `spec`, except
that the outermost axis is removed from every nested `TypeSpec`, and
`TensorShape` field. Subclasses may override this default definition, when
necessary.

| Args | |

|  |  |
| --- | --- |
| `spec` | The `TypeSpec` for a batch of values. |

| Returns | |
| A `TypeSpec` for an individual value. | |