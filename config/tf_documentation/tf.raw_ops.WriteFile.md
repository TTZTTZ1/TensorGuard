# tf.raw_ops.WriteFile

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/WriteFile](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/WriteFile)

---

Writes `contents` to the file at input `filename`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.WriteFile`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/WriteFile)

```
tf.raw_ops.WriteFile(
    filename, contents, name=None
)
```

Creates the file and recursively creates directory if it does not exist.

| Args | |

|  |  |
| --- | --- |
| `filename` | A `Tensor` of type `string`. scalar. The name of the file to which we write the contents. |
| `contents` | A `Tensor` of type `string`. scalar. The content to be written to the output file. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |