# tf.get_current_name_scope

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/get_current_name_scope](https://tensorflow.google.cn/api_docs/python/tf/get_current_name_scope)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/ops.py#L5666-L5698) |

Returns current full name scope specified by [`tf.name_scope(...)`](https://tensorflow.google.cn/api_docs/python/tf/name_scope)s.

```
tf.get_current_name_scope() -> str
```

For example,

```
with tf.name_scope("outer"):
  tf.get_current_name_scope()  # "outer"

  with tf.name_scope("inner"):
    tf.get_current_name_scope()  # "outer/inner"
```

In other words, [`tf.get_current_name_scope()`](https://tensorflow.google.cn/api_docs/python/tf/get_current_name_scope) returns the op name prefix that
will be prepended to, if an op is created at that place.

Note that [`@tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) resets the name scope stack as shown below.

```
with tf.name_scope("outer"):

  @tf.function
  def foo(x):
    with tf.name_scope("inner"):
      return tf.add(x * x)  # Op name is "inner/Add", not "outer/inner/Add"
```