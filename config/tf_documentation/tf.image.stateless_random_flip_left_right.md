# tf.image.stateless_random_flip_left_right

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/stateless_random_flip_left_right](https://tensorflow.google.cn/api_docs/python/tf/image/stateless_random_flip_left_right)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L431-L459) |

Randomly flip an image horizontally (left to right) deterministically.

```
tf.image.stateless_random_flip_left_right(
    image, seed
)
```

Guarantees the same results given the same `seed` independent of how many
times the function is called, and independent of global seed settings (e.g.
[`tf.random.set_seed`](https://tensorflow.google.cn/api_docs/python/tf/random/set_seed)).

#### Example usage:

```
>>> image = np.array([[[1], [2]], [[3], [4]]])
>>> seed = (2, 3)
>>> tf.image.stateless_random_flip_left_right(image, seed).numpy().tolist()
[[[2], [1]], [[4], [3]]]
```

| Args | |

|  |  |
| --- | --- |
| `image` | 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor of shape `[height, width, channels]`. |
| `seed` | A shape [2] Tensor, the seed to the random number generator. Must have dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.) |

| Returns | |
| A tensor of the same type and shape as `image`. | |