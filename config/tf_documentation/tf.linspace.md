# tf.linspace

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/linspace](https://tensorflow.google.cn/api_docs/python/tf/linspace)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L111-L224) |

Generates evenly-spaced values in an interval along a given axis.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.lin_space`](https://tensorflow.google.cn/api_docs/python/tf/linspace), [`tf.compat.v1.linspace`](https://tensorflow.google.cn/api_docs/python/tf/linspace)

```
tf.linspace(
    start, stop, num, name=None, axis=0
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Multilayer perceptrons for digit recognition with Core APIs](https://tensorflow.google.cn/guide/core/mlp_core) * [Advanced automatic differentiation](https://tensorflow.google.cn/guide/advanced_autodiff) * [Introduction to gradients and automatic differentiation](https://tensorflow.google.cn/guide/autodiff) * [Basic training loops](https://tensorflow.google.cn/guide/basic_training_loops) * [TensorFlow basics](https://tensorflow.google.cn/guide/basics) | * [Integrated gradients](https://tensorflow.google.cn/tutorials/interpretability/integrated_gradients) * [Learned data compression](https://tensorflow.google.cn/tutorials/generative/data_compression) * [Basic regression: Predict fuel efficiency](https://tensorflow.google.cn/tutorials/keras/regression) * [Scalable model compression](https://tensorflow.google.cn/tutorials/optimization/compression) * [TFP Release Notes notebook (0.12.1)](https://tensorflow.google.cn/probability/examples/TFP_Release_Notebook_0_12_1) |

A sequence of `num` evenly-spaced values are generated beginning at `start`
along a given `axis`.
If `num > 1`, the values in the sequence increase by
`(stop - start) / (num - 1)`, so that the last one is exactly `stop`.
If `num <= 0`, `ValueError` is raised.

Matches
[np.linspace](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html)'s
behaviour
except when `num == 0`.

#### For example:

```
tf.linspace(10.0, 12.0, 3, name="linspace") => [ 10.0  11.0  12.0]
```

`Start` and `stop` can be tensors of arbitrary size:

```
>>> tf.linspace([0., 5.], [10., 40.], 5, axis=0)
<tf.Tensor: shape=(5, 2), dtype=float32, numpy=
array([[ 0.  ,  5.  ],
       [ 2.5 , 13.75],
       [ 5.  , 22.5 ],
       [ 7.5 , 31.25],
       [10.  , 40.  ]], dtype=float32)>
```

`Axis` is where the values will be generated (the dimension in the
returned tensor which corresponds to the axis will be equal to `num`)

```
>>> tf.linspace([0., 5.], [10., 40.], 5, axis=-1)
<tf.Tensor: shape=(2, 5), dtype=float32, numpy=
array([[ 0.  ,  2.5 ,  5.  ,  7.5 , 10.  ],
       [ 5.  , 13.75, 22.5 , 31.25, 40.  ]], dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `start` | A `Tensor`. Must be one of the following types: `bfloat16`, `float32`, `float64`. N-D tensor. First entry in the range. |
| `stop` | A `Tensor`. Must have the same type and shape as `start`. N-D tensor. Last entry in the range. |
| `num` | A `Tensor`. Must be one of the following types: `int32`, `int64`. 0-D tensor. Number of values to generate. |
| `name` | A name for the operation (optional). |
| `axis` | Axis along which the operation is performed (used only when N-D tensors are provided). |

| Returns | |
| A `Tensor`. Has the same type as `start`. | |