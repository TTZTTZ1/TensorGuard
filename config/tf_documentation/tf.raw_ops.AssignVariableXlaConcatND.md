# tf.raw_ops.AssignVariableXlaConcatND

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AssignVariableXlaConcatND](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AssignVariableXlaConcatND)

---

Concats input tensor across all dimensions.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.raw_ops.AssignVariableXlaConcatND`](https://tensorflow.google.cn/api_docs/python/tf/raw_ops/AssignVariableXlaConcatND)

```
tf.raw_ops.AssignVariableXlaConcatND(
    resource, inputs, num_concats, paddings=[], name=None
)
```

An op which merges slices the input tensor based on the given num\_splits
attribute, strips paddings optionally, and writes the merged tensor without
paddings to the resource variable.

This op may be generated via the TPU bridge.

For example, with `input` tensor:

```
[[0, 1],
 [4, 5]]
[[2, 3],
 [6, 7]]
[[8, 9],
 [12, 13]]
[[10, 11],
 [14, 15]]
```

`num_splits`:

```
[2, 2]
```

and `paddings`:

```
[1, 1]
```

the expected `outputs` is:

```
[[0, 1, 2],
 [4, 5, 6],
 [8, 9, 10]]
```

| Args | |

|  |  |
| --- | --- |
| `resource` | A `Tensor` of type `resource`. Resource variable for concatenated input tensors across all dimensions. } in\_arg { name: "inputs" description: < |
| `inputs` | A list of at least 1 `Tensor` objects with the same type. |
| `num_concats` | A list of `ints`. Number of ways to merge per dimension. |
| `paddings` | An optional list of `ints`. Defaults to `[]`. Optional list of right paddings per dimension to strip from the final merged tensor. These paddings must not exceed the dimension size of the merged result prior to stripping paddings. |
| `name` | A name for the operation (optional). |

| Returns | |
| The created Operation. | |