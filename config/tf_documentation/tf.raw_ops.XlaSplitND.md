# tf.raw_ops.XlaSplitND

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/XlaSplitND](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/XlaSplitND)

---

Splits input tensor across all dimensions.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.XlaSplitND`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/XlaSplitND)

```
tf.raw_ops.XlaSplitND(
    input, N, num_splits, paddings=[], name=None
)
```

An op which slices the input tensor based on the given num\_splits attribute,
pads slices optionally, and returned the slices. Slices are returned in
row-major order.

This op may be generated via the TPU bridge.

For example, with `input` tensor:

```
[[0, 1, 2],
 [3, 4, 5],
 [6, 7, 8]]
```

`num_splits`:

```
[2, 2]
```

and `paddings`:

```
[1, 1]
```

the expected `outputs` is:

```
[[0, 1],
 [3, 4]]
[[2, 0],
 [5, 0]]
[[6, 7],
 [0, 0]]
[[8, 0],
 [0, 0]]
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Input tensor to split across all dimensions. } out\_arg { name: "outputs" description: < |
| `N` | An `int` that is `>= 1`. |
| `num_splits` | A list of `ints`. Number of ways to split per dimension. Shape dimensions must be evenly divisible. |
| `paddings` | An optional list of `ints`. Defaults to `[]`. Optional list of right paddings per dimension of input tensor to apply before splitting. This can be used to make a dimension evenly divisible. |
| `name` | A name for the operation (optional). |

| Returns | |
| A list of `N` `Tensor` objects with the same type as `input`. | |