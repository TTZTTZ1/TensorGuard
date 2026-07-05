# tf.broadcast_to

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/broadcast_to](https://tensorflow.google.cn/api_docs/python/tf/broadcast_to)

---

Broadcast an array for a compatible shape.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.broadcast_to`](https://tensorflow.google.cn/api_docs/python/tf/broadcast_to)

```
tf.broadcast_to(
    input: Annotated[Any, TV_BroadcastTo_T],
    shape: Annotated[Any, TV_BroadcastTo_Tidx],
    name=None
) -> Annotated[Any, TV_BroadcastTo_T]
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Introduction to Tensors](https://tensorflow.google.cn/guide/tensor) | * [Eight schools](https://tensorflow.google.cn/probability/examples/Eight_Schools) * [Human Pose Classification with MoveNet and TensorFlow Lite](https://tensorflow.google.cn/lite/tutorials/pose_classification) * [FFJORD](https://tensorflow.google.cn/probability/examples/FFJORD_Demo) * [TFP Release Notes notebook (0.13.0)](https://tensorflow.google.cn/probability/examples/TFP_Release_Notebook_0_13_0) |

Broadcasting is the process of making arrays to have compatible shapes
for arithmetic operations. Two shapes are compatible if for each
dimension pair they are either equal or one of them is one.

#### For example:

```
>>> x = tf.constant([[1, 2, 3]])   # Shape (1, 3,)
>>> y = tf.broadcast_to(x, [2, 3])
>>> print(y)
tf.Tensor(
    [[1 2 3]
     [1 2 3]], shape=(2, 3), dtype=int32)
```

In the above example, the input Tensor with the shape of `[1, 3]`
is broadcasted to output Tensor with shape of `[2, 3]`.

When broadcasting, if a tensor has fewer axes than necessary its shape is
padded on the left with ones. So this gives the same result as the previous
example:

```
>>> x = tf.constant([1, 2, 3])   # Shape (3,)
>>> y = tf.broadcast_to(x, [2, 3])
```

When doing broadcasted operations such as multiplying a tensor
by a scalar, broadcasting (usually) confers some time or space
benefit, as the broadcasted tensor is never materialized.

However, `broadcast_to` does not carry with it any such benefits.
The newly-created tensor takes the full memory of the broadcasted
shape. (In a graph context, `broadcast_to` might be fused to
subsequent operation and then be optimized away, however.)

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. A Tensor to broadcast. |
| `shape` | A `Tensor`. Must be one of the following types: `int32`, `int64`. An 1-D `int` Tensor. The shape of the desired output. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |