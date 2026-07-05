# tf.unravel_index

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/unravel_index](https://tensorflow.google.cn/api_docs/python/tf/unravel_index)

---

Converts an array of flat indices into a tuple of coordinate arrays.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.unravel_index`](https://tensorflow.google.cn/api_docs/python/tf/unravel_index)

```
tf.unravel_index(
    indices: Annotated[Any, TV_UnravelIndex_Tidx],
    dims: Annotated[Any, TV_UnravelIndex_Tidx],
    name=None
) -> Annotated[Any, TV_UnravelIndex_Tidx]
```

#### Example:

```
y = tf.unravel_index(indices=[2, 5, 7], dims=[3, 3])
# 'dims' represent a hypothetical (3, 3) tensor of indices:
# [[0, 1, *2*],
#  [3, 4, *5*],
#  [6, *7*, 8]]
# For each entry from 'indices', this operation returns
# its coordinates (marked with '*'), such as
# 2 ==> (0, 2)
# 5 ==> (1, 2)
# 7 ==> (2, 1)
y ==> [[0, 1, 2], [2, 2, 1]]
```

| Args | |

|  |  |
| --- | --- |
| `indices` | A `Tensor`. Must be one of the following types: `int32`, `int64`. An 0-D or 1-D `int` Tensor whose elements are indices into the flattened version of an array of dimensions dims. |
| `dims` | A `Tensor`. Must have the same type as `indices`. An 1-D `int` Tensor. The shape of the array to use for unraveling indices. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor`. Has the same type as `indices`. | |

## numpy compatibility

Equivalent to np.unravel\_index