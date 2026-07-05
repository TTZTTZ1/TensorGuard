# tf.image.random_saturation

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/random_saturation](https://tensorflow.google.cn/api_docs/python/tf/image/random_saturation)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L3006-L3055) |

Adjust the saturation of RGB images by a random factor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.random_saturation`](https://tensorflow.google.cn/api_docs/python/tf/image/random_saturation)

```
tf.image.random_saturation(
    image, lower, upper, seed=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Fine tuning models for plant disease detection](https://tensorflow.google.cn/hub/tutorials/cropnet_on_device) |

Equivalent to `adjust_saturation()` but uses a `saturation_factor` randomly
picked in the interval `[lower, upper)`.

#### Usage Example:

```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0]],
...     [[7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]]]
>>> tf.image.random_saturation(x, 5, 10)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
array([[[ 0. ,  1.5,  3. ],
        [ 0. ,  3. ,  6. ]],
       [[ 0. ,  4.5,  9. ],
        [ 0. ,  6. , 12. ]]], dtype=float32)>
```

For producing deterministic results given a `seed` value, use
[`tf.image.stateless_random_saturation`](https://tensorflow.google.cn/api_docs/python/tf/image/stateless_random_saturation). Unlike using the `seed` param
with `tf.image.random_*` ops, `tf.image.stateless_random_*` ops guarantee the
same results given the same seed independent of how many times the function is
called, and independent of global seed settings (e.g. tf.random.set\_seed).

| Args | |

|  |  |
| --- | --- |
| `image` | RGB image or images. The size of the last dimension must be 3. |
| `lower` | float. Lower bound for the random saturation factor. |
| `upper` | float. Upper bound for the random saturation factor. |
| `seed` | An operation-specific seed. It will be used in conjunction with the graph-level seed to determine the real seeds that will be used in this operation. Please see the documentation of set\_random\_seed for its interaction with the graph-level random seed. |

| Returns | |
| Adjusted image(s), same shape and DType as `image`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | if `upper <= lower` or if `lower < 0`. |