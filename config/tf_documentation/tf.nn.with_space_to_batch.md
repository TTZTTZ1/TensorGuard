# tf.nn.with_space_to_batch

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/with_space_to_batch](https://tensorflow.google.cn/api_docs/python/tf/nn/with_space_to_batch)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_ops.py#L572-L729) |

Performs `op` on the space-to-batch representation of `input`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.nn.with_space_to_batch`](https://tensorflow.google.cn/api_docs/python/tf/nn/with_space_to_batch)

```
tf.nn.with_space_to_batch(
    input,
    dilation_rate,
    padding,
    op,
    filter_shape=None,
    spatial_dims=None,
    data_format=None
)
```

This has the effect of transforming sliding window operations into the
corresponding "atrous" operation in which the input is sampled at the
specified `dilation_rate`.

In the special case that `dilation_rate` is uniformly 1, this simply returns:

op(input, num\_spatial\_dims, padding)

Otherwise, it returns:

batch\_to\_space\_nd(
op(space\_to\_batch\_nd(input, adjusted\_dilation\_rate, adjusted\_paddings),
num\_spatial\_dims,
"VALID")
adjusted\_dilation\_rate,
adjusted\_crops),

where:

adjusted\_dilation\_rate is an int64 tensor of shape [max(spatial*dims)],
adjusted*{paddings,crops} are int64 tensors of shape [max(spatial\_dims), 2]

defined as follows:

We first define two int64 tensors `paddings` and `crops` of shape
`[num_spatial_dims, 2]` based on the value of `padding` and the spatial
dimensions of the `input`:

If `padding = "VALID"`, then:

paddings, crops = required\_space\_to\_batch\_paddings(
input\_shape[spatial\_dims],
dilation\_rate)

If `padding = "SAME"`, then:

dilated\_filter\_shape =
filter\_shape + (filter\_shape - 1) \* (dilation\_rate - 1)

paddings, crops = required\_space\_to\_batch\_paddings(
input\_shape[spatial\_dims],
dilation\_rate,
[(dilated\_filter\_shape - 1) // 2,
dilated\_filter\_shape - 1 - (dilated\_filter\_shape - 1) // 2])

Because `space_to_batch_nd` and `batch_to_space_nd` assume that the spatial
dimensions are contiguous starting at the second dimension, but the specified
`spatial_dims` may not be, we must adjust `dilation_rate`, `paddings` and
`crops` in order to be usable with these operations. For a given dimension,
if the block size is 1, and both the starting and ending padding and crop
amounts are 0, then space\_to\_batch\_nd effectively leaves that dimension alone,
which is what is needed for dimensions not part of `spatial_dims`.
Furthermore, `space_to_batch_nd` and `batch_to_space_nd` handle this case
efficiently for any number of leading and trailing dimensions.

For 0 <= i < len(spatial\_dims), we assign:

adjusted\_dilation\_rate[spatial\_dims[i] - 1] = dilation\_rate[i]
adjusted\_paddings[spatial\_dims[i] - 1, :] = paddings[i, :]
adjusted\_crops[spatial\_dims[i] - 1, :] = crops[i, :]

All unassigned values of `adjusted_dilation_rate` default to 1, while all
unassigned values of `adjusted_paddings` and `adjusted_crops` default to 0.

Note in the case that `dilation_rate` is not uniformly 1, specifying "VALID"
padding is equivalent to specifying `padding = "SAME"` with a filter\_shape of
`[1]*N`.

Advanced usage. Note the following optimization: A sequence of
`with_space_to_batch` operations with identical (not uniformly 1)
`dilation_rate` parameters and "VALID" padding

net = with\_space\_to\_batch(net, dilation\_rate, "VALID", op\_1)
...
net = with\_space\_to\_batch(net, dilation\_rate, "VALID", op\_k)

can be combined into a single `with_space_to_batch` operation as follows:

def combined\_op(converted\_input, num\_spatial\_dims, \_):
result = op\_1(converted\_input, num\_spatial\_dims, "VALID")
...
result = op\_k(result, num\_spatial\_dims, "VALID")

net = with\_space\_to\_batch(net, dilation\_rate, "VALID", combined\_op)

This eliminates the overhead of `k-1` calls to `space_to_batch_nd` and
`batch_to_space_nd`.

Similarly, a sequence of `with_space_to_batch` operations with identical (not
uniformly 1) `dilation_rate` parameters, "SAME" padding, and odd filter
dimensions

net = with\_space\_to\_batch(net, dilation\_rate, "SAME", op\_1, filter\_shape\_1)
...
net = with\_space\_to\_batch(net, dilation\_rate, "SAME", op\_k, filter\_shape\_k)

can be combined into a single `with_space_to_batch` operation as follows:

def combined\_op(converted\_input, num\_spatial\_dims, \_):
result = op\_1(converted\_input, num\_spatial\_dims, "SAME")
...
result = op\_k(result, num\_spatial\_dims, "SAME")

net = with\_space\_to\_batch(net, dilation\_rate, "VALID", combined\_op)

| Args | |

|  |  |
| --- | --- |
| `input` | Tensor of rank > max(spatial\_dims). |
| `dilation_rate` | int32 Tensor of *known* shape [num\_spatial\_dims]. |
| `padding` | str constant equal to "VALID" or "SAME" |
| `op` | Function that maps (input, num\_spatial\_dims, padding) -> output |
| `filter_shape` | If padding = "SAME", specifies the shape of the convolution kernel/pooling window as an integer Tensor of shape [>=num\_spatial\_dims]. If padding = "VALID", filter\_shape is ignored and need not be specified. |
| `spatial_dims` | Monotonically increasing sequence of `num_spatial_dims` integers (which are >= 1) specifying the spatial dimensions of `input` and output. Defaults to: `range(1, num_spatial_dims+1)`. |
| `data_format` | A string or None. Specifies whether the channel dimension of the `input` and output is the last dimension (default, or if `data_format` does not start with "NC"), or the second dimension (if `data_format` starts with "NC"). For N=1, the valid values are "NWC" (default) and "NCW". For N=2, the valid values are "NHWC" (default) and "NCHW". For N=3, the valid values are "NDHWC" (default) and "NCDHW". |

| Returns | |
| The output Tensor as described above, dimensions will vary based on the op provided. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if `padding` is invalid or the arguments are incompatible. |
| `ValueError` | if `spatial_dims` are invalid. |