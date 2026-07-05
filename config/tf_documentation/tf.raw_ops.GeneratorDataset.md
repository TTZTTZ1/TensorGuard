# tf.raw_ops.GeneratorDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GeneratorDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GeneratorDataset)

---

Creates a dataset that invokes a function to generate elements.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.GeneratorDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/GeneratorDataset)

```
tf.raw_ops.GeneratorDataset(
    init_func_other_args,
    next_func_other_args,
    finalize_func_other_args,
    init_func,
    next_func,
    finalize_func,
    output_types,
    output_shapes,
    metadata='',
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `init_func_other_args` | A list of `Tensor` objects. |
| `next_func_other_args` | A list of `Tensor` objects. |
| `finalize_func_other_args` | A list of `Tensor` objects. |
| `init_func` | A function decorated with @Defun. |
| `next_func` | A function decorated with @Defun. |
| `finalize_func` | A function decorated with @Defun. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `metadata` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |