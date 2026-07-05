# tf.ragged.cross

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/ragged/cross](https://tensorflow.google.cn/api_docs/python/tf/ragged/cross)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/ragged/ragged_array_ops.py#L741-L765) |

Generates feature cross from a list of tensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.ragged.cross`](https://tensorflow.google.cn/api_docs/python/tf/ragged/cross)

```
tf.ragged.cross(
    inputs, name=None
)
```

The input tensors must have `rank=2`, and must all have the same number of
rows. The result is a `RaggedTensor` with the same number of rows as the
inputs, where `result[row]` contains a list of all combinations of values
formed by taking a single value from each input's corresponding row
(`inputs[i][row]`). Values are combined by joining their strings with '*X*'.
E.g.:

```
>>> tf.ragged.cross([tf.ragged.constant([['a'], ['b', 'c']]),
...                  tf.ragged.constant([['d'], ['e']]),
...                  tf.ragged.constant([['f'], ['g']])])
<tf.RaggedTensor [[b'a_X_d_X_f'], [b'b_X_e_X_g', b'c_X_e_X_g']]>
```

| Args | |

|  |  |
| --- | --- |
| `inputs` | A list of `RaggedTensor` or `Tensor` or `SparseTensor`. |
| `name` | Optional name for the op. |

| Returns | |
| A 2D `RaggedTensor` of type `string`. | |