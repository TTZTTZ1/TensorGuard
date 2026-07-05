# tf.sets.size

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/sets/size](https://tensorflow.google.cn/api_docs/python/tf/sets/size)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/sets_impl.py#L30-L58) |

Compute number of unique elements along last dimension of `a`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.sets.set_size`](https://tensorflow.google.cn/api_docs/python/tf/sets/size), [`tf.compat.v1.sets.size`](https://tensorflow.google.cn/api_docs/python/tf/sets/size)

```
tf.sets.size(
    a, validate_indices=True
)
```

| Args | |

|  |  |
| --- | --- |
| `a` | `SparseTensor`, with indices sorted in row-major order. |
| `validate_indices` | Whether to validate the order and range of sparse indices in `a`. Note that setting this to `false` allows for undefined behavior when calling this function with invalid indices. |

| Returns | |
| `int32` `Tensor` of set sizes. For `a` ranked `n`, this is a `Tensor` with rank `n-1`, and the same 1st `n-1` dimensions as `a`. Each value is the number of unique elements in the corresponding `[0...n-1]` dimension of `a`. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If `a` is an invalid types. |