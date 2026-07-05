# tf.raw_ops.ImmutableConst

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ImmutableConst](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ImmutableConst)

---

Returns immutable tensor from memory region.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ImmutableConst`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ImmutableConst)

```
tf.raw_ops.ImmutableConst(
    dtype, shape, memory_region_name, name=None
)
```

The current implementation memmaps the tensor from a file.

| Args | |

|  |  |
| --- | --- |
| `dtype` | A [`tf.DType`](https://tensorflow.google.cn/api_docs/python/tf/dtypes/DType). Type of the returned tensor. |
| `shape` | A [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`. Shape of the returned tensor. |
| `memory_region_name` | A `string`. Name of readonly memory region used by the tensor, see NewReadOnlyMemoryRegionFromFile in tensorflow::Env. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `dtype`. | |