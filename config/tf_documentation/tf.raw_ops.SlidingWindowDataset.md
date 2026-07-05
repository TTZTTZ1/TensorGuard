# tf.raw_ops.SlidingWindowDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SlidingWindowDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SlidingWindowDataset)

---

Creates a dataset that passes a sliding window over `input_dataset`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SlidingWindowDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SlidingWindowDataset)

```
tf.raw_ops.SlidingWindowDataset(
    input_dataset,
    window_size,
    window_shift,
    window_stride,
    output_types,
    output_shapes,
    drop_remainder=True,
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `window_size` | A `Tensor` of type `int64`. A scalar representing the number of elements in the sliding window. |
| `window_shift` | A `Tensor` of type `int64`. A scalar representing the steps moving the sliding window forward in one iteration. It must be positive. |
| `window_stride` | A `Tensor` of type `int64`. A scalar representing the stride of the input elements of the sliding window. It must be positive. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `drop_remainder` | An optional `bool`. Defaults to `True`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |