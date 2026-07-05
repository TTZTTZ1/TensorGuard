# tf.name_scope

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/name_scope](https://tensorflow.google.cn/api_docs/python/tf/name_scope)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/ops.py#L5701-L5793) |

A context manager for use when defining a Python op.

```
tf.name_scope(
    name
) -> None
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrating model checkpoints](https://tensorflow.google.cn/guide/migrate/migrating_checkpoints) | * [Displaying text data in TensorBoard](https://tensorflow.google.cn/tensorboard/text_summaries) * [Graph-based Neural Structured Learning in TFX](https://tensorflow.google.cn/tfx/tutorials/tfx/neural_structured_learning) |

This context manager pushes a name scope, which will make the name of all
operations added within it have a prefix.

For example, to define a new Python op called `my_op`:

```
def my_op(a, b, c, name=None):
  with tf.name_scope("MyOp") as scope:
    a = tf.convert_to_tensor(a, name="a")
    b = tf.convert_to_tensor(b, name="b")
    c = tf.convert_to_tensor(c, name="c")
    # Define some computation that uses `a`, `b`, and `c`.
    return foo_op(..., name=scope)
```

When executed, the Tensors `a`, `b`, `c`, will have names `MyOp/a`, `MyOp/b`,
and `MyOp/c`.

Inside a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function), if the scope name already exists, the name will be
made unique by appending `_n`. For example, calling `my_op` the second time
will generate `MyOp_1/a`, etc.

| Args | |

|  |  |
| --- | --- |
| `name` | The prefix to use on all names created within the name scope. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If name is not a string. |

| Attributes | |

|  |  |
| --- | --- |
| `name` |  |

## Methods

### `__enter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/ops.py#L5748-L5780)

```
__enter__() -> str
```

Start the scope block.

| Returns | |
| The scope name. | |

### `__exit__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/ops.py#L5782-L5786)

```
__exit__(
    type_arg: None, value_arg: None, traceback_arg: None
) -> bool
```

Raise any exception triggered within the runtime context.