# tf.logical_not

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/logical_not](https://tensorflow.google.cn/api_docs/python/tf/logical_not)

---

Returns the truth value of `NOT x` element-wise.

#### View aliases

**Main aliases**

[`tf.logical_not`](https://tensorflow.google.cn/api_docs/python/tf/math/logical_not)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.logical_not`](https://tensorflow.google.cn/api_docs/python/tf/math/logical_not), [`tf.compat.v1.math.logical_not`](https://tensorflow.google.cn/api_docs/python/tf/math/logical_not)

```
tf.math.logical_not(
    x: Annotated[Any, tf.raw_ops.Any],
    name=None
) -> Annotated[Any, tf.raw_ops.Any]

tf.raw_ops.Any
tf.raw_ops.Any
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Private Heavy Hitters](https://tensorflow.google.cn/federated/tutorials/private_heavy_hitters) * [Client-efficient large-model federated learning via `federated\_select` and sparse aggregation](https://tensorflow.google.cn/federated/tutorials/sparse_federated_learning) |

#### Example:

```
>>> tf.math.logical_not(tf.constant([True, False]))
<tf.Tensor: shape=(2,), dtype=bool, numpy=array([False,  True])>
```

| Args | |

|  |  |
| --- | --- |
| `x` | A `Tensor` of type `bool`. A `Tensor` of type `bool`. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `bool`. | |