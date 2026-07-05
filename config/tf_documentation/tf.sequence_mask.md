# tf.sequence_mask

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/sequence_mask](https://tensorflow.google.cn/api_docs/python/tf/sequence_mask)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L4132-L4196) |

Returns a mask tensor representing the first N positions of each cell.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.sequence_mask`](https://tensorflow.google.cn/api_docs/python/tf/sequence_mask)

```
tf.sequence_mask(
    lengths,
    maxlen=None,
    dtype=tf.dtypes.bool,
    name=None
)

tf.dtypes.bool
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [TFP Release Notes notebook (0.13.0)](https://tensorflow.google.cn/probability/examples/TFP_Release_Notebook_0_13_0) |

If `lengths` has shape `[d_1, d_2, ..., d_n]` the resulting tensor `mask` has
dtype `dtype` and shape `[d_1, d_2, ..., d_n, maxlen]`, with

```
mask[i_1, i_2, ..., i_n, j] = (j < lengths[i_1, i_2, ..., i_n])
```

#### Examples:

```
tf.sequence_mask([1, 3, 2], 5)  # [[True, False, False, False, False],
                                #  [True, True, True, False, False],
                                #  [True, True, False, False, False]]

tf.sequence_mask([[1, 3],[2,0]])  # [[[True, False, False],
                                  #   [True, True, True]],
                                  #  [[True, True, False],
                                  #   [False, False, False]]]
```

| Args | |

|  |  |
| --- | --- |
| `lengths` | integer tensor, all its values <= maxlen. |
| `maxlen` | scalar integer tensor, size of last dimension of returned tensor. Default is the maximum value in `lengths`. |
| `dtype` | output type of the resulting tensor. |
| `name` | name of the op. |

| Returns | |
| A mask tensor of shape `lengths.shape + (maxlen,)`, cast to specified dtype. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if `maxlen` is not a scalar. |