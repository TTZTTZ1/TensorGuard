# tf.is_tensor

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/is_tensor](https://tensorflow.google.cn/api_docs/python/tf/is_tensor)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_util.py#L1128-L1156) |

Checks whether `x` is a TF-native type that can be passed to many TF ops.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.is_tensor`](https://tensorflow.google.cn/api_docs/python/tf/is_tensor)

```
tf.is_tensor(
    x
)
```

Use `is_tensor` to differentiate types that can ingested by TensorFlow ops
without any conversion (e.g., [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor), [`tf.SparseTensor`](https://tensorflow.google.cn/api_docs/python/tf/sparse/SparseTensor), and
[`tf.RaggedTensor`](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensor)) from types that need to be converted into tensors before
they are ingested (e.g., numpy `ndarray` and Python scalars).

For example, in the following code block:

```
if not tf.is_tensor(t):
  t = tf.convert_to_tensor(t)
return t.shape, t.dtype
```

we check to make sure that `t` is a tensor (and convert it if not) before
accessing its `shape` and `dtype`. (But note that not all TensorFlow native
types have shapes or dtypes; [`tf.data.Dataset`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset) is an example of a TensorFlow
native type that has neither shape nor dtype.)

| Args | |

|  |  |
| --- | --- |
| `x` | A python object to check. |

| Returns | |
| `True` if `x` is a TensorFlow-native type. | |