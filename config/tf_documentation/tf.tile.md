# tf.tile

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/tile](https://tensorflow.google.cn/api_docs/python/tf/tile)

---

Constructs a tensor by tiling a given tensor.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.manip.tile`](https://tensorflow.google.cn/api_docs/python/tf/tile), [`tf.compat.v1.tile`](https://tensorflow.google.cn/api_docs/python/tf/tile)

```
tf.tile(
    input: Annotated[Any, TV_Tile_T],
    multiples: Annotated[Any, TV_Tile_Tmultiples],
    name=None
) -> Annotated[Any, TV_Tile_T]
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Better performance with the tf.data API](https://tensorflow.google.cn/guide/data_performance) * [Ragged tensors](https://tensorflow.google.cn/guide/ragged_tensor) * [Understanding masking & padding](https://tensorflow.google.cn/guide/keras/understanding_masking_and_padding) | * [Time series forecasting](https://tensorflow.google.cn/tutorials/structured_data/time_series) * [Calculate gradients](https://tensorflow.google.cn/quantum/tutorials/gradients) * [Quantum data](https://tensorflow.google.cn/quantum/tutorials/quantum_data) * [Parametrized Quantum Circuits for Reinforcement Learning](https://tensorflow.google.cn/quantum/tutorials/quantum_reinforcement_learning) * [A Tutorial on Multi-Armed Bandits with Per-Arm Features](https://tensorflow.google.cn/agents/tutorials/per_arm_bandits_tutorial) |

This operation creates a new tensor by replicating `input` `multiples` times.
The output tensor's i'th dimension has `input.dims(i) * multiples[i]` elements,
and the values of `input` are replicated `multiples[i]` times along the 'i'th
dimension. For example, tiling `[a b c d]` by `[2]` produces
`[a b c d a b c d]`.

```
>>> a = tf.constant([[1,2,3],[4,5,6]], tf.int32)
>>> b = tf.constant([1,2], tf.int32)
>>> tf.tile(a, b)
<tf.Tensor: shape=(2, 6), dtype=int32, numpy=
array([[1, 2, 3, 1, 2, 3],
       [4, 5, 6, 4, 5, 6]], dtype=int32)>
>>> c = tf.constant([2,1], tf.int32)
>>> tf.tile(a, c)
<tf.Tensor: shape=(4, 3), dtype=int32, numpy=
array([[1, 2, 3],
       [4, 5, 6],
       [1, 2, 3],
       [4, 5, 6]], dtype=int32)>
>>> d = tf.constant([2,2], tf.int32)
>>> tf.tile(a, d)
<tf.Tensor: shape=(4, 6), dtype=int32, numpy=
array([[1, 2, 3, 1, 2, 3],
       [4, 5, 6, 4, 5, 6],
       [1, 2, 3, 1, 2, 3],
       [4, 5, 6, 4, 5, 6]], dtype=int32)>
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Can be of any rank. |
| `multiples` | A `Tensor`. Must be one of the following types: `int32`, `int64`. 1-D. Length must be the same as the number of dimensions in `input` |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `input`. | |