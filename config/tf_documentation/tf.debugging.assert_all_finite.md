# tf.debugging.assert_all_finite

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_all_finite](https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_all_finite)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/numerics.py#L50-L78) |

Assert that the tensor does not contain any NaN's or Inf's.

```
tf.debugging.assert_all_finite(
    x, message, name=None
)
```

```
>>> @tf.function
... def f(x):
...   x = tf.debugging.assert_all_finite(x, 'Input x must be all finite')
...   return x + 1
```

```
>>> f(tf.constant([np.inf, 1, 2]))
Traceback (most recent call last):
... 
InvalidArgumentError: ...
```

| Args | |

|  |  |
| --- | --- |
| `x` | Tensor to check. |
| `message` | Message to log on failure. |
| `name` | A name for this operation (optional). |

| Returns | |
| Same tensor as `x`. | |