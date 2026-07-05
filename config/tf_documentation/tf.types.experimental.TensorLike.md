# tf.types.experimental.TensorLike

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/types/experimental/TensorLike](https://tensorflow.google.cn/api_docs/python/tf/types/experimental/TensorLike)

---

This symbol is a **type alias**.

Union of all types that can be converted to a [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) by [`tf.convert_to_tensor`](https://tensorflow.google.cn/api_docs/python/tf/convert_to_tensor).

#### Source:

```
TensorLike = Union[
    tensorflow.python.types.core.Tensor,
    tensorflow.python.types.core.TensorProtocol,
    int,
    float,
    bool,
    str,
    bytes,
    complex,
    tuple,
    list,
    numpy.ndarray,
    numpy.generic
]
```

This definition may be used in user code. Additional types may be added
in the future as more input types are supported.

#### Example:

```
def foo(x: TensorLike):
  pass
```

This definition passes static type verification for:

```
foo(tf.constant([1, 2, 3]))
foo([1, 2, 3])
foo(np.array([1, 2, 3]))
```