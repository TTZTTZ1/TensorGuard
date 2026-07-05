# tf.raw_ops.DataFormatVecPermute

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DataFormatVecPermute](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DataFormatVecPermute)

---

Permute input tensor from `src_format` to `dst_format`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.DataFormatVecPermute`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DataFormatVecPermute)

```
tf.raw_ops.DataFormatVecPermute(
    x, src_format='NHWC', dst_format='NCHW', name=None
)
```

Given source and destination format strings of length n=4 or 5, the input
tensor must be a vector of size n or n-2, or a 2D tensor of shape
(n, 2) or (n-2, 2).

If the first dimension of the input tensor is n-2, it is assumed that
non-spatial dimensions are omitted (i.e `N`, `C`).

For example, with `src_format` of `NHWC`, `dst_format` of `NCHW`, and input:

```
[1, 2, 3, 4]
```

, the output will be:

```
[1, 4, 2, 3]
```

With `src_format` of `NDHWC`, `dst_format` of `NCDHW`, and input:

```
[[1, 6], [2, 7], [3, 8], [4, 9], [5, 10]]
```

, the output will be:

```
[[1, 6], [5, 10], [2, 7], [3, 8], [4, 9]]
```

With `src_format` of `NHWC`, `dst_format` of `NCHW`, and input:

```
[1, 2]
```

, the output will be:

```
[1, 2]
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `int32`, `int64`. Tensor of rank 1 or 2 in source data format. |
| `src_format` | An optional `string`. Defaults to `"NHWC"`. source data format. |
| `dst_format` | An optional `string`. Defaults to `"NCHW"`. destination data format. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `x`. | |