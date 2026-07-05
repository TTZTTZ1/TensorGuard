# tf.train.experimental.PythonState

**Source URL:** [https://tensorflow.google.cn/api_docs/python/tf/train/experimental/PythonState](https://tensorflow.google.cn/api_docs/python/tf/train/experimental/PythonState)

---

[View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/trackable/python_state.py#L28-L87) |

A mixin for putting Python state in an object-based checkpoint.

#### View aliases

**Compat aliases for migration**

See
[Migration guide](https://tensorflow.google.cn/guide/migrate) for
more details.

[`tf.compat.v1.train.experimental.PythonState`](https://tensorflow.google.cn/api_docs/python/tf/train/experimental/PythonState)

This is an abstract class which allows extensions to TensorFlow's object-based
checkpointing (see [`tf.train.Checkpoint`](https://tensorflow.google.cn/api_docs/python/tf/train/Checkpoint)). For example a wrapper for NumPy
arrays:

```
import io
import numpy

class NumpyWrapper(tf.train.experimental.PythonState):

  def __init__(self, array):
    self.array = array

  def serialize(self):
    string_file = io.BytesIO()
    try:
      numpy.save(string_file, self.array, allow_pickle=False)
      serialized = string_file.getvalue()
    finally:
      string_file.close()
    return serialized

  def deserialize(self, string_value):
    string_file = io.BytesIO(string_value)
    try:
      self.array = numpy.load(string_file, allow_pickle=False)
    finally:
      string_file.close()
```

Instances of `NumpyWrapper` are checkpointable objects, and will be saved and
restored from checkpoints along with TensorFlow state like variables.

```
root = tf.train.Checkpoint(numpy=NumpyWrapper(numpy.array([1.])))
save_path = root.save(prefix)
root.numpy.array *= 2.
assert [2.] == root.numpy.array
root.restore(save_path)
assert [1.] == root.numpy.array
```

## Methods

### `deserialize`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/trackable/python_state.py#L79-L81)

```
@abc.abstractmethod
deserialize(
    string_value
)
```

Callback to deserialize the object.

### `serialize`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.16.1/tensorflow/python/trackable/python_state.py#L75-L77)

```
@abc.abstractmethod
serialize()
```

Callback to serialize the object. Returns a string.