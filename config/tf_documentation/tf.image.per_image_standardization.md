# tf.image.per_image_standardization

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/per_image_standardization](https://tensorflow.google.cn/api_docs/python/tf/image/per_image_standardization)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L1957-L2013) |

Linearly scales each image in `image` to have mean 0 and variance 1.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.per_image_standardization`](https://tensorflow.google.cn/api_docs/python/tf/image/per_image_standardization)

```
tf.image.per_image_standardization(
    image
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [TFF simulations with accelerators](https://tensorflow.google.cn/federated/tutorials/simulations_with_accelerators) |

For each 3-D image `x` in `image`, computes `(x - mean) / adjusted_stddev`,
where

* `mean` is the average of all values in `x`
* `adjusted_stddev = max(stddev, 1.0/sqrt(N))` is capped away from 0 to
  protect against division by 0 when handling uniform images
  + `N` is the number of elements in `x`
  + `stddev` is the standard deviation of all values in `x`

#### Example Usage:

```
>>> image = tf.constant(np.arange(1, 13, dtype=np.int32), shape=[2, 2, 3])
>>> image # 3-D tensor
<tf.Tensor: shape=(2, 2, 3), dtype=int32, numpy=
array([[[ 1,  2,  3],
        [ 4,  5,  6]],
       [[ 7,  8,  9],
        [10, 11, 12]]], dtype=int32)>
>>> new_image = tf.image.per_image_standardization(image)
>>> new_image # 3-D tensor with mean ~= 0 and variance ~= 1
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
array([[[-1.593255  , -1.3035723 , -1.0138896 ],
        [-0.7242068 , -0.4345241 , -0.14484136]],
       [[ 0.14484136,  0.4345241 ,  0.7242068 ],
        [ 1.0138896 ,  1.3035723 ,  1.593255  ]]], dtype=float32)>
```

| Args | |

|  |  |
| --- | --- |
| `image` | An n-D `Tensor` with at least 3 dimensions, the last 3 of which are the dimensions of each image. |

| Returns | |
| A `Tensor` with the same shape as `image` and its dtype is `float32`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | The shape of `image` has fewer than 3 dimensions. |