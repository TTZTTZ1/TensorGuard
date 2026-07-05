# tf.raw_ops.MatchingFiles

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MatchingFiles](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MatchingFiles)

---

Returns the set of files matching one or more glob patterns.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.MatchingFiles`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MatchingFiles)

```
tf.raw_ops.MatchingFiles(
    pattern, name=None
)
```

Note that this routine only supports wildcard characters in the
basename portion of the pattern, not in the directory portion.
Note also that the order of filenames returned is deterministic.

| Args | |

|  |  |
| --- | --- |
| `pattern` | A `Tensor` of type `string`. Shell wildcard pattern(s). Scalar or vector of type string. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |