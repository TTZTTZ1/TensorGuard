# tf.raw_ops.DebugNumericSummary

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DebugNumericSummary](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DebugNumericSummary)

---

Debug Numeric Summary Op.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.DebugNumericSummary`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/DebugNumericSummary)

```
tf.raw_ops.DebugNumericSummary(
    input,
    device_name='',
    tensor_name='',
    debug_urls=[],
    lower_bound=float('-inf'),
    upper_bound=float('inf'),
    mute_if_healthy=False,
    gated_grpc=False,
    name=None
)
```

Provide a basic summary of numeric value types, range and distribution.

output: A double tensor of shape [14 + nDimensions], where nDimensions is the
number of dimensions of the tensor's shape. The elements of output are:
[0]: is initialized (1.0) or not (0.0).
[1]: total number of elements
[2]: NaN element count
[3]: generalized -inf count: elements <= lower\_bound. lower\_bound is -inf by
default.
[4]: negative element count (excluding -inf), if lower\_bound is the default
-inf. Otherwise, this is the count of elements > lower\_bound and < 0.
[5]: zero element count
[6]: positive element count (excluding +inf), if upper\_bound is the default
+inf. Otherwise, this is the count of elements < upper\_bound and > 0.
[7]: generalized +inf count, elements >= upper\_bound. upper\_bound is +inf by
default.
Output elements [1:8] are all zero, if the tensor is uninitialized.
[8]: minimum of all non-inf and non-NaN elements.
If uninitialized or no such element exists: +inf.
[9]: maximum of all non-inf and non-NaN elements.
If uninitialized or no such element exists: -inf.
[10]: mean of all non-inf and non-NaN elements.
If uninitialized or no such element exists: NaN.
[11]: variance of all non-inf and non-NaN elements.
If uninitialized or no such element exists: NaN.
[12]: Data type of the tensor encoded as an enum integer. See the DataType
proto for more details.
[13]: Number of dimensions of the tensor (ndims).
[14+]: Sizes of the dimensions.

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Input tensor, non-Reference type. |
| `device_name` | An optional `string`. Defaults to `""`. |
| `tensor_name` | An optional `string`. Defaults to `""`. Name of the input tensor. |
| `debug_urls` | An optional list of `strings`. Defaults to `[]`. List of URLs to debug targets, e.g., file:///foo/tfdbg\_dump, grpc:://localhost:11011. |
| `lower_bound` | An optional `float`. Defaults to `float('-inf')`. (float) The lower bound <= which values will be included in the generalized -inf count. Default: -inf. |
| `upper_bound` | An optional `float`. Defaults to `float('inf')`. (float) The upper bound >= which values will be included in the generalized +inf count. Default: +inf. |
| `mute_if_healthy` | An optional `bool`. Defaults to `False`. (bool) Do not send data to the debug URLs unless at least one of elements [2], [3] and [7](/api_docs/python/tf/raw_ops/i.e.,%20the%20nan%20count%20and%20the%20generalized%20-inf%20and%0A%20%20inf%20counts) is non-zero. |
| `gated_grpc` | An optional `bool`. Defaults to `False`. Whether this op will be gated. If any of the debug\_urls of this debug node is of the grpc:// scheme, when the value of this attribute is set to True, the data will not actually be sent via the grpc stream unless this debug op has been enabled at the debug\_url. If all of the debug\_urls of this debug node are of the grpc:// scheme and the debug op is enabled at none of them, the output will be an empty Tensor. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `float64`. | |