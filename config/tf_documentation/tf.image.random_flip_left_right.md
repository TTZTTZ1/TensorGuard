# tf.image.random_flip_left_right

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/random_flip_left_right](https://tensorflow.google.cn/api_docs/python/tf/image/random_flip_left_right)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L383-L428) |

Randomly flip an image horizontally (left to right).

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.random_flip_left_right`](https://tensorflow.google.cn/api_docs/python/tf/image/random_flip_left_right)

```
tf.image.random_flip_left_right(
    image, seed=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [CycleGAN](https://tensorflow.google.cn/tutorials/generative/cyclegan) |

With a 1 in 2 chance, outputs the contents of `image` flipped along the
second dimension, which is `width`. Otherwise output the image as-is.
When passing a batch of images, each image will be randomly flipped
independent of other images.

#### Example usage:

```
>>> image = np.array([[[1], [2]], [[3], [4]]])
>>> tf.image.random_flip_left_right(image, 5).numpy().tolist()
[[[2], [1]], [[4], [3]]]
```

Randomly flip multiple images.

```
>>> images = np.array(
... [
...     [[[1], [2]], [[3], [4]]],
...     [[[5], [6]], [[7], [8]]]
... ])
>>> tf.image.random_flip_left_right(images, 6).numpy().tolist()
[[[[2], [1]], [[4], [3]]], [[[5], [6]], [[7], [8]]]]
```

For producing deterministic results given a `seed` value, use
[`tf.image.stateless_random_flip_left_right`](https://tensorflow.google.cn/api_docs/python/tf/image/stateless_random_flip_left_right). Unlike using the `seed` param
with `tf.image.random_*` ops, `tf.image.stateless_random_*` ops guarantee the
same results given the same seed independent of how many times the function is
called, and independent of global seed settings (e.g. tf.random.set\_seed).

| Args | |

|  |  |
| --- | --- |
| `image` | 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor of shape `[height, width, channels]`. |
| `seed` | A Python integer. Used to create a random seed. See [`tf.compat.v1.set_random_seed`](https://tensorflow.google.cn/api_docs/python/tf/compat/v1/set_random_seed) for behavior. |

| Returns | |
| A tensor of the same type and shape as `image`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if the shape of `image` not supported. |