# tf.raw_ops.MakeIterator

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MakeIterator](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MakeIterator)

---

Makes a new iterator from the given `dataset` and stores it in `iterator`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.MakeIterator`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/MakeIterator)

```
tf.raw_ops.MakeIterator(
    dataset, iterator, name=None
)
```

This operation may be executed multiple times. Each execution will reset the
iterator in `iterator` to the first element of `dataset`.

| Args | |

|  |  |
| --- | --- |
| `dataset` | A `Tensor` of type `variant`. |
| `iterator` | A `Tensor` of type `resource`. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |