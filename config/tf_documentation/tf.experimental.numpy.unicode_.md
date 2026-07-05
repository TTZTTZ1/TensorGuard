# tf.experimental.numpy.unicode_

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/unicode_](https://tensorflow.google.cn/api_docs/python/tf/experimental/numpy/unicode_)

---

A unicode string.

```
tf.experimental.numpy.unicode_(
    *args, **kwargs
)
```

This type strips trailing null codepoints.

```
>>> s = np.str_("abc\x00")
>>> s
'abc'
```

Unlike the builtin `str`, this supports the :ref:`python:bufferobjects`, exposing its
contents as UCS4:

```
>>> m = memoryview(np.str_("abc"))
>>> m.format
'3w'
>>> m.tobytes()
b'a\x00\x00\x00b\x00\x00\x00c\x00\x00\x00'
```

:Character code: `'U'`
:Alias: `numpy.unicode_`

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

Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower
case.

### `casefold`

```
casefold()
```

Return a version of the string suitable for caseless comparisons.

### `center`

```
center(
    width, fillchar, /
)
```

Return a centered string of length width.

Padding is done using the specified fill character (default is a space).

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

S.count(sub[, start[, end]]) -> int

Return the number of non-overlapping occurrences of substring sub in
string S[start:end]. Optional arguments start and end are
interpreted as in slice notation.

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

### `encode`

```
encode(
    encoding='utf-8', errors='strict'
)
```

Encode the string using the codec registered for encoding.

encoding
The encoding in which to encode the string.
errors
The error handling scheme to use for encoding errors.
The default is 'strict' meaning that encoding errors raise a
UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
'xmlcharrefreplace' as well as any other name registered with
codecs.register\_error that can handle UnicodeEncodeErrors.

### `endswith`

```
endswith()
```

S.endswith(suffix[, start[, end]]) -> bool

Return True if S ends with the specified suffix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
suffix can also be a tuple of strings to try.

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

S.find(sub[, start[, end]]) -> int

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.

### `flatten`

```
flatten()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.flatten`.

### `format`

```
format()
```

S.format(\*args, \*\*kwargs) -> str

Return a formatted version of S, using substitutions from args and kwargs.
The substitutions are identified by braces ('{' and '}').

### `format_map`

```
format_map()
```

S.format\_map(mapping) -> str

Return a formatted version of S, using substitutions from mapping.
The substitutions are identified by braces ('{' and '}').

### `getfield`

```
getfield()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.getfield`.

### `index`

```
index()
```

S.index(sub[, start[, end]]) -> int

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

### `isalnum`

```
isalnum()
```

Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and
there is at least one character in the string.

### `isalpha`

```
isalpha()
```

Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there
is at least one character in the string.

### `isascii`

```
isascii()
```

Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F.
Empty string is ASCII too.

### `isdecimal`

```
isdecimal()
```

Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are decimal and
there is at least one character in the string.

### `isdigit`

```
isdigit()
```

Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there
is at least one character in the string.

### `isidentifier`

```
isidentifier()
```

Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
such as "def" or "class".

### `islower`

```
islower()
```

Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are lowercase and
there is at least one cased character in the string.

### `isnumeric`

```
isnumeric()
```

Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at
least one character in the string.

### `isprintable`

```
isprintable()
```

Return True if the string is printable, False otherwise.

A string is printable if all of its characters are considered printable in
repr() or if it is empty.

### `isspace`

```
isspace()
```

Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there
is at least one character in the string.

### `istitle`

```
istitle()
```

Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only
follow uncased characters and lowercase characters only cased ones.

### `isupper`

```
isupper()
```

Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and
there is at least one cased character in the string.

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
    iterable, /
)
```

Concatenate any number of strings.

The string whose method is called is inserted in between each given string.
The result is returned as a new string.

Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

### `ljust`

```
ljust(
    width, fillchar, /
)
```

Return a left-justified string of length width.

Padding is done using the specified fill character (default is a space).

### `lower`

```
lower()
```

Return a copy of the string converted to lowercase.

### `lstrip`

```
lstrip(
    chars, /
)
```

Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.

### `maketrans`

```
maketrans()
```

Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping Unicode
ordinals (integers) or characters to Unicode ordinals, strings or None.
Character keys will be then converted to ordinals.
If there are two arguments, they must be strings of equal length, and
in the resulting dictionary, each character in x will be mapped to the
character at the same position in y. If there is a third argument, it
must be a string, whose characters will be mapped to None in the result.

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

Partition the string into three parts using the given separator.

This will search for the separator in the string. If the separator is found,
returns a 3-tuple containing the part before the separator, the separator
itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string
and two empty strings.

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

Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return string[len(prefix):].
Otherwise, return a copy of the original string.

### `removesuffix`

```
removesuffix(
    suffix, /
)
```

Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not empty,
return string[:-len(suffix)]. Otherwise, return a copy of the original
string.

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

S.rfind(sub[, start[, end]]) -> int

Return the highest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.

### `rindex`

```
rindex()
```

S.rindex(sub[, start[, end]]) -> int

Return the highest index in S where substring sub is found,
such that sub is contained within S[start:end]. Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

### `rjust`

```
rjust(
    width, fillchar, /
)
```

Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).

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

Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the end. If
the separator is found, returns a 3-tuple containing the part before the
separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty strings
and the original string.

### `rsplit`

```
rsplit(
    sep=None, maxsplit=-1
)
```

Return a list of the words in the string, using sep as the delimiter string.

sep
The delimiter according which to split the string.
None (the default value) means split according to any whitespace,
and discard empty strings from the result.
maxsplit
Maximum number of splits to do.
-1 (the default value) means no limit.

Splits are done starting at the end of the string and working to the front.

### `rstrip`

```
rstrip(
    chars, /
)
```

Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

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

Return a list of the words in the string, using sep as the delimiter string.

sep
The delimiter according which to split the string.
None (the default value) means split according to any whitespace,
and discard empty strings from the result.
maxsplit
Maximum number of splits to do.
-1 (the default value) means no limit.

### `splitlines`

```
splitlines(
    keepends=False
)
```

Return a list of the lines in the string, breaking at line boundaries.

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

S.startswith(prefix[, start[, end]]) -> bool

Return True if S starts with the specified prefix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
prefix can also be a tuple of strings to try.

### `std`

```
std()
```

Scalar method identical to the corresponding array attribute.

Please see `ndarray.std`.

### `strip`

```
strip(
    chars, /
)
```

Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

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

Convert uppercase characters to lowercase and lowercase characters to uppercase.

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

Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining
cased characters have lower case.

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
    table, /
)
```

Replace each character in the string using the given translation table.

table
Translation table, which must be a mapping of Unicode ordinals to
Unicode ordinals, strings, or None.

The table must implement lookup/indexing via **getitem**, for instance a
dictionary or list. If this operation raises LookupError, the character is
left untouched. Characters mapped to None are deleted.

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

Return a copy of the string converted to uppercase.

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

The string is never truncated.

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