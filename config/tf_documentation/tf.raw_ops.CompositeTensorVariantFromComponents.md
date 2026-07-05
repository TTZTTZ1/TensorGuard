# tf.raw_ops.CompositeTensorVariantFromComponents

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CompositeTensorVariantFromComponents](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CompositeTensorVariantFromComponents)

---

Encodes an `ExtensionType` value into a `variant` scalar Tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CompositeTensorVariantFromComponents`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CompositeTensorVariantFromComponents)

```
tf.raw_ops.CompositeTensorVariantFromComponents(
    components, metadata, name=None
)
```

Returns a scalar variant tensor containing a single `CompositeTensorVariant`
with the specified Tensor components and TypeSpec.

| Args | |

|  |  |
| --- | --- |
| `components` | A list of `Tensor` objects. The component tensors for the extension type value. |
| `metadata` | A `string`. String serialization for the TypeSpec. (Note: the encoding for the TypeSpec may change in future versions of TensorFlow.) |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |