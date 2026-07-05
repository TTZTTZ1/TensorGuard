# tf.ones

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/ones](https://tensorflow.google.cn/api_docs/python/tf/ones)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L2883-L2939) |

Creates a tensor with all elements set to one (1).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.ones`](https://tensorflow.google.cn/api_docs/python/tf/ones)

```
tf.ones(
    shape,
    dtype=tf.dtypes.float32,
    name=None,
    layout=None
)

tf.dtypes.float32
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Validating correctness & numerical equivalence](https://tensorflow.google.cn/guide/migrate/validate_correctness) * [Use TF1.x models in TF2 workflows](https://tensorflow.google.cn/guide/migrate/model_mapping) * [Better performance with tf.function](https://tensorflow.google.cn/guide/function) * [Extension types](https://tensorflow.google.cn/guide/extension_type) * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) | * [Multilevel Modeling Primer in TensorFlow Probability](https://tensorflow.google.cn/probability/examples/Multilevel_Modeling_Primer) * [Learnable Distributions Zoo](https://tensorflow.google.cn/probability/examples/Learnable_Distributions_Zoo) * [Probabilistic PCA](https://tensorflow.google.cn/probability/examples/Probabilistic_PCA) * [Policies](https://tensorflow.google.cn/agents/tutorials/3_policies_tutorial) * [Bayesian Switchpoint Analysis](https://tensorflow.google.cn/probability/examples/Bayesian_Switchpoint_Analysis) |

See also [`tf.ones_like`](https://tensorflow.google.cn/api_docs/python/tf/ones_like), [`tf.zeros`](https://tensorflow.google.cn/api_docs/python/tf/zeros), [`tf.fill`](https://tensorflow.google.cn/api_docs/python/tf/fill), [`tf.eye`](https://tensorflow.google.cn/api_docs/python/tf/eye).

This operation returns a tensor of type `dtype` with shape `shape` and
all elements set to one.

```
>>> tf.ones([3, 4], tf.int32)
<tf.Tensor: shape=(3, 4), dtype=int32, numpy=
array([[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]], dtype=int32)>
```

| Args | |

|  |  |
| --- | --- |
| `shape` | A `list` of integers, a `tuple` of integers, or a 1-D `Tensor` of type `int32`. |
| `dtype` | Optional DType of an element in the resulting `Tensor`. Default is [`tf.float32`](https://tensorflow.google.cn/api_docs/python/tf#float32). |
| `name` | Optional string. A name for the operation. |
| `layout` | Optional, [`tf.experimental.dtensor.Layout`](https://tensorflow.google.cn/api_docs/python/tf/experimental/dtensor/Layout). If provided, the result is a [DTensor](https://tensorflow.google.cn/guide/dtensor_overview) with the provided layout. |

| Returns | |
| A `Tensor` with all elements set to one (1). | |