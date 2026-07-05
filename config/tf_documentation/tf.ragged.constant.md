# tf.ragged.constant

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/ragged/constant](https://tensorflow.google.cn/api_docs/python/tf/ragged/constant)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/ragged/ragged_factory_ops.py#L35-L91) |

Constructs a constant RaggedTensor from a nested Python list.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.ragged.constant`](https://tensorflow.google.cn/api_docs/python/tf/ragged/constant)

```
tf.ragged.constant(
    pylist,
    dtype=None,
    ragged_rank=None,
    inner_shape=None,
    name=None,
    row_splits_dtype=tf.dtypes.int64
) -> Union[tf.RaggedTensor, ops._EagerTensorBase, tf.Operation]

tf.dtypes.int64
tf.RaggedTensor
tf.Operation
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) * [Introduction to Tensors](https://tensorflow.google.cn/guide/tensor) | * [TF Lattice Aggregate Function Models](https://tensorflow.google.cn/lattice/tutorials/aggregate_function_models) * [TF.Text Metrics](https://tensorflow.google.cn/text/tutorials/text_similarity) |

#### Example:

```
>>> tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
<tf.RaggedTensor [[1, 2], [3], [4, 5, 6]]>
```

All scalar values in `pylist` must have the same nesting depth `K`, and the
returned `RaggedTensor` will have rank `K`. If `pylist` contains no scalar
values, then `K` is one greater than the maximum depth of empty lists in
`pylist`. All scalar values in `pylist` must be compatible with `dtype`.

| Args | |

|  |  |
| --- | --- |
| `pylist` | A nested `list`, `tuple` or `np.ndarray`. Any nested element that is not a `list`, `tuple` or `np.ndarray` must be a scalar value compatible with `dtype`. |
| `dtype` | The type of elements for the returned `RaggedTensor`. If not specified, then a default is chosen based on the scalar values in `pylist`. |
| `ragged_rank` | An integer specifying the ragged rank of the returned `RaggedTensor`. Must be nonnegative and less than `K`. Defaults to `max(0, K - 1)` if `inner_shape` is not specified. Defaults to `max(0, K - 1 - len(inner_shape))` if `inner_shape` is specified. |
| `inner_shape` | A tuple of integers specifying the shape for individual inner values in the returned `RaggedTensor`. Defaults to `()` if `ragged_rank` is not specified. If `ragged_rank` is specified, then a default is chosen based on the contents of `pylist`. |
| `name` | A name prefix for the returned tensor (optional). |
| `row_splits_dtype` | data type for the constructed `RaggedTensor`'s row\_splits. One of [`tf.int32`](https://tensorflow.google.cn/api_docs/python/tf#int32) or [`tf.int64`](https://tensorflow.google.cn/api_docs/python/tf#int64). |

| Returns | |
| A potentially ragged tensor with rank `K` and the specified `ragged_rank`, containing the values from `pylist`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If the scalar values in `pylist` have inconsistent nesting depth; or if ragged\_rank or inner\_shape are incompatible with `pylist`. |