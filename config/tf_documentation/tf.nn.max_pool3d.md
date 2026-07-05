# tf.nn.max_pool3d

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/max_pool3d](https://tensorflow.google.cn/api_docs/python/tf/nn/max_pool3d)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_ops.py#L5084-L5124) |

Performs the max pooling on the input.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.nn.max_pool3d`](https://tensorflow.google.cn/api_docs/python/tf/nn/max_pool3d)

```
tf.nn.max_pool3d(
    input, ksize, strides, padding, data_format='NDHWC', name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `input` | A 5-D `Tensor` of the format specified by `data_format`. |
| `ksize` | An int or list of `ints` that has length `1`, `3` or `5`. The size of the window for each dimension of the input tensor. |
| `strides` | An int or list of `ints` that has length `1`, `3` or `5`. The stride of the sliding window for each dimension of the input tensor. |
| `padding` | A string, either `'VALID'` or `'SAME'`. The padding algorithm. See [here](https://tensorflow.google.cn/api_docs/python/tf/nn#notes_on_padding_2) for more information. |
| `data_format` | An optional string from: "NDHWC", "NCDHW". Defaults to "NDHWC". The data format of the input and output data. With the default format "NDHWC", the data is stored in the order of: [batch, in\_depth, in\_height, in\_width, in\_channels]. Alternatively, the format could be "NCDHW", the data storage order is: [batch, in\_channels, in\_depth, in\_height, in\_width]. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of format specified by `data_format`. The max pooled output tensor. | |