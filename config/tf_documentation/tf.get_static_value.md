# tf.get_static_value

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/get_static_value](https://tensorflow.google.cn/api_docs/python/tf/get_static_value)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_util.py#L896-L971) |

Returns the constant value of the given tensor, if efficiently calculable.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.get_static_value`](https://tensorflow.google.cn/api_docs/python/tf/get_static_value)

```
tf.get_static_value(
    tensor, partial=False
)
```

### Used in the notebooks

| Used in the tutorials |
| --- |
| * [Bayesian Modeling with Joint Distribution](https://tensorflow.google.cn/probability/examples/Modeling_with_JointDistribution) |

This function attempts to partially evaluate the given tensor, and
returns its value as a numpy ndarray if this succeeds.

#### Example usage:

```
>>> a = tf.constant(10)
>>> tf.get_static_value(a)
10
>>> b = tf.constant(20)
>>> tf.get_static_value(tf.add(a, b))
30
```

```
>>> # `tf.Variable` is not supported.
>>> c = tf.Variable(30)
>>> print(tf.get_static_value(c))
None
```

Using `partial` option is most relevant when calling `get_static_value` inside
a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function). Setting it to `True` will return the results but for the
values that cannot be evaluated will be `None`. For example:

```
class Foo:
  def __init__(self):
    self.a = tf.Variable(1)
    self.b = tf.constant(2)

  @tf.function
  def bar(self, partial):
    packed = tf.raw_ops.Pack(values=[self.a, self.b])
    static_val = tf.get_static_value(packed, partial=partial)
    tf.print(static_val)

f = Foo()
f.bar(partial=True)  # `array([None, array(2, dtype=int32)], dtype=object)`
f.bar(partial=False)  # `None`
```

Compatibility(V1): If `constant_value(tensor)` returns a non-`None` result, it
will no longer be possible to feed a different value for `tensor`. This allows
the result of this function to influence the graph that is constructed, and
permits static shape optimizations.

| Args | |

|  |  |
| --- | --- |
| `tensor` | The Tensor to be evaluated. |
| `partial` | If True, the returned numpy array is allowed to have partially evaluated values. Values that can't be evaluated will be None. |

| Returns | |
| A numpy ndarray containing the constant value of the given `tensor`, or None if it cannot be calculated. | |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | if tensor is not an tensor.Tensor. |