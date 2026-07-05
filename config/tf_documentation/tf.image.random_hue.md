# tf.image.random_hue

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/random_hue](https://tensorflow.google.cn/api_docs/python/tf/image/random_hue)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L2636-L2682) |

Adjust the hue of RGB images by a random factor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.random_hue`](https://tensorflow.google.cn/api_docs/python/tf/image/random_hue)

```
tf.image.random_hue(
    image, max_delta, seed=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Fine tuning models for plant disease detection](https://tensorflow.google.cn/hub/tutorials/cropnet_on_device) |

Equivalent to `adjust_hue()` but uses a `delta` randomly
picked in the interval `[-max_delta, max_delta)`.

`max_delta` must be in the interval `[0, 0.5]`.

#### Usage Example:

```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0]],
...     [[7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]]]
>>> tf.image.random_hue(x, 0.2)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=...>
```

For producing deterministic results given a `seed` value, use
[`tf.image.stateless_random_hue`](https://tensorflow.google.cn/api_docs/python/tf/image/stateless_random_hue). Unlike using the `seed` param with
`tf.image.random_*` ops, `tf.image.stateless_random_*` ops guarantee the same
results given the same seed independent of how many times the function is
called, and independent of global seed settings (e.g. tf.random.set\_seed).

| Args | |

|  |  |
| --- | --- |
| `image` | RGB image or images. The size of the last dimension must be 3. |
| `max_delta` | float. The maximum value for the random delta. |
| `seed` | An operation-specific seed. It will be used in conjunction with the graph-level seed to determine the real seeds that will be used in this operation. Please see the documentation of set\_random\_seed for its interaction with the graph-level random seed. |

| Returns | |
| Adjusted image(s), same shape and DType as `image`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if `max_delta` is invalid. |