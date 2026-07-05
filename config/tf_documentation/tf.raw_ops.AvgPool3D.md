# tf.raw_ops.AvgPool3D

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AvgPool3D](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AvgPool3D)

---

Performs 3D average pooling on the input.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.AvgPool3D`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AvgPool3D)

```
tf.raw_ops.AvgPool3D(
    input, ksize, strides, padding, data_format='NDHWC', name=None
)
```

Each entry in `output` is the mean of the corresponding size `ksize` window in
`value`.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. Shape `[batch, depth, rows, cols, channels]` tensor to pool over. |
| `ksize` | A list of `ints` that has length `>= 5`. 1-D tensor of length 5. The size of the window for each dimension of the input tensor. Must have `ksize[0] = ksize[4] = 1`. |
| `strides` | A list of `ints` that has length `>= 5`. 1-D tensor of length 5. The stride of the sliding window for each dimension of `input`. Must have `strides[0] = strides[4] = 1`. |
| `padding` | A `string` from: `"SAME", "VALID"`. The type of padding algorithm to use. |
| `data_format` | An optional `string` from: `"NDHWC", "NCDHW"`. Defaults to `"NDHWC"`. The data format of the input and output data. With the default format "NDHWC", the data is stored in the order of: [batch, in\_depth, in\_height, in\_width, in\_channels]. Alternatively, the format could be "NCDHW", the data storage order is: [batch, in\_channels, in\_depth, in\_height, in\_width]. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |