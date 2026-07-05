# tf.image.random_crop

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/random_crop](https://tensorflow.google.cn/api_docs/python/tf/image/random_crop)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/random_crop_ops.py#L30-L82) |

Randomly crops a tensor to a given size.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.random_crop`](https://tensorflow.google.cn/api_docs/python/tf/image/random_crop), [`tf.compat.v1.random_crop`](https://tensorflow.google.cn/api_docs/python/tf/image/random_crop)

```
tf.image.random_crop(
    value, size, seed=None, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [CycleGAN](https://tensorflow.google.cn/tutorials/generative/cyclegan) * [pix2pix: Image-to-image translation with a conditional GAN](https://tensorflow.google.cn/tutorials/generative/pix2pix) |

Slices a shape `size` portion out of `value` at a uniformly chosen offset.
Requires `value.shape >= size`.

If a dimension should not be cropped, pass the full size of that dimension.
For example, RGB images can be cropped with
`size = [crop_height, crop_width, 3]`.

#### Example usage:

```
>>> image = [[1, 2, 3], [4, 5, 6]]
>>> result = tf.image.random_crop(value=image, size=(1, 3))
>>> result.shape.as_list()
[1, 3]
```

For producing deterministic results given a `seed` value, use
[`tf.image.stateless_random_crop`](https://tensorflow.google.cn/api_docs/python/tf/image/stateless_random_crop). Unlike using the `seed` param with
`tf.image.random_*` ops, `tf.image.stateless_random_*` ops guarantee the same
results given the same seed independent of how many times the function is
called, and independent of global seed settings (e.g. tf.random.set\_seed).

| Args | |

|  |  |
| --- | --- |
| `value` | Input tensor to crop. |
| `size` | 1-D tensor with size the rank of `value`. |
| `seed` | Python integer. Used to create a random seed. See [`tf.random.set_seed`](https://tensorflow.google.cn/api_docs/python/tf/random/set_seed) for behavior. |
| `name` | A name for this operation (optional). |

| Returns | |
| A cropped tensor of the same rank as `value` and shape `size`. | |