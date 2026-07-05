# tf.ragged.cross_hashed

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/ragged/cross_hashed](https://tensorflow.google.cn/api_docs/python/tf/ragged/cross_hashed)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/ragged/ragged_array_ops.py#L768-L802) |

Generates hashed feature cross from a list of tensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.ragged.cross_hashed`](https://tensorflow.google.cn/api_docs/python/tf/ragged/cross_hashed)

```
tf.ragged.cross_hashed(
    inputs, num_buckets=0, hash_key=None, name=None
)
```

The input tensors must have `rank=2`, and must all have the same number of
rows. The result is a `RaggedTensor` with the same number of rows as the
inputs, where `result[row]` contains a list of all combinations of values
formed by taking a single value from each input's corresponding row
(`inputs[i][row]`). Values are combined by hashing together their
fingerprints. E.g.:

```
>>> tf.ragged.cross_hashed([tf.ragged.constant([['a'], ['b', 'c']]),
...                         tf.ragged.constant([['d'], ['e']]),
...                         tf.ragged.constant([['f'], ['g']])],
...                        num_buckets=100)
<tf.RaggedTensor [[78], [66, 74]]>
```

| Args | |

|  |  |
| --- | --- |
| `inputs` | A list of `RaggedTensor` or `Tensor` or `SparseTensor`. |
| `num_buckets` | A non-negative `int` that used to bucket the hashed values. If `num_buckets != 0`, then `output = hashed_value % num_buckets`. |
| `hash_key` | Integer hash\_key that will be used by the `FingerprintCat64` function. If not given, a default key is used. |
| `name` | Optional name for the op. |

| Returns | |
| A 2D `RaggedTensor` of type `int64`. | |