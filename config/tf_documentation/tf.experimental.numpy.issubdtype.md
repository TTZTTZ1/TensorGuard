# tf.experimental.numpy.issubdtype

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/issubdtype](https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/issubdtype)

---

Returns True if first argument is a typecode lower/equal in type hierarchy.

```
tf.experimental.numpy.issubdtype(
    arg1, arg2
)
```

This is like the builtin :func:`issubclass`, but for `dtype`\ s.

## Parameters

arg1, arg2 : dtype\_like
`dtype` or object coercible to one

## Returns

out : bool

## See Also

:ref:`arrays.scalars` : Overview of the numpy type hierarchy.
issubsctype, issubclass\_

## Examples

`issubdtype` can be used to check the type of arrays:

```
>>> ints = np.array([1, 2, 3], dtype=np.int32)
>>> np.issubdtype(ints.dtype, np.integer)
True
>>> np.issubdtype(ints.dtype, np.floating)
False
```

```
>>> floats = np.array([1, 2, 3], dtype=np.float32)
>>> np.issubdtype(floats.dtype, np.integer)
False
>>> np.issubdtype(floats.dtype, np.floating)
True
```

Similar types of different sizes are not subdtypes of each other:

```
>>> np.issubdtype(np.float64, np.float32)
False
>>> np.issubdtype(np.float32, np.float64)
False
```

but both are subtypes of `floating`:

```
>>> np.issubdtype(np.float64, np.floating)
True
>>> np.issubdtype(np.float32, np.floating)
True
```

For convenience, dtype-like objects are allowed too:

```
>>> np.issubdtype('S1', np.string_)
True
>>> np.issubdtype('i4', np.signedinteger)
True
```