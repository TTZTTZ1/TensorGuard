# tf.debugging.assert_equal

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_equal](https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_equal)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/check_ops.py#L762-L767) |

Assert the condition `x == y` holds element-wise.

#### View aliases

**Main aliases**

[`tf.assert_equal`](https://tensorflow.google.cn/api_docs/python/tf/debugging/assert_equal)

```
tf.debugging.assert_equal(
    x, y, message=None, summarize=None, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Bayesian Modeling with Joint Distribution](https://tensorflow.google.cn/probability/examples/Modeling_with_JointDistribution) * [TensorFlow Probability Case Study: Covariance Estimation](https://tensorflow.google.cn/probability/examples/TensorFlow_Probability_Case_Study_Covariance_Estimation) |

This Op checks that `x[i] == y[i]` holds for every pair of (possibly
broadcast) elements of `x` and `y`. If both `x` and `y` are empty, this is
trivially satisfied.

If `x` == `y` does not hold, `message`, as well as the first `summarize`
entries of `x` and `y` are printed, and `InvalidArgumentError` is raised.

When using inside [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function), this API takes effects during execution.
It's recommended to use this API with [`tf.control_dependencies`](https://tensorflow.google.cn/api_docs/python/tf/control_dependencies) to
ensure the correct execution order.

In the following example, without [`tf.control_dependencies`](https://tensorflow.google.cn/api_docs/python/tf/control_dependencies), errors may
not be raised at all.
Check [`tf.control_dependencies`](https://tensorflow.google.cn/api_docs/python/tf/control_dependencies) for more details.

```
>>> def check_size(x):
...   with tf.control_dependencies([
...       tf.debugging.assert_equal(tf.size(x), 3,
...                       message='Bad tensor size')]):
...     return x
```

```
>>> check_size(tf.ones([2, 3], tf.float32))
Traceback (most recent call last):
... 
InvalidArgumentError: ...
```

| Args | |

|  |  |
| --- | --- |
| `x` | Numeric `Tensor`. |
| `y` | Numeric `Tensor`, same dtype as and broadcastable to `x`. |
| `message` | A string to prefix to the default message. (optional) |
| `summarize` | Print this many entries of each tensor. (optional) |
| `name` | A name for this operation (optional). Defaults to "assert\_equal". |

| Returns | |
| Op that raises `InvalidArgumentError` if `x == y` is False. This can be used with [`tf.control_dependencies`](https://tensorflow.google.cn/api_docs/python/tf/control_dependencies) inside of [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function)s to block followup computation until the check has executed. | |

| Raises | |

|  |  |
| --- | --- |
| `InvalidArgumentError` | if the check can be performed immediately and `x == y` is False. The check can be performed immediately during eager execution or if `x` and `y` are statically known. |

## eager compatibility

returns None