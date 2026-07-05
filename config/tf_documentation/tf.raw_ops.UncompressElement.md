# tf.raw_ops.UncompressElement

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/UncompressElement](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/UncompressElement)

---

Uncompresses a compressed dataset element.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.UncompressElement`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/UncompressElement)

```
tf.raw_ops.UncompressElement(
    compressed, output_types, output_shapes, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `compressed` | A `Tensor` of type `variant`. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `Tensor` objects of type `output_types`. | |