# tf.nn.conv_transpose

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/conv_transpose](https://tensorflow.google.cn/api_docs/python/tf/nn/conv_transpose)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_ops.py#L3428-L3513) |

The transpose of `convolution`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.nn.conv_transpose`](https://tensorflow.google.cn/api_docs/python/tf/nn/conv_transpose)

```
tf.nn.conv_transpose(
    input,
    filters,
    output_shape,
    strides,
    padding='SAME',
    data_format=None,
    dilations=None,
    name=None
)
```

This operation is sometimes called "deconvolution" after
(Zeiler et al., 2010), but is really the transpose (gradient) of `conv3d`
rather than an actual deconvolution.

| Args | |

|  |  |
| --- | --- |
| `input` | An N+2 dimensional `Tensor` of shape `[batch_size] + input_spatial_shape + [in_channels]` if data\_format does not start with "NC" (default), or `[batch_size, in_channels] + input_spatial_shape` if data\_format starts with "NC". It must be one of the following types: `half`, `bfloat16`, `float32`, `float64`. |
| `filters` | An N+2 dimensional `Tensor` with the same type as `input` and shape `spatial_filter_shape + [in_channels, out_channels]`. |
| `output_shape` | A 1-D `Tensor` representing the output shape of the deconvolution op. |
| `strides` | An int or list of `ints` that has length `1`, `N` or `N+2`. The stride of the sliding window for each dimension of `input`. If a single value is given it is replicated in the spatial dimensions. By default the `N` and `C` dimensions are set to 0. The dimension order is determined by the value of `data_format`, see below for details. |
| `padding` | A string, either `'VALID'` or `'SAME'`. The padding algorithm. See [here](https://tensorflow.google.cn/api_docs/python/tf/nn#notes_on_padding_2) for more information. |
| `data_format` | A string or None. Specifies whether the channel dimension of the `input` and output is the last dimension (default, or if `data_format` does not start with "NC"), or the second dimension (if `data_format` starts with "NC"). For N=1, the valid values are "NWC" (default) and "NCW". For N=2, the valid values are "NHWC" (default) and "NCHW". For N=3, the valid values are "NDHWC" (default) and "NCDHW". |
| `dilations` | An int or list of `ints` that has length `1`, `N` or `N+2`, defaults to 1. The dilation factor for each dimension of`input`. If a single value is given it is replicated in the spatial dimensions. By default the `N` and `C` dimensions are set to 1. If set to k > 1, there will be k-1 skipped cells between each filter element on that dimension. The dimension order is determined by the value of `data_format`, see above for details. |
| `name` | A name for the operation (optional). If not specified "conv\_transpose" is used. |

| Returns | |
| A `Tensor` with the same type as `value`. | |

| References | |
| Deconvolutional Networks: [Zeiler et al., 2010](https://ieeexplore.ieee.org/abstract/document/5539957) ([pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.232.4023&rep=rep1&type=pdf)) | |