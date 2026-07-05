# tf.raw_ops.OrderedMapClear

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OrderedMapClear](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OrderedMapClear)

---

Op removes all elements in the underlying container.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.OrderedMapClear`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/OrderedMapClear)

```
tf.raw_ops.OrderedMapClear(
    dtypes,
    capacity=0,
    memory_limit=0,
    container='',
    shared_name='',
    name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `dtypes` | A list of `tf.DTypes`. |
| `capacity` | An optional `int` that is `>= 0`. Defaults to `0`. |
| `memory_limit` | An optional `int` that is `>= 0`. Defaults to `0`. |
| `container` | An optional `string`. Defaults to `""`. |
| `shared_name` | An optional `string`. Defaults to `""`. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |