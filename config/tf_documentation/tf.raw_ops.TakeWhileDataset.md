# tf.raw_ops.TakeWhileDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TakeWhileDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TakeWhileDataset)

---

Creates a dataset that stops iteration when predicate` is false.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.TakeWhileDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/TakeWhileDataset)

```
tf.raw_ops.TakeWhileDataset(
    input_dataset,
    other_arguments,
    predicate,
    output_types,
    output_shapes,
    metadata='',
    name=None
)
```

The `predicate` function must return a scalar boolean and accept the
following arguments:

* One tensor for each component of an element of `input_dataset`.
* One tensor for each value in `other_arguments`.

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. |
| `other_arguments` | A list of `Tensor` objects. A list of tensors, typically values that were captured when building a closure for `predicate`. |
| `predicate` | A function decorated with @Defun. A function returning a scalar boolean. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |