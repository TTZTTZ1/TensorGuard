# tf.image.random_brightness

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/random_brightness](https://tensorflow.google.cn/api_docs/python/tf/image/random_brightness)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L2016-L2057) |

Adjust the brightness of images by a random factor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.random_brightness`](https://tensorflow.google.cn/api_docs/python/tf/image/random_brightness)

```
tf.image.random_brightness(
    image, max_delta, seed=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Fine tuning models for plant disease detection](https://tensorflow.google.cn/hub/tutorials/cropnet_on_device) |

Equivalent to `adjust_brightness()` using a `delta` randomly picked in the
interval `[-max_delta, max_delta)`.

For producing deterministic results given a `seed` value, use
[`tf.image.stateless_random_brightness`](https://tensorflow.google.cn/api_docs/python/tf/image/stateless_random_brightness). Unlike using the `seed` param
with `tf.image.random_*` ops, `tf.image.stateless_random_*` ops guarantee the
same results given the same seed independent of how many times the function is
called, and independent of global seed settings (e.g. tf.random.set\_seed).

| Args | |

|  |  |
| --- | --- |
| `image` | An image or images to adjust. |
| `max_delta` | float, must be non-negative. This parameter controls the maximum relative change in brightness. |
| `seed` | A Python integer. Used to create a random seed. See [`tf.compat.v1.set_random_seed`](https://tensorflow.google.cn/api_docs/python/tf/compat/v1/set_random_seed) for behavior. |

#### Usage Example:

```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0]],
...      [[7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]]]
>>> tf.image.random_brightness(x, 0.2)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=...>
```

| Returns | |
| The brightness-adjusted image(s). | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if `max_delta` is negative. |