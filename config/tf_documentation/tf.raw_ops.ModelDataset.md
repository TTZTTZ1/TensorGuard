# tf.raw_ops.ModelDataset

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ModelDataset](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ModelDataset)

---

Identity transformation that models performance.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ModelDataset`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ModelDataset)

```
tf.raw_ops.ModelDataset(
    input_dataset,
    output_types,
    output_shapes,
    algorithm=0,
    cpu_budget=0,
    ram_budget=0,
    name=None
)
```

Identity transformation that models performance.

| Args | |

|  |  |
| --- | --- |
| `input_dataset` | A `Tensor` of type `variant`. A variant tensor representing the input dataset. |
| `output_types` | A list of `tf.DTypes` that has length `>= 1`. |
| `output_shapes` | A list of shapes (each a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape) or list of `ints`) that has length `>= 1`. |
| `algorithm` | An optional `int`. Defaults to `0`. |
| `cpu_budget` | An optional `int`. Defaults to `0`. |
| `ram_budget` | An optional `int`. Defaults to `0`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `variant`. | |