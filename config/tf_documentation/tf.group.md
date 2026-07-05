# tf.group

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/group](https://tensorflow.google.cn/api_docs/python/tf/group)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/control_flow_ops.py#L1958-L2034) |

Create an op that groups multiple operations.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.group`](https://tensorflow.google.cn/api_docs/python/tf/group)

```
tf.group(
    *inputs, **kwargs
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrating model checkpoints](https://tensorflow.google.cn/guide/migrate/migrating_checkpoints) * [Estimators](https://tensorflow.google.cn/guide/estimator) * [Validating correctness & numerical equivalence](https://tensorflow.google.cn/guide/migrate/validate_correctness) | * [Wiki40B Language Models](https://tensorflow.google.cn/hub/tutorials/wiki40b_lm) |

When this op finishes, all ops in `inputs` have finished. This op has no
output.

**Note:** *In TensorFlow 2 with eager and/or Autograph, you should not require
this method, as ops execute in the expected order thanks to automatic control
dependencies.* Only use [`tf.group`](https://tensorflow.google.cn/api_docs/python/tf/group) when working with v1
[`tf.Graph`](https://tensorflow.google.cn/api_docs/python/tf/Graph) code.

When operating in a v1-style graph context, ops are not executed in the same
order as specified in the code; TensorFlow will attempt to execute ops in
parallel or in an order convenient to the result it is computing. [`tf.group`](https://tensorflow.google.cn/api_docs/python/tf/group)
allows you to request that one or more results finish before execution
continues.

[`tf.group`](https://tensorflow.google.cn/api_docs/python/tf/group) creates a single op (of type `NoOp`), and then adds appropriate
control dependencies. Thus, `c = tf.group(a, b)` will compute the same graph
as this:

```
with tf.control_dependencies([a, b]):
    c = tf.no_op()
```

See also [`tf.tuple`](https://tensorflow.google.cn/api_docs/python/tf/tuple) and
[`tf.control_dependencies`](https://tensorflow.google.cn/api_docs/python/tf/control_dependencies).

| Args | |

|  |  |
| --- | --- |
| `*inputs` | Zero or more tensors to group. |
| `name` | A name for this operation (optional). |

| Returns | |
| An Operation that executes all its inputs. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If an unknown keyword argument is provided. |