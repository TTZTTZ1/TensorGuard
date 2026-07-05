# tf.image.is_jpeg

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/image/is_jpeg](https://tensorflow.google.cn/api_docs/python/tf/image/is_jpeg)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/image_ops_impl.py#L3163-L3180) |

Convenience function to check if the 'contents' encodes a JPEG image.

#### View aliases

**Main aliases**

[`tf.image.is_jpeg`](https://tensorflow.google.cn/api_docs/python/tf/io/is_jpeg)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.image.is_jpeg`](https://tensorflow.google.cn/api_docs/python/tf/io/is_jpeg), [`tf.compat.v1.io.is_jpeg`](https://tensorflow.google.cn/api_docs/python/tf/io/is_jpeg)

```
tf.io.is_jpeg(
    contents, name=None
)
```

| Args | |

|  |  |
| --- | --- |
| `contents` | 0-D `string`. The encoded image bytes. |
| `name` | A name for the operation (optional) |

| Returns | |
| A scalar boolean tensor indicating if 'contents' may be a JPEG image. is\_jpeg is susceptible to false positives. | |