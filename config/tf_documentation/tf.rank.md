# tf.rank

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/rank](https://tensorflow.google.cn/api_docs/python/tf/rank)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L877-L910) |

Returns the rank of a tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.rank`](https://tensorflow.google.cn/api_docs/python/tf/rank)

```
tf.rank(
    input, name=None
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Introduction to Tensors](https://tensorflow.google.cn/guide/tensor) |

See also [`tf.shape`](https://tensorflow.google.cn/api_docs/python/tf/shape).

Returns a 0-D `int32` `Tensor` representing the rank of `input`.

#### For example:

```
# shape of tensor 't' is [2, 2, 3]
t = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
tf.rank(t)  # 3
```

**Note:** The rank of a tensor is not the same as the rank of a matrix. The
rank of a tensor is the number of indices required to uniquely select each
element of the tensor. Rank is also known as "order", "degree", or "ndims."

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor` or `SparseTensor`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `int32`. | |

## numpy compatibility

Equivalent to np.ndim