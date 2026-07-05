# tf.linalg.global_norm

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linalg/global_norm](https://tensorflow.google.cn/api_docs/python/tf/linalg/global_norm)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/clip_ops.py#L245-L295) |

Computes the global norm of multiple tensors.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.global_norm`](https://tensorflow.google.cn/api_docs/python/tf/linalg/global_norm), [`tf.compat.v1.linalg.global_norm`](https://tensorflow.google.cn/api_docs/python/tf/linalg/global_norm)

```
tf.linalg.global_norm(
    t_list, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Composing Learning Algorithms](https://tensorflow.google.cn/federated/tutorials/composing_learning_algorithms) |

Given a tuple or list of tensors `t_list`, this operation returns the
global norm of the elements in all tensors in `t_list`. The global norm is
computed as:

`global_norm = sqrt(sum([l2norm(t)**2 for t in t_list]))`

Any entries in `t_list` that are of type None are ignored.

| Args | |

|  |  |
| --- | --- |
| `t_list` | A tuple or list of mixed `Tensors`, `IndexedSlices`, or None. |
| `name` | A name for the operation (optional). |

| Returns | |
| A 0-D (scalar) `Tensor` of type `float`. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If `t_list` is not a sequence. |