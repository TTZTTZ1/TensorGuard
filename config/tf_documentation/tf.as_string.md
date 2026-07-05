# tf.as_string

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/as_string](https://tensorflow.google.cn/api_docs/python/tf/as_string)

---

Converts each entry in the given tensor to strings.

#### View aliases

**Main aliases**

[`tf.as_string`](https://tensorflow.google.cn/api_docs/python/tf/strings/as_string)

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.as_string`](https://tensorflow.google.cn/api_docs/python/tf/strings/as_string), [`tf.compat.v1.dtypes.as_string`](https://tensorflow.google.cn/api_docs/python/tf/strings/as_string), [`tf.compat.v1.strings.as_string`](https://tensorflow.google.cn/api_docs/python/tf/strings/as_string)

```
tf.strings.as_string(
    input: Annotated[Any, TV_AsString_T],
    precision: int = -1,
    scientific: bool = False,
    shortest: bool = False,
    width: int = -1,
    fill: str = '',
    name=None
) -> Annotated[Any, _atypes.String]
```

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| * [Migrating Keras 2 code to multi-backend Keras 3](https://tensorflow.google.cn/guide/keras/migrating_to_keras_3) * [Signatures in TensorFlow Lite](https://tensorflow.google.cn/lite/guide/signatures) | * [Recommending movies: retrieval using a sequential model](https://tensorflow.google.cn/recommenders/examples/sequential_retrieval) * [Using TensorFlow Recommenders with TFX](https://tensorflow.google.cn/recommenders/examples/ranking_tfx) * [TFX Keras Component Tutorial](https://tensorflow.google.cn/tfx/tutorials/tfx/components_keras) |

Supports many numeric types and boolean.

For Unicode, see the
[https://www.tensorflow.org/tutorials/representation/unicode](/api_docs/python/tf/strings/Working%20with%20Unicode%20text)
tutorial.

#### Examples:

```
>>> tf.strings.as_string([3, 2])
<tf.Tensor: shape=(2,), dtype=string, numpy=array([b'3', b'2'], dtype=object)>
>>> tf.strings.as_string([3.1415926, 2.71828], precision=2).numpy()
array([b'3.14', b'2.72'], dtype=object)
```

| Args | |

|  |  |
| --- | --- |
| `input` | A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`, `complex64`, `complex128`, `bool`, `variant`, `string`. |
| `precision` | An optional `int`. Defaults to `-1`. The post-decimal precision to use for floating point numbers. Only used if precision > -1. |
| `scientific` | An optional `bool`. Defaults to `False`. Use scientific notation for floating point numbers. |
| `shortest` | An optional `bool`. Defaults to `False`. Use shortest representation (either scientific or standard) for floating point numbers. |
| `width` | An optional `int`. Defaults to `-1`. Pad pre-decimal numbers to this width. Applies to both floating point and integer numbers. Only used if width > -1. |
| `fill` | An optional `string`. Defaults to `""`. The value to pad if width > -1. If empty, pads with spaces. Another typical value is '0'. String cannot be longer than 1 character. |
| `name` | A name for the operation (optional). |

| Returns | |
| A `Tensor` of type `string`. | |