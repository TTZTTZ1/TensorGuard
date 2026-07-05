# tf.data.experimental.unbatch

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/unbatch](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/unbatch)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/batching.py#L268-L295) |

Splits elements of a dataset into multiple elements on the batch dimension. (deprecated)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.unbatch`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/unbatch)

```
tf.data.experimental.unbatch()
```

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use [`tf.data.Dataset.unbatch()`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#unbatch).

For example, if elements of the dataset are shaped `[B, a0, a1, ...]`,
where `B` may vary for each input element, then for each element in the
dataset, the unbatched dataset will contain `B` consecutive elements
of shape `[a0, a1, ...]`.

```
# NOTE: The following example uses `{ ... }` to represent the contents
# of a dataset.
a = { ['a', 'b', 'c'], ['a', 'b'], ['a', 'b', 'c', 'd'] }

a.unbatch() == {
    'a', 'b', 'c', 'a', 'b', 'a', 'b', 'c', 'd'}
```

| Returns | |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#apply). | |