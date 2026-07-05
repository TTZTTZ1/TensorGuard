# tf.linalg.band_part

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linalg/band_part](https://tensorflow.google.cn/api_docs/python/tf/linalg/band_part)

---

Copy a tensor setting everything outside a central band in each innermost matrix to zero.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.linalg.band_part`](https://tensorflow.google.cn/api_docs/python/tf/linalg/band_part), [`tf.compat.v1.matrix_band_part`](https://tensorflow.google.cn/api_docs/python/tf/linalg/band_part)

```
tf.linalg.band_part(
    input: Annotated[Any, TV_MatrixBandPart_T],
    num_lower: Annotated[Any, TV_MatrixBandPart_Tindex],
    num_upper: Annotated[Any, TV_MatrixBandPart_Tindex],
    name=None
) -> Annotated[Any, TV_MatrixBandPart_T]
```

The `band` part is computed as follows:
Assume `input` has `k` dimensions `[I, J, K, ..., M, N]`, then the output is a
tensor with the same shape where

`band[i, j, k, ..., m, n] = in_band(m, n) * input[i, j, k, ..., m, n]`.

The indicator function

`in_band(m, n) = (num_lower < 0 || (m-n) <= num_lower)) &&
(num_upper < 0 || (n-m) <= num_upper)`.

#### For example:

```
# if 'input' is [[ 0,  1,  2, 3]
#                [-1,  0,  1, 2]
#                [-2, -1,  0, 1]
#                [-3, -2, -1, 0]],

tf.linalg.band_part(input, 1, -1) ==> [[ 0,  1,  2, 3]
                                       [-1,  0,  1, 2]
                                       [ 0, -1,  0, 1]
                                       [ 0,  0, -1, 0]],

tf.linalg.band_part(input, 2, 1) ==> [[ 0,  1,  0, 0]
                                      [-1,  0,  1, 0]
                                      [-2, -1,  0, 1]
                                      [ 0, -2, -1, 0]]
```

#### Useful special cases:

```
 tf.linalg.band_part(input, 0, -1) ==> Upper triangular part.
 tf.linalg.band_part(input, -1, 0) ==> Lower triangular part.
 tf.linalg.band_part(input, 0, 0) ==> Diagonal.
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Rank `k` tensor. |
| `num_lower` | A `Tensor`. Must be one of the following types: `int32`, `int64`. 0-D tensor. Number of subdiagonals to keep. If negative, keep entire lower triangle. |
| `num_upper` | A `Tensor`. Must have the same type as `num_lower`. 0-D tensor. Number of superdiagonals to keep. If negative, keep entire upper triangle. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |