# tf.experimental.numpy.float_

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/float_](https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/float_)

---

Double-precision floating-point number type, compatible with Python `float` and C `double`.

Inherits From: [`inexact`](https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/inexact)

#### View aliases

**Main aliases**

[`tf.experimental.numpy.float_`](https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/float64)

```
tf.experimental.numpy.float64(
    *args, **kwargs
)
```

:Character code: `'d'`
:Canonical name: `numpy.double`
:Alias: `numpy.float_`
:Alias on this platform (Linux x86\_64): `numpy.float64`: 64-bit precision floating-point number type: sign bit, 11 bits exponent, 52 bits mantissa.

| Attributes | |

|  |  |
| --- | --- |
| `T` | Scalar attribute identical to the corresponding array attribute. |

Please see `ndarray.T`.| `base` | Scalar attribute identical to the corresponding array attribute. |

Please see `ndarray.base`.| `data` | Pointer to start of data. |
| `dtype` | Get array data-descriptor. |
| `flags` | The integer value of flags. |
| `flat` | A 1-D view of the scalar. |
| `imag` | The imaginary part of the scalar. |
| `itemsize` | The length of one element in bytes. |
| `nbytes` | The length of the scalar in bytes. |
| `ndim` | The number of array dimensions. |
| `real` | The real part of the scalar. |
| `shape` | Tuple of array dimensions. |
| `size` | The number of elements in the gentype. |
| `strides` | Tuple of bytes steps in each dimension. |

## Methods

### `all`

```
all()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.all`.

### `any`

```
any()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.any`.

### `argmax`

```
argmax()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.argmax`.

### `argmin`

```
argmin()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.argmin`.

### `argsort`

```
argsort()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.argsort`.

### `as_integer_ratio`

```
as_integer_ratio()
```

double.as\_integer\_ratio() -> (int, int)

Return a pair of integers, whose ratio is exactly equal to the original
floating point number, and with a positive denominator.
Raise `OverflowError` on infinities and a `ValueError` on NaNs.

```
>>> np.double(10.0).as_integer_ratio()
(10, 1)
>>> np.double(0.0).as_integer_ratio()
(0, 1)
>>> np.double(-.25).as_integer_ratio()
(-1, 4)
```

### `astype`

```
astype()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.astype`.

### `byteswap`

```
byteswap()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.byteswap`.

### `choose`

```
choose()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.choose`.

### `clip`

```
clip()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.clip`.

### `compress`

```
compress()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.compress`.

### `conj`

```
conj()
```

### `conjugate`

```
conjugate()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.conjugate`.

### `copy`

```
copy()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.copy`.

### `cumprod`

```
cumprod()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.cumprod`.

### `cumsum`

```
cumsum()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.cumsum`.

### `diagonal`

```
diagonal()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.diagonal`.

### `dump`

```
dump()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.dump`.

### `dumps`

```
dumps()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.dumps`.

### `fill`

```
fill()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.fill`.

### `flatten`

```
flatten()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.flatten`.

### `fromhex`

```
fromhex()
```

Create a floating-point number from a hexadecimal string.

```
>>> float.fromhex('0x1.ffffp10')
2047.984375
>>> float.fromhex('-0x1p-1074')
-5e-324
```

### `getfield`

```
getfield()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.getfield`.

### `hex`

```
hex()
```

Return a hexadecimal representation of a floating-point number.

```
>>> (-0.1).hex()
'-0x1.999999999999ap-4'
>>> 3.14159.hex()
'0x1.921f9f01b866ep+1'
```

### `is_integer`

```
is_integer()
```

double.is\_integer() -> bool

Return `True` if the floating point number is finite with integral
value, and `False` otherwise.

.. versionadded:: 1.22

## Examples

```
>>> np.double(-2.0).is_integer()
True
>>> np.double(3.2).is_integer()
False
```

### `item`

```
item()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.item`.

### `itemset`

```
itemset()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.itemset`.

### `max`

```
max()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.max`.

### `mean`

```
mean()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.mean`.

### `min`

```
min()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.min`.

### `newbyteorder`

```
newbyteorder()
```

newbyteorder(new\_order='S', /)

Return a new `dtype` with a different byte order.

Changes are also made in all fields and sub-arrays of the data type.

The `new_order` code can be any from the following:

* 'S' - swap dtype from current to opposite endian

### '<', 'little'

- little endian

### '>', 'big'

- big endian

### '=', 'native'

- native order

### '|', 'I'

- ignore (no change to byte order)

## Parameters

new\_order : str, optional
Byte order to force; a value from the byte order specifications
above. The default value ('S') results in swapping the current
byte order.

## Returns

new\_dtype : dtype
New `dtype` object with the given change to the byte order.

### `nonzero`

```
nonzero()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.nonzero`.

### `prod`

```
prod()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.prod`.

### `ptp`

```
ptp()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.ptp`.

### `put`

```
put()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.put`.

### `ravel`

```
ravel()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.ravel`.

### `repeat`

```
repeat()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.repeat`.

### `reshape`

```
reshape()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.reshape`.

### `resize`

```
resize()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.resize`.

### `round`

```
round()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.round`.

### `searchsorted`

```
searchsorted()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.searchsorted`.

### `setfield`

```
setfield()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.setfield`.

### `setflags`

```
setflags()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.setflags`.

### `sort`

```
sort()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.sort`.

### `squeeze`

```
squeeze()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.squeeze`.

### `std`

```
std()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.std`.

### `sum`

```
sum()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.sum`.

### `swapaxes`

```
swapaxes()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.swapaxes`.

### `take`

```
take()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.take`.

### `tobytes`

```
tobytes()
```

### `tofile`

```
tofile()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.tofile`.

### `tolist`

```
tolist()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.tolist`.

### `tostring`

```
tostring()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.tostring`.

### `trace`

```
trace()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.trace`.

### `transpose`

```
transpose()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.transpose`.

### `var`

```
var()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.var`.

### `view`

```
view()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.view`.

### `__abs__`

```
__abs__()
```

abs(self)

### `__add__`

```
__add__(
    value, /
)
```

Return self+value.

### `__and__`

```
__and__(
    value, /
)
```

Return self&value.

### `__array__`

```
__array__()
```

sc.**array**(dtype) return 0-dim array from scalar with specified dtype

### `__bool__`

```
__bool__()
```

True if self else False

### `__eq__`

```
__eq__(
    value, /
)
```

Return self==value.

### `__floordiv__`

```
__floordiv__(
    value, /
)
```

Return self//value.

### `__ge__`

```
__ge__(
    value, /
)
```

Return self>=value.

### `__getitem__`

```
__getitem__(
    key, /
)
```

Return self[key].

### `__gt__`

```
__gt__(
    value, /
)
```

Return self>value.

### `__invert__`

```
__invert__()
```

~self

### `__le__`

```
__le__(
    value, /
)
```

Return self<=value.

### `__lshift__`

```
__lshift__(
    value, /
)
```

Return self<<value.

### `__lt__`

```
__lt__(
    value, /
)
```

Return self<value.

### `__mod__`

```
__mod__(
    value, /
)
```

Return self%value.

### `__mul__`

```
__mul__(
    value, /
)
```

Return self\*value.

### `__ne__`

```
__ne__(
    value, /
)
```

Return self!=value.

### `__neg__`

```
__neg__()
```

-self

### `__or__`

```
__or__(
    value, /
)
```

Return self|value.

### `__pos__`

```
__pos__()
```

+self

### `__pow__`

```
__pow__(
    value, mod, /
)
```

Return pow(self, value, mod).

### `__radd__`

```
__radd__(
    value, /
)
```

Return value+self.

### `__rand__`

```
__rand__(
    value, /
)
```

Return value&self.

### `__rfloordiv__`

```
__rfloordiv__(
    value, /
)
```

Return value//self.

### `__rlshift__`

```
__rlshift__(
    value, /
)
```

Return value<<self.

### `__rmod__`

```
__rmod__(
    value, /
)
```

Return value%self.

### `__rmul__`

```
__rmul__(
    value, /
)
```

Return value\*self.

### `__ror__`

```
__ror__(
    value, /
)
```

Return value|self.

### `__rpow__`

```
__rpow__(
    value, mod, /
)
```

Return pow(value, self, mod).

### `__rrshift__`

```
__rrshift__(
    value, /
)
```

Return value>>self.

### `__rshift__`

```
__rshift__(
    value, /
)
```

Return self>>value.

### `__rsub__`

```
__rsub__(
    value, /
)
```

Return value-self.

### `__rtruediv__`

```
__rtruediv__(
    value, /
)
```

Return value/self.

### `__rxor__`

```
__rxor__(
    value, /
)
```

Return value^self.

### `__sub__`

```
__sub__(
    value, /
)
```

Return self-value.

### `__truediv__`

```
__truediv__(
    value, /
)
```

Return self/value.

### `__xor__`

```
__xor__(
    value, /
)
```

Return self^value.