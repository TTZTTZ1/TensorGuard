# tf.math.accumulate_n

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/accumulate_n](https://tensorflow.google.cn/api_docs/python/tf/math/accumulate_n)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L3976-L4059) |

Returns the element-wise sum of a list of tensors. (deprecated)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.accumulate_n`](https://tensorflow.google.cn/api_docs/python/tf/math/accumulate_n), [`tf.compat.v1.math.accumulate_n`](https://tensorflow.google.cn/api_docs/python/tf/math/accumulate_n)

```
tf.math.accumulate_n(
    inputs, shape=None, tensor_dtype=None, name=None
)
```

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use [`tf.math.add_n`](https://tensorflow.google.cn/api_docs/python/tf/math/add_n) Instead

Optionally, pass `shape` and `tensor_dtype` for shape and type checking,
otherwise, these are inferred.

#### For example:

```
>>> a = tf.constant([[1, 2], [3, 4]])
>>> b = tf.constant([[5, 0], [0, 6]])
>>> tf.math.accumulate_n([a, b, a]).numpy()
array([[ 7, 4],
       [ 6, 14]], dtype=int32)
```

```
>>> # Explicitly pass shape and type
>>> tf.math.accumulate_n(
...     [a, b, a], shape=[2, 2], tensor_dtype=tf.int32).numpy()
array([[ 7,  4],
       [ 6, 14]], dtype=int32)
```

**Note:** The input must be a list or tuple. This function does not handle
`IndexedSlices`

#### See Also:

* [`tf.reduce_sum(inputs, axis=0)`](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_sum) - This performe the same mathematical
  operation, but [`tf.add_n`](https://tensorflow.google.cn/api_docs/python/tf/math/add_n) may be more efficient because it sums the
  tensors directly. `reduce_sum` on the other hand calls
  [`tf.convert_to_tensor`](https://tensorflow.google.cn/api_docs/python/tf/convert_to_tensor) on the list of tensors, unncessairly stacking them
  into a single tensor before summing.
* [`tf.add_n`](https://tensorflow.google.cn/api_docs/python/tf/math/add_n) - This is another python wrapper for the same Op. It has
  nearly identical functionality.

| Args | |

|  |  |
| --- | --- |
| `inputs` | A list of `Tensor` objects, each with same shape and type. |
| `shape` | Expected shape of elements of `inputs` (optional). Also controls the output shape of this op, which may affect type inference in other ops. A value of `None` means "infer the input shape from the shapes in `inputs`". |
| `tensor_dtype` | Expected data type of `inputs` (optional). A value of `None` means "infer the input dtype from `inputs[0]`". |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of same shape and type as the elements of `inputs`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `inputs` don't all have same shape and dtype or the shape cannot be inferred. |