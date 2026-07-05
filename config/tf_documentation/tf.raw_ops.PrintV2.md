# tf.raw_ops.PrintV2

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/PrintV2](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/PrintV2)

---

Prints a string scalar.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.PrintV2`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/PrintV2)

```
tf.raw_ops.PrintV2(
    input, output_stream='stderr', end='\n', name=None
)
```

Prints a string scalar to the desired output\_stream.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` of type `string`. The string scalar to print. |
| `output_stream` | An optional `string`. Defaults to `"stderr"`. A string specifying the output stream or logging level to print to. |
| `end` | An optional `string`. Defaults to `"\n"`. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |