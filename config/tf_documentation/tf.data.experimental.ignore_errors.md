# tf.data.experimental.ignore_errors

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/data/experimental/ignore_errors](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/ignore_errors)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/data/experimental/ops/error_ops.py#L20-L51) |

Creates a `Dataset` from another `Dataset` and silently ignores any errors. (deprecated)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.data.experimental.ignore_errors`](https://tensorflow.google.cn/api_docs/python/tf/data/experimental/ignore_errors)

```
tf.data.experimental.ignore_errors(
    log_warning=False
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Image captioning with visual attention](https://tensorflow.google.cn/text/tutorials/image_captioning) |

**Deprecated:** THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use [`tf.data.Dataset.ignore_errors`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#ignore_errors) instead.

Use this transformation to produce a dataset that contains the same elements
as the input, but silently drops any elements that caused an error. For
example:

```
dataset = tf.data.Dataset.from_tensor_slices([1., 2., 0., 4.])

# Computing `tf.debugging.check_numerics(1. / 0.)` will raise an
InvalidArgumentError.
dataset = dataset.map(lambda x: tf.debugging.check_numerics(1. / x, "error"))

# Using `ignore_errors()` will drop the element that causes an error.
dataset =
    dataset.apply(tf.data.experimental.ignore_errors())  # ==> {1., 0.5, 0.2}
```

Args:
log\_warning: (Optional.) A 'tf.bool' scalar indicating whether ignored
errors should be logged to stderr. Defaults to 'False'.

| Returns | |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://tensorflow.google.cn/api_docs/python/tf/data/Dataset#apply). | |