# tf.raw_ops.ConfigureDistributedTPU

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ConfigureDistributedTPU](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ConfigureDistributedTPU)

---

Sets up the centralized structures for a distributed TPU system.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.ConfigureDistributedTPU`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ConfigureDistributedTPU)

```
tf.raw_ops.ConfigureDistributedTPU(
    embedding_config='',
    tpu_embedding_config='',
    is_global_init=False,
    enable_whole_mesh_compilations=False,
    compilation_failure_closes_chips=True,
    tpu_cancellation_closes_chips=0,
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `embedding_config` | An optional `string`. Defaults to `""`. Reserved. Do not use. |
| `tpu_embedding_config` | An optional `string`. Defaults to `""`. Serialized tensorflow.tpu.TPUEmbeddingConfiguration that describes the embedding lookups of the program. |
| `is_global_init` | An optional `bool`. Defaults to `False`. Reserved. Do not use. |
| `enable_whole_mesh_compilations` | An optional `bool`. Defaults to `False`. |
| `compilation_failure_closes_chips` | An optional `bool`. Defaults to `True`. |
| `tpu_cancellation_closes_chips` | An optional `int`. Defaults to `0`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |