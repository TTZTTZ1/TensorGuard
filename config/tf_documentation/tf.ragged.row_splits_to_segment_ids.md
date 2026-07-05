# tf.ragged.row_splits_to_segment_ids

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/ragged/row_splits_to_segment_ids](https://tensorflow.google.cn/api_docs/python/tf/ragged/row_splits_to_segment_ids)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/ragged/segment_id_ops.py#L31-L70) |

Generates the segmentation corresponding to a RaggedTensor `row_splits`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.ragged.row_splits_to_segment_ids`](https://tensorflow.google.cn/api_docs/python/tf/ragged/row_splits_to_segment_ids)

```
tf.ragged.row_splits_to_segment_ids(
    splits, name=None, out_type=None
)
```

Returns an integer vector `segment_ids`, where `segment_ids[i] == j` if
`splits[j] <= i < splits[j+1]`. Example:

```
>>> print(tf.ragged.row_splits_to_segment_ids([0, 3, 3, 5, 6, 9]))
 tf.Tensor([0 0 0 2 2 3 4 4 4], shape=(9,), dtype=int64)
```

| Args | |

|  |  |
| --- | --- |
| `splits` | A sorted 1-D integer Tensor. `splits[0]` must be zero. |
| `name` | A name prefix for the returned tensor (optional). |
| `out_type` | The dtype for the return value. Defaults to `splits.dtype`, or [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64) if `splits` does not have a dtype. |

| Returns | |
| A sorted 1-D integer Tensor, with `shape=[splits[-1]]` | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `splits` is invalid. |