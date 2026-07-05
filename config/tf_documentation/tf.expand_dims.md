# tf.expand_dims

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/expand_dims](https://tensorflow.google.cn/api_docs/python/tf/expand_dims)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/array_ops.py#L391-L458) |

Returns a tensor with a length 1 axis inserted at index `axis`.

```
tf.expand_dims(
    input, axis, name=None
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Extension types](https://tensorflow.google.cn/guide/extension_type) * [Import a JAX model using JAX2TF](https://tensorflow.google.cn/guide/jax2tf) * [Migrate `tf.feature\_column`s to Keras preprocessing layers](https://tensorflow.google.cn/guide/migrate/migrating_feature_columns) * [Understanding masking & padding](https://tensorflow.google.cn/guide/keras/understanding_masking_and_padding) * [Working with RNNs](https://tensorflow.google.cn/guide/keras/working_with_rnns) | * [Integrated gradients](https://tensorflow.google.cn/tutorials/interpretability/integrated_gradients) * [Playing CartPole with the Actor-Critic method](https://tensorflow.google.cn/tutorials/reinforcement_learning/actor_critic) * [Generate music with an RNN](https://tensorflow.google.cn/tutorials/audio/music_generation) * [DeepDream](https://tensorflow.google.cn/tutorials/generative/deepdream) * [pix2pix: Image-to-image translation with a conditional GAN](https://tensorflow.google.cn/tutorials/generative/pix2pix) |

Given a tensor `input`, this operation inserts a dimension of length 1 at the
dimension index `axis` of `input`'s shape. The dimension index follows Python
indexing rules: It's zero-based, a negative index it is counted backward
from the end.

This operation is useful to:

* Add an outer "batch" dimension to a single element.
* Align axes for broadcasting.
* To add an inner vector length axis to a tensor of scalars.

#### For example:

If you have a single image of shape `[height, width, channels]`:

```
>>> image = tf.zeros([10,10,3])
```

You can add an outer `batch` axis by passing `axis=0`:

```
>>> tf.expand_dims(image, axis=0).shape.as_list()
[1, 10, 10, 3]
```

The new axis location matches Python `list.insert(axis, 1)`:

```
>>> tf.expand_dims(image, axis=1).shape.as_list()
[10, 1, 10, 3]
```

Following standard Python indexing rules, a negative `axis` counts from the
end so `axis=-1` adds an inner most dimension:

```
>>> tf.expand_dims(image, -1).shape.as_list()
[10, 10, 3, 1]
```

This operation requires that `axis` is a valid index for `input.shape`,
following Python indexing rules:

```
-1-tf.rank(input) <= axis <= tf.rank(input)
```

This operation is related to:

* [`tf.squeeze`](https://tensorflow.google.cn/api_docs/python/tf/squeeze), which removes dimensions of size 1.
* [`tf.reshape`](https://tensorflow.google.cn/api_docs/python/tf/reshape), which provides more flexible reshaping capability.
* [`tf.sparse.expand_dims`](https://tensorflow.google.cn/api_docs/python/tf/sparse/expand_dims), which provides this functionality for
  [`tf.SparseTensor`](https://tensorflow.google.cn/api_docs/python/tf/sparse/SparseTensor)

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. |
| `axis` | Integer specifying the dimension index at which to expand the shape of `input`. Given an input of D dimensions, `axis` must be in range `[-(D+1), D]` (inclusive). |
| `name` | Optional string. The name of the output `Tensor`. |

| Returns | |
| A tensor with the same data as `input`, with an additional dimension inserted at the index specified by `axis`. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If `axis` is not specified. |
| `InvalidArgumentError` | If `axis` is out of range `[-(D+1), D]`. |