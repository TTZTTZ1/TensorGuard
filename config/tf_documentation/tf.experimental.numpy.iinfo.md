# tf.experimental.numpy.iinfo

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/iinfo](https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/iinfo)

---

iinfo(type)

```
tf.experimental.numpy.iinfo(
    int_type
)
```

Machine limits for integer types.

## Attributes

bits : int
The number of bits occupied by the type.
dtype : dtype
Returns the dtype for which `iinfo` returns information.
min : int
The smallest integer expressible by the type.
max : int
The largest integer expressible by the type.

## Parameters

int\_type : integer type, dtype, or instance
The kind of integer data type to get information about.

## See Also

finfo : The equivalent for floating point data types.

## Examples

With types:

```
>>> ii16 = np.iinfo(np.int16)
>>> ii16.min
-32768
>>> ii16.max
32767
>>> ii32 = np.iinfo(np.int32)
>>> ii32.min
-2147483648
>>> ii32.max
2147483647
```

#### With instances:

```
>>> ii32 = np.iinfo(np.int32(10))
>>> ii32.min
-2147483648
>>> ii32.max
2147483647
```

| Attributes | |

|  |  |
| --- | --- |
| `max` | Maximum value of given dtype. |
| `min` | Minimum value of given dtype. |