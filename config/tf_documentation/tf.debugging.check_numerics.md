# tf.debugging.check_numerics

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/debugging/check_numerics](https://tensorflow.google.cn/api_docs/python/tf/debugging/check_numerics)

---

Checks a tensor for NaN and Inf values.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.check_numerics`](https://tensorflow.google.cn/api_docs/python/tf/debugging/check_numerics)

```
tf.debugging.check_numerics(
    tensor: Annotated[Any, TV_CheckNumerics_T], message: str, name=None
) -> Annotated[Any, TV_CheckNumerics_T]
```

### Used in the notebooks

| Used in the guide |
| --- |
| * [TensorFlow graph optimization with Grappler](https://tensorflow.google.cn/guide/graph_optimization) |

When run, reports an `InvalidArgument` error if `tensor` has any values
that are not a number (NaN) or infinity (Inf). Otherwise, returns the input
tensor.

#### Example usage:

```
a = tf.Variable(1.0)
tf.debugging.check_numerics(a, message='')

b = tf.Variable(np.nan)
try:
  tf.debugging.check_numerics(b, message='Checking b')
except Exception as e:
  assert "Checking b : Tensor had NaN values" in e.message

c = tf.Variable(np.inf)
try:
  tf.debugging.check_numerics(c, message='Checking c')
except Exception as e:
  assert "Checking c : Tensor had Inf values" in e.message
```

| Args | |

|  |  |
| --- | --- |
| `tensor` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `message` | A `string`. Prefix of the error message. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `tensor`. | |