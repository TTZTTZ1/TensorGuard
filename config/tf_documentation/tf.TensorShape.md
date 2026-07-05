# tf.TensorShape

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/TensorShape](https://tensorflow.google.cn/api_docs/python/tf/TensorShape)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L747-L1515) |

Represents the shape of a `Tensor`.

Inherits From: [`TraceType`](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/TraceType)

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape)

```
tf.TensorShape(
    dims
)
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [TensorFlow 1.x vs TensorFlow 2 - Behaviors and APIs](https://tensorflow.google.cn/guide/migrate/tf1_vs_tf2) * [DTensor concepts](https://tensorflow.google.cn/guide/dtensor_overview) * [Working with RNNs](https://tensorflow.google.cn/guide/keras/working_with_rnns) | * [Distributed Input](https://tensorflow.google.cn/tutorials/distribute/input) * [Tensorflow datasets from MongoDB collections](https://tensorflow.google.cn/io/tutorials/mongodb) |

```
>>> t = tf.constant([[1,2,3],[4,5,6]])
>>> t.shape
TensorShape([2, 3])
```

`TensorShape` is the *static* shape representation of a Tensor.
During eager execution a Tensor always has a fully specified shape but
when tracing a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) it may be one of the following:

* *Fully-known shape:* has a known number of dimensions and a known size
  for each dimension. e.g. `TensorShape([16, 256])`
* *Partially-known shape:* has a known number of dimensions, and an unknown
  size for one or more dimension. e.g. `TensorShape([None, 256])`
* *Unknown shape:* has an unknown number of dimensions, and an unknown
  size in all dimensions. e.g. `TensorShape(None)`

During function tracing `t.shape` will return a `TensorShape` object
representing the shape of Tensor as it is known during tracing.
This static representation will be partially defined in cases where the
exact shape depends on the values within the tensors. To get the
*dynamic* representation, please use [`tf.shape(t)`](https://tensorflow.google.cn/api_docs/python/tf/shape)
which will return Tensor representing the fully defined shape of `t`.
This way, you can express logic that manipulates the shapes of tensors by
building other tensors that depend on the dynamic shape of `t`.

**Note:** [`tf.RaggedTensor.shape`](https://tensorflow.google.cn/api_docs/python/tf/RaggedTensor#shape) also returns a [`tf.TensorShape`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape),
the lengths of any ragged dimensions are unknown (`None`).

For example, this function prints the `TensorShape' (`t.shape`), when you
trace the function, and returns a tensor <a href="../tf/shape"><code>tf.shape(t)</code></a> for given input`t`:

```
>>> @tf.function
... def get_dynamic_shape(t):
...   print("tracing...")
...   print(f"static shape is {t.shape}")
...   return tf.shape(t)
```

Just calling the function traces it with a fully-specified static shape:

```
>>> result = get_dynamic_shape(tf.constant([[1, 1, 1], [0, 0, 0]]))
tracing...
static shape is (2, 3)
>>> result.numpy()
array([2, 3], dtype=int32)
```

But [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function) can also trace the function with a partially specified
(or even unspecified) shape:

```
>>> cf1 = get_dynamic_shape.get_concrete_function(tf.TensorSpec(
...                                               shape=[None, 2]))
tracing...
static shape is (None, 2)
>>> cf1(tf.constant([[1., 0],[1, 0],[1, 0]])).numpy()
array([3, 2], dtype=int32)
```

```
>>> cf2 = get_dynamic_shape.get_concrete_function(tf.TensorSpec(shape=None))
tracing...
static shape is <unknown>
>>> cf2(tf.constant([[[[[1., 0]]]]])).numpy()
array([1, 1, 1, 1, 2], dtype=int32)
```

If a tensor is produced by an operation of type `"Foo"`, its shape
may be inferred if there is a registered shape function for
`"Foo"`. See [Shape
functions](https://tensorflow.google.cn/guide/create_op#shape_functions_in_c)
for details of shape functions and how to register them. Alternatively,
you may set the shape explicitly using `tf.Tensor.ensure_shape`.

| Args | |

|  |  |
| --- | --- |
| `dims` | A list of Dimensions, or None if the shape is unspecified. |

| Raises | |

|  |  |
| --- | --- |
| `TypeError` | If dims cannot be converted to a list of dimensions. |

| Attributes | |

|  |  |
| --- | --- |
| `dims` | Deprecated. Returns list of dimensions for this shape. |

Suggest [`TensorShape.as_list`](https://tensorflow.google.cn/api_docs/python/tf/TensorShape#as_list) instead.| `ndims` | Deprecated accessor for `rank`. |
| `rank` | Returns the rank of this shape, or None if it is unspecified. |

## Methods

### `as_list`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1430-L1441)

```
as_list()
```

Returns a list of integers or `None` for each dimension.

| Returns | |
| A list of integers or `None` for each dimension. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `self` is an unknown shape with an unknown rank. |

### `as_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1443-L1451)

```
as_proto()
```

Returns this shape as a `TensorShapeProto`.

### `assert_has_rank`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1097-L1107)

```
assert_has_rank(
    rank
)
```

Raises an exception if `self` is not compatible with the given `rank`.

| Args | |

|  |  |
| --- | --- |
| `rank` | An integer. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `self` does not represent a shape with the given `rank`. |

### `assert_is_compatible_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1371-L1384)

```
assert_is_compatible_with(
    other
)
```

Raises exception if `self` and `other` do not represent the same shape.

This method can be used to assert that there exists a shape that both
`self` and `other` represent.

| Args | |

|  |  |
| --- | --- |
| `other` | Another TensorShape. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `self` and `other` do not represent the same shape. |

### `assert_is_fully_defined`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1421-L1428)

```
assert_is_fully_defined()
```

Raises an exception if `self` is not fully defined in every dimension.

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `self` does not have a known value for every dimension. |

### `assert_same_rank`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1081-L1095)

```
assert_same_rank(
    other
)
```

Raises an exception if `self` and `other` do not have compatible ranks.

| Args | |

|  |  |
| --- | --- |
| `other` | Another `TensorShape`. |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `self` and `other` do not represent shapes with the same rank. |

### `concatenate`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1058-L1079)

```
concatenate(
    other
)
```

Returns the concatenation of the dimension in `self` and `other`.

**Note:** If either `self` or `other` is completely unknown,
concatenation will discard information about the other shape. In
future, we might support concatenation that preserves this
information for use with slicing.

| Args | |

|  |  |
| --- | --- |
| `other` | Another `TensorShape`. |

| Returns | |
| A `TensorShape` whose dimensions are the concatenation of the dimensions in `self` and `other`. | |

### `experimental_as_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1319-L1321)

```
experimental_as_proto() -> tensor_shape_pb2.TensorShapeProto
```

Returns a proto representation of the TensorShape instance.

### `experimental_from_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1313-L1317)

```
@classmethod
experimental_from_proto(
    proto: tensor_shape_pb2.TensorShapeProto
) -> 'TensorShape'
```

Returns a TensorShape instance based on the serialized proto.

### `experimental_type_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1308-L1311)

```
@classmethod
experimental_type_proto() -> Type[tensor_shape_pb2.TensorShapeProto]
```

Returns the type of proto associated with TensorShape serialization.

### `is_compatible_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1324-L1369)

```
is_compatible_with(
    other
)
```

Returns True iff `self` is compatible with `other`.

Two possibly-partially-defined shapes are compatible if there
exists a fully-defined shape that both shapes can represent. Thus,
compatibility allows the shape inference code to reason about
partially-defined shapes. For example:

* TensorShape(None) is compatible with all shapes.
* TensorShape([None, None]) is compatible with all two-dimensional
  shapes, such as TensorShape([32, 784]), and also TensorShape(None). It is
  not compatible with, for example, TensorShape([None]) or
  TensorShape([None, None, None]).
* TensorShape([32, None]) is compatible with all two-dimensional shapes
  with size 32 in the 0th dimension, and also TensorShape([None, None])
  and TensorShape(None). It is not compatible with, for example,
  TensorShape([32]), TensorShape([32, None, 1]) or TensorShape([64, None]).
* TensorShape([32, 784]) is compatible with itself, and also
  TensorShape([32, None]), TensorShape([None, 784]), TensorShape([None,
  None]) and TensorShape(None). It is not compatible with, for example,
  TensorShape([32, 1, 784]) or TensorShape([None]).

The compatibility relation is reflexive and symmetric, but not
transitive. For example, TensorShape([32, 784]) is compatible with
TensorShape(None), and TensorShape(None) is compatible with
TensorShape([4, 4]), but TensorShape([32, 784]) is not compatible with
TensorShape([4, 4]).

| Args | |

|  |  |
| --- | --- |
| `other` | Another TensorShape. |

| Returns | |
| True iff `self` is compatible with `other`. | |

### `is_fully_defined`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1416-L1419)

```
is_fully_defined()
```

Returns True iff `self` is fully defined in every dimension.

### `is_subtype_of`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1167-L1225)

```
is_subtype_of(
    other: tf.types.experimental.TraceType
) -> bool

tf.types.experimental.TraceType
```

Returns True iff `self` is subtype of `other`.

Shape A is a subtype of shape B if shape B can successfully represent it:

* A `TensorShape` of any rank is a subtype of `TensorShape(None)`.
* TensorShapes of equal ranks are covariant, i.e.
  `TensorShape([A1, A2, ..])` is a subtype of
  `TensorShape([B1, B2, ..])` iff An is a subtype of Bn.

  An is subtype of Bn iff An == Bn or Bn is None.
* TensorShapes of different defined ranks have no subtyping relation.

The subtyping relation is reflexive and transitive, but not symmetric.

#### Some examples:

* `TensorShape([32, 784])` is a subtype of `TensorShape(None)`, and
  `TensorShape([4, 4])` is also a subtype of `TensorShape(None)` but
  `TensorShape([32, 784])` and `TensorShape([4, 4])` are not subtypes of
  each other.
* All two-dimensional shapes are subtypes of `TensorShape([None, None])`,
  such as `TensorShape([32, 784])`. There is no subtype relationship with,
  for example, `TensorShape([None])` or `TensorShape([None, None, None])`.
* `TensorShape([32, None])` is also a subtype of `TensorShape([None, None])`
  and `TensorShape(None)`. It is not a subtype of, for example,
  `TensorShape([32])`, `TensorShape([32, None, 1])`,
  `TensorShape([64, None])` or `TensorShape([None, 32])`.
* `TensorShape([32, 784])` is a subtype of itself, and also
  `TensorShape([32, None])`, `TensorShape([None, 784])`,
  `TensorShape([None, None])` and `TensorShape(None)`.
  It has no subtype relation with, for example, `TensorShape([32, 1, 784])`
  or `TensorShape([None])`.

| Args | |

|  |  |
| --- | --- |
| `other` | Another `TensorShape`. |

| Returns | |
| True iff `self` is subtype of `other`. | |

### `merge_with`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L998-L1048)

```
merge_with(
    other
)
```

Returns a `TensorShape` combining the information in `self` and `other`.

The dimensions in `self` and `other` are merged element-wise,
according to the rules below:

```
Dimension(n).merge_with(Dimension(None)) == Dimension(n)
Dimension(None).merge_with(Dimension(n)) == Dimension(n)
Dimension(None).merge_with(Dimension(None)) == Dimension(None)
# raises ValueError for n != m
Dimension(n).merge_with(Dimension(m))
```

> > ts = tf.TensorShape([1,2])
> > ot1 = tf.TensorShape([1,2])
> > ts.merge\_with(ot).as\_list()
> > [1,2]

> > ot2 = tf.TensorShape([1,None])
> > ts.merge\_with(ot2).as\_list()
> > [1,2]

> > ot3 = tf.TensorShape([None, None])
> > ot3.merge\_with(ot2).as\_list()
> > [1, None]

| Args | |

|  |  |
| --- | --- |
| `other` | Another `TensorShape`. |

| Returns | |
| A `TensorShape` containing the combined information of `self` and `other`. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `self` and `other` are not compatible. |

### `most_specific_common_supertype`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1227-L1281)

```
most_specific_common_supertype(
    others: Sequence[tf.types.experimental.TraceType]
) -> Optional['TensorShape']

tf.types.experimental.TraceType
```

Returns the most specific supertype `TensorShape` of self and others.

* `TensorShape([None, 1])` is the most specific `TensorShape` supertyping
  both `TensorShape([2, 1])` and `TensorShape([5, 1])`. Note that
  `TensorShape(None)` is also a supertype but it is not "most specific".
* `TensorShape([1, 2, 3])` is the most specific `TensorShape` supertyping
  both `TensorShape([1, 2, 3])` and `TensorShape([1, 2, 3]`). There are
  other less specific TensorShapes that supertype above mentioned
  TensorShapes, e.g. `TensorShape([1, 2, None])`, `TensorShape(None)`.

  + `TensorShape([None, None])` is the most specific `TensorShape`
    supertyping both `TensorShape([2, None])` and `TensorShape([None, 3])`.
    As always, `TensorShape(None)` is also a supertype but not the most
    specific one.
  + `TensorShape(None`) is the only `TensorShape` supertyping both
    `TensorShape([1, 2, 3])` and `TensorShape([1, 2])`. In general, any two
    shapes that have different ranks will only have `TensorShape(None)`
    as a common supertype.
  + `TensorShape(None)` is the only `TensorShape` supertyping both
    `TensorShape([1, 2, 3])` and `TensorShape(None)`. In general, the common
    supertype of any shape with `TensorShape(None)` is `TensorShape(None)`.

| Args | |

|  |  |
| --- | --- |
| `others` | Sequence of `TensorShape`. |

| Returns | |
| A `TensorShape` which is the most specific supertype shape of `self` and `others`. None if it does not exist. | |

### `most_specific_compatible_shape`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1386-L1414)

```
most_specific_compatible_shape(
    other
) -> 'TensorShape'
```

Returns the most specific TensorShape compatible with `self` and `other`.

* TensorShape([None, 1]) is the most specific TensorShape compatible with
  both TensorShape([2, 1]) and TensorShape([5, 1]). Note that
  TensorShape(None) is also compatible with above mentioned TensorShapes.
* TensorShape([1, 2, 3]) is the most specific TensorShape compatible with
  both TensorShape([1, 2, 3]) and TensorShape([1, 2, 3]). There are more
  less specific TensorShapes compatible with above mentioned TensorShapes,
  e.g. TensorShape([1, 2, None]), TensorShape(None).

| Args | |

|  |  |
| --- | --- |
| `other` | Another `TensorShape`. |

| Returns | |
| A `TensorShape` which is the most specific compatible shape of `self` and `other`. | |

### `num_elements`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L991-L996)

```
num_elements()
```

Returns the total number of elements, or none for incomplete shapes.

### `with_rank`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1109-L1127)

```
with_rank(
    rank
)
```

Returns a shape based on `self` with the given rank.

This method promotes a completely unknown shape to one with a
known rank.

| Args | |

|  |  |
| --- | --- |
| `rank` | An integer. |

| Returns | |
| A shape that is at least as specific as `self` with the given rank. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `self` does not represent a shape with the given `rank`. |

### `with_rank_at_least`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1129-L1146)

```
with_rank_at_least(
    rank
)
```

Returns a shape based on `self` with at least the given rank.

| Args | |

|  |  |
| --- | --- |
| `rank` | An integer. |

| Returns | |
| A shape that is at least as specific as `self` with at least the given rank. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `self` does not represent a shape with at least the given `rank`. |

### `with_rank_at_most`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1148-L1165)

```
with_rank_at_most(
    rank
)
```

Returns a shape based on `self` with at most the given rank.

| Args | |

|  |  |
| --- | --- |
| `rank` | An integer. |

| Returns | |
| A shape that is at least as specific as `self` with at most the given rank. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `self` does not represent a shape with at most the given `rank`. |

### `__add__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1050-L1051)

```
__add__(
    other
)
```

### `__bool__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L924-L926)

```
__bool__()
```

Returns True if this shape contains non-zero information.

### `__concat__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1514-L1515)

```
__concat__(
    other
)
```

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1453-L1506)

```
__eq__(
    other
)
```

Returns True if `self` is equivalent to `other`.

It first tries to convert `other` to `TensorShape`. `TypeError` is thrown
when the conversion fails. Otherwise, it compares each element in the
TensorShape dimensions.

* Two *Fully known* shapes, return True iff each element is equal.

```
>>> t_a = tf.TensorShape([1,2])
>>> a = [1, 2]
>>> t_b = tf.TensorShape([1,2])
>>> t_c = tf.TensorShape([1,2,3])
>>> t_a.__eq__(a)
True
>>> t_a.__eq__(t_b)
True
>>> t_a.__eq__(t_c)
False
```

* Two *Partially-known* shapes, return True iff each element is equal.

```
>>> p_a = tf.TensorShape([1,None])
>>> p_b = tf.TensorShape([1,None])
>>> p_c = tf.TensorShape([2,None])
>>> p_a.__eq__(p_b)
True
>>> t_a.__eq__(p_a)
False
>>> p_a.__eq__(p_c)
False
```

* Two *Unknown shape*, return True.

```
>>> unk_a = tf.TensorShape(None)
>>> unk_b = tf.TensorShape(None)
>>> unk_a.__eq__(unk_b)
True
>>> unk_a.__eq__(t_a)
False
```

| Args | |

|  |  |
| --- | --- |
| `other` | A `TensorShape` or type that can be converted to `TensorShape`. |

| Returns | |
| True if the dimensions are all equal. | |

| Raises | |
| TypeError if `other` can not be converted to `TensorShape`. | |

### `__getitem__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L941-L989)

```
__getitem__(
    key
)
```

Returns the value of a dimension or a shape, depending on the key.

| Args | |

|  |  |
| --- | --- |
| `key` | If `key` is an integer, returns the dimension at that index; otherwise if `key` is a slice, returns a TensorShape whose dimensions are those selected by the slice from `self`. |

| Returns | |
| An integer if `key` is an integer, or a `TensorShape` if `key` is a slice. | |

| Raises | |

|  |  |
| --- | --- |
| `ValueError` | If `key` is a slice and `self` is completely unknown and the step is set. |

### `__iter__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L931-L939)

```
__iter__()
```

Returns `self.dims` if the rank is known, otherwise raises ValueError.

### `__len__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L918-L922)

```
__len__()
```

Returns the rank of this shape, or raises ValueError if unspecified.

### `__nonzero__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L924-L926)

```
__nonzero__()
```

Returns True if this shape contains non-zero information.

### `__radd__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/framework/tensor_shape.py#L1053-L1056)

```
__radd__(
    other
)
```