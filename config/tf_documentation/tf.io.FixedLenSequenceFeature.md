# tf.io.FixedLenSequenceFeature

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/io/FixedLenSequenceFeature](https://tensorflow.google.cn/api_docs/python/tf/io/FixedLenSequenceFeature)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/parsing_config.py#L318-L350) |

Configuration for parsing a variable-length input feature into a `Tensor`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.FixedLenSequenceFeature`](https://tensorflow.google.cn/api_docs/python/tf/io/FixedLenSequenceFeature), [`tf.compat.v1.io.FixedLenSequenceFeature`](https://tensorflow.google.cn/api_docs/python/tf/io/FixedLenSequenceFeature)

```
tf.io.FixedLenSequenceFeature(
    shape, dtype, allow_missing=False, default_value=None
)
```

The resulting `Tensor` of parsing a single `SequenceExample` or `Example` has
a static `shape` of `[None] + shape` and the specified `dtype`.
The resulting `Tensor` of parsing a `batch_size` many `Example`s has
a static `shape` of `[batch_size, None] + shape` and the specified `dtype`.
The entries in the `batch` from different `Examples` will be padded with
`default_value` to the maximum length present in the `batch`.

To treat a sparse input as dense, provide `allow_missing=True`; otherwise,
the parse functions will fail on any examples missing this feature.

| Fields | |

|  |  |
| --- | --- |
| `shape` | Shape of input data for dimension 2 and higher. First dimension is of variable length `None`. |
| `dtype` | Data type of input. |
| `allow_missing` | Whether to allow this feature to be missing from a feature list item. Is available only for parsing `SequenceExample` not for parsing `Examples`. |
| `default_value` | Scalar value to be used to pad multiple `Example`s to their maximum length. Irrelevant for parsing a single `Example` or `SequenceExample`. Defaults to "" for dtype string and 0 otherwise (optional). |

| Attributes | |

|  |  |
| --- | --- |
| `shape` | A `namedtuple` alias for field number 0 |
| `dtype` | A `namedtuple` alias for field number 1 |
| `allow_missing` | A `namedtuple` alias for field number 2 |
| `default_value` | A `namedtuple` alias for field number 3 |