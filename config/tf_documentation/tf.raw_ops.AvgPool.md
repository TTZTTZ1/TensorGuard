# tf.raw_ops.AvgPool

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AvgPool](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AvgPool)

---

Performs average pooling on the input.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.AvgPool`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AvgPool)

```
tf.raw_ops.AvgPool(
    value, ksize, strides, padding, data_format='NHWC', name=None
)
```

Each entry in `output` is the mean of the corresponding size `ksize`
window in `value`.

| Args | |

|  |  |
| --- | --- |
| `value` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. 4-D with shape `[batch, height, width, channels]`. |
| `ksize` | A list of `ints` that has length `>= 4`. The size of the sliding window for each dimension of `value`. |
| `strides` | A list of `ints` that has length `>= 4`. The stride of the sliding window for each dimension of `value`. |
| `padding` | A `string` from: `"SAME", "VALID"`. The type of padding algorithm to use. |
| `data_format` | An optional `string` from: `"NHWC", "NCHW"`. Defaults to `"NHWC"`. Specify the data format of the input and output data. With the default format "NHWC", the data is stored in the order of: [batch, in\_height, in\_width, in\_channels]. Alternatively, the format could be "NCHW", the data storage order of: [batch, in\_channels, in\_height, in\_width]. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `value`. | |