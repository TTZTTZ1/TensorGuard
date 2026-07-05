# tf.experimental.numpy.string_

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/string_](https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/string_)

---

A byte string.

```
tf.experimental.numpy.string_(
    *args, **kwargs
)
```

When used in arrays, this type strips trailing null bytes.

:Character code: `'S'`
:Alias: `numpy.string_`

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

### `capitalize`

```
capitalize()
```

B.capitalize() -> copy of B

Return a copy of B with only its first character capitalized (ASCII)
and the rest lower-cased.

### `center`

```
center(
    width, fillchar, /
)
```

Return a centered string of length width.

Padding is done using the specified fill character.

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

### `count`

```
count()
```

B.count(sub[, start[, end]]) -> int

Return the number of non-overlapping occurrences of subsection sub in
bytes B[start:end]. Optional arguments start and end are interpreted
as in slice notation.

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

### `decode`

```
decode(
    encoding='utf-8', errors='strict'
)
```

Decode the bytes using the codec registered for encoding.

encoding
The encoding with which to decode the bytes.
errors
The error handling scheme to use for the handling of decoding errors.
The default is 'strict' meaning that decoding errors raise a
UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
as well as any other name registered with codecs.register\_error that
can handle UnicodeDecodeErrors.

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

### `endswith`

```
endswith()
```

B.endswith(suffix[, start[, end]]) -> bool

Return True if B ends with the specified suffix, False otherwise.
With optional start, test B beginning at that position.
With optional end, stop comparing B at that position.
suffix can also be a tuple of bytes to try.

### `expandtabs`

```
expandtabs(
    tabsize=8
)
```

Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

### `fill`

```
fill()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.fill`.

### `find`

```
find()
```

B.find(sub[, start[, end]]) -> int

Return the lowest index in B where subsection sub is found,
such that sub is contained within B[start,end]. Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.

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

Create a bytes object from a string of hexadecimal numbers.

Spaces between two numbers are accepted.
Example: bytes.fromhex('B9 01EF') -> b'\xb9\x01\xef'.

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

Create a str of hexadecimal numbers from a bytes object.

sep
An optional single character or byte to separate hex bytes.
bytes\_per\_sep
How many bytes between separators. Positive values count from the
right, negative values count from the left.

#### Example:

```
>>> value = b'\xb9\x01\xef'
>>> value.hex()
'b901ef'
>>> value.hex(':')
'b9:01:ef'
>>> value.hex(':', 2)
'b9:01ef'
>>> value.hex(':', -2)
'b901:ef'
```

### `index`

```
index()
```

B.index(sub[, start[, end]]) -> int

Return the lowest index in B where subsection sub is found,
such that sub is contained within B[start,end]. Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the subsection is not found.

### `isalnum`

```
isalnum()
```

B.isalnum() -> bool

Return True if all characters in B are alphanumeric
and there is at least one character in B, False otherwise.

### `isalpha`

```
isalpha()
```

B.isalpha() -> bool

Return True if all characters in B are alphabetic
and there is at least one character in B, False otherwise.

### `isascii`

```
isascii()
```

B.isascii() -> bool

Return True if B is empty or all characters in B are ASCII,
False otherwise.

### `isdigit`

```
isdigit()
```

B.isdigit() -> bool

Return True if all characters in B are digits
and there is at least one character in B, False otherwise.

### `islower`

```
islower()
```

B.islower() -> bool

Return True if all cased characters in B are lowercase and there is
at least one cased character in B, False otherwise.

### `isspace`

```
isspace()
```

B.isspace() -> bool

Return True if all characters in B are whitespace
and there is at least one character in B, False otherwise.

### `istitle`

```
istitle()
```

B.istitle() -> bool

Return True if B is a titlecased string and there is at least one
character in B, i.e. uppercase characters may only follow uncased
characters and lowercase characters only cased ones. Return False
otherwise.

### `isupper`

```
isupper()
```

B.isupper() -> bool

Return True if all cased characters in B are uppercase and there is
at least one cased character in B, False otherwise.

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

### `join`

```
join(
    iterable_of_bytes, /
)
```

Concatenate any number of bytes objects.

The bytes whose method is called is inserted in between each pair.

The result is returned as a new bytes object.

Example: b'.'.join([b'ab', b'pq', b'rs']) -> b'ab.pq.rs'.

### `ljust`

```
ljust(
    width, fillchar, /
)
```

Return a left-justified string of length width.

Padding is done using the specified fill character.

### `lower`

```
lower()
```

B.lower() -> copy of B

Return a copy of B with all ASCII characters converted to lowercase.

### `lstrip`

```
lstrip(
    bytes, /
)
```

Strip leading bytes contained in the argument.

If the argument is omitted or None, strip leading ASCII whitespace.

### `maketrans`

```
maketrans(
    frm, to, /
)
```

Return a translation table useable for the bytes or bytearray translate method.

The returned table will be one where each byte in frm is mapped to the byte at
the same position in to.

The bytes objects frm and to must be of the same length.

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

### `partition`

```
partition(
    sep, /
)
```

Partition the bytes into three parts using the given separator.

This will search for the separator sep in the bytes. If the separator is found,
returns a 3-tuple containing the part before the separator, the separator
itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original bytes
object and two empty bytes objects.

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

### `removeprefix`

```
removeprefix(
    prefix, /
)
```

Return a bytes object with the given prefix string removed if present.

If the bytes starts with the prefix string, return bytes[len(prefix):].
Otherwise, return a copy of the original bytes.

### `removesuffix`

```
removesuffix(
    suffix, /
)
```

Return a bytes object with the given suffix string removed if present.

If the bytes ends with the suffix string and that suffix is not empty,
return bytes[:-len(prefix)]. Otherwise, return a copy of the original
bytes.

### `repeat`

```
repeat()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.repeat`.

### `replace`

```
replace(
    old, new, count, /
)
```

Return a copy with all occurrences of substring old replaced by new.

count
Maximum number of occurrences to replace.
-1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are
replaced.

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

### `rfind`

```
rfind()
```

B.rfind(sub[, start[, end]]) -> int

Return the highest index in B where subsection sub is found,
such that sub is contained within B[start,end]. Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.

### `rindex`

```
rindex()
```

B.rindex(sub[, start[, end]]) -> int

Return the highest index in B where subsection sub is found,
such that sub is contained within B[start,end]. Optional
arguments start and end are interpreted as in slice notation.

Raise ValueError when the subsection is not found.

### `rjust`

```
rjust(
    width, fillchar, /
)
```

Return a right-justified string of length width.

Padding is done using the specified fill character.

### `round`

```
round()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.round`.

### `rpartition`

```
rpartition(
    sep, /
)
```

Partition the bytes into three parts using the given separator.

This will search for the separator sep in the bytes, starting at the end. If
the separator is found, returns a 3-tuple containing the part before the
separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty bytes
objects and the original bytes object.

### `rsplit`

```
rsplit(
    sep=None, maxsplit=-1
)
```

Return a list of the sections in the bytes, using sep as the delimiter.

sep
The delimiter according which to split the bytes.
None (the default value) means split on ASCII whitespace characters
(space, tab, return, newline, formfeed, vertical tab).
maxsplit
Maximum number of splits to do.
-1 (the default value) means no limit.

Splitting is done starting at the end of the bytes and working to the front.

### `rstrip`

```
rstrip(
    bytes, /
)
```

Strip trailing bytes contained in the argument.

If the argument is omitted or None, strip trailing ASCII whitespace.

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

### `split`

```
split(
    sep=None, maxsplit=-1
)
```

Return a list of the sections in the bytes, using sep as the delimiter.

sep
The delimiter according which to split the bytes.
None (the default value) means split on ASCII whitespace characters
(space, tab, return, newline, formfeed, vertical tab).
maxsplit
Maximum number of splits to do.
-1 (the default value) means no limit.

### `splitlines`

```
splitlines(
    keepends=False
)
```

Return a list of the lines in the bytes, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and
true.

### `squeeze`

```
squeeze()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.squeeze`.

### `startswith`

```
startswith()
```

B.startswith(prefix[, start[, end]]) -> bool

Return True if B starts with the specified prefix, False otherwise.
With optional start, test B beginning at that position.
With optional end, stop comparing B at that position.
prefix can also be a tuple of bytes to try.

### `std`

```
std()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.std`.

### `strip`

```
strip(
    bytes, /
)
```

Strip leading and trailing bytes contained in the argument.

If the argument is omitted or None, strip leading and trailing ASCII whitespace.

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

### `swapcase`

```
swapcase()
```

B.swapcase() -> copy of B

Return a copy of B with uppercase ASCII characters converted
to lowercase ASCII and vice versa.

### `take`

```
take()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.take`.

### `title`

```
title()
```

B.title() -> copy of B

Return a titlecased version of B, i.e. ASCII words start with uppercase
characters, all remaining cased characters have lowercase.

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

### `translate`

```
translate(
    table, /, delete=b''
)
```

Return a copy with each character mapped by the given translation table.

table
Translation table, which must be a bytes object of length 256.

All characters occurring in the optional argument delete are removed.
The remaining characters are mapped through the given translation table.

### `transpose`

```
transpose()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.transpose`.

### `upper`

```
upper()
```

B.upper() -> copy of B

Return a copy of B with all ASCII characters converted to uppercase.

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

### `zfill`

```
zfill(
    width, /
)
```

Pad a numeric string with zeros on the left, to fill a field of the given width.

The original string is never truncated.

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

### `__contains__`

```
__contains__(
    key, /
)
```

Return key in self.

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

### `__iter__`

```
__iter__()
```

Implement iter(self).

### `__le__`

```
__le__(
    value, /
)
```

Return self<=value.

### `__len__`

```
__len__()
```

Return len(self).

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