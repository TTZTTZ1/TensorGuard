# tf.raw_ops.SparseFillEmptyRowsGrad

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseFillEmptyRowsGrad](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseFillEmptyRowsGrad)

---

The gradient of SparseFillEmptyRows.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.SparseFillEmptyRowsGrad`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/SparseFillEmptyRowsGrad)

```
tf.raw_ops.SparseFillEmptyRowsGrad(
    reverse_index_map, grad_values, name=None
)
```

Takes vectors reverse\_index\_map, shaped `[N]`, and grad\_values,
shaped `[N_full]`, where `N_full >= N` and copies data into either
`d_values` or `d_default_value`. Here `d_values` is shaped `[N]` and
`d_default_value` is a scalar.

d\_values[j] = grad\_values[reverse\_index\_map[j]]
d\_default*value = sum*{k : 0 .. N\_full - 1} (
grad\_values[k] \* 1{k not in reverse\_index\_map})

| Args | |

|  |  |
| --- | --- |
| `reverse_index_map` | A `Tensor` of type `int64`. 1-D. The reverse index map from SparseFillEmptyRows. |
| `grad_values` | A `Tensor`. 1-D. The gradients from backprop. |
| `name` | A name for the operation (optional). |

| Returns | |
| A tuple of `Tensor` objects (d\_values, d\_default\_value). | |
| `d_values` | A `Tensor`. Has the same type as `grad_values`. |
| `d_default_value` | A `Tensor`. Has the same type as `grad_values`. |