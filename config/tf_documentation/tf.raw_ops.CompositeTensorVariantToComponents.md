# tf.raw_ops.CompositeTensorVariantToComponents

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CompositeTensorVariantToComponents](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CompositeTensorVariantToComponents)

---

Decodes a `variant` scalar Tensor into an `ExtensionType` value.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.CompositeTensorVariantToComponents`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/CompositeTensorVariantToComponents)

```
tf.raw_ops.CompositeTensorVariantToComponents(
    encoded, metadata, Tcomponents, name=None
)
```

Returns the Tensor components encoded in a `CompositeTensorVariant`.

Raises an error if `type_spec_proto` doesn't match the TypeSpec
in `encoded`.

| Args | |

|  |  |
| --- | --- |
| `encoded` | A `Tensor` of type `variant`. A scalar `variant` Tensor containing an encoded ExtensionType value. |
| `metadata` | A `string`. String serialization for the TypeSpec. Must be compatible with the `TypeSpec` contained in `encoded`. (Note: the encoding for the TypeSpec may change in future versions of TensorFlow.) |
| `Tcomponents` | A list of `tf.DTypes`. Expected dtypes for components. |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `Tensor` objects of type `Tcomponents`. | |