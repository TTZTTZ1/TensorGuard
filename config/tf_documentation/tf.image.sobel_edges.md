# tf.image.sobel_edges

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/sobel_edges](https://tensorflow.google.cn/api_docs/python/tf/image/sobel_edges)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L4686-L4752) |

Returns a tensor holding Sobel edge maps.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.sobel_edges`](https://tensorflow.google.cn/api_docs/python/tf/image/sobel_edges)

```
tf.image.sobel_edges(
    image
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Neural style transfer](https://tensorflow.google.cn/tutorials/generative/style_transfer) |

#### Example usage:

For general usage, `image` would be loaded from a file as below:

```
image_bytes = tf.io.read_file(path_to_image_file)
image = tf.image.decode_image(image_bytes)
image = tf.cast(image, tf.float32)
image = tf.expand_dims(image, 0)
```

But for demo purposes, we are using randomly generated values for `image`:

```
>>> image = tf.random.uniform(
...   maxval=255, shape=[1, 28, 28, 3], dtype=tf.float32)
>>> sobel = tf.image.sobel_edges(image)
>>> sobel_y = np.asarray(sobel[0, :, :, :, 0]) # sobel in y-direction
>>> sobel_x = np.asarray(sobel[0, :, :, :, 1]) # sobel in x-direction
```

For displaying the sobel results, PIL's [Image Module](https://pillow.readthedocs.io/en/stable/reference/Image.html) can be used:

```
# Display edge maps for the first channel (at index 0)
Image.fromarray(sobel_y[..., 0] / 4 + 0.5).show()
Image.fromarray(sobel_x[..., 0] / 4 + 0.5).show()
```

| Args | |

|  |  |
| --- | --- |
| `image` | Image tensor with shape [batch\_size, h, w, d] and type float32 or float64. The image(s) must be 2x2 or larger. |

| Returns | |
| Tensor holding edge maps for each channel. Returns a tensor with shape [batch\_size, h, w, d, 2] where the last two dimensions hold [[dy[0], dx[0]], [dy[1], dx[1]], ..., [dy[d-1], dx[d-1]]] calculated using the Sobel filter. | |