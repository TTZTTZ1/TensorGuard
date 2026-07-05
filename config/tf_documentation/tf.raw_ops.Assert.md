# tf.raw_ops.Assert

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Assert](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Assert)

---

Asserts that the given condition is true.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.Assert`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/Assert)

```
tf.raw_ops.Assert(
    condition, data, summarize=3, name=None
)
```

If `condition` evaluates to false, print the list of tensors in `data`.
`summarize` determines how many entries of the tensors to print.

| Args | |

|  |  |
| --- | --- |
| `condition` | A `Tensor` of type `bool`. The condition to evaluate. |
| `data` | A list of `Tensor` objects. The tensors to print out when condition is false. |
| `summarize` | An optional `int`. Defaults to `3`. Print this many entries of each tensor. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |