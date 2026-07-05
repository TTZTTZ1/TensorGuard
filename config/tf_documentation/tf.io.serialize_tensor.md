# tf.io.serialize_tensor

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/io/serialize_tensor](https://tensorflow.google.cn/api_docs/python/tf/io/serialize_tensor)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/ops/io_ops.py#L137-L214) |

Transforms a Tensor into a serialized TensorProto proto.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.io.serialize_tensor`](https://tensorflow.google.cn/api_docs/python/tf/io/serialize_tensor), [`tf.compat.v1.serialize_tensor`](https://tensorflow.google.cn/api_docs/python/tf/io/serialize_tensor)

```
tf.io.serialize_tensor(
    tensor, name=None
)
```

This operation transforms data in a [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) into a [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor) of type
[`tf.string`](https://tensorflow.google.cn/api_docs/python/tf#string) containing the data in a binary string in little-endian format.
This operation can transform scalar data and linear arrays, but it is most
useful in converting multidimensional arrays into a format accepted by binary
storage formats such as a `TFRecord` or [`tf.train.Example`](https://tensorflow.google.cn/api_docs/python/tf/train/Example).

#### See also:

* [`tf.io.parse_tensor`](https://tensorflow.google.cn/api_docs/python/tf/io/parse_tensor): inverse operation of [`tf.io.serialize_tensor`](https://tensorflow.google.cn/api_docs/python/tf/io/serialize_tensor) that
  transforms a scalar string containing a serialized Tensor in little-endian
  format into a Tensor of a specified type.
* [`tf.ensure_shape`](https://tensorflow.google.cn/api_docs/python/tf/ensure_shape): `parse_tensor` cannot statically determine the shape of
  the parsed tensor. Use [`tf.ensure_shape`](https://tensorflow.google.cn/api_docs/python/tf/ensure_shape) to set the static shape when running
  under a [`tf.function`](https://tensorflow.google.cn/api_docs/python/tf/function)
* `.SerializeToString`, serializes a proto to a binary-string

Example of serializing scalar data:

```
>>> t = tf.constant(1)
>>> tf.io.serialize_tensor(t)
<tf.Tensor: shape=(), dtype=string, numpy=b'\x08...\x00'>
```

Example of storing non-scalar data into a [`tf.train.Example`](https://tensorflow.google.cn/api_docs/python/tf/train/Example):

```
>>> t1 = [[1, 2]]
>>> t2 = [[7, 8]]
>>> nonscalar = tf.concat([t1, t2], 0)
>>> nonscalar
<tf.Tensor: shape=(2, 2), dtype=int32, numpy=
array([[1, 2],
       [7, 8]], dtype=int32)>
```

Serialize the data using [`tf.io.serialize_tensor`](https://tensorflow.google.cn/api_docs/python/tf/io/serialize_tensor).

```
>>> serialized_nonscalar = tf.io.serialize_tensor(nonscalar)
>>> serialized_nonscalar
<tf.Tensor: shape=(), dtype=string, numpy=b'\x08...\x00'>
```

Store the data in a [`tf.train.Feature`](https://tensorflow.google.cn/api_docs/python/tf/train/Feature).

```
>>> feature_of_bytes = tf.train.Feature(
...   bytes_list=tf.train.BytesList(value=[serialized_nonscalar.numpy()]))
>>> feature_of_bytes
bytes_list {
  value: "\010...\000"
}
```

Put the [`tf.train.Feature`](https://tensorflow.google.cn/api_docs/python/tf/train/Feature) message into a [`tf.train.Example`](https://tensorflow.google.cn/api_docs/python/tf/train/Example).

```
>>> features_for_example = {
...   'feature0': feature_of_bytes
... }
>>> example_proto = tf.train.Example(
...   features=tf.train.Features(feature=features_for_example))
>>> example_proto
features {
  feature {
    key: "feature0"
    value {
      bytes_list {
        value: "\010...\000"
      }
    }
  }
}
```

| Args | |

|  |  |
| --- | --- |
| `tensor` | A [`tf.Tensor`](https://tensorflow.google.cn/api_docs/python/tf/Tensor). |
| `name` | string. Optional name for the op. |

| Returns | |
| A Tensor of dtype string. | |