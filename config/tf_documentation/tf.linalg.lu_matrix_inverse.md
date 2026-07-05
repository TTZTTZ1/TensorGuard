# tf.linalg.lu_matrix_inverse

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linalg/lu_matrix_inverse](https://tensorflow.google.cn/api_docs/python/tf/linalg/lu_matrix_inverse)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/linalg/linalg_impl.py#L1035-L1097) |

Computes the inverse given the LU decomposition(s) of one or more matrices.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.linalg.lu_matrix_inverse`](https://tensorflow.google.cn/api_docs/python/tf/linalg/lu_matrix_inverse)

```
tf.linalg.lu_matrix_inverse(
    lower_upper, perm, validate_args=False, name=None
)
```

This op is conceptually identical to,

```
inv_X = tf.lu_matrix_inverse(*tf.linalg.lu(X))
tf.assert_near(tf.matrix_inverse(X), inv_X)
# ==> True
```

**Note:** this function does not verify the implied matrix is actually invertible
nor is this condition checked even when `validate_args=True`.

| Args | |

|  |  |
| --- | --- |
| `lower_upper` | `lu` as returned by [`tf.linalg.lu`](https://tensorflow.google.cn/api_docs/python/tf/linalg/lu), i.e., if `matmul(P, matmul(L, U)) = X` then `lower_upper = L + U - eye`. |
| `perm` | `p` as returned by `tf.linag.lu`, i.e., if `matmul(P, matmul(L, U)) = X` then `perm = argmax(P)`. |
| `validate_args` | Python `bool` indicating whether arguments should be checked for correctness. Note: this function does not verify the implied matrix is actually invertible, even when `validate_args=True`. Default value: `False` (i.e., don't validate arguments). |
| `name` | Python `str` name given to ops managed by this object. Default value: `None` (i.e., 'lu\_matrix\_inverse'). |

| Returns | |

|  |  |
| --- | --- |
| `inv_x` | The matrix\_inv, i.e., `tf.matrix_inverse(tf.linalg.lu_reconstruct(lu, perm))`. |

#### Examples

```
import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp

x = [[[3., 4], [1, 2]],
     [[7., 8], [3, 4]]]
inv_x = tf.linalg.lu_matrix_inverse(*tf.linalg.lu(x))
tf.assert_near(tf.matrix_inverse(x), inv_x)
# ==> True
```