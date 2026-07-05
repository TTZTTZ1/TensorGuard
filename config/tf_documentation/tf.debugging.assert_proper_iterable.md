# tf.debugging.assert_proper_iterable

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_proper_iterable](https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_proper_iterable)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/check_ops.py#L511-L540) |

Static assert that values is a "proper" iterable.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.assert_proper_iterable`](https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_proper_iterable), [`tf.compat.v1.debugging.assert_proper_iterable`](https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_proper_iterable)

```
tf.debugging.assert_proper_iterable(
    values
)
```

`Ops` that expect iterables of `Tensor` can call this to validate input.
Useful since `Tensor`, `ndarray`, byte/text type are all iterables themselves.

| Args | |

|  |  |
| --- | --- |
| `values` | Object to be checked. |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If `values` is not iterable or is one of `Tensor`, `SparseTensor`, `np.array`, [`tf.compat.bytes_or_text_types`](https://tensorflow.google.cn/api_docs/python/tf/compat#bytes_or_text_types). |