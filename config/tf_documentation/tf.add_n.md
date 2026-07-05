# tf.add_n

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/add_n](https://tensorflow.google.cn/api_docs/python/tf/add_n)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/math_ops.py#L3916-L3973) |

Returns the element-wise sum of a list of tensors.

#### View aliases

**Main aliases**

[`tf.add_n`](https://tensorflow.google.cn/api_docs/python/tf/math/add_n)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.add_n`](https://tensorflow.google.cn/api_docs/python/tf/math/add_n), [`tf.compat.v1.math.add_n`](https://tensorflow.google.cn/api_docs/python/tf/math/add_n)

```
tf.math.add_n(
    inputs, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Validating correctness & numerical equivalence](https://tensorflow.google.cn/guide/migrate/validate_correctness) * [Use TF1.x models in TF2 workflows](https://tensorflow.google.cn/guide/migrate/model_mapping) * [Effective Tensorflow 2](https://tensorflow.google.cn/guide/effective_tf2) * [Distributed training with TensorFlow](https://tensorflow.google.cn/guide/distributed_training) * [Use a GPU](https://tensorflow.google.cn/guide/gpu) | * [Neural style transfer](https://tensorflow.google.cn/tutorials/generative/style_transfer) * [Custom training with tf.distribute.Strategy](https://tensorflow.google.cn/tutorials/distribute/custom_training) * [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://tensorflow.google.cn/tutorials/distribute/multi_worker_with_ctl) * [Parameter server training with ParameterServerStrategy](https://tensorflow.google.cn/tutorials/distribute/parameter_server_training) * [Overfit and underfit](https://tensorflow.google.cn/tutorials/keras/overfit_and_underfit) |

All inputs in the list must have the same shape. This op does not
[broadcast](https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html)
its inputs. If you need broadcasting, use [`tf.math.add`](https://tensorflow.google.cn/api_docs/python/tf/math/add) (or the `+` operator)
instead.

#### For example:

```
>>> a = tf.constant([[3, 5], [4, 8]])
>>> b = tf.constant([[1, 6], [2, 9]])
>>> tf.math.add_n([a, b, a]).numpy()
array([[ 7, 16],
       [10, 25]], dtype=int32)
```

#### See Also:

* [`tf.reduce_sum(inputs, axis=0)`](https://tensorflow.google.cn/api_docs/python/tf/math/reduce_sum) - This performs the same mathematical
  operation, but [`tf.add_n`](https://tensorflow.google.cn/api_docs/python/tf/math/add_n) may be more efficient because it sums the
  tensors directly. `reduce_sum` on the other hand calls
  [`tf.convert_to_tensor`](https://tensorflow.google.cn/api_docs/python/tf/convert_to_tensor) on the list of tensors, unnecessarily stacking them
  into a single tensor before summing.

| Args | |

|  |  |
| --- | --- |
| `inputs` | A list of [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) or [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices) objects, each with the same shape and type. [`tf.IndexedSlices`](https://tensorflow.google.cn/api_docs/python/tf/IndexedSlices) objects will be converted into dense tensors prior to adding. |
| `name` | A name for the operation (optional). |

| Returns | |
| A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) of the same shape and type as the elements of `inputs`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `inputs` don't all have same shape and dtype or the shape cannot be inferred. |