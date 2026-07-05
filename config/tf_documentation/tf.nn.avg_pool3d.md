# tf.nn.avg_pool3d

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/avg_pool3d](https://tensorflow.google.cn/api_docs/python/tf/nn/avg_pool3d)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_ops.py#L4663-L4701) |

Performs the average pooling on the input.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.nn.avg_pool3d`](https://tensorflow.google.cn/api_docs/python/tf/nn/avg_pool3d)

```
tf.nn.avg_pool3d(
    input, ksize, strides, padding, data_format='NDHWC', name=None
)
```

Each entry in `output` is the mean of the corresponding size `ksize`
window in `value`.

| Args | |

|  |  |
| --- | --- |
| `input` | A 5-D `Tensor` of shape `[batch, depth, height, width, channels]` and type `float32`, `float64`, `qint8`, `quint8`, or `qint32`. |
| `ksize` | An int or list of `ints` that has length `1`, `3` or `5`. The size of the window for each dimension of the input tensor. |
| `strides` | An int or list of `ints` that has length `1`, `3` or `5`. The stride of the sliding window for each dimension of the input tensor. |
| `padding` | A string, either `'VALID'` or `'SAME'`. The padding algorithm. See [here](https://tensorflow.google.cn/api_docs/python/tf/nn#notes_on_padding_2) for more information. |
| `data_format` | A string. 'NDHWC' and 'NCDHW' are supported. |
| `name` | Optional name for the operation. |

| Returns | |
| A `Tensor` with the same type as `value`. The average pooled output tensor. | |