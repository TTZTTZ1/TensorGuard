# tf.debugging.Assert

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/debugging/Assert](https://tensorflow.google.cn/api_docs/python/tf/debugging/Assert)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/control_flow_assert.py#L62-L130) |

Asserts that the given condition is true.

#### View aliases

**Main aliases**

[`tf.Assert`](https://tensorflow.google.cn/api_docs/python/tf/debugging/Assert)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.Assert`](https://tensorflow.google.cn/api_docs/python/tf/debugging/Assert), [`tf.compat.v1.debugging.Assert`](https://tensorflow.google.cn/api_docs/python/tf/debugging/Assert)

```
tf.debugging.Assert(
    condition, data, summarize=None, name=None
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Client-efficient large-model federated learning via `federated\_select` and sparse aggregation](https://tensorflow.google.cn/federated/tutorials/sparse_federated_learning) |

If `condition` evaluates to false, print the list of tensors in `data`.
`summarize` determines how many entries of the tensors to print.

| Args | |

|  |  |
| --- | --- |
| `condition` | The condition to evaluate. |
| `data` | The tensors to print out when condition is false. |
| `summarize` | Print this many entries of each tensor. |
| `name` | A name for this operation (optional). |

| Returns | |

|  |  |
| --- | --- |
| `assert_op` | An `Operation` that, when executed, raises a [`tf.errors.InvalidArgumentError`](https://tensorflow.google.cn/api_docs/python/tf/errors/InvalidArgumentError) if `condition` is not true. |

| Raises | |

**Note:** The output of this function should be used. If it is not, a warning will be logged or an error may be raised. To mark the output as used, call its .mark\_used() method.

## TF1 compatibility

When in TF V1 mode (that is, outside [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function)) Assert needs a control
dependency on the output to ensure the assertion executes:

```
# Ensure maximum element of x is smaller or equal to 1
assert_op = tf.Assert(tf.less_equal(tf.reduce_max(x), 1.), [x])
with tf.control_dependencies([assert_op]):
  ... code using x ...
```