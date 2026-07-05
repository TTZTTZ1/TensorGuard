# tf.image.stateless_random_contrast

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/stateless_random_contrast](https://tensorflow.google.cn/api_docs/python/tf/image/stateless_random_contrast)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L2153-L2197) |

Adjust the contrast of images by a random factor deterministically.

```
tf.image.stateless_random_contrast(
    image, lower, upper, seed
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Data augmentation](https://tensorflow.google.cn/tutorials/images/data_augmentation) |

Guarantees the same results given the same `seed` independent of how many
times the function is called, and independent of global seed settings (e.g.
[`tf.random.set_seed`](https://tensorflow.google.cn/api_docs/python/tf/random/set_seed)).

| Args | |

|  |  |
| --- | --- |
| `image` | An image tensor with 3 or more dimensions. |
| `lower` | float. Lower bound for the random contrast factor. |
| `upper` | float. Upper bound for the random contrast factor. |
| `seed` | A shape [2] Tensor, the seed to the random number generator. Must have dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.) |

#### Usage Example:

```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0]],
...      [[7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]]]
>>> seed = (1, 2)
>>> tf.image.stateless_random_contrast(x, 0.2, 0.5, seed)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
array([[[3.4605184, 4.4605184, 5.4605184],
        [4.820173 , 5.820173 , 6.820173 ]],
       [[6.179827 , 7.179827 , 8.179828 ],
        [7.5394816, 8.539482 , 9.539482 ]]], dtype=float32)>
```

| Returns | |
| The contrast-adjusted image(s). | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if `upper <= lower` or if `lower < 0`. |