# tf.stack

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/stack](https://tensorflow.google.cn/api_docs/python/tf/stack)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops_stack.py#L24-L85) |

Stacks a list of rank-`R` tensors into one rank-`(R+1)` tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.stack`](https://tensorflow.google.cn/api_docs/python/tf/stack)

```
tf.stack(
    values, axis=0, name='stack'
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Extension types](https://tensorflow.google.cn/guide/extension_type) * [tf.data: Build TensorFlow input pipelines](https://tensorflow.google.cn/guide/data) * [TensorFlow basics](https://tensorflow.google.cn/guide/basics) * [Random number generation](https://tensorflow.google.cn/guide/random_numbers) | * [Time series forecasting](https://tensorflow.google.cn/tutorials/structured_data/time_series) * [Custom training: walkthrough](https://tensorflow.google.cn/tutorials/customization/custom_training_walkthrough) * [pix2pix: Image-to-image translation with a conditional GAN](https://tensorflow.google.cn/tutorials/generative/pix2pix) * [Overfit and underfit](https://tensorflow.google.cn/tutorials/keras/overfit_and_underfit) * [Load CSV data](https://tensorflow.google.cn/tutorials/load_data/csv) |

See also [`tf.concat`](https://tensorflow.google.cn/api_docs/python/tf/concat), [`tf.tile`](https://tensorflow.google.cn/api_docs/python/tf/tile), [`tf.repeat`](https://tensorflow.google.cn/api_docs/python/tf/repeat).

Packs the list of tensors in `values` into a tensor with rank one higher than
each tensor in `values`, by packing them along the `axis` dimension.
Given a list of length `N` of tensors of shape `(A, B, C)`;

if `axis == 0` then the `output` tensor will have the shape `(N, A, B, C)`.
if `axis == 1` then the `output` tensor will have the shape `(A, N, B, C)`.
Etc.

#### For example:

```
>>> x = tf.constant([1, 4])
>>> y = tf.constant([2, 5])
>>> z = tf.constant([3, 6])
>>> tf.stack([x, y, z])
<tf.Tensor: shape=(3, 2), dtype=int32, numpy=
array([[1, 4],
       [2, 5],
       [3, 6]], dtype=int32)>
>>> tf.stack([x, y, z], axis=1)
<tf.Tensor: shape=(2, 3), dtype=int32, numpy=
array([[1, 2, 3],
       [4, 5, 6]], dtype=int32)>
```

This is the opposite of unstack. The numpy equivalent is `np.stack`

```
>>> np.array_equal(np.stack([x, y, z]), tf.stack([x, y, z]))
True
```

| Args | |

|  |  |
| --- | --- |
| `values` | A list of `Tensor` objects with the same shape and type. |
| `axis` | An `int`. The axis to stack along. Defaults to the first dimension. Negative values wrap around, so the valid range is `[-(R+1), R+1)`. |
| `name` | A name for this operation (optional). |

| Returns | |

|  |  |
| --- | --- |
| `output` | A stacked `Tensor` with the same type as `values`. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `axis` is out of the range [-(R+1), R+1). |