# tf.meshgrid

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/meshgrid](https://tensorflow.google.cn/api_docs/python/tf/meshgrid)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L3344-L3423) |

Broadcasts parameters for evaluation on an N-D grid.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.meshgrid`](https://tensorflow.google.cn/api_docs/python/tf/meshgrid)

```
tf.meshgrid(
    *args, **kwargs
)
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [Optimizers with Core APIs](https://tensorflow.google.cn/guide/core/optimizers_core) |

Given N one-dimensional coordinate arrays `*args`, returns a list `outputs`
of N-D coordinate arrays for evaluating expressions on an N-D grid.

#### Notes:

`meshgrid` supports cartesian ('xy') and matrix ('ij') indexing conventions.
When the `indexing` argument is set to 'xy' (the default), the broadcasting
instructions for the first two dimensions are swapped.

#### Examples:

Calling `X, Y = meshgrid(x, y)` with the tensors

```
x = [1, 2, 3]
y = [4, 5, 6]
X, Y = tf.meshgrid(x, y)
# X = [[1, 2, 3],
#      [1, 2, 3],
#      [1, 2, 3]]
# Y = [[4, 4, 4],
#      [5, 5, 5],
#      [6, 6, 6]]
```

| Args | |

|  |  |
| --- | --- |
| `*args` | `Tensor`s with rank 1. |
| `**kwargs` |  |

* indexing: Either 'xy' or 'ij' (optional, default: 'xy').
* name: A name for the operation (optional).

| Returns | |

|  |  |
| --- | --- |
| `outputs` | A list of N `Tensor`s with rank N. |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | When no keyword arguments (kwargs) are passed. |
| `ValueError` | When indexing keyword argument is not one of `xy` or `ij`. |