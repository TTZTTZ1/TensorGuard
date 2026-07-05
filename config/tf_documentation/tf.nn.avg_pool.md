# tf.nn.avg_pool

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/avg_pool](https://tensorflow.google.cn/api_docs/python/tf/nn/avg_pool)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_ops.py#L4463-L4527) |

Performs the avg pooling on the input.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.nn.avg_pool_v2`](https://tensorflow.google.cn/api_docs/python/tf/nn/avg_pool)

```
tf.nn.avg_pool(
    input, ksize, strides, padding, data_format=None, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Fast Style Transfer for Arbitrary Styles](https://tensorflow.google.cn/hub/tutorials/tf2_arbitrary_image_stylization) |

Each entry in `output` is the mean of the corresponding size `ksize`
window in `value`.

| Args | |

|  |  |
| --- | --- |
| `input` | Tensor of rank N+2, of shape `[batch_size] + input_spatial_shape + [num_channels]` if `data_format` does not start with "NC" (default), or `[batch_size, num_channels] + input_spatial_shape` if data\_format starts with "NC". Pooling happens over the spatial dimensions only. |
| `ksize` | An int or list of `ints` that has length `1`, `N` or `N+2`. The size of the window for each dimension of the input tensor. |
| `strides` | An int or list of `ints` that has length `1`, `N` or `N+2`. The stride of the sliding window for each dimension of the input tensor. |
| `padding` | A string, either `'VALID'` or `'SAME'`. The padding algorithm. See [here](https://tensorflow.google.cn/api_docs/python/tf/nn#notes_on_padding_2) for more information. |
| `data_format` | A string. Specifies the channel dimension. For N=1 it can be either "NWC" (default) or "NCW", for N=2 it can be either "NHWC" (default) or "NCHW" and for N=3 either "NDHWC" (default) or "NCDHW". |
| `name` | Optional name for the operation. |

| Returns | |
| A `Tensor` of format specified by `data_format`. The average pooled output tensor. | |