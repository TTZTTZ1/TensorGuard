# tf.math.multiply_no_nan

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/multiply_no_nan](https://tensorflow.google.cn/api_docs/python/tf/math/multiply_no_nan)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L1575-L1601) |

Computes the product of x and y and returns 0 if the y is zero, even if x is NaN or infinite.

```
tf.math.multiply_no_nan(
    x, y, name=None
)
```

#### Example:

```
import numpy as np
x = tf.constant([5.0, np.inf, np.nan])
y = tf.constant([-6.0, 0, 0])
tf.math.multiply_no_nan(x, y) ==> [-30. ,0. ,0.]

import numpy as np
x = tf.constant([-2.0, -5.0, 0, 0])
y = tf.constant([-1.0, -6, np.inf, np.nan])
tf.math.multiply_no_nan(x, y) ==> [2. ,30. ,nan ,nan]
```

Note this is noncommutative: if y is NaN or infinite and x is 0, the result
will be NaN.

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `complex64`, `complex128`. |
| `y` | A `Tensor` whose dtype is compatible with `x`. |
| `name` | A name for the operation (optional). |

| Returns | |
| The element-wise value of the x times y. | |