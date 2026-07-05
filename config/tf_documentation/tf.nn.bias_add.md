# tf.nn.bias_add

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/nn/bias_add](https://tensorflow.google.cn/api_docs/python/tf/nn/bias_add)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/nn_ops.py#L3516-L3560) |

Adds `bias` to `value`.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.nn.bias_add`](https://tensorflow.google.cn/api_docs/python/tf/nn/bias_add)

```
tf.nn.bias_add(
    value, bias, data_format=None, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Use TF1.x models in TF2 workflows](https://tensorflow.google.cn/guide/migrate/model_mapping) | * [Scalable model compression](https://tensorflow.google.cn/tutorials/optimization/compression) |

This is (mostly) a special case of [`tf.add`](https://tensorflow.google.cn/api_docs/python/tf/math/add) where `bias` is restricted to 1-D.
Broadcasting is supported, so `value` may have any number of dimensions.
Unlike [`tf.add`](https://tensorflow.google.cn/api_docs/python/tf/math/add), the type of `bias` is allowed to differ from `value` in the
case where both types are quantized.

| Args | |

|  |  |
| --- | --- |
| `value` | A `Tensor` with type `float`, `double`, `int64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, or `complex128`. |
| `bias` | A 1-D `Tensor` with size matching the channel dimension of `value`. Must be the same type as `value` unless `value` is a quantized type, in which case a different quantized type may be used. |
| `data_format` | A string. 'N...C' and 'NC...' are supported. If `None` (the default) is specified then 'N..C' is assumed. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` with the same type as `value`. | |

| Raises | |
| ValueError if data format is unrecognized, if `value` has less than two dimensions when `data_format` is 'N..C'/`None` or `value` has less then three dimensions when `data_format` is `NC..`, if `bias` does not have exactly one dimension (is a vector), or if the size of `bias` does not match the size of the channel dimension of `value`. | |