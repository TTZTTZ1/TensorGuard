# tf.math.bincount

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/math/bincount](https://tensorflow.google.cn/api_docs/python/tf/math/bincount)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/bincount_ops.py#L29-L187) |

Counts the number of occurrences of each value in an integer array.

```
tf.math.bincount(
    arr,
    weights=None,
    minlength=None,
    maxlength=None,
    dtype=tf.dtypes.int32,
    name=None,
    axis=None,
    binary_output=False
)

tf.dtypes.int32
```

If `minlength` and `maxlength` are not given, returns a vector with length
`tf.reduce_max(arr) + 1` if `arr` is non-empty, and length 0 otherwise.

```
>>> values = tf.constant([1,1,2,3,2,4,4,5])
>>> tf.math.bincount(values)
<tf.Tensor: ... numpy=array([0, 2, 2, 1, 2, 1], dtype=int32)>
```

Vector length = Maximum element in vector `values` is 5. Adding 1, which is 6
will be the vector length.

Each bin value in the output indicates number of occurrences of the particular
index. Here, index 1 in output has a value 2. This indicates value 1 occurs
two times in `values`.

**Bin-counting with weights**

```
>>> values = tf.constant([1,1,2,3,2,4,4,5])
>>> weights = tf.constant([1,5,0,1,0,5,4,5])
>>> tf.math.bincount(values, weights=weights)
<tf.Tensor: ... numpy=array([0, 6, 0, 1, 9, 5], dtype=int32)>
```

When `weights` is specified, bins will be incremented by the corresponding
weight instead of 1. Here, index 1 in output has a value 6. This is the
summation of `weights` corresponding to the value in `values` (i.e. for index
1, the first two values are 1 so the first two weights, 1 and 5, are
summed).

There is an equivilance between bin-counting with weights and
`unsorted_segement_sum` where `data` is the weights and `segment_ids` are the
values.

```
>>> values = tf.constant([1,1,2,3,2,4,4,5])
>>> weights = tf.constant([1,5,0,1,0,5,4,5])
>>> tf.math.unsorted_segment_sum(weights, values, num_segments=6).numpy()
array([0, 6, 0, 1, 9, 5], dtype=int32)
```

On GPU, `bincount` with weights is only supported when XLA is enabled
(typically when a function decorated with [`@tf.function(jit_compile=True)`](https://tensorflow.google.cn/api_docs/python/tf/function)).
`unsorted_segment_sum` can be used as a workaround for the non-XLA case on
GPU.

**Bin-counting matrix rows independently**

This example uses `axis=-1` with a 2 dimensional input and returns a
`Tensor` with bincounting where axis 0 is **not** flattened, i.e. an
independent bincount for each matrix row.

```
>>> data = np.array([[1, 2, 3, 0], [0, 0, 1, 2]], dtype=np.int32)
>>> tf.math.bincount(data, axis=-1)
<tf.Tensor: shape=(2, 4), dtype=int32, numpy=
  array([[1, 1, 1, 1],
         [2, 1, 1, 0]], dtype=int32)>
```

**Bin-counting with binary\_output**

This example gives binary output instead of counting the occurrence.

```
>>> data = np.array([[1, 2, 3, 0], [0, 0, 1, 2]], dtype=np.int32)
>>> tf.math.bincount(data, axis=-1, binary_output=True)
<tf.Tensor: shape=(2, 4), dtype=int32, numpy=
  array([[1, 1, 1, 1],
         [1, 1, 1, 0]], dtype=int32)>
```

**Missing zeros in SparseTensor**

Note that missing zeros (implict zeros) in SparseTensor are **NOT** counted.
This supports cases such as `0` in the values tensor indicates that index/id
`0`is present and a missing zero indicates that no index/id is present.

If counting missing zeros is desired, there are workarounds.
For the `axis=0` case, the number of missing zeros can computed by subtracting
the number of elements in the SparseTensor's `values` tensor from the
number of elements in the dense shape, and this difference can be added to the
first element of the output of `bincount`. For all cases, the SparseTensor
can be converted to a dense Tensor with [`tf.sparse.to_dense`](https://tensorflow.google.cn/api_docs/python/tf/sparse/to_dense) before calling
[`tf.math.bincount`](https://tensorflow.google.cn/api_docs/python/tf/math/bincount).

| Args | |

|  |  |
| --- | --- |
| `arr` | A Tensor, RaggedTensor, or SparseTensor whose values should be counted. These tensors must have a rank of 2 if `axis=-1`. |
| `weights` | If non-None, must be the same shape as arr. For each value in `arr`, the bin will be incremented by the corresponding weight instead of |

1. If non-None, `binary_output` must be False.| `minlength` | If given, ensures the output has length at least `minlength`, padding with zeros at the end if necessary. |
   | `maxlength` | If given, skips values in `arr` that are equal or greater than `maxlength`, ensuring that the output has length at most `maxlength`. |
   | `dtype` | If `weights` is None, determines the type of the output bins. |
   | `name` | A name scope for the associated operations (optional). |
   | `axis` | The axis to slice over. Axes at and below `axis` will be flattened before bin counting. Currently, only `0`, and `-1` are supported. If None, all axes will be flattened (identical to passing `0`). |
   | `binary_output` | If True, this op will output 1 instead of the number of times a token appears (equivalent to one\_hot + reduce\_any instead of one\_hot + reduce\_add). Defaults to False. |

| Returns | |
| A vector with the same dtype as `weights` or the given `dtype` containing the bincount values. | |

| Raises | |
| `InvalidArgumentError` if negative values are provided as an input. | |